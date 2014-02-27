from __future__ import absolute_import

from fabric.api import local
import os
import inonemonth.settings.base


LOCAL = "local"
LOCAL_DOMAIN = "http://localhost"
LOCAL_SETTING = LOCAL
LOCAL_DB_NAME = "inonemonth"

TEST = "test"
TEST_DOMAIN = LOCAL_DOMAIN
TEST_SETTING = TEST

STAGING = "staging"
STAGING_DOMAIN = "https://inonemonth.staging.herokuapp.com"
STAGING_HEROKU_APP = "inonemonth-staging"
STAGING_ENV_FILE = ".heroku_env/staging.txt"
STAGING_REMOTE = STAGING
STAGING_SETTING = STAGING

PRODUCTION = "production"
PRODUCTION_DOMAIN = "https://inonemonth.herokuapp.com"
PRODUCTION_HEROKU_APP = "inonemonth"
PRODUCTION_ENV_FILE = ".heroku_env/production.txt"
PRODUCTION_REMOTE = PRODUCTION
PRODUCTION_SETTING = PRODUCTION

DEFAULT_REMOTE = "heroku"


def local_manage(django_command="shell", setting=LOCAL_SETTING):
    local("python manage.py {0} --settings=inonemonth.settings.{1} --traceback".format(django_command, setting))


def cov_run(app_name="core", options="", setting=TEST_SETTING):
    local("coverage run --rcfile=.coveragerc --source='.' manage.py test {0} "
          "{1} --settings=inonemonth.settings.{2} --traceback".format(app_name, options, setting))


def setup_allauth_social(domain=LOCAL_DOMAIN, setting=LOCAL_SETTING):
    """
    E.g. setup_allauth_social:"http://localhost","local"
    """
    local_manage(django_command="setup_allauth_social github --domain='{0}' "
                                "--social_app_name='github_social_app'".format(domain),
                 setting=setting)


# Simply in the hope that this works with Lettuce
def remake_fixtures():#domain, setting):
    """
    """
    #local("python manage.py dumpdata sites --indent 4")
    #local("python manage.py dumpdata socialaccount --indent 4")
    local("python manage.py dumpdata sites socialaccount --indent 4 > core/initial_data.json")


# Shortcut
def loc(command="runserver", setting=LOCAL_SETTING):
    """
    E.g. loc:"runserver 8004"
    """
    local_manage(django_command=command,
                 setting=setting)


def loc_new_db(create_superuser=False):
    """
    E.g. loc_new_db:True
    Remove old Postgresql db and set it up all necessary initial data.
    """
    try:
        local("dropdb {0}".format(LOCAL_DB_NAME))
    except:
        local("createdb {0}".format(LOCAL_DB_NAME))
    local_manage(django_command="syncdb --noinput",
                 setting=LOCAL_SETTING)
    if create_superuser:
        local_manage(django_command="createsuperuser",
                     setting=LOCAL_SETTING)
    local_manage(django_command="migrate",
                 setting=LOCAL_SETTING)
    setup_allauth_social(LOCAL_DOMAIN, setting=LOCAL_SETTING)
    #remake_fixtures()


def ftest(app_name="", option="", setting=TEST_SETTING):
    """
    E.g. ftest:'core,challenges','-S'
         ftest:core,'--pdb"
         ftest:app_name=core,option='--pdb',setting=local

    -T option does django test setup and teardown
    Running with -v2 option gets rid of colorized output somehow

    There is an IndexError at the end of running harvest,
    likely caused by Lettuce or Django.
    Error reported : https://github.com/gabrielfalcao/lettuce/issues/391
    """
    local_manage(django_command="harvest -T -d --failfast --apps={0} {1}".format(app_name, option),
                 setting=setting)


def ftest_all(setting=TEST_SETTING):
    # Confer utest_all
    pass


def utest(app_name="core", setting=TEST_SETTING):
    """
    E.g. utest:challenges
    """
    cov_run(app_name=app_name, options="-v2", setting=setting)


def utestff(app_name="core", setting=TEST_SETTING):
    """
    utest with failfast option
    """
    cov_run(app_name=app_name, options="--failfast -v2", setting=setting)


def utest_all(setting=TEST_SETTING):
    """
    Test all local(=project) apps.
    """
    local_apps = " ".join(inonemonth.settings.base.LOCAL_APPS)
    local("coverage run --rcfile=.coveragerc --source='.' manage.py test {0} "
          "--settings=inonemonth.settings.{1} --traceback".format(local_apps, setting))
    cov_run(app_name=local_apps, options="", setting=setting)


def cov():
    """
    Run coverage report. E.g. cov
    """
    local("coverage report -m")
    local("coverage html")
    local("coverage xml")


def heroku_command(heroku_command="run bash", heroku_remote=DEFAULT_REMOTE):
    local("cd ..; heroku {0} --remote {1}".format(heroku_command, heroku_remote))


def heroku_manage(django_command="shell", setting=STAGING_SETTING, heroku_remote=STAGING_REMOTE):
    heroku_command(heroku_command="run python inonemonth/manage.py {0} --settings=inonemonth.settings.{1} --traceback".format(django_command, setting),
                   heroku_remote=heroku_remote)


def setup_heroku_allauth_social(domain=STAGING_DOMAIN, setting=STAGING_SETTING, heroku_remote=STAGING_REMOTE):
    """
    E.g. setup_heroku_allauth_social:"https://inonemonth-staging.herokuapp.com","staging", "staging"
    """
    heroku_manage(django_command="setup_allauth_social github --domain='{0}' --social_app_name='github_social_app'".format(domain),
                  setting=setting,
                  heroku_remote=heroku_remote)


def setup_heroku_env(env_file=STAGING_ENV_FILE, heroku_remote=STAGING_REMOTE):
    """
    Reads from a .heroku_env.txt file
    Run this command each time you add new env_variables to .heroku_env.txt
    E.g. setup_heroku_env:heroku_remote='staging'
    """
    # To enable 1 Procfile for staging and production
    heroku_command(heroku_command="config:set DEPLOYMENT_ENV={0}".format(heroku_remote),
                   heroku_remote=heroku_remote)

    # Set env variables from heroku env file

    # Execute a heroku env file with pip style syntax
    # However, put comments on a seperate line!!
    def execute_heroku_env_file(env_file):
        env_file
        env_dir_name = os.path.dirname(env_file)
        with open(env_file) as f:
            env_lines_list = f.readlines()
        for line in env_lines_list:
            if line.startswith("#"):
                # Ignore comments
                pass
            elif line.strip() == "":
                # Ignore empty lines
                pass
            elif line.startswith("-r "):
                base_file_pre_clean = line.strip("-r ")
                # To strip \n
                base_file_base_name = base_file_pre_clean.strip()
                base_file = os.path.join(env_dir_name, base_file_base_name)
                # Yay, recursion!
                execute_heroku_env_file(base_file)
           else:
                heroku_command(heroku_command="config:set {0}".format(line.strip()),
                               heroku_remote=heroku_remote)

                # Call back implementation for easier testing of logic
                # but how to implement it if it uses the line parameter?
                #heroku_frozen_env_command(line) #

    #import functools
    #part_her = functools.partial(heroku_command, **{"heroku_command": "config:set{0}".format(line.strip()),
    #                                  "heroku_remote": heroku_remote})
    #execute_heroku_env_file(env_file, part_her)
    execute_heroku_env_file(env_file)


def setup_heroku_after_fresh_db(domain=STAGING_DOMAIN,
                                env_file=STAGING_ENV_FILE,
                                heroku_remote=STAGING_REMOTE):
    """
    You must run this once on fresh db in heroku!
    e.g. : setup_heroku_after_fresh_db: domain="https://inonemonth-staging.herokuapp.com",heroku_remote="staging"
    """
    setup_heroku_env(env_file, heroku_remote)
    setup_heroku_allauth_social(domain, heroku_remote)



def heroku_new_db(heroku_app=STAGING_HEROKU_APP, branch="master",
                  domain=STAGING_DOMAIN, env_file=STAGING_ENV_FILE,
                  create_superuser=False, setting=STAGING_SETTING,
                  heroku_remote=STAGING_REMOTE):
    local("git push {0} {1}".format(heroku_remote, branch))
    # reset db
    heroku_command(heroku_command="pg:reset DATABASE --confirm {0}".format(heroku_app),
                   heroku_remote=heroku_remote)
    heroku_manage(django_command="syncdb --noinput",
                         setting=setting)
    if create_superuser:
        heroku_manage(django_command="createsuperuser",
                             setting=setting)
    heroku_manage(django_command="migrate --noinput",
                         setting=setting)
    setup_heroku_after_fresh_db(domain, env_file, heroku_remote)


def stag_new_db(heroku_app=PRODUCTION_HEROKU_APP, branch="master", create_superuser=False):
    heroku_new_db(heroku_app=heroku_app,
                  branch=branch,
                  domain=STAGING_DOMAIN,
                  env_file=STAGING_ENV_FILE,
                  create_superuser=create_superuser,
                  setting=STAGING_SETTING,
                  heroku_remote=STAGING_REMOTE)


def prod_new_db(heroku_app=PRODUCTION_HEROKU_APP, branch="master", create_superuser=False):
    heroku_new_db(heroku_app=heroku_app,
                  branch=branch,
                  domain=PRODUCTION_DOMAIN,
                  env_file=PRODUCTION_ENV_FILE,
                  create_superuser=create_superuser,
                  setting=PRODUCTION_SETTING,
                  heroku_remote=PRODUCTION_REMOTE)


# Create remote env
# heroku create --remote production
# also implement delete

def stag_initial_deploy(heroku_app=STAGING_HEROKU_APP):
    # Creates a heroku app called "inonemonth" and creates a git remote tied to
    # that location
    heroku_command(heroku_command="create {0}".format(heroku_app),
                   heroku_remote=STAGING_REMOTE)
    prod_new_db(heroku_app=heroku_app)


def prod_initial_deploy(heroku_app=PRODUCTION_HEROKU_APP):
    # Creates a heroku app called "inonemonth" and creates a git remote tied to
    # that location
    heroku_command(heroku_command="create {0}".format(heroku_app),
                   heroku_remote=PRODUCTION_REMOTE)
    prod_new_db(heroku_app=heroku_app)


'''
# (After having created an amazon S3 bucket and updated settings.staging)
# Bucket creation could be optimised via using amazon S3 API: http://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUT.html

# Heroku staging setup run:
#heroku apps:create my-heroku-app --remote staging
#setup.heroku_env.txt:staging
#git push staging master

# Run a command in heroku staging:
#heroku run --remote staging python inonmonth/manage.py shell --settings=inonemonth.settings.staging

# If I get my custom url instead of herokuapp.com, then you need a heroku add on to llow ssl
#https://devcenter.heroku.com/articles/ssl-endpoint



# With pjb data, I didn't have to activate worker
# That's probably because I used the -w 3 option in gunicorn, use this in procfile!
# pjb_data command: `web: python inonemonth/manage.py run_gunicorn -b 0.0.0.0:$PORT -w 3 --settings=inonemonth.settings.production`

# Set heroku configs automatically
# see http://pydanny.com/you-should-heroku.html
# E.g. heroku config:add S3_KEY=HAHAHAHAHAHA S3_SECRET=NOTGIVINGITOUT

# Works:
heroku run --remote staging python inonmonth/manage.py shell --settings=inonemonth.settings.production

# Test production email ####
heroku run --remote staging python inonmonth/manage.py shell --settings=inonemonth.settings.production
from django.core.mail import send_mail

send_mail('Subject here', 'Here is the message.', 'automercurius@gmail.com',
    ['de.rouck.robrecht@gmail.com'], fail_silently=False)
###########################

web: cd inonemonth; python manage.py collectstatic --noinput --settings=inonemonth.settings.$DEPLOYMENT_ENV; gunicorn inonemonth.wsgi -w 3 --settings=inonemonth.settings.$DEPLOYMENT_ENV
# if you use django-admin.py instead of python manage.py the command fails, wth, why??


def heroku_staging_command(heroku_command):
    """
    E.g. heroku_staging_command:heroku_command
    """
    local("heroku logs --remote staging")


def heroku_staging_setup(heroku_staging_app_name):
    """
    E.g. heroku_setup_staging:my_heroku_staging_app_name
    """
    local("git flow init -d")
    local("git checkout master")
    local("git add .")
    try:
        local("git commit -m 'First commit'")
    except:
        pass
    local("heroku apps:create %s --remote staging" % heroku_staging app_name)


def heroku_staging_push(commit_msg="undefined commit"):
    """
    Push to heroku staging environment
    You should push to master, not develop!
    """
    local("git checkout master")
    local("git add .")
    try:
        local("git commit -m '%s'" % commit_msg)
    except:
        pass
    local("git push staging master")


def heroku_production_setup(heroku_production_app_name):
    """
    E.g. heroku_setup_production:my_heroku_production_app_name
    """
    local("git flow init -d")
    local("git checkout master")
    local("git add .")
    try:
        local("git commit -m 'First commit'")
    except:
        pass
    local("heroku apps:create %s --remote production" % heroku_production_app_name)


def heroku_production_push(commit_msg="undefined commit"):
    """
    Push to heroku production environment
    You should push to master, not develop!
    """
    local("git checkout master")
    local("git add .")
    try:
        local("git commit -m '%s'" % commit_msg)
    except:
        pass
    local("git push production master")
'''

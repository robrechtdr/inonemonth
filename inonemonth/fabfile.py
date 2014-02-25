from __future__ import absolute_import

from fabric.api import local
import os
import inonemonth.settings.base


def setup_allauth_social(domain, setting):
    """
    E.g. setup_allauth_social:"http://localhost","local"
    """
    local("python manage.py setup_allauth_social github --domain='{0}' "
          "--social_app_name='github_social_app' --settings=inonemonth.settings.{1} "
          "--traceback".format(domain, setting))


# Simply in the hope that this works with Lettuce
def remake_fixtures():#domain, setting):
    """
    """
    #local("python manage.py dumpdata sites --indent 4")
    #local("python manage.py dumpdata socialaccount --indent 4")
    local("python manage.py dumpdata sites socialaccount --indent 4 > core/initial_data.json")


def loc(command="runserver"):
    """
    E.g. loc:"runserver 8004"
    """
    local("django-admin.py %s "
      "--settings=inonemonth.settings.local --traceback" % command)


def loc_new_db(create_superuser=False):
    """
    E.g. loc_new_db:True
    Remove old Postgresql db and set it up all necessary initial data.
    """
    local("dropdb inonemonth")
    local("createdb inonemonth")
    local("django-admin.py syncdb --settings=inonemonth.settings.local --noinput")
    if create_superuser:
        local("django-admin.py createsuperuser --username='inonemonth' "
              "--email='de.rouck.robrecht@gmail.com' "
              "--settings=inonemonth.settings.local")
    local("django-admin.py migrate --settings=inonemonth.settings.local")
    setup_allauth_social("http://localhost", "local")
    remake_fixtures()


def ftest(app_name="", option="", setting="test"):
    """
    E.g. ftest:'core,challenges', '-S'
         ftest:core,'--pdb"
         ftest:app_name=core,option='--pdb',setting=local

    -T option does django test setup and teardown
    Running with -v2 option gets rid of colorized output somehow

    There is an IndexError at the end of running harvest,
    likely caused by Lettuce or Django.
    Error reported : https://github.com/gabrielfalcao/lettuce/issues/391
    """
    local("python manage.py harvest -T -d --failfast --apps=%s %s "
          "--settings=inonemonth.settings.%s --traceback" % (app_name, option, setting))


def utest(app_name="", setting="test"):
    """
    E.g. utest:accounts
    """
    #local("django-admin.py %s "
    #  "--settings=inonemonth.settings.test" % command)
    local("coverage run --rcfile=.coveragerc --source='.' manage.py test {0} "
          "--settings=inonemonth.settings.{1} -v2 --traceback".format(app_name, setting))

def utestff(app_name="", setting="test"):
    """
    utest with failfast option
    """
    #local("django-admin.py %s "
    #  "--settings=inonemonth.settings.test" % command)
    local("coverage run --rcfile=.coveragerc --source='.' manage.py test {0} "
          "--failfast --settings=inonemonth.settings.{1} -v2 --traceback".format(app_name, setting))


def utest_all(setting="test"):
    """
    Test all local(=project) apps.
    """
    local_apps = " ".join(inonemonth.settings.base.LOCAL_APPS)
    local("coverage run --rcfile=.coveragerc --source='.' manage.py test {0} "
          "--settings=inonemonth.settings.{1} --traceback".format(local_apps, setting))

def cov():
    """
    Run coverage report. E.g. cov
    """
    local("coverage report -m")
    local("coverage html")
    local("coverage xml")


def stag(command="shell"):
    """
    E.g. stag:syncdb
    """
    local("django-admin.py %s "
      "--settings=inonemonth.settings.staging" % command)


def prod(command="shell"):
    """
    E.g. prod:syncdb
    """
    local("django-admin.py %s "
      "--settings=inonemonth.settings.production" % command)



def setup_local_env(envi="local", env_file="local_env.txt"):
    """
    E.g. setup_local_env:local
    This should be one command with setup_heroku_env
    For local command, should only add a command line if that line isn't already there!
    """
    virtual_env_path = os.environ.get("VIRTUAL_ENV")
    activate_path = os.path.join(virtual_env_path, 'bin/activate')
    with open(env_file) as f:
        env_lines_list = f.readlines()
    with open(activate_path, "r") as activate_f:
        activate_lines_list = activate_f.readlines()
    for line in env_lines_list:
        if line not in activate_lines_list:
            with open(activate_path, "a") as activate_f:
                activate_f.write(line.strip() + '\n')
    # Now reread the activate file so the new env variables are read.
    local("bash {0}".format(activate_path)) # 'bash' should be made os independant


def heroku_command(heroku_command="run bash", heroku_remote="heroku"):
    local("cd ..; heroku {0} --remote {1}".format(heroku_command, heroku_remote))


def heroku_django_manage(django_command="shell", setting="staging", heroku_remote="heroku"):
    heroku_command(heroku_command="run python inonemonth/manage.py {0} --settings=inonemonth.settings.{1} --traceback".format(django_command, setting),
                   heroku_remote=heroku_remote)


def setup_heroku_allauth_social(domain="http://inonemonth-staging.herokuapp.com", setting="staging", heroku_remote="staging"):
    """
    E.g. setup_heroku_allauth_social:"https://inonemonth-staging.herokuapp.com","staging", "staging"
    """
    heroku_django_manage(django_command="setup_allauth_social github --domain='{0}' --social_app_name='github_social_app'".format(domain),
                         setting=setting,
                         heroku_remote=heroku_remote)


'''
def setup_heroku_allauth_social(domain, setting, heroku_remote="staging"):
    """
    E.g. setup_heroku_allauth_social:"https://inonemonth-staging.herokuapp.com","staging"
    """
    # Inside heroku, must use cd inonemonth first
    local("cd ..; heroku run --remote {0} python inonemonth/manage.py setup_allauth_social github --domain='{1}' "
          "--social_app_name='github_social_app' --settings=inonemonth.settings.{2} "
          "--traceback".format(domain, setting, heroku_remote))
'''



def setup_heroku_env(heroku_remote="staging", env_file="heroku_env.txt"):
    """
    Reads from a heroku_env.txt file
    Run this command each time you add new env_variables to heroku_env.txt
    E.g. setup_heroku_env:staging
    """
    # To enable 1 Procfile for staging and production
    heroku_command(heroku_command="config:set DEPLOYMENT_ENV={0}".format(heroku_remote),
                   heroku_remote=heroku_remote)
    # Set env variables from heroku env file
    with open(env_file) as f:
        env_lines_list = f.readlines()
    for line in env_lines_list:
        heroku_command(heroku_command="config:set {0}".format(line.strip()),
                       heroku_remote=heroku_remote)

'''
def setup_heroku_env(envi="staging", env_file="heroku_env.txt"):
    """
    Reads from a heroku_env.txt file
    Run this command each time you add new env_variables to heroku_env.txt
    E.g. setup_heroku_env:staging
    """
    prefix = "cd .. ;"
    # To enable 1 Procfile for staging and production
    local("{0} heroku config:set DEPLOYMENT_ENV={1} --remote {1}".format(prefix, envi))

    with open(env_file) as f:
        env_lines_list = f.readlines()
    for line in env_lines_list:
        local(prefix + line.strip() + " --remote {0}".format(envi))
'''




def setup_heroku_after_fresh_db(domain="http://inonemonth.com",
                                envi="staging",
                                env_file="heroku_env.txt"):
    """
    You must run this once on fresh db in heroku!
    e.g. : setup_heroku_after_fresh_db: "https://inonemonth-staging.herokuapp.com", "staging"
    """
    setup_heroku_env(envi, env_file)
    setup_heroku_allauth_social(domain, envi)
    # This is just running locally, must run on heroku
    #setup_allauth_social(domain, envi)
    #local("cd .. ; heroku run --remote staging python inonemonth/manage.py shell --settings=inonemonth.settings.production")


def heroku_new_db(envi="staging", domain="https://inonemonth.staging.herokuapp.com", app_name="inonemonth-staging", create_superuser=False):
    """
    E.g. loc_new_db:True
    Remove old Postgresql db and set it up all necessary initial data.
    How to do with Heroku?
    """
    local("git push {0} master".format(envi))
    local("cd .. ; heroku pg:reset DATABASE --confirm {0} "
          "--remote {1}".format(app_name, envi))
    local("cd .. ; heroku run --remote {0} python inonemonth/manage.py syncdb "
          "--settings=inonemonth.settings.{0} --noinput --traceback".format(envi))
    if create_superuser:
        local("cd .. ; heroku run --remote {0} python inonemonth/manage.py createsuperuser "
              "--username=inonemonth --email='de.rouck.robrecht@gmail.com' "
              "--settings=inonemonth.settings.{0} --traceback".format(envi))
    local("cd .. ; heroku run --remote {0} python inonemonth/manage.py migrate "
          "--settings=inonemonth.settings.{0} --noinput --traceback".format(envi))
    setup_heroku_after_fresh_db(domain, envi)


def stag_new_db(create_superuser=False):
    heroku_new_db(envi="staging", domain="https://inonemonth.staging.herokuapp.com", app_name="inonemonth-staging", create_superuser=create_superuser)


def prod_new_db(create_superuser=False):
    heroku_new_db(envi="production", domain="https://inonemonth.herokuapp.com", app_name="inonemonth", create_superuser=create_superuser)

# Create remote env
# heroku create --remote production


def initial_deploy_production(heroku_app="inonemonth"):
    # Creates a heroku app called "inonemonth" and creates a git remote tied to
    # that location
    local("cd .. ; heroku create {0} --remote production".format(heroku_app))
    prod_new_db()



'''
# (After having created an amazon S3 bucket and updated settings.staging)
# Bucket creation could be optimised via using amazon S3 API: http://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUT.html

# Heroku staging setup run:
#heroku apps:create my-heroku-app --remote staging
#setup_heroku_env:staging
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

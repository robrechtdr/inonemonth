from __future__ import absolute_import

import os

import inonemonth.settings.base

from fabric.api import local


LOCAL = "local"
LOCAL_DOMAIN = "http://localhost"
LOCAL_SETTING = LOCAL
LOCAL_DB_NAME = "inonemonth"

TEST = "test"
TEST_DOMAIN = LOCAL_DOMAIN
TEST_SETTING = TEST

STAGING = "staging"
STAGING_HEROKU_APP = "inonemonth-staging"
STAGING_DOMAIN = "https://{0}.herokuapp.com".format(STAGING_HEROKU_APP)
STAGING_ENV_FILE = ".heroku_env/staging.txt"
STAGING_REMOTE = STAGING
STAGING_SETTING = STAGING

PRODUCTION = "production"
PRODUCTION_HEROKU_APP = "inonemonth"
PRODUCTION_DOMAIN = "https://{0}.herokuapp.com".format(PRODUCTION_HEROKU_APP)
PRODUCTION_ENV_FILE = ".heroku_env/production.txt"
PRODUCTION_REMOTE = PRODUCTION
PRODUCTION_SETTING = PRODUCTION

DEFAULT_REMOTE = "heroku"


def local_manage(django_command="shell", setting=LOCAL_SETTING):
    local("python manage.py {0} --settings=inonemonth.settings.{1} "
          "--traceback".format(django_command, setting))


def cov_run(app_name="core", options="", setting=TEST_SETTING):
    local("coverage run --rcfile=.coveragerc --source='.' manage.py test {0} "
          "{1} --settings=inonemonth.settings.{2} "
          "--traceback".format(app_name, options, setting))


def setup_allauth_social(domain=LOCAL_DOMAIN, setting=LOCAL_SETTING):
    """
    E.g. setup_allauth_social:"http://localhost","local"
    """
    local_manage(django_command="setup_allauth_social github --domain='{0}' "
                                "--social_app_name="
                                "'github_social_app'".format(domain),
                 setting=setting)


def celery_worker():
    local("celery -A inonemonth worker -l info")


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
        local("createdb {0}".format(LOCAL_DB_NAME))
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
    print "Not implemented yet"
    #local_manage(django_command=(
    #    "harvest -T -d --failfast --apps={0} {1}".format(app_name, option)),
    #    setting=setting)


def ftest_all(setting=TEST_SETTING):
    # Confer utest_all
    print "Not implemented yet"


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
    cov_run(app_name=local_apps, options="", setting=setting)


def cov():
    """
    Run coverage report. E.g. cov
    """
    local("coverage report -m")
    local("coverage html")
    local("coverage xml")


def heroku(heroku_command="run bash", heroku_remote=DEFAULT_REMOTE):
    local("cd ..; heroku {0} --remote {1}".format(heroku_command,
                                                  heroku_remote))


def stag_heroku(heroku_command="run bash"):
    heroku(heroku_command=heroku_command, heroku_remote=STAGING_REMOTE)


def prod_heroku(heroku_command="run bash"):
    heroku(heroku_command=heroku_command, heroku_remote=PRODUCTION_REMOTE)


def heroku_manage(django_command="shell",
                  setting=STAGING_SETTING,
                  heroku_remote=STAGING_REMOTE):
    heroku(heroku_command=("run python inonemonth/manage.py {0} "
                           "--settings=inonemonth.settings.{1} "
                           "--traceback".format(django_command, setting)),
           heroku_remote=heroku_remote)


def stag_manage(django_command="shell"):
    heroku_manage(django_command=django_command,
                  setting=STAGING_SETTING,
                  heroku_remote=STAGING_REMOTE)


def prod_manage(django_command="shell"):
    heroku_manage(django_command=django_command,
                  setting=PRODUCTION_SETTING,
                  heroku_remote=PRODUCTION_REMOTE)


def setup_heroku_allauth_social(domain=STAGING_DOMAIN,
                                setting=STAGING_SETTING,
                                heroku_remote=STAGING_REMOTE):
    """
    E.g. setup_heroku_allauth_social:
        "https://inonemonth-staging.herokuapp.com","staging", "staging"
    """
    heroku_manage(django_command=("setup_allauth_social github --domain='{0}' "
                                  "--social_app_name="
                                  "'github_social_app'".format(domain)),
                  setting=setting,
                  heroku_remote=heroku_remote)


def setup_heroku_env(env_file=STAGING_ENV_FILE, heroku_remote=STAGING_REMOTE):
    """
    Run this command each time you add new env_variables to .heroku_env.txt
    E.g. setup_heroku_env:heroku_remote='staging'
    """
    # To enable 1 Procfile for staging and production
    heroku(heroku_command="config:set DEPLOYMENT_ENV={0}".format(heroku_remote),
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
                heroku(heroku_command="config:set {0}".format(line.strip()),
                       heroku_remote=heroku_remote)

                # Call back implementation for easier testing of logic
                # but how to implement it if it uses the line parameter?
                #heroku_frozen_env_command(line) #

    #import functools
    #part_her = functools.partial(heroku, **{"heroku_command":
    #                                     "config:set{0}".format(line.strip()),
    #                             "heroku_remote": heroku_remote})
    #execute_heroku_env_file(env_file, part_her)
    execute_heroku_env_file(env_file)


def heroku_deploy(branch="master",
                  heroku_remote=STAGING_REMOTE,
                  env_file=STAGING_ENV_FILE):
    # Must set env variables before doing syncdb
    setup_heroku_env(env_file, heroku_remote)
    # Forcing to push amends to heroku repo
    if branch == "master":
        local("git push {0} {1} --force".format(heroku_remote, branch))
    # Heroku by default ignores pushes from non-master branches
    # To enable pushing from non-master branch, needs different format
    # https://devcenter.heroku.com/articles/git#deploying-code
    else:
        local("git push {0} {1}:master --force".format(heroku_remote, branch))


def stag_deploy(branch="master"):
    heroku_deploy(branch=branch,
                  heroku_remote=STAGING_REMOTE,
                  env_file=STAGING_ENV_FILE)


def prod_deploy(branch="master"):
    heroku_deploy(branch=branch,
                  heroku_remote=PRODUCTION_REMOTE,
                  env_file=PRODUCTION_ENV_FILE)


def heroku_new_db(heroku_app=STAGING_HEROKU_APP, branch="master",
                  domain=STAGING_DOMAIN, env_file=STAGING_ENV_FILE,
                  create_superuser=False, setting=STAGING_SETTING,
                  heroku_remote=STAGING_REMOTE):
    heroku_deploy(branch, heroku_remote, env_file)
    try:
        # reset db
        heroku(heroku_command=(
            "pg:reset DATABASE --confirm {0}".format(heroku_app)),
            heroku_remote=heroku_remote)
    except:
        raise Exception("Die")
    heroku_manage(django_command="syncdb --noinput",
                  setting=setting,
                  heroku_remote=heroku_remote)
    if create_superuser:
        heroku_manage(django_command="createsuperuser",
                      setting=setting,
                      heroku_remote=heroku_remote)
    heroku_manage(django_command="migrate --noinput",
                  setting=setting,
                  heroku_remote=heroku_remote)
    setup_heroku_allauth_social(domain, setting, heroku_remote)


def stag_new_db(branch="master", create_superuser=False):
    heroku_new_db(heroku_app=STAGING_HEROKU_APP,
                  branch=branch,
                  domain=STAGING_DOMAIN,
                  env_file=STAGING_ENV_FILE,
                  create_superuser=create_superuser,
                  setting=STAGING_SETTING,
                  heroku_remote=STAGING_REMOTE)


def prod_new_db(branch="master", create_superuser=False):
    heroku_new_db(heroku_app=PRODUCTION_HEROKU_APP,
                  branch=branch,
                  domain=PRODUCTION_DOMAIN,
                  env_file=PRODUCTION_ENV_FILE,
                  create_superuser=create_superuser,
                  setting=PRODUCTION_SETTING,
                  heroku_remote=PRODUCTION_REMOTE)


def heroku_initial_deploy(branch="master",
                          heroku_app=STAGING_HEROKU_APP,
                          heroku_remote=STAGING_REMOTE):
    # Creates a heroku app called "inonemonth" and creates a git remote tied to
    # that location
    heroku(heroku_command="create {0}".format(heroku_app),
           heroku_remote=heroku_remote)
    heroku(heroku_command="addons:add cloudamqp:lemur {0}".format(heroku_app),
           heroku_remote=heroku_remote)
    if heroku_remote == STAGING_REMOTE:
        stag_new_db(branch=branch)
    elif heroku_remote == PRODUCTION_REMOTE:
        prod_new_db(branch=branch)
    else:
        raise Exception("Else Die")


def stag_initial_deploy(branch="master"):
    heroku_initial_deploy(branch=branch,
                          heroku_app=STAGING_HEROKU_APP,
                          heroku_remote=STAGING_REMOTE)


def prod_initial_deploy(branch="master"):
    heroku_initial_deploy(branch=branch,
                          heroku_app=PRODUCTION_HEROKU_APP,
                          heroku_remote=PRODUCTION_REMOTE)

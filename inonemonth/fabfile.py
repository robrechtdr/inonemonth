from fabric.api import local

def loc(command="runserver"):
    """
    E.g. loc:"runserver 8004"
    """
    local("django-admin.py %s "
      "--settings=inonemonth.settings.local" % command)


def test(command="test"):
    """
    E.g. test:"runserver 8004"
    """
    local("django-admin.py %s "
      "--settings=inonemonth.settings.test" % command)


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


'''
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

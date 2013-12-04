web: cd inonemonth; python manage.py collectstatic --noinput --settings=inonemonth.settings.$DEPLOYMENT_ENV; gunicorn inonemonth.wsgi -w 3 --settings=inonemonth.settings.$DEPLOYMENT_ENV

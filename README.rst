==========
Inonemonth
==========

------
Setup
------

Local (Ubuntu)
=====

1. Go to https://github.com/settings/applications/ and set up application
   with `http://localhost` as `Homepage URL` and 
   `http://localhost:8000/callback/` as `Authorization callback URL`.
2. Set `Client ID` string as value to `ALLAUTH_SOCIAL_APP_GITHUB_ID` in 
   `inonemonth/inonemonth/settings/local.py`.
3. Set `Client Secret` string to a local environment variable called 
   `ALLAUTH_SOCIAL_APP_GITHUB_SECRET`.
x. ....


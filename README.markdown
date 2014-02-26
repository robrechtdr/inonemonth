==========
Inonemonth
==========

------
Setup
------


1. Have [vagrant](http://www.vagrantup.com/downloads) and [virtualbox](https://www.virtualbox.org/wiki/Downloads) installed. It's also advised to keep your guest additions in sync with your virtual box by  running `vagrant plugin install vagrant-vbguest` once vagrant is installed.

2. Get repo in your current dir: 
  `git clone https://github.com/RobrechtDR/inonemonth.git`
3. `cd inonemonth`
4. Set up vagrant for inonemonth, this takes about 8 mins 22 secs with a connection of 54 Mb/s: 
  `vagrant up`
5. Crawl into your vagrant box:
   `vagrant ssh`
6. Get into the local virtual environment: 
   `sudo -i`
   `source /root/.venvburrito/startup.sh`
   `workon inonemonth_local`
7. Go to the toplevel django dir of the project:
  `cd /vagrant/inonemonth
(Make sure autoenv is loaded: 
 source ~/.autoenv/activate.sh)
8. fab loc_new_db
9. Run the local server:
  `fab loc`


(Then set up email server, set up github apps, set up write .env file,
write heroku_env.txt(change to .heroku_env) file)

..


for heroku
First time:
x. fab prod_new_deploy:"my_heroku_production_app"
Db reset after first deploy:
fab prod_new_db:"my_heroku_production_app"
For regular push to heroku:

Similar for staging.










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





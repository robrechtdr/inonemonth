# Install

## Local Setup

This setup allows you to run the local and testing environment.

**Requirements**   
Have [vagrant](http://www.vagrantup.com/downloads) and [virtualbox](https://www.virtualbox.org/wiki/Downloads) installed. It's also advised to keep your guest additions in sync with your virtual box by  running `vagrant plugin install vagrant-vbguest` once vagrant is installed.


**Steps**

1. Get repo in your current dir:  
  `git clone https://github.com/RobrechtDR/inonemonth.git`
2. Go to the project dir:  
  `cd inonemonth`
3. Set up vagrant for inonemonth, this takes about 11 mins 42 secs with a connection of 54 Mb/s:   
  `vagrant up`
4. Crawl into your vagrant box:  
   `vagrant ssh`  
5. Go to the toplevel django dir of the project:   
  `cd /vagrant/inonemonth`     
   It doesn't matter what you answer when prompted to source `.env` at this stage.
6. Make a Github app for local developent on https://github.com/settings/applications:
  1. Click on `Register new application`
  2. As `Authorization callback URL` write `http://localhost:8000/accounts/github/login/callback/`
  3. As `HomePage URL` write `http://localhost:8000`
  4. Write whatever you want for the other fields and click on `Register application`
  5. Copy the value of `Client Secret` to the value of `ALLAUTH_SOCIAL_APP_GITHUB_SECRET` in `.env`.
  6. Copy the value of `Client ID` to the value of `ALLAUTH_SOCIAL_APP_GITHUB_ID` in `inonemonth/settings/local.py`.
7. Create a [gmail address which can send automated mails](https://support.google.com/mail/answer/14257?hl=en):   
   Copy the email address and password to the values of `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` in `.env`. 
8. Load local environment variables:   
   `source .env`
9. Get into the local virtual environment:    
   `workon inonemonth_local`

**Running the server**  
1. Run the local server on your guest machine as the db is already set up with syncdb and migrate:  
  `fab loc:"runserver 0.0.0.0:8000"`  
2. View the site in the browser of your host machine by visiting `http://localhost:8009`.

> If you want to view the site on the browser of your host machine then you NEED 
> to use runserver `0.0.0.0:8000` instead of the default `127.0.0.1:8000`. This is because 
> `127.0.0.1` is a [loopback address](http://stackoverflow.com/questions/18157353/connection-reset-when-port-forwarding-with-vagrant),
> an address which is not available to other machines on the local network

**Testing**  
If you are still in the `inonemonth_local` env, first run `deactivate`  

1. Get on the test environment:   
  `workon inonemonth_test`  
2. * Run all unit tests:  
     `fab utest_all`   
   * Run all functional tests:   
     `fab ftest_all` 


**Handy commands**   

* Run a local manage.py command:  
   `fab loc:shell`
* Destroy the current db and rebuild it from scratch running syncdb and migrate:  
  `fab loc_new_db`  
* Run unit tests for a specific app:   
  `fab utest:core`
* Run unit tests for a specific app with the failfast option:    
  `fab utestff:core`
* Get unit test coverage report:   
  `fab cov`


## Deploy

The following deploys the app to a staging environment on Heroku. It is assumed you 've just finished the last step of the *local setup*. This guide uses `my-staging-app` as Heroku app name.

**Requirements**   
Have a [Heroku](https://id.heroku.com/signup) and an [Amazon S3 account](http://aws.amazon.com/s3/).

**Steps**

1. Set `STAGING_HEROKU_APP` to `my-staging-app` in `fabfile.py`
2. Make a Github app for staging on https://github.com/settings/applications:
  1. Click on `Register new application`
  2. As `Authorization callback URL` write `https://my-staging-app.herokuapp.com/accounts/github/login/callback/`
  3. As `HomePage URL` write `https://my-staging-app.herokuapp.com`
  4. Write whatever you want for the other fields and click on `Register application`
  5. Copy the value of `Client Secret` to the value of `ALLAUTH_SOCIAL_APP_GITHUB_SECRET` in `.heroku_env/staging.txt`
  6. Copy the value of `Client ID` to the value of `ALLAUTH_SOCIAL_APP_GITHUB_ID` in `inonemonth/settings/staging.py`

3. Setup mailing
4. Setup Amazon S3 configurations:
    1. [Create a bucket](http://www.hongkiat.com/blog/amazon-s3-the-beginners-guide/#Gettting_an_Amazon_S3_Account) called `inonemonth`
    2. Copy the domain of your bucket url to `STATIC_URL` in `inonemonth/settings/production.py` 
    3. Copy the value of `Access Key ID` to the value of `AWS_ACCESS_KEY_ID` in `.heroku_env/staging.txt`
    4. Copy the value of `Secret Access Key` to the value of `AWS_SECRET_ACCESS_KEY` in `.heroku_env/staging.txt`

5. heroku login
6. heroku keys:add
7. Create the `my-staging-app` heroku app and push code to heroku:   
  `fab stag_initial_deploy:branch=master`


**Handy comamnds**

* Make command for regular push




Similar for production. 

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
3. Set up vagrant for inonemonth, this takes about 12 mins 53 secs with a connection of 54 Mb/s:   
  `vagrant up`
4. Crawl into your vagrant box:  
   `vagrant ssh`  
5. Go to the toplevel django dir of the project:   
  `cd /vagrant/inonemonth`     
   It doesn't matter what you answer when prompted to source `.env` at this stage.
6. Make a github app for local developent on https://github.com/settings/applications:
  1. Click on `Register new application`
  2. As `Authorization callback URL` write `http://localhost:8000/accounts/github/login/callback/`
  3. As `HomePage URL` write `http://localhost:8000`
  4. Write whatever you want for the other fields and click on `Register application`
  5. Copy the value of `Client Secret` to the value of `ALLAUTH_SOCIAL_APP_GITHUB_SECRET` in `.env`.
  6. Copy the value of `Client ID` to the value of `ALLAUTH_SOCIAL_APP_GITHUB_ID` in `inonemonth/settings/local.py`.
7. Create a gmail address for sending automated mails:   
   Copy the email address and password to the values of `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` in `.env`.
8. Load local environment variables:   
   `source .env`
9. Get into the local virtual environment:    
   `workon inonemonth_local`

You can now run the local server (db is already set up with syncdb and migrate):  
  `fab loc:runserver`


**Testing**  
If you are still in the `inonemonth_local` env, first run `deactivate`.  

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

The following deploys the app to a staging environment on Heroku. It is assumed you 've just finished the last step of the *local setup*.

**Requirements**   
Have a [Heroku account](https://id.heroku.com/signup).

**Steps**

1. Setup github app
2. Setup mailing
3. fab stag_new_db:heroku_app=my_staging_app,branch=master



**Handy comamnds**

* Make comamnd for regular push






(I should modify fab command a line is skipped if I place a # sign)

Not advised but it will work with these settings
SECRET_KEY=my_secret_key
DBUSER=me
DBPASSWORD=my_password

Get these yourself
EMAIL_HOST_USER=some_email@gmail.com
EMAIL_HOST_PASSWORD=some_password
AWS_ACCESS_KEY_ID=GKIAJFM6TMFHH4SBRDOQ
AWS_SECRET_ACCESS_KEY=dwKXYggGcnb7R2UgMcL0H8t5mpMRUkHoAzql7mTk
ALLAUTH_SOCIAL_APP_GITHUB_SECRET=K29bf835bc0c98K0fc7a9cc106f88b89016225


Modify admin email address to send error mails


Similar for staging.


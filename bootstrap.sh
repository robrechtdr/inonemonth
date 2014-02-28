#!/usr/bin/env bash

#VAGRANT_HOME = "/home/vagrant"

sudo apt-get update

sudo apt-get install -y git
sudo apt-get install -y vim 

# Necessary for pip installing psycopg2
sudo apt-get install -y postgresql
sudo apt-get install -y libpq-dev

# Install development stuff (Python).
sudo apt-get -y install python-pip 

# Needed to install PIL
sudo apt-get -y install python-dev

sudo pip install -U fabric

sudo pip install -U ipython

# Install the Heroku toolbelt.
wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh

# Create a postgres db with username root
sudo -u postgres createuser $USER --superuser

sudo apt-get -y install curl

git clone git://github.com/kennethreitz/autoenv.git ~/.autoenv

# shld work (or use /home/vagrant)
echo 'source ~/.autoenv/activate.sh' >> ~/.profile

# install with wget
curl -s https://raw.github.com/brainsik/virtualenv-burrito/master/virtualenv-burrito.sh | $SHELL

# This should be appended to ~/.profile or ~/.bashrc
# + /root/.venvburrito/startup.sh should be made executable 
echo 'source ~/.venvburrito/startup.sh' >> ~/.profile

source ~/.profile

cd /vagrant

###########################
# Set up environment files
###########################
# ¢opy .env file from .script_templates if it doesn't exist
if [ ! -f inonemonth/.env ]; then
    echo ".env not found!"
    cp .script_templates/.env inonemonth/.env  
    echo "Copied .env from .script_templates"

fi


# Make a .heroku_env dir if it doesn't already exist
mkdir -p inonemonth/.heroku_env


# ¢opy .heroku_env/base.txt file from .script_templates if it doesn't exist
# Careful, this file is read differently then .env! Don't put comments in there 
if [ ! -f inonemonth/.heroku_env/base.txt ]; then
    echo ".heroku_env/base.txt not found!"
    cp .script_templates/.heroku_env/base.txt inonemonth/.heroku_env/base.txt
    echo "Copied .heroku_env/base.txt from .script_templates"

fi


# ¢opy .heroku_env/staging.txt file from .script_templates if it doesn't exist
# Careful, this file is read differently then .env! Don't put comments in there 
if [ ! -f inonemonth/.heroku_env/staging.txt ]; then
    echo ".heroku_env/staging.txt not found!"
    cp .script_templates/.heroku_env/staging.txt inonemonth/.heroku_env/staging.txt
    echo "Copied .heroku_env/staging.txt from .script_templates"

fi


# ¢opy .heroku_env/production.txt file from .script_templates if it doesn't exist
# Careful, this file is read differently then .env! Don't put comments in there 
if [ ! -f inonemonth/.heroku_env/production.txt ]; then
    echo ".heroku_env/production.txt not found!"
    cp .script_templates/.heroku_env/production.txt inonemonth/.heroku_env/production.txt
    echo "Copied .heroku_env/production.txt from .script_templates"

fi


############################

mkvirtualenv inonemonth_local

pip install -r requirements/local.txt 

# Why doesn't port forwarding work?

cd inonemonth 
echo "y"

source .env

fab loc_new_db

deactivate

mkvirtualenv inonemonth_test
pip install -r ../requirements/test.txt
# I don't have permission in vagrant ssh to run mkvirtualenv though

# when doing `vagrant ssh` you get
# -bash: /home/vagrant/.autoenv/activate.sh: No such file or directory

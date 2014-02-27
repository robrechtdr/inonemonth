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

########
# ¢opy .env file from .script_templates if it doesn't exist

if [ ! -f .env ]; then
    echo ".env not found!"
    cp .script_templates/.env inonemonth/.env  
    echo "Copied .env from .script_templates"

fi


# ¢opy .heroku_env file from .script_templates if it doesn't exist
# Careful, this file is read differently then .env! Don't put comments in there 

if [ ! -f .heroku_env.txt ]; then
    echo ".heroku_env.txt not found!"
    cp .script_templates/.heroku_env.txt inonemonth/.heroku_env.txt
    echo "Copied .heroku_env.txt from .script_templates"

fi

#######


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

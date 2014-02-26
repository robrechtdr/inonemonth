#!/usr/bin/env bash

VAGRANT_HOME = "/home/vagrant"

apt-get update

apt-get install -y git
apt-get install -y vim 


# Necessary for pip installing psycopg2
apt-get install -y postgresql
apt-get install -y libpq-dev
# You might also have to run:
#apt-get install postgresql-server-dev-all

# Install development stuff (Python).
#apt-get -y install python-dev python-pip build-essential python-gpgme
apt-get -y install python-pip 

# Needed to install PIL
apt-get -y install python-dev

pip install -U fabric

#apt-get -y install libpq-dev libevent-dev
#sudo pip install -U virtualenvwrapper autoenv
#sudo pip install git+git://github.com/kevinw/pyflakes.git
#sudo pip install -U pip

pip install -U ipython

# Install the Heroku toolbelt.
wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh

# Create a postgres db with username root
# How to automate saying yes?
#sudo -u postgres createuser $USERNAME
# How to say y ?
echo "y"|sudo -u postgres createuser $USER --superuser
# Shall the new role be a superuser? y


apt-get -y install curl

git clone git://github.com/kennethreitz/autoenv.git /home/vagrant/.autoenv

# shld work (or use /home/vagrant)
echo 'source ~/.autoenv/activate.sh' >> /home/vagrant/.profile


# install with wget
#curl -s https://raw.github.com/brainsik/virtualenv-burrito/master/virtualenv-burrito.sh | $SHELL
#curl -s https://raw.github.com/brainsik/virtualenv-burrito/master/virtualenv-burrito.sh | exclude_profile=1 $SHELL

#source /root/.venvburrito/startup.sh

# This should be appended to ~/.profile or ~/.bashrc
# + /root/.venvburrito/startup.sh should be made executable 
#echo '/root/.venvburrito/startup.sh' >> ~/.profile
#echo '/root/.venvburrito/startup.sh' >> /home/vagrant/.profile

pip install virtualenv
pip install virtualenvwrapper

echo 'export WORKON_HOME=/home/vagrant/.virtualenvs' >> /home/vagrant/.profile
echo 'source /usr/local/bin/virtualenvwrapper.sh' >> /home/vagrant/.profile
echo 'export PIP_VIRTUALENV_BASE=$WORKON_HOME' >> /home/vagrant/.profile
echo 'export PIP_RESPECT_VIRTUALENV=true' >> /home/vagrant/.profile

source /home/vagrant/.profile

cd /vagrant

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

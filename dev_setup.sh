# Enabling adding apt repository
sudo apt-get install -y software-properties-common

# Setting up Postgres latest key in apt
sudo add-apt-repository "deb https://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main"
wget --quiet -O - https://postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add - 

# Setting up Rabbitmq apt key
sudo add-apt-repository "deb http://www.rabbitmq.com/debian/ testing main"
wget --quiet -O - https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | sudo apt-key add - 

# Installing up Postgres and Rabbitmq
sudo apt-get update
sudo apt-get install -y libpq-dev postgresql-9.4 rabbitmq-server --force-yes

# Installing phantomjs
sudo npm install -g phantomjs

# Allow rabbitmq-management to access from host browser
sudo bash -c "echo '[{rabbit, [{loopback_users, []}]}].' >> /etc/rabbitmq/rabbitmq.config"

# Enable rabbitmq-management to be viewed host browser
sudo rabbitmq-plugins enable rabbitmq_management

# creating user with createdb permission
sudo -u postgres psql -c "CREATE USER vagrant WITH PASSWORD 'root'; ALTER USER vagrant CREATEDB"
# creating db, executing seperately as db creation cannot be cascaded or done in a transaction
sudo -u postgres psql -c "CREATE DATABASE in_accounts_dev OWNER vagrant"

# Setting up virtual environment
sudo pip install virtualenvwrapper
export WORKON_HOME=$HOME/Env
source /usr/local/bin/virtualenvwrapper.sh

# Setting up application
mkvirtualenv -p /usr/bin/python3.4 in_accounts
export DJANGO_SETTINGS_MODULE=in_accounts.settings.development
cd /vagrant

#Remove .example extension
cp in_accounts/settings/development.py.example in_accounts/settings/development.py
cp requirements/development.txt.example requirements/development.txt
cp env_var.py.example env_var.py
cp reports/settings.py.example reports/settings.py

pip install -r requirements/development.txt
python manage.py migrate
python manage.py loaddata fixture reports/fixtures/report_type.json reports/fixtures/report_setting_state.json

# Setting up application settings at the time of vagrant login
echo 'export WORKON_HOME=$HOME/Env' >> /home/vagrant/.bashrc
echo 'source /usr/local/bin/virtualenvwrapper.sh' >> /home/vagrant/.bashrc
echo 'workon in_accounts && cd /vagrant' >> /home/vagrant/.bashrc
echo 'export DJANGO_SETTINGS_MODULE=in_accounts.settings.development' >> /home/vagrant/.bashrc
echo 'python manage.py runserver 0.0.0.0:8000' >> /home/vagrant/.bashrc

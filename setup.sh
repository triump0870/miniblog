#!/bin/bash

set -e

sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get install -y linux-image-extra-$(uname -r) linux-image-extra-virtual
sudo apt-get install -y gcc mysql-client libmysqlclient-dev build-essential
sudo apt-get install -y apt-transport-https ca-certificates
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"

sudo apt-get update
apt-cache policy docker-ce
sudo apt-get update
sudo apt-get install -y docker-ce
sudo apt-get autoremove -y
sudo curl -o /usr/local/bin/docker-compose -L "https://github.com/docker/compose/releases/download/1.16.1/docker-compose-$(uname -s)-$(uname -m)"
sudo chmod +x /usr/local/bin/docker-compose
sudo apt-get install -y python3-pip
export LC_ALL=C
locale
sudo pip3 install --upgrade pip
sudo -H pip3 install fabric3 django-environ
sudo chmod 666 /var/run/docker.sock
sudo service docker start

mv miniblog/settings/local.env.example miniblog/settings/local.env

echo "You need to reboot the system"
echo "Type 'yes' to continue, or 'no' to abort:"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) echo "System is going for restart";
              sudo reboot; break;;
        No ) echo "Don't forget to restart the system";
             fab build_images; exit;;
    esac
done

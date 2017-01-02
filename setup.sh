#!/bin/bash

set -e

sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get install -y linux-image-extra-$(uname -r) linux-image-extra-virtual
sudo apt-get install -y gcc mysql-client libmysqlclient-dev build-essential
sudo apt-get install -y apt-transport-https ca-certificates
sudo apt-key adv \
           --keyserver hkp://ha.pool.sks-keyservers.net:80 \
           --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
echo "deb https://apt.dockerproject.org/repo ubuntu-xenial main" \
 | sudo tee /etc/apt/sources.list.d/docker.list
sudo apt-get update
apt-cache policy docker-engine
sudo apt-get update
sudo apt-get install -y docker-engine
sudo apt-get autoremove -y
sudo curl -o /usr/local/bin/docker-compose -L "https://github.com/docker/compose/releases/download/1.8.1/docker-compose-$(uname -s)-$(uname -m)"
sudo chmod +x /usr/local/bin/docker-compose
sudo apt-get install -y python3-pip
export LC_ALL=C
locale
sudo pip3 install --upgrade pip
sudo -H pip3 install fabric3 django-environ
echo "You need to reboot the system"
echo "Type 'yes' to continue, or 'no' to abort:"
read res
if ( "$res" == "yes" ); then
    ehco "System is going for restart"
    sudo reboot
else
    echo "Aborted, but remember to restart your system to use the upgraded packages"
fi
#!/bin/bash

sudo apt-get update
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
sudo curl -L https://github.com/docker/compose/releases/download/1.9.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo service docker start

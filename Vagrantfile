# encoding: utf-8
# This file originally created at http://rove.io/ed4f780b39f13a85e28057bf4856bf33

# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.box = "precise64.box"
  config.ssh.forward_agent = true

  config.vm.provision :chef_solo do |chef|
    chef.cookbooks_path = ["cookbooks"]
    chef.add_recipe :apt
    chef.add_recipe "system::install_packages"
    chef.json = {
      :system => {
          :packages => {
            :install => ["build-essential","python-dev","libpq-dev","python-virtualenv", "g++", "flex", "bison", "gperf", "ruby", "perl", "libsqlite3-dev", "libfontconfig1-dev", "libicu-dev", "libfreetype6", "libssl-dev", "libpng-dev", "libjpeg-dev", "libx11-dev", "libxext-dev", "mysql"]
          }
      }
    }
  end

  config.vm.provision :shell, privileged: false, path: "dev_setup.sh"

end

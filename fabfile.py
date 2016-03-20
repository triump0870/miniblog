from fabric.api import local
from os.path import dirname,join
import sys
import os

BASE_DIR = dirname(__file__)

def manage(command):
	manage_command = join(BASE_DIR,'src/manage.py')
	local('python %s %s'%(manage_command,command))

def init():
	local('git init')
	local('curl -u "triump0870:ohankissme0870" https://api.github.com/user/repo -d {"name":"rohan"}')
	local('git remote add origin git@github.com:triump0870/rohan.git')

def push(files='.',comment="Updated", branch='master'):
	local('git add %s'%files)
	local('git commit -m %s'%comment)
	local('git push origin %s'%branch)

def pull(branch='master'):
	local('git pull origin %s'%branch)


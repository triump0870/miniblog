from fabric.api import local
from os.path import dirname,join
import sys
import os

BASE_DIR = dirname(__file__)

def manage(command):
	manage_command = join(BASE_DIR,'src/manage.py')
	local('python %s %s'%(manage_command,command))
	
def push(files='.',comment="Updated", branch='master'):
	local('git add %s'%files)
	local('git commit -m %s'%comment)
	local('git push origin %s'%branch)

def pull(branch='master'):
	local('git pull origin %s'%branch)



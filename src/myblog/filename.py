from time import time
import uuid
from django.utils.deconstruct import deconstructible

@deconstructible
class generatefilename(object):
	''' Generates filename based on the time of upload'''
	def __init__(self, sub_path):
		self.path = sub_path

	def __call__(self, instance, filename):
		ext = filename.split('.')[-1]
		prefix = '-%s.%s'%(uuid.uuid4(),ext)
		return self.path+str(int(time()))+prefix
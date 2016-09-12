from __future__ import unicode_literals

from django.test import TestCase
from blog.models import Tag, Post


class TestTag(TestCase):
	
	def setUp(self):
		
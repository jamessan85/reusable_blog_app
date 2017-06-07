# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import post
# Create your tests here.

class PostTests(TestCase):

    def test_str(self):
        test_title = post(title='My latest blog post')
        self.assertEqual(str(test_title),
                         'My latest blog post')

# -*- coding: utf-8 -*-

from {{{ package.namespace }}}.{{{ package.namespace2 }}}.{{{ package.name }}}.interfaces import IExample
from five import grok

grok.templatedir('templates')

class HelloWorld (IExample):
    ''' Browserview
    '''

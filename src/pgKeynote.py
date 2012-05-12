'''
Created on Apr 24, 2012

@author: lgoff
'''
import from appscript import app, k

class PGKeynote(object):
    '''
    PGKeynote class extends PowerGlove 
    '''


    def __init__(self,params):
        '''
        Constructor
        '''
        pass
    
    def sendKey(self,key):
        app('System Events').keystroke(key, using=k.command_down)
        pass
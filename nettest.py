# -*- coding: utf-8 -*-

"""
    @description: this programas is for test the computer internet connection
    @author: Manuel Parra
    @date: 12/01/19
"""

import subprocess
import sys

class chargetest:
    hosts = list()

    def __init__(self, hosts):
        self.hosts = hosts

    def ping(self, host):
        if sys.platform.lower()[:3] == 'lin':
            ret = subprocess.call(['ping', '-c', '3', '-W', '5', host],
                                  stdout=open('/dev/null', 'w'),
                                  stderr=open('/dev/null', 'w'))
        elif sys.platform.lower()[:3] == 'win':
            ret = subprocess.call(['ping', '-n', '3', '-w', '5', host],
                                  stdout=open('type c:\autoexec.bat > NUL',
                                  'w'),
                                  stderr=open('type c:\autoexec.bat > NUL',
                                  'w'))
        return ret == 0

    def isnetup(self):
        status = 0
        for host in self.hosts:
            if self.ping(host):
                status = 1
                break
        return status

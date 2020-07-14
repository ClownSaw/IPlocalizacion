#!/usr/bin/env python3
# encoding: UTF-8

__author__ = 'ClownSaw'

from datetime import datetime
import os
from termcolor import colored
from sys import platform as _platform


if _platform == 'win32':
    import colorama
    colorama.init()

def Red(value):
        return colored(value, 'red', attrs=['bold'])
    
def Green(value):
    return colored(value, 'green', attrs=['bold'])
    
          
class Logger:
    
    def __init__(self, nolog=False, verbose=False):
        self.NoLog = nolog
        self.Verbose = verbose
        
        
    def WriteLog(self, messagetype, message):
        filename = '{}.log'.format(datetime.strftime(datetime.now(), "%Y%m%d"))
        path = os.path.join('.', 'logs', filename)
        with open(path, 'a') as logFile:
            logFile.write('[{}] {} - {}\n'.format(messagetype, datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S"), message))
              
              
    def PrintError(self, message):
        """Print/Log error message"""
        if not self.NoLog:
            self.WriteLog('ERROR', message)
        
        print('[{}] {}'.format(Red('ERROR'), message))
    
    
    def PrintResult(self, title, value):
        """print result to terminal"""
        print('{}: {}'.format(title, Red(value)))
    
    
    def Print(self, message):
        """print/log info message"""
        if not self.NoLog:
            self.WriteLog('INFO', message)
            
        if self.Verbose:
            print('[{}] {}'.format(Green('**'), message))
    
    
    def PrintIPGeoLocation(self, ipGeoLocation):
        """print IP Geolocation information to terminal"""
        self.PrintResult(Green('Target'), ipGeoLocation.Query)
        self.PrintResult(Green('IP'), ipGeoLocation.IP)
        self.PrintResult(Green('ASN'), ipGeoLocation.ASN)
        self.PrintResult(Green('City'), ipGeoLocation.City)
        self.PrintResult(Green('Country'), ipGeoLocation.Country)
        self.PrintResult(Green('Country Code'), ipGeoLocation.CountryCode)
        self.PrintResult(Green('ISP'), ipGeoLocation.ISP)
        self.PrintResult(Green('Latitude'), str(ipGeoLocation.Latitude))
        self.PrintResult(Green('Longitude'), str(ipGeoLocation.Longtitude))
        self.PrintResult(Green('Organizatión'), ipGeoLocation.Organization)
        self.PrintResult(Green('Región Code'), ipGeoLocation.Region)
        self.PrintResult(Green('Región Name'), ipGeoLocation.RegionName)
        self.PrintResult(Green('Timezone'), ipGeoLocation.Timezone)
        self.PrintResult(Green('Zip Code'), ipGeoLocation.Zip)
        self.PrintResult(Green('Google Maps'), ipGeoLocation.GoogleMapsLink)
        print()
        #.encode('cp737', errors='replace').decode('cp737')
    

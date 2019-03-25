# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
# import urlparse
import os.path
from datetime import datetime
from dateutil import tz

try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse

url_list = []



def time_remaining(request):
    d = datetime(2019, 3, 29, 23, 0,0,0,tz.tzoffset('GMT', 0))
    
    # book.creationTime = book.creationTime.replace(tzinfo=EST)
    dnow = datetime.utcnow()
    dnow = dnow.replace(tzinfo=tz.tzoffset('CET', 3600))
    
    #birthday = datetime(1988, 2, 19, 12, 0, 0)
    diff =d - dnow
    # print diff

#     tussen = dnow.s
#     DateTime startTime = DateTime.Now;

#  DateTime endTime = DateTime.Now.AddSeconds( 75 );

#  TimeSpan span = endTime.Subtract ( startTime );


    seconds = diff.total_seconds()
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    retval = 'hours: '
    retval += str(round(hours)) #(diff.hour + diff.timetuple().tm_yday * 24)
    retval += ' minutes: ' + str(round(minutes)) # diff.minute
    retval += ' seconds: ' + str(round(seconds)) # diff.second
    # tzlocal = tz.tzoffset('GMT', 0)
    # local = naive.replace(tzinfo=tzlocal)
    # now = utcnow.astimezone(tzlocal)

    # utcnow = datetime.utcnow().replace(tzinfo=tz.tzutc())


    
    # s = ''
    # add_url(request)
    # for entry in url_list:
    #     s += entry + '<br/>'

    return HttpResponse(retval)

def index(request):
    s = ''
    add_url(request)
    for entry in url_list:
        s += entry + '<br/>'

    return HttpResponse(s)

def add_url(request):
    path = request.path
    if '//' not in path:
        s = ''
        temp = ""
        
        #first entry is empty
        temp = os.path.split(path)
        path = temp[0]

        while path != '/':
            temp = os.path.split(path)
            path = temp[0]
            if temp[1] != 'urlparts':
                s += temp[1] + '---'

        #remove last ---
        s = s[:len(s)-3]

        url_list.append(s)

from django.shortcuts import render
from django.http import HttpResponse
import re
import requests
import json
import socket
from urllib.request import urlopen

# key: AKIAIDOF3JTWMWSD3SEQ 
# secret: 2/lxtJ4vBOo6EN9hH5X83QXbn1t1jqmqn9oP1uFC 


# Create your views here.
def myView(request):

    hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method
    IP = socket.gethostbyname(hostname)
## printing the hostname and ip_address
    print(f"Hostname: {hostname}")
    #print(f"IP Address: {ip_address}")


    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    #response = requests.get(url)
    data = json.load(response)

    #IP=data['ip']
    org=data['org']
    org= org[7:]
    city = data['city']
    country=data['country']
    region=data['region']

    print ('Your IP detail\n ')
    print ('IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'.format(org,region,country,city,IP))

    #return HttpResponse('hello world')
    return render(request, 'index.html', {'IP':IP,'org':org,'city': city, 'country': country, 'region':region})
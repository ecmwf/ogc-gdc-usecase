#!/usr/bin/env python3

from polytope.api import Client

# Instantiate and configure the client
# If using EmailKey or Bearer credentials, you can specify them in the Client constructor
# You can disregard these parameters if you have specified your credentials via environment 
# variables or configuration file
c = Client(user_email = '<user_email>',
           user_key = '<user_api_key>')

# List the available collections to retrieve from
c.list_collections()

request = {
    'stream': 'oper',
    'levtype': 'pl',
    'levellist': '1/10/30/50/70/100/150/200/250/300/400/500/600/700/750/800/850/875/900/925/950/975/1000',
    'param': '129.128/130.128/131/132/133.128/135.128/138.128/155.128/157.128',
    'step': '0/1/2/3/4/5/6/7',
    'time': '00:00:00',
    'date': '20161028',
    'type': 'fc',
    'class': 'rd',
    'expver': 'ht3e',
    'domain': 'g'
}

# Retrieve data
c.retrieve('ecmwf-mars', request, 'ht3e.grib')


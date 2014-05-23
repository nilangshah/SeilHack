'''
	Data is stored in mongodb.Establish the connection and use it to extract data.
'''

import pymongo as pym
import json
def establish_connection_to_host(host,port):
	
	client = pym.Connection(host,port)
	return client

def connect_to_database(client,database_name):
	db = client[database_name] 
	return db



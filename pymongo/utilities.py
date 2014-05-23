from string import split
import time
from datetime import datetime
import random
def getDateComponents(date_str):
	date_components = date_str.split('/')
	month = int(date_components[0])
	day = int(date_components[1])
	year = int(date_components[2])

	return day,month,year


def get_epoch_time(day,month,year,hr,minute,second):
	epoch = datetime(year,month,day,hr,minute,second).strftime('%s')
	return int(epoch)

def getTimeComponents(time_str):
	''' get the time in hh:mm:ss format'''
	time_components = time_str.split(':')
	hr = int(time_components[0])
	mint = int(time_components[1])
	sec = int(time_components[2])
		
	return hr,mint,sec
	

def getDateComponentsFromWeek(week,year,weekday):
	needed_format = '%d %d %d' %(int(year),int(week) - 1,weekday)
	resulting_date = time.strptime(needed_format , '%Y %W %w')

	day = resulting_date.tm_mday
	month = resulting_date.tm_mon
	year = resulting_date.tm_year

	return day,month,year

		
		


'''
	apis to get the data from the database

'''

#from connect import  *
from utilities_kresit import *
from datetime import date,timedelta

def get_data_on_date(db_handle,table_name,date_string):
	'''
		get data of X date
		X = mm/dd/yyyy
	'''
	day,month,year = getDateComponents(date_string) 
	start_epoch_time= get_epoch_time(day,month,year,0,0,0)
	end_epoch_time= get_epoch_time(day,month,year,23,59,59)

	#get the data from the collection 
	data_list = []
	for doc in db_handle[table_name].find({'timestamp':{'$gte':start_epoch_time,'$lte':end_epoch_time}}):
		data_list.append(doc)

	return data_list

def get_data_of_hour_on_date(db_handle,table_name,hour,date_string):
	'''
		get data of X hour on Z date
		X = 0 to 23
		Z = mm/dd/yyyy
	'''
	day,month,year = getDateComponents(date_string)
	start_epoch_time = get_epoch_time(day,month,year,hour,0,0)
	end_epoch_time = get_epoch_time(day,month,year,hour,59,59)
	
	data_list = []
	for doc in db_handle[table_name].find({'timestamp':{'$gte':start_epoch_time,'$lte':end_epoch_time}}):
		data_list.append(doc)

	return data_list

def get_data_from_date_to_date(db_handle,table_name,from_date,end_date):
	'''
		get data from X date to Y date
		X & Y = mm/dd/yyyy
	'''
	s_day,s_month,s_year = getDateComponents(from_date)
	e_day,e_month,e_year = getDateComponents(end_date)
	
	start_epoch_time = get_epoch_time(s_day,s_month,s_year,0,0,0)
	end_epoch_time = get_epoch_time(e_day,e_month,e_year,23,59,59)
	
	data_list=  []
	for doc in db_handle[table_name].find({'timestamp':{'$gte':start_epoch_time,'$lte':end_epoch_time}}):
		data_list.append(doc)

	return data_list

def get_hdata_from_date_to_date(db_handle,table_name,from_date,end_date):
	'''
		get data from X date to Y date
		X & Y = mm/dd/yyyy
	'''
	s_day,s_month,s_year = getDateComponents(from_date)
	e_day,e_month,e_year = getDateComponents(end_date)
	
	start_epoch_time = get_epoch_time(s_day,s_month,s_year,0,0,0)
	end_epoch_time = get_epoch_time(e_day,e_month,e_year,23,59,59)
	
	data_list=  []
	for doc in db_handle[table_name].find({'epoch':{'$gte':start_epoch_time,'$lte':end_epoch_time}}):
		data_list.append(doc)

	return data_list


def get_data_from_hour_to_hour_on_date(db_handle,table_name,from_hour,end_hour,date_string):
	
	'''
	 get the data from X hour to Y hour on Z date
	 X = 0 to 23
	 Y = 0 to 23
	 Z = mm/dd/yyyy
	'''
	day,month,year = getDateComponents(date_string)
	
	start_epoch_time = get_epoch_time(day,month,year,from_hour,0,0)
	end_epoch_time = get_epoch_time(day,month,year,end_hour,59,59)
	
	data_list=  []
	for doc in db_handle[table_name].find({'timestamp':{'$gte':start_epoch_time,'$lte':end_epoch_time}}):
		data_list.append(doc)

	return data_list
	

	

def get_data_on_date_first_last(db_handle,table_name,date_string):
	'''
		get data of X date
		X = mm/dd/yyyy
	'''
	day,month,year = getDateComponents(date_string) 
	start_epoch_time= get_epoch_time(day,month,year,0,0,0)
	end_epoch_time= get_epoch_time(day,month,year,23,59,59)

	data_list = []
	for doc in db_handle[table_name].find({'timestamp':start_epoch_time}):
		data_list.append(doc)
		
	for doc in db_handle[table_name].find({'timestamp':end_epoch_time}):
		data_list.append(doc)
	return data_list

	
#Below function gives data of current day from start of the day to current time
def get_data_on_today_first_last(db_handle,table_name,date_string):
	'''
		get data of X date
		X = mm/dd/yyyy
	'''
	day,month,year = getDateComponents(date_string) 
	start_epoch_time= get_epoch_time(day,month,year,0,0,0)
	tm=datetime.now().strftime('%H:%M:%S')
	
	hour,minute,second = getTimeComponents(tm)
	end_epoch_time= get_epoch_time(day,month,year,hour,minute,second)

	data_list = []
	for doc in db_handle[table_name].find({'timestamp':start_epoch_time}):
		data_list.append(doc)
		
	for doc in db_handle[table_name].find({'timestamp':end_epoch_time}):
		data_list.append(doc)
	return data_list

#Below function returns peak power of the day	
def get_peak_power_data(db_handle,table_name,date_string):
	'''
		get data of X date
		X = mm/dd/yyyy
	'''
	
	data_list = []
	day,month,year = getDateComponents(date_string)
	
	start_epoch_time = get_epoch_time(day,month,year,0,0,0)
	end_epoch_time = get_epoch_time(day,month,year,23,59,59)
	
	for doc in db_handle[table_name].find({'timestamp':{'$gte':start_epoch_time,'$lte':end_epoch_time}}).sort([('values.W', -1)]).limit(1):
		data_list.append(doc)
	#data_list=db_handle[table_name].get_column_name()	
	return data_list
	
def get_data_on_last_200_epoch(db_handle,table_name,date_string):
	'''
		get data of X date
		X = mm/dd/yyyy
	'''
	day,month,year = getDateComponents(date_string) 
	#start_epoch_time= get_epoch_time(day,month,year,0,0,0)
	d1=datetime.now()
	d=d1-timedelta(seconds=330)

	tm1=d1.strftime('%H:%M:%S')
	
	
	tm=d.strftime('%H:%M:%S')
#	print d
#	print d1
#	print tm
#	print tm1
	hour1,minute1,second1 = getTimeComponents(tm1)
	hour,minute,second = getTimeComponents(tm)
	end_epoch_time= get_epoch_time(day,month,year,hour1,minute1,second1)
	
	start_epoch_time=get_epoch_time(day,month,year,hour,minute,second)
#	print start_epoch_time
#	print end_epoch_time
	data_list = []
	for doc in db_handle[table_name].find({'timestamp':{'$gte':start_epoch_time,'$lte':end_epoch_time}}):
		data_list.append(doc)
		
	
	return data_list

from connect import *
from get_raw_data_kresit import *
from datetime import date, timedelta
import urllib
import sys
from dateutil import parser

if __name__ == '__main__':
	client = establish_connection_to_host("10.129.28.202",27017) 
	db = connect_to_database(client,"smartmeter")
	
	#data_list = get_data_from_hour_to_hour_on_date(db,"data",10,10,"03/14/2014")
	#data_list = get_data_from_hour_to_hour_on_date(db,"data",13,14,"04/28/2014")
	outputstr = '';
	
	
	#Calculate consumption for today	
	
	#Calculate consumption for last 14 days
	month_count=sys.argv[1]
	parameter=sys.argv[2]

	if month_count == '1' and parameter == '1':
		today=date.today()
		end=date.today()
		end_date=end.strftime("%m/%d/%Y")

		start=date.today()-timedelta(days=30)
		start_date=start.strftime("%m/%d/%Y")
	        meter=get_hdata_from_date_to_date(db,"hour",start_date,end_date)		
		for i in range(0,len(meter)-1):
			outputstr = outputstr + str(meter[i]["A"]) + ","
	
		outputstr = outputstr + str(meter[len(meter)-1]["A"])
		
	elif month_count == '1' and parameter == '2':
		today=date.today()
		end=date.today()
		end_date=end.strftime("%m/%d/%Y")

		start=date.today()-timedelta(days=30)
		start_date=start.strftime("%m/%d/%Y")
		meter=get_hdata_from_date_to_date(db,"hour",start_date,end_date)		
		#print len(meter)
		for i in range(0,len(meter)-1):
		        outputstr = outputstr + str(meter[i]["V2"]) + ","
		
		outputstr = outputstr + str(meter[len(meter)-1]["V2"])
	elif month_count == '1' and parameter == '3':
		today=date.today()
		end=date.today()
		end_date=end.strftime("%m/%d/%Y")

		start=date.today()-timedelta(days=30)
		start_date=start.strftime("%m/%d/%Y")
	        meter=get_hdata_from_date_to_date(db,"hour",start_date,end_date)		
		#print len(meter)
		for i in range(0,len(meter)-1):
		        outputstr = outputstr + str(meter[i]["W"]) + ","
		
		outputstr = outputstr + str(meter[len(meter)-1]["W"]) 
		
	elif month_count == '2' and parameter == '1':
		today=date.today()
		end=date.today()
		end_date=end.strftime("%m/%d/%Y")

		start=date.today()-timedelta(days=60)
		start_date=start.strftime("%m/%d/%Y")
		meter=get_hdata_from_date_to_date(db,"hour",start_date,end_date)		
		#print len(meter)
		for i in range(0,len(meter)-1):
		        outputstr = outputstr + str(meter[i]["A"]) + ","
		
		outputstr = outputstr + str(meter[len(meter)-1]["A"])
	elif month_count == '2' and parameter == '2':
		today=date.today()
		end=date.today()
		end_date=end.strftime("%m/%d/%Y")

		start=date.today()-timedelta(days=60)
		start_date=start.strftime("%m/%d/%Y")
		meter=get_hdata_from_date_to_date(db,"hour",start_date,end_date)		
		#print len(meter)
		for i in range(0,len(meter)-1):
		        outputstr = outputstr + str(meter[i]["V2"]) + ","
		
		outputstr = outputstr + str(meter[len(meter)-1]["V2"]) 
		
	else:
		today=date.today()
		end=date.today()
		end_date=end.strftime("%m/%d/%Y")

		start=date.today()-timedelta(days=90)
		start_date=start.strftime("%m/%d/%Y")
		meter=get_hdata_from_date_to_date(db,"hour",start_date,end_date)		
		#print len(meter)
		for i in range(0,len(meter)-1):
		        outputstr = outputstr + str(meter[i]["W"]) + ","
		
		outputstr = outputstr + str(meter[len(meter)-1]["W"])
		
	
	print outputstr

	



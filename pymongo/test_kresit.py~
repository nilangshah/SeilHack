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
	perday_energy=open("kresit_energy_vs_temprature.csv","w+")
	
	perday_energy.write("Date,Energy,Temprature\n")
	
	#Calculate consumption for today
	d=date.today()
	data_form=d.strftime("%m/%d/%Y")	
	#meter=get_data_on_today_first_last(db,"data",data_form)
	#energy=float(meter[1]["values"]["FwdWh"])-float(meter[0]["values"]["FwdWh"])
	#temp_t=urllib.urlopen("http://api.wunderground.com/api/0b22cdc8b9ea32db/history_"+d.strftime("%Y%m%d")+"/q/19.13,72.91.json")
	#temp=json.loads(temp_t.read())
	#perday_energy.write(str(data_form)+","+str(energy)+","+ str (temp["history"]["dailysummary"][0]["meantempm"])+"\n")
	
	
	
	#Calculate consumption for last 14 days
	date_str=sys.argv[1]
	date_components = date_str.split('/')
	month = int(date_components[0])
	day = int(date_components[1])
	year = int(date_components[2])
	dr=datetime.strptime(date_str,"%m/%d/%Y")
	for i in range(1,5):
		d=dr-timedelta(days=i)
		data_form=d.strftime("%m/%d/%Y")	
		meter=get_data_on_date_first_last(db,"data",data_form)
		#print meter[i]
		energy=float(meter[1]["values"]["FwdWh"])-float(meter[0]["values"]["FwdWh"])
		temp_t=urllib.urlopen("http://api.wunderground.com/api/0b22cdc8b9ea32db/history_"+d.strftime("%Y%m%d")+"/q/19.13,72.91.json")
		temp=json.loads(temp_t.read())
		perday_energy.write(str(data_form)+","+str(energy)+","+ str (temp["history"]["dailysummary"][0]["meantempm"])+"\n")
		
	
	

	perday_energy.close()



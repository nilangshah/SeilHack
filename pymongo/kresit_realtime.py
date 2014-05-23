from connect import *
from get_raw_data_kresit import *
from datetime import date, timedelta
import urllib
import datetime


if __name__ == '__main__':
	client = establish_connection_to_host("10.129.28.202",27017) 
	db = connect_to_database(client,"smartmeter")	
	kresit_current_data=open("kresit_data.csv","w+")
	kresit_current_data.write("current,A1,A2,A3,voltage,power,frequency\n")
	print 
	#Calculate consumption for today
	d=date.today()
	data_form=d.strftime("%m/%d/%Y")	
	meter=get_data_on_today_first_last(db,"data",data_form)
	current=float(meter[1]["values"]["A"])
	A1=float(meter[1]["values"]["A1"])
	A2=float(meter[1]["values"]["A2"])
	A3=float(meter[1]["values"]["A3"])
	voltage=float(meter[1]["values"]["V1"])
	power=float(meter[1]["values"]["W"])
	frequency=float(meter[1]["values"]["F"])
	time_temp=int(meter[1]["timestamp"])	
	time=datetime.datetime.fromtimestamp(time_temp).strftime('%H:%M:%S')	
	print "{ \"time\":\""+str(time)+"\",\"current\":\""+str(current)+"\", \"A1\":\""+str(A1)+"\",\"A2\":\""+str(A2)+"\",\"A3\":\""+str(A3)+"\",\"voltage\":\""+str(voltage)+"\",\"power\":\""+ str(power)+ "\",\"frequency\":\""+str(frequency)+"\"}\n"
	kresit_current_data.write(str(current)+","+str(A1)+","+str(A2)+","+str(A3)+","+str(voltage)+","+str(power)+","+str(frequency)+"\n")	
	kresit_current_data.close()



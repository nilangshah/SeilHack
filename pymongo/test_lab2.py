from connect import *
from get_raw_data import *
from datetime import date, timedelta
date_data=[]
if __name__ == '__main__':
	client = establish_connection_to_host("10.129.23.100",27017) 
	db = connect_to_database(client,"SEIL_smartmeters")
		
	date_now=time.strftime("%m/%d/%Y")
	
	perday_energy=open("appliance_energy_data2.csv","w+")
	perday_energy.write("Date,Energy1,Energy2,Energy3,Total,Occupancy,PerCapitaEnergy,PeakPower1,PeakPower2,PeakPower3\n")
	
	d=date.today()
	data_form=d.strftime("%m/%d/%Y")	
	meter1=get_data_on_today_first_last(db,"meter1",data_form)
	meter2=get_data_on_today_first_last(db,"meter2",data_form)
	meter3=get_data_on_today_first_last(db,"meter3",data_form)
	meter1_peak=get_peak_power_data(db,"meter1",data_form)	
	meter2_peak=get_peak_power_data(db,"meter2",data_form)	
	meter3_peak=get_peak_power_data(db,"meter3",data_form)	
	peak_power1=meter1_peak[0]["W"]	
	peak_power2=meter2_peak[0]["W"]	
	peak_power3=meter3_peak[0]["W"]	
	
	energy1=meter1[1]["FwdWh"]-meter1[0]["FwdWh"]
	energy2=meter2[1]["FwdWh"]-meter2[0]["FwdWh"]
	energy3=meter3[1]["FwdWh"]-meter3[0]["FwdWh"]
	rand_no=random.randrange(4,9)	
	perday_energy.write(str(data_form)+","+str(energy1)+","+str(energy2)+","+str(energy3)+","+str(energy1+energy2+energy3)+","+str(rand_no)+","+str((energy1+energy2+energy3)/rand_no)+","+str(peak_power1)+","+str(peak_power2)+","+str(peak_power3)+"\n")
	for i in range(1,8):
		d=date.today()-timedelta(days=i)
		data_form=d.strftime("%m/%d/%Y")	
		meter1=get_data_on_date_first_last(db,"meter1",data_form)
		meter2=get_data_on_date_first_last(db,"meter2",data_form)
		meter3=get_data_on_date_first_last(db,"meter3",data_form)
		meter1_peak=get_peak_power_data(db,"meter1",data_form)	
		meter2_peak=get_peak_power_data(db,"meter2",data_form)	
		meter3_peak=get_peak_power_data(db,"meter3",data_form)	
		peak_power1=meter1_peak[0]["W"]	
		peak_power2=meter2_peak[0]["W"]	
		peak_power3=meter3_peak[0]["W"]	
	
		energy1=meter1[1]["FwdWh"]-meter1[0]["FwdWh"]
		energy2=meter2[1]["FwdWh"]-meter2[0]["FwdWh"]
		energy3=meter3[1]["FwdWh"]-meter3[0]["FwdWh"]
		rand_no=random.randrange(4,9)	
		perday_energy.write(str(data_form)+","+str(energy1)+","+str(energy2)+","+str(energy3)+","+str(energy1+energy2+energy3)+","+str(rand_no)+","+str((energy1+energy2+energy3)/rand_no)+","+str(peak_power1)+","+str(peak_power2)+","+str(peak_power3)+"\n")

	perday_energy.close()

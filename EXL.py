import pandas as pd
df=pd.read_excel(r'C:\Users\tanya\Downloads\final.xlsx')
t1=df[:3144]
t2=df[3142:6284]
t3=df[6284:9426]
t4=df[9426:12568]
t5=df[12568:15710]
t6=df[15710:18852]
t7=df[18852:21994]
t8=df[21994:25136]
t9=df[25136:28278]
t10=df[28278:31420]
t11=df[31420:34562]
t12=df[34562:37704]
t13=df[37704:40846]
t14=df[40846:43988]
t15=df[43988:47130]

a={48: 254, 13: 159, 51: 121, 21: 120, 29: 115, 20: 105, 17: 102, 37: 100, 19: 99,
   47: 95, 31: 93, 18: 92, 39: 88, 27: 87, 26: 83, 28: 82, 40: 77, 5: 75, 55: 72, 1: 67, 12: 67, 42: 67, 46: 66, 8: 64, 22: 64, 36: 63, 6: 59, 30: 56,
       54: 55, 38: 53, 45: 46, 16: 44, 53: 39, 41: 36, 35: 33, 2: 30, 49: 29, 24: 24,
       56: 23, 34: 21, 32: 17, 23: 16, 4: 15, 25: 14, 50: 12, 33: 10, 9: 8, 15: 5, 44: 5,
       10: 3, 11: 1}
pop_state={1: 4822023, 2: 727554, 4: 6553255, 5: 2949131, 6: 38041430, 8: 5129284, 
           9: 3590347, 10: 917092, 11: 632323, 12: 16726533, 13: 9919945, 15: 1392313, 
           16: 1595728, 17: 12875255, 18: 6537334, 19: 3074186, 20: 2885905, 21: 4380415,
           22: 4601893, 23: 1329192, 24: 5884563, 25: 6646144, 26: 9883360, 27: 5379139,
           28: 2984926, 29: 6021988, 30: 1005141, 31: 1855525, 32: 2758931, 33: 1320718, 
           34: 8864590, 35: 2085538, 36: 19570261, 37: 9752073, 38: 699628, 39: 11544225,
           40: 3814820, 41: 3899353, 42: 12763536, 44: 1050292, 45: 4723723, 46: 826595, 
           47: 6456243, 48: 26059203, 49: 2855287, 50: 626011, 51: 8179903, 53: 6897012,
           54: 1855413, 55: 5726398, 56: 314400}

def value(a):
    x=a['stateFIPS']
    f=a['C_TOT_POP']/pop_state[x]
    google=((a['google_mobility_retail_and_recreation']+100)+(a['google_mobility_grocery_and_pharmacy']+100)+(a['google_mobility_parks']+100)+(a['google_mobility_transit_stations']+100)+(a['google_mobility_workplaces']+100))*(a['C_TOT_POP']/1000000000)
    #print('f:',f,'google:',google)
    apple=((a['apple_mobility_transit']*0.000001)+(a['apple_mobility_driving']*0.000005))*a['C_TOT_POP']*f
    electricity=((a['Electricity_Sales_Customers_Count_Commercial']*0.0005)+(a['Electricity_Sales_Customers_Count_Industrial']*0.0001)+(a['Electricity_Sales_Customers_Count_Transportation']*0.0005))*f
    yoy=a['YoY_Reopened_Seated_Diner_Data']*a['C_TOT_POP']*(0.0000025/15)
    test=a['new_test_count']*f
    p=(a['new_test_rate']*pop_state[x])/(100000*a['S_D_dly_new_test'])
    onset=a['hospital_onset_covid_SD']*f
    previous_day_adult=(a['previous_day_admission_adult_covid_confirmed_SD']*f)+(a['previous_day_admission_adult_covid_suspected_SD']*f*p)
    previous_day_paedritic=(a['previous_day_admission_pediatric_covid_confirmed_SD']*f)+(a['previous_day_admission_pediatric_covid_suspected_SD']*f*p)   
    total_adult=(a['total_adult_patients_hospitalized_confirmed_covid_SD']+((a['total_adult_patients_hospitalized_confirmed_and_suspected_covid_SD']-a['total_adult_patients_hospitalized_confirmed_covid_SD'])*p))*f
    total_child=(a['total_pediatric_patients_hospitalized_confirmed_covid_SD']+((a['total_pediatric_patients_hospitalized_confirmed_and_suspected_covid_SD']-a['total_pediatric_patients_hospitalized_confirmed_covid_SD'])*p))*f
    extra=(a['inpatient_beds_SD']/a['inpatient_beds_coverage_SD'])*(a['critical_staffing_shortage_today_yes_SD']*f)
    extra=extra+(extra/2)
    s=google+apple+electricity+yoy+test+onset+previous_day_adult+previous_day_paedritic+total_adult+total_child
    
    #print('google:',google,'apple:',apple,'electricity:',electricity,'yoy:',yoy,'test:',test,'onset:',onset,'previous_day_adult:',previous_day_adult,'previous_day_paedritc:',previous_day_paedritic,'total_child:',total_child,'total_adult:',total_adult,'extra:',extra)
    
    
    
    
    if(int(s)==0):
        return(1)
    return(int(s))
    
r=[]
#for i in range(0,1):
 #   a=t1.loc[i]
  
print(t1.loc[0])
    
for i in range(3144):
    x=t1.loc[i]
    c=value(x)
    r.append(c)
for i in range(3142,6284):
    x=t2.loc[i]
    c=value(x)
    r.append(c)
for i in range(6284,9426):
    x=t3.loc[i]
    c=value(x)
    r.append(c)
for i in range(9426,12568):
    x=t4.loc[i]
    c=value(x)
    r.append(c)
for i in range(12568,15710):
    x=t5.loc[i]
    c=value(x)
    r.append(c)
for i in range(15710,18852):
    x=t6.loc[i]
    c=value(x)
    r.append(c)
for i in range(18852,21994):
    x=t7.loc[i]
    c=value(x)
    r.append(c)
for i in range(21994,25136):
    x=t8.loc[i]
    c=value(x)
    r.append(c)
for i in range(25136,28278):
    x=t9.loc[i]
    c=value(x)
    r.append(c)
for i in range(28278,31420):
    x=t10.loc[i]
    c=value(x)
    r.append(c)
for i in range(31420,34562):
    x=t11.loc[i]
    c=value(x)
    r.append(c)

for i in range(34562,37704):
    x=t12.loc[i]
    c=value(x)
    r.append(c)


df=pd.DataFrame()
df['confirmed_cases']=r
df.to_excel('exl.xlsx',index=False)




  

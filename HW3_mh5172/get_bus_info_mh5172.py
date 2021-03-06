import requests
import json
import pandas as pd
import sys
url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + sys.argv[1] +'&VehicleMonitoringDetailLevel=calls&LineRef='+ sys.argv[2]
if not len(sys.argv) == 4:
    print ('wrong input')
else:
    data = requests.get(url)
    text = json.loads(data.text)
    siri_read = text['Siri']
    ServiceDelivery_read = siri_read['ServiceDelivery']
    VehicleMonitoringDelivery_read = ServiceDelivery_read['VehicleMonitoringDelivery']
    if 'ErrorCondition' in VehicleMonitoringDelivery_read[0]:
        if 'API key is not authorized' in VehicleMonitoringDelivery_read[0]['ErrorCondition']['OtherError']['ErrorText']:
            print ('API key is not authorized')
        elif 'No such route' in VehicleMonitoringDelivery_read[0]['ErrorCondition']['OtherError']['ErrorText']:
            print ('No such route')
    else:
        VehicleActivity_read = VehicleMonitoringDelivery_read[0]['VehicleActivity']
        num = len(VehicleActivity_read)
        LNG = []
        LAT = []
        STOP_NAME = []
        STATUS = []
        for i in range(num):
            MonitoredVehicleJourney_read = VehicleActivity_read[i]['MonitoredVehicleJourney']
            location = MonitoredVehicleJourney_read['VehicleLocation']
            OnwardCalls_read = MonitoredVehicleJourney_read['OnwardCalls']
            LNG.append(location['Longitude'])
            LAT.append(location['Latitude'])
            if OnwardCalls_read == {}:
                STOP_NAME.append('N/A')
                STATUS.append('N/A')
            else:
                Onwardcall_read = OnwardCalls_read['OnwardCall']
                STOP_NAME.append(Onwardcall_read[0]['StopPointName'])
                STATUS.append(Onwardcall_read[0]['Extensions']['Distances']['PresentableDistance'])
        file = pd.DataFrame({'Latitude':LAT,'Longitude':LNG,'Stop_Name':STOP_NAME,'Status':STATUS})
<<<<<<< HEAD
        file.to_csv('%s'%(sys.argv[3]),sep = ',')
=======
        file.to_csv('%s'%(sys.argv[3]),sep = ',')
>>>>>>> 5fb84949c86b1f389cef8e0fa6ae2ac001bcedfa

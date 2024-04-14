import os
import json
from datetime import datetime 

def store_event_in_file(dir_name = "logFolder",file_name = "master.txt",event_data={}):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    file_path = os.path.join(dir_name,file_name)
    
    local_Time = datetime.now()
    formated_Time = "Event Time : " + local_Time.strftime("%Y-%m-%d %H:%M:%S")+"\n"

    with open(file_path,"a") as file:
        file.write(formated_Time)
        for event in event_data:
            json.dump(event,file)
            file.write('\n')
        
        file.write('\n\n')



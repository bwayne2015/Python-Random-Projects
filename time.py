import datetime
import time
print("**********************Welcome to your personal Reminder setter************")
ask_time_input = input("Time? : ")
description = input("What to remind")
get_time = datetime.datetime.now().time()
get_time_hour = str(get_time)
print(get_time)
hour_time = get_time_hour.split(":")
print(hour_time)
set_time = hour_time.pop()
print(set_time)
print(hour_time)
ask_list = []
ask_list.append(ask_time_input)
print(ask_list)
des_list = []
des_list.append(description)
print(des_list)
if ask_list:
    #print("vghjb")
    for x in ask_list:
        if(get_time_hour == x):
            print("reminder")
            sleep(60)
        else:
            print("no")
            
            pass
        


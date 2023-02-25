'''
Sun Sensors - Stats for Calibration
'''

import math as m
import statistics as stats

# This is the main fuction that will carry
# most of the operations and return a dict
# with that info. 
def stats_func(array):
    std_dev=stats.stdev(array)
    mean_d = stats.mean(array)
    std_error = std_dev/m.sqrt(len(array))
    data_max=max(array)
    data_min=min(array)
    print("Standard Deviation: ",std_dev)
    print("Mean: ", mean_d)
    print("Standard Error: ", std_error)
    print("Max Value: ",data_max)
    print("Min Value: ",data_min)
    s_dict={'std_dev':std_dev,'mean':mean_d,'std_error':std_error,'max':data_max,'min':data_min}
    return s_dict

def map(oldval, oldmin, oldmax, newmin, newmax):
    return((((oldval - oldmin) * (newmax - newmin)) / (oldmax - oldmin)) + newmin)

# This is a changing name, use it for whatever file.
file=open("data6_raw_attempt2.txt","r")
s1=file.readlines()
# Since we are importing a string.
# we remove the brackets and then
# Split the values to create an array.
# This method works with this file, change accordingly.
s1 = s1[0][1:-2]
s1 = s1.split(',')

f_data=[]
for i in s1:
    f_data.append(float(i))
print("Data: ",s1)
stat_dict = stats_func(f_data)


with open("data6_raw_stats_test.txt","w") as external_file:
    print(stat_dict,file=external_file)
    external_file.close()

map_data=[]
for i in range(len(s1)):
    value = map(f_data[i], stat_dict['min'], stat_dict['max'], 0, 1)
    map_data.append(float(value))
print("Data: ",map_data)

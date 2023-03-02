# 1. Create a JSON file (employee.json) containing employee information of minimum 5 employees. 
#    Each employee information consists of Name, DOB, Height, City, State. Write a python program that reads 
#    this information from the JSON file and saves the information into a list of objects of Employee class. 
#    Finally print the list of the Employee objects.

import json

file = open("C:\\Users\\Nithin\\Documents\\Python cls\\PRACTICE SESSION\\PYTHON\\Assignment_6_\\employee.json")
data = json.load(file)
for i in data["employee_details"]:
    print(f'Name = {i["name"]} \nDOB={i["DOB"]} \nHeight={i["Height"]} \nCity={i["City"]} \nState={i["State"]} \n')




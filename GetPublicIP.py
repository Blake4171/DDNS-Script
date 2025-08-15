import yaml
import requests
import json
import os
from datetime import datetime

def public_ip():

    #load the contents of yaml folder created and stored in same directory. Store as the f variable
    with open('ddns.yaml') as f:
        config = yaml.safe_load(f)

# ip_public is what the url is stored under in the yaml file. This gets that url and stores it as the ip_url variable
    ip_url = config.get("ip_public")

# using the url, make a request to ipify 
    response = requests.get(ip_url)
    ip_address = response.text.strip() # response.text gets the body of the http request .strip removes any trailing whitespace
    return ip_address
public_ip()

#def current_ip():
    # store the current date & time as the variable timestamp
    #timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #.strftime details what format 'timestamp' should be outputted as 

    #print contents of 'ip_address' and 'timestamp' variables 
    #print("The public ip is", public_ip(),'at',timestamp)
    
 #   print(public_ip())

  #  current_ip()

def check_ip(): 
    with open("IPcheck.json", "r") as file: #opens and reads json file 'IPcheck.json
       last_ip = json.load(file) #stores contents as 'last_ip'

    if last_ip == public_ip:  
        print('There has been no recent change in your networks public IP')
    else:
        with open('IPcheck.json', 'w')as file: #if ip store in json 'last_ip' is not the same as the current IP. Store the new IP in the json file
            json.dump(public_ip(), file)

    
    
check_ip()   



 
    

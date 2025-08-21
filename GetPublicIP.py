import yaml
import requests
import json
import os
from datetime import datetime


def current_ip():

    #load the contents of yaml folder created and stored in same directory. Store as the f variable
    with open('ddns.yaml') as f:
        config = yaml.safe_load(f)

# ip_public is what the url is stored under in the yaml file. This gets that url and stores it as the ip_url variable
    ip_url = config.get("ip_public")

# using the url, make a request to ipify 
    response = requests.get(ip_url)
    ip_address = response.text.strip() # response.text gets the body of the http request .strip removes any trailing whitespace
    return ip_address
current_ip()

def ip_2json(): 
    with open("IPcheck.json", "r") as file: #opens and reads json file 'IPcheck.json
       last_ip = json.load(file) #stores contents as 'last_ip'

    if last_ip != current_ip: 
        with open('IPcheck.json', 'w')as file: #if ip store in json 'last_ip' is not the same as the current IP. Store the new IP in the json file
            json.dump(current_ip(), file)
            return(last_ip, current_ip)
        
ip_2json()   

def update_dns():
    if ip_2json != current_ip:
        client.dns.records.update(
            zone_id=zone_id,
            dns_record_id=record_id,
            type="A",
            name="",
            content=current_ip(),
            ttl=300,
            proxied=True
            )

update_dns()




 
    

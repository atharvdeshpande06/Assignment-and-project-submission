from fastapi import FastAPI
import requests
import json
url="https://outpost.mapmyindia.com/api/security/oauth/token"   #URL for Post request
app=FastAPI()   #Creating object for FastAPI
r=requests.post(url,{"grant_type":"client_credentials","client_id":"Client-id","client_secret":"Client-secret"}) #Creadential for Post request
t=r.content  #Respose of Post request
j=json.loads(t)  #Creating the json object
@app.get("/ref-location/{Location}")     #making the endpoint
def work(location:str=""):
    url = "https://atlas.mapmyindia.com/api/places/nearby/json?explain&richData&&keywords=school&refLocation="+location+"&itemCount=5"    #URL for Get Request
    r = requests.get(url, {"token_type": j["token_type"], 'access_token': j["access_token"]})     #Credential for Get request
    return json.loads(r.content)["suggestedLocations"][0:5]  #returnig the json object respon
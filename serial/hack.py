import serial
import time
import requests
ser = serial.Serial('COM9', 9600, timeout=1)

def scrivi(x):
    #x=input(">")
    ser.write(bytes(x, "utf-8"))         

while True:
    ser.flushInput()
    response=ser.read(12)    

    if response != b'':
        responsereal=response.decode().replace(' ','')
        print(responsereal)
        URL = "http://localhost:8080/api/v1/story"
        PARAMS = {
            'textile_id': responsereal,
            'place':'lavatrice',
            'comment':'',
            'code':'0'
            }
        r = requests.post(URL, json=PARAMS)        
        data = r.json()
        print(data)        
        if(data["message"] == "error"):
            scrivi("<")

    time.sleep(1)

ser.close()
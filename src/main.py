# -*- coding: utf-8 -*-
#!/usr/bin/python

import random
import math
import requests
import json
import time

class RedAlert():

    def __init__(self):

        # initialize locations list
        self.locations = self.get_locations_list()
        # cookies
        self.cookies = ""
        # initialize user agent for web requests
        self.headers = {
           "Host":"www.oref.org.il",
           "Connection":"keep-alive",
           "Content-Type":"application/json",
           "charset":"utf-8",
           "X-Requested-With":"XMLHttpRequest",
           "sec-ch-ua-mobile":"?0",
           "User-Agent":"",
           "sec-ch-ua-platform":"macOS",
           "Accept":"*/*",
           "sec-ch-ua": '".Not/A)Brand"v="99", "Google Chrome";v="103", "Chromium";v="103"',
           "Sec-Fetch-Site":"same-origin",
           "Sec-Fetch-Mode":"cors",
           "Sec-Fetch-Dest":"empty",
           "Referer":"https://www.oref.org.il/12481-he/Pakar.aspx",
           "Accept-Encoding":"gzip, deflate, br",
           "Accept-Language":"en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        }
        # intiiate cokies
        self.get_cookies()


    def get_cookies(self):
        HOST = "https://www.oref.org.il/"
        r = requests.get(HOST,headers=self.headers)
        self.cookies = r.cookies

    def get_coordinates(self,location_name):

        #This function will get city coordinates by given city name
        #so later on it will be possible to visualization the flying rocket to the city
        HOST = "https://maps.google.com/maps/api/geocode/json?address=%s" % location_name
        r = requests.get(HOST, headers=self.headers)
        j = json.loads(r.content)
        return j["results"][0]["geometry"]["location"]

    def random_coordinates(self,latitude,longitude):

        # get random coordinates within the city for random visualization
        # radius of the circle
        circle_r = 1
        # center of the circle (x, y)
        circle_x = latitude
        circle_y = longitude
        # random angle
        alpha = 2 * math.pi * random.random()
        # random radius
        r = circle_r * random.random()
        # calculating coordinates
        x = r * math.cos(alpha) + circle_x
        y = r * math.sin(alpha) + circle_y
        return {"latitude":x,"longitude":y}

    def count_alerts(self,alerts_data):
        # this function literally return how many alerts there are currently
        return len(alerts_data)

    def get_locations_list(self):

        '''
        This function is to build a locations list of cities and the time they have
        before the rocket hit the fan. for better parsing later
        '''

        f = open('targets.json', encoding='utf-8')
        # returns JSON object as 
        return json.load(f)

    def get_red_alerts(self):

        # get red alerts
        HOST = "https://www.oref.org.il/WarningMessages/alert/alerts.json"
        r = requests.get(HOST, headers=self.headers, cookies=self.cookies)
        alerts = r.content.decode("UTF-8").replace("\n","").replace("\r","")
        if(len(alerts) <= 1):
            return None
        # parse the json response
        j = json.loads(r.content)
        # check if there is no alerts - if so, return null.
        if(len(j["data"]) == 0):
            return None
        # initialize the current timestamp to know when the rocket alert started
        j["timestamp"] = time.time()
        # parse data
        return j

def main():

    # initalize the red alert object
    alert = RedAlert()
    # check for alerts all the time and do stuff, never stop.
    while True:
        # set empty alert data dict
        alert_data = {}
        city_data = []
        migun_time = 0
        # sleep 1 second before checking alerts over again to not put pressure on the server.
        time.sleep(1)
        # get alerts from pikud ha-oref website
        red_alerts = alert.get_red_alerts()
        # if there is red alerts right now, get into action, quickly!
        if(red_alerts != None):
            # loop through each city there is red alert currently
            for alert_city in red_alerts["data"]:
                # get unique alert id for the current looping alerts
                alert_id = red_alerts["id"]
                # get the data of the current alert code
                for i in alert.locations:
                    if(alert.locations[i]["label"] == alert_city):
                        migun_time = alert.locations[i]["migun_time"]
                        # set the timestamp of the current alert
                        city_data.append(alert.locations[i])
                        # get the coordinates of the city where the rocket is flying to
                        '''
                        # Google Maps requires API key #
                        '''
                        #alert_data["coordinates"] = alert.get_coordinates(location_name=alert_city)
                        # random coordinates where the rocket should fly to in the visualization map
                        #alert_data["random_coordinates"] = alert.random_coordinates(latitude=alert_data["coordinates"]["lat"],longitude=alert_data["coordinates"]["lng"])
                red_alerts["cities_labels"] = city_data
                red_alerts["time_to_run"] = migun_time
                '''
                In this block you do what you have to do with your code,
                now when you have all what you could possibly have including:
                alert id, alert city, time to run away, coordinates of city,
                random coordinates where the missle may land and timestamp when the missle started fireup.
                '''
        else:
            print("[-] No alerts for now, keep checking ...")

if __name__ == "__main__":
    main()

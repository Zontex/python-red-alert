# -*- coding: utf-8 -*-
#!/usr/bin/python

import requests
import json
import time

class RedAlert():

    def __init__(self):

        # initialize locations list
        self.locations = self.get_locations_list()
        # initialize user agent for web requests
        self.headers = {"User-Agent":""}

    def get_coredinates(location_name):

        #This function will get city cordinates by given city name
        #so later on it will be possible to virtualize the flying rocket to the city
        return True

    def random_cordinates(longtitude,latitude):

        # get random cordinates within the city for random virtualization
        return True

    def count_alerts(alerts_data):
        # this function literally return how many alerts there are currently
        return len(alerts_data)

    def get_locations_list(self):

        '''
        This function is to build a locations list of cities and the time they have
        before the rocket hit the fan. for better parsing later
        '''

        # table of keys > values of the time people have to get a shelter
        string_to_miliseconds = {
            "3 דקות":"180000",
            "דקה וחצי":"90000",
            "דקה":"60000",
            "45 שניות":"45000",
            "30 שניות":"30000",
            "15 שניות":"15000",
            "מיידי":"10000"
        }

        # open csv with unparsed data
        csv = open("targets.csv", "r")
        # prepare empty dictionary
        locations = {}

        # for each line in the csv, we gonna parse it baby
        for line in csv:
            # split the line with "," so we know where things belongs to
            line = line.split("\n")[0].split(",")
            # get town name
            location_name = line[0]
            # get time people have to run in miliseconds
            time_to_run = string_to_miliseconds[line[1]]
            # get town code name where the rocket is about to fall
            alert_code = line[2]
            # align it all beautifully into a row
            row = {alert_code:{"location_name":location_name,"time_to_run":time_to_run}}
            # update locations dictionary
            locations.update(row)
        # close the csv to save memory
        csv.close()
        # finally, return the locations
        return locations

    def get_red_alerts(self):

        # get red alerts
        HOST = "http://www.oref.org.il/WarningMessages/Alert/alerts.json?v=1"
        r = requests.get(HOST, headers=self.headers})
        # parse the json response
        j = json.loads(r.content)
        # check if there is no alerts - if so, return null.
        if(len(j["data"]) == 0):
            return None
        # initialize the current timestamp to know when the rocket alert started
        j["timestamp"] = time.time()
        return j

def main():

    # initalize the red alert object
    alert = RedAlert()
    # check for alerts all the time and do stuff, never stop.
    while True:
        # get alerts from pikud ha-oref website
        red_alerts = alert.get_red_alerts()
        # if there is red alerts right now, get into action, quickly!
        if(red_alerts != None):
            # loop through each city there is red alert currently
            for alert_code in red_alerts["data"]:
                # get the data of the current alert code
                alert_data = alert.locations[alert_code]
                # set the timestamp of the current alert
                alert_data["ts"] = red_alerts["ts"]
                # get the cordinates of the city where the rocket is flying to
                alert_data["cordinates"] = alert.get_coredinates(location_name=alert_data["location_name"])
                # random cordinates where the rocket should fly to in the virtualization map
                alert_data["random_cordinates"] = alert.random_cordinates(longtitude=alert_data["cordinates"][0],latitude=alert_data["cordinates"][1])

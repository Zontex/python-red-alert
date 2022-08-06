<p align="center">
  <img src="https://pbs.twimg.com/media/Dsc_wzpWkAI-Srm.jpg">
</p>

# Description

API Class to get data about rockets flying from Gaza strip to Israel.
the API use's the official public API provided by "Pikud ha-oref" in Israel.

## Mivtza halot-ha-shahar Update

On August 5th 2022 the Islamic Jihad opened an attack on Israel sending hundreds of rockets per day targeting Israeli civilians.
The API was updated to suport the latest locations, cities and districts.

Google API currently disabled because it requires API key, if you still need the API apply your own Google key to make it work.

## Features

* Get red-alerts in real-time from "Pikud ha-oref" public API
* Fetch location data from alerts codes (coordinates, city names, time to run for shelters)
* Generate random coordinates within a city for visualization of a flying rocket
* Count number of alerts currently there is

Example response from the API:
``` json
{
  "id": "133042653750000000",
  "cat": "1",
  "title": "ירי רקטות וטילים",
  "data": [
    "מטווח ניר עם",
    "גבים, מכללת ספיר",
    "שדרות, איבים, ניר עם"
  ],
  "desc": "היכנסו למרחב המוגן ושהו בו 10 דקות",
  "timestamp": 1659791786.927377,
  "cities_labels": [
    {
      "label": "מטווח ניר עם",
      "value": "20C0B212CB4A85AB765743BB2A748106",
      "areaid": 26,
      "areaname": "עוטף עזה",
      "label_he": "מטווח ניר עם",
      "migun_time": 15,
      "city_data": {
        "label": "מטווח ניר עם I אזור עוטף עזה",
        "rashut": "",
        "value": "0",
        "areaid": 26,
        "mixname": "מטווח ניר עם I אזור עוטף עזה | עוטף עזה",
        "color": "O"
      }
    },
    {
      "label": "גבים, מכללת ספיר",
      "value": "89679BD023B4DE666AD79E1470E20D83",
      "areaid": 26,
      "areaname": "עוטף עזה",
      "label_he": "גבים, מכללת ספיר",
      "migun_time": 15,
      "city_data": {
        "label": "גבים, מכללת ספיר I אזור עוטף עזה",
        "rashut": "מועצה אזורית: שער הנגב",
        "value": "0",
        "areaid": 26,
        "mixname": "גבים, מכללת ספיר I אזור עוטף עזה | עוטף עזה",
        "color": "O"
      }
    },
    {
      "label": "שדרות, איבים, ניר עם",
      "value": "C5FD35F7510C4E1D535EDD8DE05A7961",
      "areaid": 26,
      "areaname": "עוטף עזה",
      "label_he": "שדרות, איבים, ניר עם",
      "migun_time": 15,
      "city_data": {
        "label": "ניר עם I אזור עוטף עזה",
        "rashut": "מועצה אזורית: שער הנגב",
        "value": "0",
        "areaid": 26,
        "mixname": "ניר עם I אזור עוטף עזה | עוטף עזה",
        "color": "O"
      }
    },
    {
      "label": "שדרות, איבים, ניר עם",
      "value": "3202695F8E2D49A4FCA18B95A88C0CA4",
      "areaid": 26,
      "areaname": "עוטף עזה",
      "label_he": "שדרות, איבים, ניר עם",
      "migun_time": 15,
      "city_data": {
        "label": "שדרות I אזור עוטף עזה",
        "rashut": "",
        "value": "0",
        "areaid": 26,
        "mixname": "שדרות I אזור עוטף עזה | עוטף עזה",
        "color": "O"
      }
    },
    {
      "label": "שדרות, איבים, ניר עם",
      "value": "F53EA9083272E342ADE0146DA1C25E59",
      "areaid": 26,
      "areaname": "עוטף עזה",
      "label_he": "שדרות, איבים, ניר עם",
      "migun_time": 15,
      "city_data": {
        "label": "איבים I אזור עוטף עזה",
        "rashut": "מועצה אזורית: שער הנגב",
        "value": "0",
        "areaid": 26,
        "mixname": "איבים I אזור עוטף עזה | עוטף עזה",
        "color": "O"
      }
    }
  ],
  "time_to_run": 15
}
```

# FAQ

## Q) Why is this even helpful?

*    The Class I made is helpful for developers and makers as one
     Who are willing to develop platforms / apps based on Israeli "Pikud ha-oref" system.
     The class provides the necessary functions and tools to get the latest information
     About the Israeli missiles status and when Israel is under attack.

## Q) Can't the enemy use it against Israel?

*    No. All the information in the Class is public and available,
     All I did is to organize it at one place for easy access.
     I also scraped and organized the cities names with their area codes for easy reading.

## Q) Can I take the code and make a product of my own using your Class?

*    Absolutely. The code and everything inside the repository is open-sourced.
     The Code is under MIT license - please make sure to understand the meaning.
     The Code provided AS IS WITHOUT ANY WARRANTY.

## Q) How can I visualize how much time the rocket have till it will hit the city?

*    Use the milliseconds calculated from how much time left for people to run to shelters,
     Then visualize using that seconds of long the rocket has to fly till it will hit the city.
     
## Q) Is it possible to predict or to know where exactly the missile will land?

*    No, at least not for the developers. the military may have such capabilities.
     The prediction is not possible due to many parameters such as:
     Where the rocket came from, How much fuel is inside the rocket, at what speed is the rocket flying,
     Directions of the rocket and weather conditions - something which make it impossible for any
     non-military individual, even with technology such as machine learning and prediction algorithms.

# Requirements

* Python requests library
```sh
$ pip3 install requests
```

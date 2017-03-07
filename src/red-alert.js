// NodeJS module wrote by Samuel LESPES CARDILLO (@cyberwarfighte1)
// For Roni Gorodetsky red alert open source API
// -------------
// #############
// USAGE EXAMPLE
// #############
/** 
  var red_alert = require('red-alert');

  setInterval(function(){
    red_alert.get_alerts(function(alerts){
 
      // In this block you do what you have to do with your code,
      // now when you have all what you could possibly have including:
      // alert id, alert city, time to run away, coordinates of city,
      // random coordinates where the rocket may land and timestamp when the rocket was fired.

    })
  }, 1000) // sleep 1 sec. before checking alerts again to reduce server pressure.
**/

/*****************************
      PUBLIC FUNCTIONS
*****************************/

var exports   = module.exports = {}
  , request   = require('request')
  , fs        = require('fs')
  , readline  = require('readline')
  , locations = []
  , alerts    = []

/** 
 Check if there is ongoing alerts and add more precise details to them
 It return an array of objects.
 **/ 
exports.get_alerts = function(callback) {
  // load the locations
  get_locations_list();

  // get alerts from pikud ha-oref website
  check_oref(function(raw_alerts) {
    if(raw_alerts === null || !raw_alerts) return callback(null);
    var i = 0, alerts = [];

    // loop through every alerts in order to attach more details
    for(var key in raw_alerts) {
      try {
        alerts.push({
          id                  : alert[key].id,
          location            : locations[alerts[key]],
          timestamp           : alert[key].ts,
          coordinates         : get_coordinates(alert[key]["location_name"]),
          // random_coordinates  : random_coordinates(alert[key]["coordinates"]["lat"],alert[key]["coordinates"]["lng"])
        });
      } catch(e) {}

      // Return the alerts
      (i >= raw_alerts.length) ? return callback(alerts) : i++;
    }
  });
}

/** 
 This function literally return the number of ongoing alerts. 
 WARNING: The number of alerts is reinitialized everytime "get_alerts" is called
 **/
exports.count_alerts() {
  return alerts.length;
}


/*****************************
      PRIVATE FUNCTIONS
*****************************/

/** 
  This function will get city coordinates by given city name by using Google Maps API
 **/
function get_coordinates(location_name, callback) {
  request("https://maps.google.com/maps/api/geocode/json?address=" + location_name, function (error, response, body) {
    if(error) return callback(false);
    response = JSON.parse(response);

    return callback(response["results"][0]["geometry"]["location"]);
  })

}

/** 
 Get random coordinates within the city for random virtualization
 TO BE DONE<----
 **/
function random_coordinates(longitude, latitude, callback) {
  var circle_r, circle_x, circle_y, alpha, r, x, y;

  // radius of the circle
  circle_r = 1;
  // center of the circle (x, y)
  circle_x = latitude;
  circle_y = longitude;
  // random angle
  alpha = 2 * Math.pi * (Math.random() * (1 - 0) + 0);
  // random radius
  r = circle_r * (Math.random() * (1 - 0) + 0);
  // calculating coordinates
  x = r * Math.cos(alpha) + circle_x;
  y = r * Math.sin(alpha) + circle_y;

  return callback({"latitude":x,"longitude":y});
}

/** 
 This function is to build a locations list of cities and the time they have 
 before the rocket hit the area for better parsing.
 **/
function get_locations_list() {
  // table of keys > values of the time people have to get a shelter
  var string_to_miliseconds = {
      "3 דקות":"180000",
      "דקה וחצי":"90000",
      "דקה":"60000",
      "45 שניות":"45000",
      "30 שניות":"30000",
      "15 שניות":"15000",
      "מיידי":"10000"
  }

  var lineReader = require('readline').createInterface({
    input: require('fs').createReadStream('targets.csv')
  });

  lineReader.on('line', function (line) {
    var location_name, time_to_run, alert_code;

    // split the line with "," so we know where things belongs to
    line = line.split(",")
    // get town name
    location_name = line[0]
    // get time people have to run in miliseconds
    time_to_run = string_to_miliseconds[line[1]]
    // get town code name where the rocket is about to fall
    alert_code = line[2];
    // align it all beautifully into a row
    locations[alert_code] = {
      "location_name" : location_name,
      "time_to_run"   : time_to_run
    }
  });
}

/** 
 Check pikud ha-oref API endpoint in order to see if there is any active alerts
 **/
function check_oref(callback) {
  request("http://www.oref.org.il/WarningMessages/Alert/alerts.json?v=1", function (error, response, body) {
    if(error) return callback(false); // if there is an error in the request, return false

    response = JSON.parse(response); // parse the json response
    if(response["data"].length == 0) return callback(null); // check if there is no alerts - if so, return null.

    // initialize the current timestamp to know when the rocket alert started
    response["timestamp"] = new Date().getTime();
    
    return callback(response); // Return the alert
  });
}
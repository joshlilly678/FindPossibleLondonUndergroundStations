import requests
import json
from time import sleep

primary_key = "" # ENTER YOUR API KEY HERE. See https://api.tfl.gov.uk/ to register for a key.

def _url(path):
    return "https://api.tfl.gov.uk" + path

def get_all_tube_lines():
    counter = 0
    while counter < 10:
        response = requests.get(_url("/Line/Mode/tube?app_key=" + primary_key))
        
        # if 500 internal server error - try again
        if response.status_code not in [500, 503]:
            counter += 11
        else:
            print(response.status_code, "Status Code")
            sleep(2)
            counter += 1
        
    if response.status_code != 200:
        print("ERROR, status code:")
        print(response.status_code)
        print(response.json())
        
    # Parse Json Response
    response_json = response.json()
    leng = len(response_json)
    
    # Get list of tube names iterating through the response body
    tubes = []
    for i in range(leng):
        for key, value in response_json[i].items():
            if key == "name":
                tubes.append(value.replace(" & ", "-"))
                
    return tubes
    
def get_all_stations_on_line(lineName):
    counter = 0
    while counter < 10:
        response = requests.get(_url("/Line/" + lineName+ "/Arrivals?app_key=" + primary_key))
        
        # if 500 internal server error - try again
        if response.status_code not in [500, 503]:
            counter += 11
        else:
            print(response.status_code, "Status Code")
            sleep(2)
            counter += 1
    
    if response.status_code != 200:
        print("ERROR, status code:")
        print(response.status_code)
        print(response.json())
    
    # Parse Json Response
    response_json = response.json()
    
    leng = len(response_json)
    
    stations_ids = []
    stations_names = []
    for i in range(leng):
        for key, value in response_json[i].items():
            if key == "naptanId" and value not in stations_ids:
                stations_ids.append(value)
            if key == "stationName" and value not in stations_names:
                stations_names.append(value)
    
    return stations_ids
    
def create_line_station_dict():
    lines = get_all_tube_lines()
    line_station_dict = {}
    for line in lines:
        # line_station_dict.update( {line : get_all_stations_on_line(line) } )
        line_station_dict[line] = get_all_stations_on_line(line)
    
    return line_station_dict
    
def get_all_stations():
    lines = get_all_tube_lines()
    stations = []
    for line in lines:
        stations_on_line = get_all_stations_on_line(line)
        for station in stations_on_line:
            if station not in stations:
                stations.append(station)
                
    stations.sort()
    return stations

def shortest_duration_for_journey(start, end):
    # Start and end can be a postcode, station name, place name (ambiguous) etc

    counter = 0
    while counter < 10:
        response = requests.get(_url("/Journey/JourneyResults/" + start + "/to/" + end + "?app_key=" + primary_key))
        if response.status_code not in [500, 503]:
            counter += 11
        else:
            print(response.status_code, "Status Code")
            sleep(2)
            counter += 1
    
    if response.status_code != 200:
        print("ERROR, status code:")
        print(response.status_code)
        print(response.json())
        
    response_json = response.json()
    journeys = response_json["journeys"]
    leng = len(journeys)
    
    shortest_duration = 0
    for i in range(leng):
        for key, value in journeys[i].items():
            if key == "duration":
                if shortest_duration == 0:
                    shortest_duration = value
                elif shortest_duration > value:
                    shortest_duration = value
    
    return shortest_duration
    
def find_duration_from_station(end):
    stations = get_all_stations()
    journey_duration = {}
    for station in stations:

        counter = 0
        while counter < 10:
            response = requests.get(_url("/StopPoint/" + station + "?app_key=" + primary_key))
            if response.status_code not in [500, 503]:
                counter += 11
            else:
                print(response.status_code, "Status Code")
                sleep(2)
                counter += 1
        
        if response.status_code != 200:
            print("ERROR, status code:")
            print(response.status_code)
            print(response.json())
            
        response_json = response.json()
        commonName = response_json["commonName"]

        print("Station:", commonName)
        journey_duration[commonName] = shortest_duration_for_journey(station, end)
    
    return journey_duration

def main():
    #  ~~~ If you wish to run this script without the PyQt GUI. ~~~  #
    #  ~~~ Call the functions from within this function.        ~~~  #
    #  ~~~ Some examples below                                  ~~~  #
    
    # stations = get_all_stations()
    # for station in stations:
        # print(station)

    # bakerloo = get_all_stations_on_line("bakerloo")
    # central = get_all_stations_on_line("central")
    # circle = get_all_stations_on_line("circle")
    # district = get_all_stations_on_line("district")
    # hammersmith_city = get_all_stations_on_line("hammersmith-city")
    # jubilee = get_all_stations_on_line("jubilee")
    # metropolitan = get_all_stations_on_line("metropolitan")
    # northern = get_all_stations_on_line("northern")
    # piccadilly = get_all_stations_on_line("piccadilly")
    # victoria = get_all_stations_on_line("victoria")
    # waterloo_city = get_all_stations_on_line("waterloo-city")

    # print("bakerloo: ", bakerloo)
    # print("central: ", central)
    # print("circle: ", circle)
    # print("district: ", district)
    # print("hammersmith & city: ", hammersmith_city)
    # print("jubilee: ", jubilee)
    # print("metropolitan: ", metropolitan)
    # print("northern: ", northern)
    # print("piccadilly: ", piccadilly)
    # print("victoria: ", victoria)
    # print("waterloo & city: ", waterloo_city)

if __name__ == "__main__":
    main()

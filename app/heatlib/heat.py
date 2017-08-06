import os
import requests
import gmaps

class coordinates(object):

    def __init__(self, addr, lat, lng):
        self.addr = addr
        self.lat = lat
        self.long = lng

    def address(self):
        return self.addr

    def latitude(self):
        return self.lat

    def longitude(self):
        return self.long

def format_time(ins_date):

    format_check = check_date_format(ins_date)

    if format_check != True:
        return format_check
    beginning = ins_date + "T00:00:00"
    end = ins_date + "T23:59:59"
    return {"beginning" : beginning, "end" : end}

def check_date_format(fomatted_date):
    split_date = fomatted_date.split("-")

    if len(split_date) < 3:
        return "ERROR: Make sure you use '-' to partition date"
    for num in split_date:
        try:
            num = int(num)
        except ValueError:
            return "ERROR: Please only enter numbers"
    if len(split_date[0]) != 4:
        return "ERROR: Make sure the year is formatted correctly"
    elif len(split_date[1]) != 2 or int(split_date[1]) > 12:
        return "ERROR: Make sure the month is formatted correctly"
    elif len(split_date[2]) != 2 or int(split_date[2]) > 31:
        return "ERROR: Make sure the day is formatted correctly"
    else:
        return True

def get_city_data(start, finish):
    endpoint = "https://data.cityofnewyork.us/resource/8end-qv57.json"
    suffix = "start_date_time between '{0}' and '{1}'".format(start, finish)
    payload = {"$select" : "event_location","$where" : suffix}
    event_data_object = requests.get(endpoint, params=payload)
    event_data_json = event_data_object.json()
    dict_list = []

    for event in event_data_json:
        temp_dict = event_data_json.pop(0)
        split_events = temp_dict["event_location"].split(",")
        for sub_event in split_events:
            strip_ev = sub_event.strip(" ")
            append_dict = {"event_location": strip_ev}
            dict_list.append(append_dict)
    return dict_list

def get_coords(key, locations):
    coords = []

    for location in locations:
        address_param = location["event_location"].replace(" ", "+")
        ret_json = get_json(address_param, key)
        if ret_json["status"] != "OK":
            if ret_json["status"] == "INVALID_REQUEST":
                continue
            else:
                new_address = address_param.split(":")[0]
                ret_json = get_json(new_address, key)
                if ret_json["status"] != "OK":
                    continue
        address = ret_json["results"][0]["formatted_address"]
        lat = ret_json["results"][0]["geometry"]["location"]["lat"]
        lng = ret_json["results"][0]["geometry"]["location"]["lng"]
        new_coord = coordinates(address, lat, lng)
        coords.append(new_coord)
    return coords

def transform_coords(coords):
    pairs = []
    for pair in coords:
        temp_coord = (pair.latitude(), pair.longitude())
        pairs.append(temp_coord)
    return pairs

def create_map(pairs, key):
    new_york_coordinates = (40.75, -74.00)
    gmaps.configure(api_key=key)
    fig = gmaps.figure(center=new_york_coordinates, zoom_level=11)
    heatmap_layer = gmaps.heatmap_layer(pairs)
    heatmap_layer.max_intensity = 1
    heatmap_layer.point_radius = 15
    fig.add_layer(heatmap_layer)
    return fig

def get_json(address, key):
    geo_code_url = "https://maps.googleapis.com/maps/api/geocode/json"
    payload = {"address" : address, "key" : key}
    coord_json = requests.get(geo_code_url, params = payload).json()
    return coord_json

# Project Planning

#### Project Objectives

The objective of this project is to be able to pull data for any given day (in recent history or near future) on events in NYC and display a heat map of them.

#### How did I arrive at this project?

I was generally curious in answering the question "Where are all the events in NYC centered?" To do this, I decided a heat map was the right way to go. I found that New York City published an abundance of data, including event permit data, accessible via API.

#### External data sources and packages

To do this analysis, I found that i would need to use the [gmaps](https://github.com/pbugnion/gmaps) package with [Jupyter Notebook](https://github.com/jupyter/jupyter) ([website](http://http://jupyter.org/)).

My data would be retrieved from NYC OneData site; specifically [this](https://data.cityofnewyork.us/City-Government/NYC-Permitted-Event-Information/tvpp-9vvx/data) table which lists all permitted events in NYC.

Because this data is given by address, it needs to be converted to latitude and longitude to be useful to gmaps. To convert it I have to use the Google Geocoding API to convert the addresses to coordinates. This requires a Google API key, which I stored as an environment variable.

#### Data flow

The general flow will be:

1. Input and format date
2. Retrieve event permit data
3. Send addresses to Google Geocode API to get latitude and longitude
4. Create Heat map

##### *Input and format date*

The user will have to input the date in a specific format. I will then have to check it for errors and if none are found, convert it to a usable format for the city data API.

##### *Retrieve event permit data*

I will then format the endpoint url with the given date and parameters necessary to return the required fields. I would then use the requests package to retrieve the data from NYC OneData.

##### *Send addresses to Google Geocode API to get latitude and longitude*

Then I would use the Google Geocode API to transform the addresses to latitude and longitude. This will require a Google Cloud Platform account and a Google API key. Once the data is returned, I will create tuple pairs for each latitude and longitude to be used in the heat map.

##### *Create heat map*

This consists of creating the map and the heat map layer and displaying it in the notebook.

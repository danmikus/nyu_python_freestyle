# New York Event Permit Heatmap Analysis

This repo uses Jupyter Notebook with IPython Kernel to do analyses on where events are happening in New York City on any given day. The notebook uses NYC event permit data to do this analysis. The data is pulled in from the [NYC OpenData Site](https://data.cityofnewyork.us/City-Government/NYC-Permitted-Event-Information/tvpp-9vvx/data) via API and uses the gmaps module to create a heatmap of the events around the city. The general flow is:

1. Input and format date
2. Retrieve event permit data
3. Send addresses to Google Geocode API to get latitude and longitude
4. Create Heatmap

#### Installing Jupyter Notebook
To install Jupyter run the following command:

    pip3 install -U jupyter

You'll also need to make sure that you have enabled widgets extensions for Jupyter:

    jupyter nbextension enable --py --sys-prefix widgetsnbextension

#### Installing gmaps with pip

You can then install gmaps with:

    pip install gmaps

Then tell Jupyter to load the extension with:

jupyter nbextension enable --py --sys-prefix gmaps

#### Google API keys

To access Google maps, gmaps needs a Google API key. To create an API key, follow the [instructions in the documentation](https://developers.google.com/maps/documentation/geocoding/start#auth). Once you have an API key, pass it to gmaps.

#### Running the Notebook

To open the notebook, navigate to the root folder and run the following:

    jupyter notebook --browser=chrome

Note that I specified chrome as the browser. An open issue with Jupyter requires Mac users to specify the browser.

Once the directory is open, click into *nyc_event_heatmap.ipynb* to begin the analysis.

# New York Event Permit Heatmap Analysis

This repo uses Jupyter Notebook with IPython Kernel to do analyses on where events are happening in New York City on any given day. The notebook uses NYC event permit data to do this analysis. The data is pulled in from the [NYC OpenData Site](https://data.cityofnewyork.us/City-Government/NYC-Permitted-Event-Information/tvpp-9vvx/data) via API and uses the gmaps module to create a heatmap of the events around the city. The general flow is:

1. Input and format date
2. Retrieve event permit data
3. Send addresses to Google Geocode API to get latitude and longitude
4. Create Heat map

As a note, it's written in Python3, so make sure it is configured correctly in the notebook.

#### Using the notebook

If you think you'll be making changes to the notebook, it's a good idea to fork it first. Then navigate to your preferred location and run the following (substituting your github username):

    git clone https://github.com/[github_username]/nyu_python_freestyle.git

If you don't plan on making changes, you can clone it directly from my repo:

    git clone https://github.com/danmikus/nyu_python_freestyle.git

#### Installing packages with requirements.txt

You can install all required packages by navigating to the root directory and running the following:

    pip3 install -r requirements.txt

Alternatively, you can install the packages separately.

##### *Installing the Packages Individually*

To install the packages individually run the following commands:

    pip3 install -U jupyter
    pip3 install gmaps
    pip3 install requests
    pip3 install pprint

#### Installing Widgets

You'll also need to make sure that you have enabled widgets extensions for Jupyter:

    jupyter nbextension enable --py --sys-prefix widgetsnbextension

Then tell Jupyter to load the gmaps extension with:

    jupyter nbextension enable --py --sys-prefix gmaps

#### Google API keys

To access Google maps, gmaps needs a Google API key. To create an API key, follow the [instructions in the documentation](https://developers.google.com/maps/documentation/geocoding/start#auth). Once you have an API key, pass it to gmaps.

#### Running the Notebook

To open the notebook, navigate from the root folder to the app folder and run the following:

    jupyter notebook --browser=chrome

Note that I specified chrome as the browser. An open issue with Jupyter requires Mac users to specify the browser.

Once the directory is open, click into *nyc_event_heatmap.ipynb* to begin the analysis.

#### Running the Tests

To run tests, first make sure you have pytest installed:

    pip3 install pytest

To run the tests, navigate to the *test* folder and run:

    pytest heatmap_tests.py

# nyu_python_freestyle
    jupyter notebook --browser=chrome

    Installing gmaps with pip

    If you do not use conda, you can install gmaps with pip. The current version of gmaps is only tested with IPython 4.2 or later and ipywidgets 6.0.0 or later. To upgrade to the latest versions, use:

    $ pip install -U jupyter
    Make sure that you have enabled widgets extensions to Jupyter:

    $ jupyter nbextension enable --py --sys-prefix widgetsnbextension
    You can then install gmaps with:

    $ pip install gmaps
    Then tell Jupyter to load the extension with:

    $ jupyter nbextension enable --py --sys-prefix gmaps




    Google API keys

    To access Google maps, gmaps needs a Google API key. This key tells Google who you are, presumably so it can keep track of rate limits and such things. To create an API key, follow the instructions in the documentation. Once you have an API key, pass it to gmaps before creating widgets:

    gmaps.configure(api_key="AI...")

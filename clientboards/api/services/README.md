# Services

This directory serves as the middle layer between the Django view and the model. Table information will be retrieved from the model in the files located in this directory and will be passed to the view. The code here should generally be functions that return some list or object that the view can use to turn into a JSON formatted data (serialized) and returned by the endpoint that made the API call.

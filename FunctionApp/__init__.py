# Load Packages.
from typing import List
import logging
import datetime
import urllib.request
import json
import azure.functions as func

# Declare your azure machine learning predictive model url and api key for web service. 
url = 'https://asiasoutheast.services.azureml.net/workspaces/cc032ee688744372b4902889be809043/services/1162df773b784d9d8332a292d78bf62a/execute?api-version=2.0&format=swagger'
api_key = '5istkoxokpskUPNJr7ZDHsgBMg15+RjIR3QQioVTREZGzGJwkjjf7Yt6NEBgxW0LAMEiz1uv+UaNwkHLUly5fA==' # Replace this with the API key for the web service

# Whenever a event is received by event hub the main function will be triggered automatically.
def main(events: List[func.EventHubEvent]):
    for event in events:
        # Logging the event
        logging.info('Python EventHub trigger processed an event')
        # Get the event message from event hub (In our case generated credit transactions).
        s = event.get_body()
        # Convert the received json message into a dictionary.
        res = json.loads(s)
        # Prepare the data to be sent to predictive model.
        data = {
                "Inputs": {
                    "input1":
                    [
                        {
                            'Time': res['Time'],   
                            'V1': res['V1'],   
                            'V2': res['V2'],   
                            'V3': res['V3'],   
                            'V4': res['V4'],   
                            'V5': res['V5'],   
                            'V6': res['V6'],   
                            'V7': res['V7'],   
                            'V8': res['V8'],   
                            'V9': res['V9'],   
                            'V10': res['V10'],   
                            'V11': res['V11'],   
                            'V12': res['V12'],   
                            'V13': res['V13'],   
                            'V14': res['V14'],   
                            'V15': res['V15'],   
                            'V16': res['V16'],   
                            'V17': res['V17'],   
                            'V18': res['V18'],   
                            'V19': res['V19'],   
                            'V20': res['V20'],   
                            'V21': res['V21'],   
                            'V22': res['V22'],   
                            'V23': res['V23'],   
                            'V24': res['V24'],   
                            'V25': res['V25'],   
                            'V26': res['V26'],   
                            'V27': res['V27'],   
                            'V28': res['V28'],   
                            'Amount': res['Amount'],
                        }
                    ],},
                "GlobalParameters":  {}
                }
        # Encode the data into json format.
        body = str.encode(json.dumps(data))
        # Prepare the headers.
        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
        # Make a urllib request to azure ml predictive model.
        req = urllib.request.Request(url, body, headers)
        # Try and Except blocks for response code.
        try:
            # Store received response from ml model into a response variable. 
            response = urllib.request.urlopen(req)
            # Read the response and store it in a result variable.
            result = response.read()
            # Convert the result to a python dictionary for checking the output locally.
            res_dict = json.loads(result.decode('utf-8'))  
            #print(res_dict['Results']) to check results locally.
            # Convert the dictionary object to a json document to pass it to event hub 2.
            json_object = json.dumps(res_dict, indent = 4)
        except urllib.error.HTTPError as error:
            print("The request failed with status code: " + str(error.code))
            # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
            print(error.info())
            print(json.loads(error.read().decode("utf8", 'ignore')))
    # Get the present timestamp to log the message process time.
    timestamp = datetime.datetime.utcnow()
    logging.info('Message created at: %s', timestamp)
    # Return the json_object to event hub2 which details are present in output binding of function.json.
    return json_object
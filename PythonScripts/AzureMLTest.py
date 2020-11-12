# Load Packages
import urllib.request
import json

# Declare your azure machine learning predictive model url and api key for web service. 
url = 'https://asiasoutheast.services.azureml.net/workspaces/cc032ee688744372b4902889be809043/services/1162df773b784d9d8332a292d78bf62a/execute?api-version=2.0&format=swagger'
api_key = '5istkoxokpskUPNJr7ZDHsgBMg15+RjIR3QQioVTREZGzGJwkjjf7Yt6NEBgxW0LAMEiz1uv+UaNwkHLUly5fA=='

# Enter the credit values manually for test.
data = {
        "Inputs": {
                "input1":
                [
                    {
                            'Time': "1",   
                            'V1': "1",   
                            'V2': "1",   
                            'V3': "1",   
                            'V4': "1",   
                            'V5': "1",   
                            'V6': "1",   
                            'V7': "1",   
                            'V8': "1",   
                            'V9': "1",   
                            'V10': "1",   
                            'V11': "1",   
                            'V12': "1",   
                            'V13': "1",   
                            'V14': "1",   
                            'V15': "1",   
                            'V16': "1",   
                            'V17': "1",   
                            'V18': "1",   
                            'V19': "1",   
                            'V20': "1",   
                            'V21': "1",   
                            'V22': "1",   
                            'V23': "1",   
                            'V24': "1",   
                            'V25': "1",   
                            'V26': "1",   
                            'V27': "1",   
                            'V28': "1",   
                            'Amount': "1",   
                    }
                ],
        },
    "GlobalParameters":  {
    }
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
    #print(res_dict)
    json_object = json.dumps(res_dict, indent = 4)   
    #print(json_object)
    results = res_dict['Results']
    output1 = results['output1'][0]
    scored_labels = output1['Scored Labels']
    scored_probability = output1['Scored Probabilities']
    print(scored_labels)
    print(scored_probability)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))
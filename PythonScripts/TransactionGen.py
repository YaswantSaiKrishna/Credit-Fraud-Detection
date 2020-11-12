# Load Packages.
import time
import os
import uuid
import datetime
import random
import json
from azure.eventhub import EventHubProducerClient, EventData

# Declare your eventhub name and eventhub namespace connection string.
EventhubName = "capgemhub"
EventhubNamespace_ConnStr = "Endpoint=sb://capgeminihub.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=MmUYgnW2ZDU4NLBrCRiXByXHZbhmFRsXgO06abPFApc="

# Initialise a count variable for generating transaction time.
count = 0

# Generate sample data continuously.
while True:
    # Create a producer client to produce and publish events to the event hub.
    producer = EventHubProducerClient.from_connection_string(conn_str = EventhubNamespace_ConnStr, eventhub_name = EventhubName)
    # Create a batch. You will add events to the batch later. In our case each batch has only 1 transaction.
    event_data_batch = producer.create_batch()
    # Generating random transactions
    reading = { 'Time'  : str(count),   
                'V1'    : str(random.uniform(-56.407509631329, 2.45492999121121)),   
                'V2'    : str(random.uniform(-72.7157275629303, 22.0577289904909)),   
                'V3'    : str(random.uniform(-48.3255893623954, 9.38255843282114)),   
                'V4'    : str(random.uniform(-5.68317119816995, 16.8753440335975)),   
                'V5'    : str(random.uniform(-5.68317119816995, 16.8753440335975)),   
                'V6'    : str(random.uniform(-26.1605059358433, 73.3016255459646)),   
                'V7'    : str(random.uniform(-43.5572415712451, 120.589493945238)),   
                'V8'    : str(random.uniform(-73.21671845526741, 20.0072083651213)),   
                'V9'    : str(random.uniform(-13.4340663182301, 15.5949946071278)),   
                'V10'   : str(random.uniform(-24.5882624372475, 23.7451361206545)),   
                'V11'   : str(random.uniform(-4.79747346479757, 12.018913181619899)),   
                'V12'   : str(random.uniform(-18.683714633344298, 7.8483920756445995)),   
                'V13'   : str(random.uniform(-5.7918812063208405, 7.126882958593759)),   
                'V14'   : str(random.uniform(-19.2143254902614, 10.5267660517847)),   
                'V15'   : str(random.uniform(-4.49894467676621, 8.87774159774277)),   
                'V16'   : str(random.uniform(-14.1298545174931, 17.315111517627802)),   
                'V17'   : str(random.uniform(-25.162799369324798, 9.25352625047285)),   
                'V18'   : str(random.uniform(-9.498745921046769, 5.04106918541184)),   
                'V19'   : str(random.uniform(-7.21352743017759, 5.59197142733558)),   
                'V20'   : str(random.uniform(-54.497720494566, 39.4209042482199)),   
                'V21'   : str(random.uniform(-34.8303821448146, 27.2028391573154)),   
                'V22'   : str(random.uniform(-10.933143697655, 10.5030900899454)),   
                'V23'   : str(random.uniform(-44.807735203791296, 22.5284116897749)),   
                'V24'   : str(random.uniform(-2.83662691870341, 4.58454913689817)),   
                'V25'   : str(random.uniform(-10.2953970749851, 7.51958867870916)),   
                'V26'   : str(random.uniform(-2.60455055280817, 3.5173456116237998)),   
                'V27'   : str(random.uniform(-22.5656793207827, 31.612198106136304)),   
                'V28'   : str(random.uniform(-15.430083905534898, 33.8478078188831)),   
                'Amount': str(random.uniform(0.0, 25691.16)),}
    # Convert the reading into a JSON string.
    s = json.dumps(reading)
    # Add event data to the batch.
    event_data_batch.add(EventData(s))
    # Send the batch of events to the event hub.
    producer.send_batch(event_data_batch)
    # Close the producer.
    producer.close()
    # Increment Count
    count+=1
# Load Packages.
import logging
from azure.eventhub import EventHubConsumerClient

# Declare the Connection string of event hub namespace, Event hub 2 name, consumer_group ($Default is the default consumer group).
connection_str = 'Endpoint=sb://capgeminihub.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=MmUYgnW2ZDU4NLBrCRiXByXHZbhmFRsXgO06abPFApc='
consumer_group = '$Default'
eventhub_name = 'eventhub2'
# Create a consumer client to consume events from the event hub.
client = EventHubConsumerClient.from_connection_string(connection_str, consumer_group, eventhub_name=eventhub_name)
logger = logging.getLogger("azure.eventhub")
logging.basicConfig(level=logging.INFO)

# Whenever a event is received by event hub 2 the on_event function will be run.
def on_event(partition_context, event):
    #logger.info("Received event from partition {}".format(partition_context.partition_id))
    print("Received the event: \"{}\" from the partition with ID: \"{}\"".format(event.body_as_str(encoding='UTF-8'), partition_context.partition_id))
    print(event.body_as_str(encoding='UTF-8'))
    #res_dict = json.loads(result.decode('utf-8')) 
    partition_context.update_checkpoint(event)
    print('-' * 20)

with client:
    client.receive(
        on_event=on_event, 
        starting_position="-1",  # "-1" is from the beginning of the partition.
    )
    # receive events from specified partition:
    # client.receive(on_event=on_event, partition_id='0')
from datetime import datetime
import random
import json
from kafka import KafkaProducer
import time


KAFKA_HOST_IP="localhost"
TOPIC = 'demo'

user_ids = list(range(1, 101))
recipient_ids = list(range(1, 101))


# Messages will be serialized as JSON 
def serializer(message):
    return json.dumps(message).encode('utf-8')

kafka_p = KafkaProducer(
    bootstrap_servers = [f'{KAFKA_HOST_IP}:29092'],  
    value_serializer=serializer
)


# Create Message sample
def generate_message() -> dict:
    random_user_id = random.choice(user_ids)
    # Copy the recipients array
    recipient_ids_copy = recipient_ids.copy()
    # User can't send message to himself
    recipient_ids_copy.remove(random_user_id)
    # random_recipient_id = random.choice(recipient_ids_copy)
    list_name = ["BTC", "ETH", "BTT", "DOT"]
    end = []
    time_now = int(datetime.utcnow().timestamp())
    for item in list_name:
        if item == "BTC": data = random.randint(10, 400)
        elif item == 'ETH': data = random.randint(10, 250)
        elif item == 'DOT': data = random.randint(40, 170)
        else: data = random.randint(10, 40)
        end.append({
            "data_id" : data,
            "name": item,
            "timestamp": time_now
        })
    return end


def demo_func():
    dummy_message = generate_message()
    for item in dummy_message:
        # Send it to our 'messages' topic
        print(f'Producing message @ {datetime.now()} | Message = {str(item)}')
        kafka_p.send('demo', item)

while True:
    demo_func()
    time.sleep(60)
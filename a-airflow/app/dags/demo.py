from datetime import datetime
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
import random
import time
import json
from kafka import KafkaProducer


KAFKA_HOST_IP="kafka"
TOPIC = 'demo'
user_ids = list(range(1, 101))
recipient_ids = list(range(1, 101))


# Messages will be serialized as JSON 
def serializer(message):
    return json.dumps(message).encode('utf-8')

kafka_p = KafkaProducer(
    bootstrap_servers = [f'{KAFKA_HOST_IP}:9092'],  
    value_serializer=serializer
)


dag =  DAG(
    dag_id='Demo',
    description="This DAG runs a full workflow for Demo druid and superset.",
    # schedule_interval=None,
    schedule_interval='*/1 * * * *',
    start_date=datetime(2022, 2, 26),
    catchup=False,
    tags=['production'],)


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
    
    
producer_task = PythonOperator(
    task_id="producer",
    provide_context=True,
    python_callable=demo_func,
    dag= dag
)

producer_task
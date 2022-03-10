# from datetime import datetime
# from airflow.models import DAG
# from airflow.operators.python_operator import PythonOperator
# from airflow.dags.data import get_row
# import random
# import time



# dag =  DAG(
#     dag_id='Demo',
#     description="This DAG runs a full workflow for Demo druid and superset.",
#     schedule_interval=None,
#     start_date=datetime(2022, 2, 26),
#     catchup=False,
#     tags=['production'],)

# TOPIC = 

# def demo_func():
#     row = get_row()
#     for r in row:
#         print(r)
#         producer.send(f"{TOPIC}", r)  
#         random_int= random.uniform(1, 3)
#         time.sleep(random_int)
            
#     print('''This is a function that will run within the DAG execution''')
#     pass
    
# producer = PythonOperator(
#     task_id="producer",
#     provide_context=True,
#     python_callable=demo_func,
#     dag= dag
# )

# producer
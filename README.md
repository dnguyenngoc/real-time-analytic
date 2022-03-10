# Real Time Analytic With Druid - Airflow - Kafka - Superset
[![Kafka](https://img.shields.io/badge/kafka-5.2.0-green)](https://kafka.apache.org/documentation/)
[![Airflow](https://img.shields.io/badge/airflow-2.2.4-green)](https://airflow.apache.org/docs/)
[![Druid](https://img.shields.io/badge/druid-0.22.1-orange)](https://druid.apache.org/docs/latest/design/)
[![Redis](https://img.shields.io/badge/redis-6.2.6-orange)](https://redis.io/)
[![Posgresql](https://img.shields.io/badge/postgres-14.1-brown)](https://www.postgresql.org/)
[![Superset](https://img.shields.io/badge/Superset-1.4.1-lightgrey)](https://superset.apache.org/docs/intro/)

In today's world you want to learn from your customers as quickly as possible. This blog gives an introduction to setting up streaming analytics using open source technologies. We'll use Apache {Kafka, Superset, Druid, Airflow} to set up a system that allows you to get a deeper understanding of the behaviour of your customers.

## Screenshots & Gifs

**View System**

<div>
    <kbd>
        <img title="View System" src="https://github.com/apot-group/real-time-analytic/blob/main/public/chart.png?raw=true" />
    </kbd>
    <br/>
</div>
<br>

## Contents
- [Screenshots & Gifs](#screenshots--gifs)
- [Example](#example)
    - [1. Install docker, docker-compose](https://github.com/apot-group/real-time-analytic#1-install-docker-and-docker-compose)
    - [2. Pull git repo](https://github.com/apot-group/real-time-analytic#2-pull-git-repo)
    - [3. Start Server](https://github.com/apot-group/real-time-analytic#3-start-server)
- [Contact Us](#contact-us)


## Example

### 1. Install docker and docker-compose

`https://www.docker.com/`

### 2. Pull git repo
`git clone https://github.com/apot-group/real-time-analytic.git` 

### 3. Start Server
`cd real-time-analytic && docker-compose up`

| Service               | URL                              | User/Password                                 |
| :-------------------: | :------------------------------: | :-------------------------------------------: |
| Druid Unified Console | http://localhost:8888/           | None                                          |
| Druid Legacy Console  | http://localhost:8081/           | None                                          |
| Superset              | http://localhost:8088/           | docker exec -it superset bash superset-init   |
| Airflow               | http://localhost:3000/           | a-airflow/app/standalone_admin_password.txt   |

### 3. Create Dashboard sample from druid streaming
 - Airflow dags at a-airflow/app/dags/demo.py each one min sent message to kafka 'demo' topic with data 
```
   {
            "data_id" : 454,
            "name": 'BTC',
            "timestamp": '2021-02-05T10:10:01'
    }
```

 - From druid load data from kafka, choice 'demo' topic and config data result table
 - From superset add druid like database sqlalchemy uri: druid://broker:8082/druid/v2/sql/
 - Create Chart and dashboard on superset from demo table.
 - Enjoy! :fire: :fire: :fire:

## Contact Us
- Email-1: duynnguyenngoc@hotmail.com - Duy Nguyen :heart: :heart: :heart: 
# Real Time Analytic With Druid - Airflow - Kafka - Superset
[![Kafka](https://img.shields.io/badge/kafka-5.2.0-green)](https://kafka.apache.org/documentation/)
[![Airflow](https://img.shields.io/badge/airflow-2.2.4-green)](https://airflow.apache.org/docs/)
[![Druid](https://img.shields.io/badge/druid-0.22.1-orange)](https://druid.apache.org/docs/latest/design/)
[![Redis](https://img.shields.io/badge/redis-6.2.6-orange)](https://redis.io/)
[![Posgresql](https://img.shields.io/badge/postgres-14.1-brown)](https://www.postgresql.org/)
[![Superset](https://img.shields.io/badge/Superset-0.63-lightgrey)](https://superset.apache.org/docs/intro/)

In today's world you want to learn from your customers as quickly as possible. This blog gives an introduction to setting up streaming analytics using open source technologies. We'll use Apache {Kafka, Superset, Druid, Airflow} to set up a system that allows you to get a deeper understanding of the behaviour of your customers.

## Screenshots & Gifs

**View System**

<div>
    <kbd>
        <img title="View System" src="https://github.com/apot-group/document-processing/blob/main/o-statics/images/server.png?raw=true" />
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


| Service               | URL                              |
| :-------------------: | :------------------------------: |
| Druid Unified Console | http://localhost:8888/           |
| Druid Legacy Console  | http://localhost:8081/           |
| Superset              | http://localhost:8088/           |
| Airflow               | http://localhost:3000/           |


## Contact Us
- Email-1: duynnguyenngoc@hotmail.com - Duy Nguyen :heart: :heart: :heart: 
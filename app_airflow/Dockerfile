FROM python:3.9

WORKDIR /airflow/

RUN apt-get update && apt-get upgrade -y

RUN pip3 install "apache-airflow[apache.spark]==2.2.5" \
    --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.2.5/constraints-3.9.txt"

COPY ./requirements.txt requirements.txt

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

COPY ./app/ /airflow/

COPY ./start.sh /start.sh

RUN chmod +x /start.sh

EXPOSE 8080

ENTRYPOINT [ "/bin/bash", "/start.sh" ]
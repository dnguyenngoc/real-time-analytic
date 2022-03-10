######################################################################
# IMAGE for airflow
######################################################################
FROM python:3.7

LABEL maintainer="Duy Nguyen <duyngunyenngoc@hotmail.com>"

WORKDIR /airflow/

# Install OpenJDK-11
RUN apt update && \
    apt-get install -y openjdk-11-jdk && \
    apt-get install -y ant && \
    apt-get clean;

# Set JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/
RUN export JAVA_HOME

RUN pip3 install "apache-airflow[apache.spark]==2.2.4" \
    --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.2.4/constraints-3.7.txt"

COPY ./requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY ./app/ /airflow/

EXPOSE 8080

FROM python:3.9-slim

#RUN apt-get update && \
#    apt-get install -yq --no-install-recommends \
#    curl \
#    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && \
    pip install boto3 selenium cx_Oracle
    
WORKDIR /opt/oracle
RUN wget https://download.oracle.com/otn_software/linux/instantclient/instantclient-basiclite-linuxx64.zip && \
    unzip instantclient-basiclite-linuxx64.zip

WORKDIR /app
COPY cat.py device_farm_test.py /app/

ENTRYPOINT [ "python3", "cat.py" ]

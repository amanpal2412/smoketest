FROM python:3.9-slim

#RUN apt-get update && \
#    apt-get install -yq --no-install-recommends \
#    curl \
#    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && \
    pip install boto3 selenium

WORKDIR /app
COPY cat.py device_farm_test.py /app/

ENTRYPOINT [ "python3", "cat.py" ]

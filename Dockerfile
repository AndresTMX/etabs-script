FROM python:3.10.12

WORKDIR /app
COPY requirements.txt /app/

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /app/

CMD bash -c "while true; do sleep 1; done"
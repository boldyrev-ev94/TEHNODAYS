FROM python:3.12.3-slim

WORKDIR /TEHNODAYS

COPY . /TEHNODAYS
COPY .env /TEHNODAYS/.env

RUN apt-get update && \
	apt-get install -y gcc libpq-dev python3-dev && \
	rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["python","-m", "backend/main.py"]
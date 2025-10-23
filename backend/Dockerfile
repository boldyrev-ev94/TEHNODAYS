FROM python:3.12.3-slim

WORKDIR /app

COPY . /app
COPY .env /app/.env

RUN apt-get update && \
	apt-get install -y gcc libpq-dev python3-dev && \
	rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt

# RUN ls -la /app
# RUN ls -la /app/backend

CMD ["python","-m", "backend/main.py"]
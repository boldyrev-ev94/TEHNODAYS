FROM python:3.12.3-slim

WORKDIR /TEHNODAYS
COPY . /TEHNODAYS

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "TEHNODAYS/backend/main.py"]
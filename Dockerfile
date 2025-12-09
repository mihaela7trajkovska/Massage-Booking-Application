FROM python:3.11-slim

WORKDIR /app

# netcat за wait-for-it.sh
RUN apt-get update && apt-get install -y netcat-openbsd && apt-get clean


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .


ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000


RUN chmod +x wait-for-it.sh


CMD ["./wait-for-it.sh", "db", "5432", "--", "flask", "run"]

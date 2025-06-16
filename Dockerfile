FROM python:3.11-slim

WORKDIR /app

# Инсталирај netcat-openbsd за wait-for-it.sh
RUN apt-get update && apt-get install -y netcat-openbsd && apt-get clean

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Дозволи wait-for-it.sh да биде извршна
RUN chmod +x wait-for-it.sh

CMD ["./wait-for-it.sh", "db", "5432", "--", "flask", "run", "--host=0.0.0.0"]

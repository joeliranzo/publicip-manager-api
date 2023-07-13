FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN pip install gunicorn

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8010", "app:app"]

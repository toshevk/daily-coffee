FROM python:3.8

WORKDIR /app24-daily-coffee
COPY . /app24-daily-coffee

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000

ENV FLASK_APP=main.py
ENV FLASK_ENV=production

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
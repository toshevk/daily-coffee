FROM python:3.12-alpine

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000

ENV FLASK_APP=main.py
ENV FLASK_ENV=production

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
FROM python:latest

# expose to nginx
EXPOSE 9000

# ptvsd (VisualStudio debug)
EXPOSE 3000

COPY requirements.txt .

RUN pip3 install --no-cache-dir  -r requirements.txt

CMD ["gunicorn", "--workers=5", "--threads=2", "--bind=0.0.0.0:9000", "app:app"]

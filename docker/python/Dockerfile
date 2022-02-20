FROM python:3.10.0b3

# expose to nginx
EXPOSE 9000

# ptvsd (VisualStudio debug)
EXPOSE 3000

COPY requirements.txt .

RUN pip3 install --no-cache-dir  -r requirements.txt

RUN pip3 install pylint

# --reload: in dev mode, ask gunicorn to restart worker on any source file change
CMD ["gunicorn", "--workers=1", "--threads=2", "--bind=0.0.0.0:9000", "--reload", "app:app"]

FROM python:3.6-slim

RUN apt-get update && apt-get install -y git

COPY . /app/

WORKDIR /app/VolunteerNetwork

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "manage.py", "makemigrations"]
ENTRYPOINT ["python", "manage.py", "migrate"]
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]

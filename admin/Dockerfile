# Get the base python
FROM python:3.9
# Container Application directory to run the application from
WORKDIR /app
# Setup all the requirements needed in container to run the app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Finally run the Django server in the conatiner
CMD python manage.py runserver 0.0.0.0:8000

# Use the official Python base image
FROM python:3.10.4

# Set the working directory in the container
WORKDIR /black

# Set the locale
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Install system locales
RUN apt-get update && apt-get install -y locales locales-all

# Generate and set the desired locale
RUN locale-gen fa_IR.UTF-8
ENV LANG fa_IR.UTF-8
ENV LC_ALL fa_IR.UTF-8

# Copy project
COPY . .

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create a virtual environment
RUN python -m venv venv

# Activate the virtual environment
SHELL ["/bin/bash", "-c"]
RUN source venv/bin/activate

# Run migrations
RUN python3 manage.py makemigrations --empty index && python3 manage.py makemigrations --empty blog && python3 manage.py makemigrations --empty product && python3 manage.py makemigrations --empty category && python3 manage.py makemigrations index && python3 manage.py makemigrations blog && python3 manage.py makemigrations category && python3 manage.py makemigrations users && python3 manage.py makemigrations product
RUN python3 manage.py migrate

# Create a superuser
RUN python3 manage.py createsuperuser

# Run tests
RUN python manage.py test

# Expose the Django development server port
EXPOSE 8000

# Start the Django development server
CMD python manage.py runserver 0.0.0.0:8000

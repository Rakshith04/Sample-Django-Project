#!/usr/bin/env bash

#!/bin/bash

# Apply Django migrations
python manage.py makemigrations
python manage.py migrate

# Create a superuser (change the values as needed)
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')" | python manage.py shell

python manage.py loaddata seed_data.json

# Start the Django application
python manage.py runserver 0.0.0.0:8000


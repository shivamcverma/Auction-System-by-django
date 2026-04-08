#!/usr/bin/env bash

# Render build script for AuctionSystem
# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Apply migrations
python manage.py migrate --noinput

# Optional: create a superuser if needed (commented out)
# echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')" | python manage.py shell

# End of script

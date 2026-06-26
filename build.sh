#!/usr/bin/env bash
# exit on error
set -o errexit

# 1. Upgrade the package installer and pull down your required dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

# 2. Compile and package your static layout design frameworks
python manage.py collectstatic --noinput

# 3. Synchronize your administrative database tables schema
python manage.py migrate

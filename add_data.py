import django
import os

from adminapp.models import Artist

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OAGProject.settings")
artist = Artist(name="John Doe", email="manchi@gmail.com", gender="male", birth_date="1990-01-15")
artist.save()
print("success")
# Add more data as neede
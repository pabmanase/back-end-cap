To use pipenv dependencies:
pipenv install
*This will install all dependencies required.
*If this does not work, delete Pipfile.lock then run pipenv install again.

Superuser:
username: user
password: password


API Paths to test:
/restaurant/menu/
/restaurant/menu/<int:pk>
/restaurant/booking/

Important notes:
- Authentication requirements are commented out for testing as seen in restaurant/views.py.
- Edit your own MySQL credentials in DATABASES in LittleLemon/settings.py.
- Migrate models to test the API.:
  python manage.py makemigrations
  python manage.py migrate

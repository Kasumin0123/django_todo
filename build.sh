pip install -r requirements.txt

python manage.py collectstatic

python manage.py makemigrations
python manage.py migrate
if [ $CREATE_SUPERUSER ];
then
    python manage.py createsuperuser --no-input
fi
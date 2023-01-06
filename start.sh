pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata start_data.json
python manage.py runserver
python test_script.py

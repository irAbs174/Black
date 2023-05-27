Black shop :

Deploy :
ls && virtualenv venv && source venv/bin/activate && pip3 install -r requirements.txt && clear && python3 manage.py makemigrations --empty index && python3 manage.py makemigrations --empty blog && python3 manage.py makemigrations --empty product && python3 manage.py makemigrations --empty category && python3 manage.py makemigrations index && python3 manage.py makemigrations blog && python3 manage.py makemigrations category && python3 manage.py makemigrations users && python3 manage.py makemigrations product && python3 manage.py migrate && clear && python3 manage.py createsuperuser && python3 manage.py test && clear && python3 manage.py runserver






# expense_tracker

## Link to site: http://localhost:8000/users/login/

## Installing

Python3 must be already installed.

```shell
git 
cd expense_tracker
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver #stsrts Django Server
```

 
`python manage.py loaddata account/currencies_db_data.json`

- After loading data from fixture you can use following superuser:
  - Login: `admin`
  - Password: `Qay12345`

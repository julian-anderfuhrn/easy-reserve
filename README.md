# EasyReserve

Web app developed with Django to manage schedules expenses for professionals and patients


## Objective

This project was created for educaional purposes to practice:
- Django(models, views, forms, auth)
- Relations between models
- CRUD
- Basic good practices(env vars, git, refactor)


## Installation
1 Clone the repository

``` bash
git clone https://github.com/julian-anderfuhrn/django-expenses
cd django-expenses

2 Create the virtual environment
python -m venv venv
venv\Scripts\activate

3 install dependencies
pip install -r requirements.txt

4 create the .env file
SECRET_KEY=your_secret_key
DEBUG=True

5 Execute migrations and server
python manage.py migrate
python manage.py loaddata service_categories
python manage.py runserver

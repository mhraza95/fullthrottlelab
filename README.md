# Fullthrottle Lab API #


----------
## Python Version ##
**Developed Using `Python V3.7.4`**


**Database  Used `Sqlite`**


## Quick Setup ##
1. **Install `pip install -r "requirements.txt"`**
2. **Run `python manage.py migrate` to create the tables in DB.**
3. **Run `python manage.py load_items` to dump intial data**
3. **Run `python manage.py runserver` to get static files.**
4. **Start the development server and visit `http://127.0.0.1:8000/admin/` to create db  object manually (username- admin, password- admin)**




## API Endpoints ##

1. **Call `GET http://127.0.0.1:8000/api/user` to get users list**


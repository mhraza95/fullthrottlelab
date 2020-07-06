# Cricket API #


----------
## Python Version ##
**Developed Using `Python V3.7.4`**


**Database  Used `Sqlite`**


## Quick Setup ##
1. **Install `pip install -r "requirements.txt"`**
2. **Run `python manage.py migrate` to create the cricket models.**
3. **Run `python manage.py loaddata fixtures.json` to dump intial data (In case using other DB)**
3. **Run `python manage.py runserver` to get static files.**
4. **Start the development server and visit `http://127.0.0.1:8000/admin/` to create a match**
5. **Visit `http://127.0.0.1:8000/` to view API Documentation details.**
5. **Visit `http://127.0.0.1:8000/matches` to view match details.**



## API Endpoints ##

1. **Call `GET /api/matches` to get matches list**
2. **Call `GET /api/match/fixture` to create random matches**
3. **Call `GET /api/players` to get players list**
4. **Call `GET /api/player/{player_id}` to get player details**
5. **Call `GET /api/teams` to get teams list**
6. **Call `GET /api/team/{team_id}` to get Team wise Players list**

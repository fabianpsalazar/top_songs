# Python Backend Developer Test


This repository is a backend challenge proposed for the python developer vacancy.

Thank you in advance for the opportunity to present this test!

## How run the code?
1. Install Python
2. Clone this Repository: `git clone https://github.com/fabianpsalazar/top_songs`.
3. `cd` in  `top_songs`: `cd top_songs`.
4. Create a virtual env: `virtualenv -p python env`(optional but recommended).
5. Activate virtual env: `source env/bin/activate`.
6. `cd` into `core`: `cd core`.
7. Install packages with: `pip install -r requirements.txt`.
8. Run the follow command to fill the database with the json data and create a test user for auth api endpoints: `python manage.py util_songs`.
9. Run server and enjoy it!: `python manage.py runserver`



## Code structure

We have the 'core' directory as heart of settings API, then we have an app called top_songs in the top
_songs directory and this is our store of the API logic.

```
top_songs/
├── core
│   ├── core
│   │   ├── asgi.py
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── db.sqlite3
│   ├── __init__.py
│   ├── manage.py
│   ├── requirements.txt
│   ├── static
│   │   ├── admin
│   │   └── rest_framework
│   └── top_songs
│       ├── admin.py
│       ├── apps.py
│       ├── __init__.py
│       ├── json_variables.py
│       ├── loginviews.py
│       ├── management
│       ├── migrations
│       ├── models.py
│       ├── __pycache__
│       ├── serializers.py
│       ├── tests.py
│       ├── urls.py
│       └── views.py
└── README.md
```


## Solutions implemented for each exercise

### Requirements
1. Given the following JSON Data as source:
https://rss.applemarketingtools.com/api/v2/us/music/most-played/100/songs.json
Develop a solution to the given requirements.
Create an API that has the following endpoints:

### We use Class-based Views to implement this endpoints
#### Note: A song in this project is conformed for track, artist and genre.

<ul>

<li>An endpoint to provide a search lookup within the tracks (at least by name, but is
open to any suggestions)</li>

<b>SOLUTION:</b> this was implemented with a 'get' method called get_song that receives a request through the url and look for a song that contains the name of the song that you want to get.

<li>An endpoint that would allow to get top 50 popularity tracks.</li>

<b>SOLUTION:</b> this was implemented with a 'get' method called get_top_50 that take the first 50 songs of the top 100 list.

<li>An endpoint to remove a track, using a given identifier (defined by you)</li>

<b>SOLUTION:</b> This was implemented with a 'delete' method called delete_track that only delete the track, not artist or genre, because theses must be reused.
This method take pk in the URL and try to get a track with matches with that track_id to be deleted.

<li>An endpoint to add new tracks using ORM.</li>

<b>SOLUTION:</b> this was implemented with two 'post', create_song and create_track.

<b>create_song:</b> This method allows to create a song when have a new artist and a new genre.

<b>create_track:</b> This method allows to create a new track with a unique track_id

<li>Use a Database (suggested: SQLite), instead of the JSON File. Include a create
schema in the repo and instructions on how to implement it.</li>

<b>SOLUTION:</b> For this we used the recommended db (sqlite3), we downloaded the json file about the top 100 songs
and save it in our directory, exactly in top_songs/management/commands. Inside commands are two django commands, util_songs and delete_songs.

<b>util_songs:</b> Handle function that open the json file and create new elements for tables track, artist and genre using a 'for' loop.
<b>delete_songs:</b>  Handle function that delete track, artist and genre tables.

Image of schema

<li>Add authentication API endpoint(s) with Django Rest Framework (DRF).</li>
<br>SOLUTION:</b> I created a method called login in loginviews.py to separate the logic between auth and SongViewSet.

I used authtoken from rest_framework to check the authentication for who want to try make a request for the Song-view set methods.
I create a test user 'username:admin, password:admin' in util_songs command to check the auth implementation.
Through the url spot/songs/login you can try to login with the test user through contentType form-data.

<li>Create an endpoint to return the tracks grouped by genres.</li>

<b>SOLUTION:</b>  This was implemented with 'get' methods, get_song_genre and get_group_genre.

<b>get_song_genre</b>: A get method that returns all genres with their songs.
<b>get_group_genre</b>: take a pk argument in the url to return a group of songs by that genre.


</ul>

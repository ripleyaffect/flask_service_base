# Flask Service Base

A starter app for creating a flask service

## Setup

The app contains modules for `views`, `database`, and `api`.

To connect to the api, you'll need to point the `SQLALCHEMY_DATABASE_URI`
in `app.config.py` to a running postres server.

To set up a postgres server with Docker:
```bash
docker run --name postgres_db -e POSTGRES_PASSWORD=password -d -p 5432:5432 postgres
```

You'll need to create the database:
```bash
$ docker exec -it postgres_db bash
$ root@[hash]# psql -U postgres
```
```sql
CREATE DATABASE my_service;
```
Your URI is now something like:
```
postgresql://postgres:password@0.0.0.0:5432/my_service
```

You'll need to create the models in the database:
```py
from app import db

db.create_all()
```
TODO: Set up alembic migrations

## Running the service

You can run the app with
```bash
$ python app.main.py
```
or with another server

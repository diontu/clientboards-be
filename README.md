## Run app

To run the app locally, you will need to run the following command.

```bash
python3 manage.py runserver
```

## Migrations

To run a migration on the `api` app, run the following command.

For Mac:

```bash
# make the migrations
python3 manage.py makemigrations api
# execute the migrations
python3 manage.py migrate
```

For Windows:

```bash
# make the migrations
python manage.py makemigrations api
# execute the migrations
python manage.py migrate
```

## Go into the DB

```bash
sqlite3 db.sqlite3 # <-- the arg is the name of the sqlite3 file.
```

## Show the tables

```bash
.tables # <-- to see all the tables.
```

## Clear DB

To clear your local DB, run the following command.

For Mac:

```bash
# make the migrations
python3 manage.py flush
```

For Windows:

```bash
# make the migrations
python manage.py flush
```

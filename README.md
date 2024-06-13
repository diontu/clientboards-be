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
python3 manage.py makemigrations api # for the rest of the apis
python3 manage.py makemigrations user # for the user sessions
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

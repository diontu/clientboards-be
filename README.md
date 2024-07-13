## Run app

To run the app, you must have Docker instead and have the docker daemon running. Run the following command from the terminal in the project's root directory.

```bash
./scripts/start.sh
```

This will start the required Docker containers and put you inside the docker container.

## To stop the app

Exit the Docker terminal by entering `exit` in the terminal and run the following command.

```bash
./scripts/stop.sh
```

## Custom commands

To add custom commands to the Docker container, add the command to the file `./scripts/dev/custom-commands.sh`.

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

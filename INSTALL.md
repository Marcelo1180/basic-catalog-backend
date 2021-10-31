# INSTALL test zebrands backend

Setup config settings
```sh
cp .env.example .env
```

__DEBUG=true__ is used for debugging mode, in this mode you can use:
- admin/ (Classic admin of django)
- apidoc/ (Swagger api documentation)
- logging with level DEBUG

## Installing in DEVELOPMENT MODE
Installing general and dev dependencies
```sh
pipenv install --ignore-pipfile --dev
```

Access to the virtualenv
```sh
pipenv shell
```

Run migrations
```sh
(env)$ python manage.py migrate
```

Create a super user
```sh
(env)$ python manage.py createsuperuser
```

Load sample data
```sh
(env)$ python manage.py loaddata catalog
```

## Installing in PRODUCTION MODE
Requirements:
- Debian 10

In production mode .env its important to set __DEBUG=false__

Installing dependencies
```sh
pipenv install --ignore-pipfile
```

Run migrations
```sh
(env)$ python manage.py migrate
```

Create a super user
```sh
(env)$ python manage.py createsuperuser
```

Demon service install
```sh
cd /etc/systemd/system
sudo ln -s <path root project>/main.service .
```

Start service
```sh
sudo service main start
```

Watch logs
```sh
sudo journalctl -e -u main.service
```

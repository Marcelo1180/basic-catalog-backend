# INSTALL django base project

## Installing in DEVELOPMENT MODE
Installing general and dev dependencies
```sh
pipenv install --ignore-pipfile
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

## Installing in PRODUCTION MODE
Requirements:
- Debian 10

In production mode settings.json its important to set __DEBUG=false__

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

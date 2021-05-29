# INSTALL django base project

Making a virtualenvironment
```sh
virtualenv .venv
source .venv/bin/activate
```

Installing requirements
```sh
pip install -r requirements.txt
```

If you don't have a ssh key then use following command
after that config you privatekey.pub into your github account
```sh
ssh-keygen -t rsa -C "demo@email.com"
Generating public/private rsa key pair.
Enter file in which to save the key (~/.ssh/id_rsa): ~/.ssh/privatekey
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
```

Instancing your key to forwarding agent for git push
```sh
ssh-add -k ~/.ssh/privatekey
```

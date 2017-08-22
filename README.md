# Python Flask Application
A Python sample for Heroku/Cloud Foundry application written in Python using Flask

## Getting Started
This application requires the following python modules:

[Flask](http://flask.pocoo.org/docs/0.10/quickstart)


They can be installed by using the following commands

```bash
pip install flask
pip install flask-cors
```

## Run Locally

The application can be run locally with the command

```bash
python cf-python-sample.py
```

## Run on Cloud Foundry

To push the application, use the following command:

```bash
cf push -f manifest
```

## Run on Heroku

To push the application, use the following command:

```bash
git push heroku master
```

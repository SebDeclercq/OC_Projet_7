# README

This repo is containing the entire development built to fulfill the requirements of OC DA Python's Project \#7.

This program is built uppon Python 3.7+ and has multiple requirements including `pipenv`.

# DEPLOYEMENT

## SETTING UP

To prepare your environment, please run the following commands in the project directory (for linux ; please note that it may differ on other platforms):

```bash
pip3 install pipenv
pipenv install
```

Defining your environment variables is required. To do so, you may rename the `env-example` file to `.env` and change the values to fit your config.

## FLASK

To run the website w/ Flask as a minimal version (for dev purpose only), please run

```bash
pipenv run flask run
```

## GUNICORN

To run the website w/ Gunicorn (for production purpose), run

```bash
pipenv run gunicorn DEPLOY:app
```

## HEROKU

The `Procfile` provided w/ this repo enables to deploy the program on heroku. Please refer to the official documentation for more details : https://devcenter.heroku.com/categories/reference


# LICENSE

GNU GPLv3 license: https://www.gnu.org/licenses/gpl-3.0.txt

- **Author**: Sébastien Declercq
- **URL**: https://github.com/SebDeclercq/OC_Projet_7

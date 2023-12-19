## Overview
- Byteaq inspired by Bitly (aq is the top level domain code for Antarctica like ly is the code for Libya)

## Set Up
1. Install Python 3.11
    -  if using homebrew on a mac, run `brew install python@3.11`
1. Clone this repo locally to your machine
1. Navigate into the repo from a terminal window: `cd byteaq`
1. Create a Python virtual environment: `python3 -m venv venv`
1. Active the virtual environment: `source venv/bin/activate`
    -  Your terminal prompt should now be prepended with `(venv)`
1. install dependencies needed for the virtual environment: `python -m pip install -r requirements.txt`
1. Migrate database: `python manage.py migrate`
1. Start server: `python manage.py runserver`
1. Navigate to `localhost:8000/byteaq`

## Run Tests
1. Open new terminal window and activate new virtual env: `source venv/bin/activate`
1. Run tests: `python manage.py test byteaq`
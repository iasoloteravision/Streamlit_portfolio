#!/bin/bash

echo "Proceed to install virtualenv"
python3 -m pip install --user virtualenv

echo "Creating a virtual environment called env"
python3 -m venv env

echo "Activating the environment (type 'source env/bin/activate' on terminal to start)"
source env/bin/activate

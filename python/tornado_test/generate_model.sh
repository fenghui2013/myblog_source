#!/bin/bash

python -m pwiz -e mysql -H 127.0.0.1 -p 3306 -u root -P  peewee_test > peewee_test_model.py

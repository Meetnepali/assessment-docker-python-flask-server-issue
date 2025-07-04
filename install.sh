#!/bin/bash
sudo apt-get install python3 -y
sudo apt-get install docker -y
sudo apt-get install docker-compose -y
sudo apt-get install postgresql-client -y

pip install flask || echo 'Flask is already installed'
pip install flask_sqlalchemy || echo 'Flask-SQLAlchemy is already installed'
pip install psycopg2-binary || echo 'psycopg2-binary is already installed'
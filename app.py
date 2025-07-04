from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db = SQLAlchemy(app)

@app.route('/')
def hello():
    try:
        db.session.execute('SELECT 1')
        return 'Database connection successful', 200
    except Exception as e:
        return str(e), 500
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
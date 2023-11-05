from app import app
from util.db import db

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True, port=5000)

with app.app_context():
    db.create_all()  
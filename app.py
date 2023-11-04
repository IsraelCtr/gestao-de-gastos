from app import app
from utils.db import db
from routes.debitos import debitos
with app.app_context():
    db.create_all()
if __name__ == '__main__':
    app.run(host='127.0.0.1',debug=True, port=5000)

app.register_blueprint (debitos)
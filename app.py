from backend import create_app, db
from backend.models import Appointment

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

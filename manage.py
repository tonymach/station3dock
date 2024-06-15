from app import app, db
from models import Participant, Session  # Import your models
from flask_migrate import upgrade

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, Participant=Participant, Session=Session)

def create_db():
    with app.app_context():
        db.create_all()
    print("Database created successfully!")

def migrate_db():
    with app.app_context():
        upgrade()
    print("Database migration applied successfully!")

if __name__ == "__main__":
    create_db()
    # migrate_db()  # Uncomment this line if you want to apply migrations
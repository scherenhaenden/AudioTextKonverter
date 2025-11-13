import typer
from dotenv import load_dotenv

load_dotenv()

from core.db.database import get_db, Base, engine
from core.models.user import User
from core.schemas.user import UserCreate
from core.security import get_password_hash

app = typer.Typer()

@app.command()
def create_user(username: str, email: str, password: str):
    """
    Creates a new user.
    """
    db = next(get_db())
    user = UserCreate(username=username, email=email, password=password)
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    print(f"User {db_user.username} created successfully.")

@app.command()
def init_db():
    """
    Initializes the database.
    """
    Base.metadata.create_all(bind=engine)
    print("Database initialized successfully.")

if __name__ == "__main__":
    app()

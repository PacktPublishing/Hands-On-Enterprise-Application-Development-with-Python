from user_service.user_service import app, db
from user_service.models import User, Token

db.create_all()

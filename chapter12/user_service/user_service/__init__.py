from user_service.user_service import app, db, tracer
from user_service.models import User, Token

print(dir(tracer))
db.create_all()

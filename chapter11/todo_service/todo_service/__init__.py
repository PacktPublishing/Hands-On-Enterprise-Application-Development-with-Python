from todo_service.user_service import app, db
from todo_service.models import List, Item

db.create_all()

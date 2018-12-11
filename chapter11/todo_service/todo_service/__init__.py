from todo_service.todo_service import app, db
from todo_service.models import List, Item

db.create_all()

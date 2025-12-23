from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Todo

router = APIRouter(prefix="/todos", tags=["todos"])

@router.get("/")
def get_all_todos(db: Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return todos

@router.get("/{todo_id}")
def get_todo(todo: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    db.add(todo)
    db.commit()
    return todo

@router.post("/")
def add_todo(title: str, db: Session = Depends(get_db)):
    new_todo = Todo(title=title, complete=False)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

@router.put("/{todo_id}")
def update_todo(todo_id: int, title:str, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    todo.title = title
    db.commit()
    return title

@router.delete("/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    db.delete(todo)
    db.commit()
    return{"message": "todo deleted"}

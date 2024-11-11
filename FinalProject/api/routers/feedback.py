from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from ..controllers import feedback as controller
from ..schemas import feedback as schema
from ..dependencies.database import get_db

router = APIRouter(
    prefix="/feedbacks",
    tags=["Feedbacks"]
)

@router.post("/", response_model=schema.Feedback, status_code=status.HTTP_201_CREATED)
def create_feedback(request: schema.FeedbackCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)

@router.get("/", response_model=list[schema.Feedback])
def read_all_feedbacks(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{feedback_id}", response_model=schema.Feedback)
def read_one_feedback(feedback_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, feedback_id)

@router.put("/{feedback_id}", response_model=schema.Feedback)
def update_feedback(feedback_id: int, request: schema.FeedbackUpdate, db: Session = Depends(get_db)):
    return controller.update(db, feedback_id, request)

@router.delete("/{feedback_id}", response_model=schema.Feedback)
def delete_feedback(feedback_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, feedback_id)

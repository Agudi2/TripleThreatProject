from sqlalchemy.orm import Session
from ..models import feedback as model
from ..schemas import feedback as schema

def create(db: Session, feedback: schema.FeedbackCreate):
    db_feedback = model.Feedback(**feedback.dict())
    db.add(db_feedback)
    db.commit()
    db.refresh(db_feedback)
    return db_feedback

def read_all(db: Session):
    return db.query(model.Feedback).all()

def read_one(db: Session, feedback_id: int):
    return db.query(model.Feedback).filter(model.Feedback.id == feedback_id).first()

def update(db: Session, feedback_id: int, feedback: schema.FeedbackUpdate):
    db_feedback = db.query(model.Feedback).filter(model.Feedback.id == feedback_id).first()
    if db_feedback is None:
        return None
    for var, value in vars(feedback).items():
        setattr(db_feedback, var, value) if value else None
    db.commit()
    db.refresh(db_feedback)
    return db_feedback

def delete(db: Session, feedback_id: int):
    db_feedback = db.query(model.Feedback).filter(model.Feedback.id == feedback_id).first()
    if db_feedback is None:
        return None
    db.delete(db_feedback)
    db.commit()
    return db_feedback

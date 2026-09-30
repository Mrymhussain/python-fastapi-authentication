from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.base import BaseModel
from data.user_data import user_list
from data.tea_data import teas_list, comments_list
from config.environment import db_URI


engine = create_engine(db_URI)
SessionLocal = sessionmaker(bind=engine)


try:
    print("Recreating database...")

    BaseModel.metadata.drop_all(bind=engine)
    BaseModel.metadata.create_all(bind=engine)

    print("Seeding the database...")

    db = SessionLocal()

    # Users first because teas need a user_id
    db.add_all(user_list)
    db.commit()

    db.add_all(teas_list)
    db.commit()

    db.add_all(comments_list)
    db.commit()

    db.close()

    print("Database seeding complete! 👋")

except Exception as e:
    print("An error occurred:", e)
from sqlalchemy.orm import declarative_base
from sqlalchemy import String, Column, String, Integer
from sqlalchemy import create_engine
from src.config import Settings
from sqlalchemy.dialects.mysql import ENUM


#Creates connector to the database engine = create_engine("mysql+pymysql://user:pw@host/db", pool_pre_ping=True)
engine = create_engine(Settings().database_connection)

BaseDatabaseModel = declarative_base()

# Models Definition
class Account_database_Model(BaseDatabaseModel):
    __tablename__ = "Account"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    email = Column(String(50))
    password = Column(String(50))
    whatAmI: Column( 'account.what_am_i', ENUM("Traveller", "Local"))
    age: Column( 'account.age', ENUM("<20", "22-39", "40-59", "60+"))
    gender: Column( 'account.gender', ENUM("Female", "Male", "Complex", "Prefer not to say"))
    i_currently_live_in: Column(String(100))
    i_can_give_advices_for: Column(String(100))
    travel_experiences_preferences: Column('account.travel_experiences_preferences', ENUM("Party", "Sightseeing", "Art", "History", "Music", "Sports", "Adventure", "Spiritual", "Nature", "Food") )
     
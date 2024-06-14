import tkinter as tk
from tkinter import messagebox
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import random

Base = declarative_base()

class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    num_min_players = Column(Integer)
    num_max_players = Column(Integer)
    game_type = Column(String)
    duration = Column(Integer)

    engine = create_engine('sqlite:///games.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    def add_game():
        name = name_entry.get()
        num_players = int(players_entry.get())
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

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
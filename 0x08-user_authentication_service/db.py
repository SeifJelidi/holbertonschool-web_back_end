#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from user import Base
from user import User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a user to DB
        """
        user = User(email=email, hashed_password=hashed_password)
        session = self._session
        session.add(user)
        session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """
        takes in arbitrary keyword arguments and returns
        the first row found in the users table.
        """
        if not kwargs:
            raise InvalidRequestError
        else:
            data = User.__table__.columns.keys()
            for key in kwargs.keys():
                if key not in data:
                    raise InvalidRequestError
            user = self._session.query(User).filter_by(**kwargs).first()
            if not user:
                raise NoResultFound
            return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        takes as argument a required user_id integer
        and arbitrary keyword arguments, and returns None
        """
        user = self.find_user_by(id=user_id)
        for k in kwargs:
            if hasattr(user, k):
                setattr(user, k, kwargs[k])
            else:
                raise ValueError
        self._session.commit()

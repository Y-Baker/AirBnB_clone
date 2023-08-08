#!/usr/bin/python3

"""Module For User Class that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User Class from BaseModel class will have user information

    Attributes:
        email (str): the email of the user
        password (str): the password of the user
        first_name (str): the first name of the user
        last_name (str): the last name of the user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

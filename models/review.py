#!/usr/bin/python3

"""Module For Review Class that inherits from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review Class from BaseModel class will have Review information

    Attributes:
        text (str): the review details
        place_id (str): the id of the state
        user_id (str): the User id
    """

    text = ""
    place_id = ""  # will be the id of the Place class <Place.id>
    user_id = ""  # will be the id of the User class <User.id>

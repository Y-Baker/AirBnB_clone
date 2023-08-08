#!/usr/bin/python3

"""Module For city Class that inherits from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City Class from BaseModel class will have city information

    Attributes:
        name (str): the name of the city
        state_id (str): the id of the state
    """

    name = ""
    state_id = ""  # will be the id of the State class <State.id>

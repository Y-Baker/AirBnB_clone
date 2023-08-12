#!/usr/bin/python3

"""Module For state Class that inherits from BaseModel"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    state Class from BaseModel class will have state information

    Attributes:
        name (str): the name of the state
    """

    name = ""

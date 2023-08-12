#!/usr/bin/python3

"""Module For amenity Class that inherits from BaseModel"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity Class from BaseModel class will have one menity information

    Attributes:
        name (str): the name of the Amenity
    """

    name = ""

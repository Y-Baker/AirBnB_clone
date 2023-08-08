#!/usr/bin/python3

"""Module For place Class that inherits from BaseModel"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place Class from BaseModel class will have Place information

    Attributes:
        name (str): the name of the Place
        description (str): information about the place
        number_rooms (int): the number of room of the place
        number_bathrooms (int): the number of bathrooms of the place
        max_guest (int): the maximum number of the guests at the same time
        price_by_night (int): the price for a one night in the place
        latitude (float): the latitude of the place
        longitude (float): the longitude of the place
        city_id (str): the City id
        user_id (str): the User id
        amenity_ids (list of str): list of Amenity ids
    """

    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0

    city_id = ""  # will be the id of the City class <State.id>
    user_id = ""  # will be the id of the User class <User.id>
    amenity_ids = []  # will be list of the Amenitys in the place <Amenity.id>

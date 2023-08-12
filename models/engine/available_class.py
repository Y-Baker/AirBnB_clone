#!/usr/bin/python3
"""
module for file storage class that contains all the common operations
for savin
"""

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review


class FileUtil:
    """
    class file util
    """

    my_Classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "City": City,
        "State": State,
        "Amenity": Amenity,
        "Review": Review
    }
    saved_file = "./saved_object.json"

    @classmethod
    def create_class(cls, name_obj):
        """
        return the class that match with the entre name
        """
        if name_obj in cls.my_Classes:
            return cls.my_Classes[name_obj]

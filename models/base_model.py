#!/usr/bin/python3

"""
module for base model class that contains all the common operations
for project classes
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """Base Model Class and will use as super class for multi classes"""

    def __init__(self, *args, **kwargs):
        """
        init method that initializes an instance
        :id: unique string id
        :created_at: time of creation of object
        :updated_at: time of instance update
        """
        self.id = str(uuid.uuid4())
        if kwargs:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                elif k == "id":
                    if v is not None:
                        self.id = v

                elif k in ['created_at', 'updated_at']:
                    date_obj = datetime.fromisoformat(v)
                    setattr(self, k, date_obj)
                else:
                    setattr(self, k, v)
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):

        """
        method to update the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        :return: a dictionary containing all keys/values
        of __dict__ of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__

        return new_dict

    def __str__(self):
        """
        method to return string representation  :return:  of a class
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

#!/usr/bin/python3
"""
module for file storage class that contains all the common operations
for saving project classes
"""
import json
import os
from models.engine.available_class import FileUtil


class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to instances
    :file_path: : string - path to the JSON file (ex: file.json )
    :objects: dictionary - empty but will store all objects by <class name>.id
    """
    __file_path = FileUtil.saved_file
    __objects = {}

    def all(self):
        """_summary_
            method to return the dictionary will all the instnces created
        Returns:
            dictionary: dictionary containing objects persisted in my app
        """
        return self.__class__.__objects

    def new(self, obj):
        """_summary_

        Args:
            obj (any type of my project classes):
            sets the object in the objects
            dictionary with key classname.obj_id
        """
        obj_key = f"{obj.__class__.__name__}.{obj.id}"
        self.__class__.__objects[obj_key] = obj

    def save(self):
        """
        function to save the __objects persisted so far into the __file_path
        via serialization technique
        """
        directory = os.path.dirname(self.__class__.__file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        new_dict = {
            key: value.to_dict()
            for key, value in self.__class__.__objects.items()
        }
        with open(self.__class__.__file_path, "w") as f:
            json.dump(new_dict, f, indent=4)

    def reload(self):
        """
        method to reload all persisted objects from specified path to the\
        memory of the application
        :return:no return
        """
        from models.engine.available_class import FileUtil

        try:
            with open(self.__class__.__file_path) as fp:
                try:
                    stored_data = json.load(fp)
                except json.decoder.JSONDecodeError:
                    raise ValueError("File Empty")
                for key, value in stored_data.items():
                    class_name = value['__class__']
                    obj = FileUtil.create_class(class_name)
                    self.__class__.__objects[key] = obj(**value)
        except FileNotFoundError:
            pass

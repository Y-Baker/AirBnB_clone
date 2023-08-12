#!/usr/bin/python3

"""
test module for Amenity class
Define unittests for models/Amenity.py
Unittest classes:
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""

from models.engine.Basic_Test_Classes import Basic_Instantiation, Basic_Save
from models.engine.Basic_Test_Classes import Basic_to_dict
from models.engine.available_class import FileUtil
from models.amenity import Amenity
from time import sleep
import json
import unittest


class TestAmenity_Instantiation(Basic_Instantiation):
    """Unittests for testing instantiation of the Amenity class."""

    def __init__(self, *args, **kwargs):
        """
        Initialize The Class and Object For Amenity Class
        """
        super().__init__(*args, **kwargs)
        self.obj = Amenity()
        sleep(0.05)
        self.obj2 = Amenity()
        self.cls_name = 'Amenity'
        self.cls = Amenity

    def test_name_cls_attribute(self):
        """
        Make Testes In name class attribute
        """
        self.assertEqual(str, type(self.cls.name))
        self.assertIn("name", dir(self.obj))
        self.assertNotIn("name", self.obj.__dict__)


class TestAmenity_Save(Basic_Save):
    """Unittests for testing save method of the Amenity class."""

    def __init__(self, *args, **kwargs):
        """
        Initialize The Class and Object For Amenity Class
        """
        super().__init__(*args, **kwargs)
        self.obj = Amenity()
        sleep(0.05)
        self.obj2 = Amenity()
        self.cls_name = 'Amenity'
        self.cls = Amenity

    def test_name_save(self):
        """
        Test if name cls saved in json
        """
        new_obj = self.cls()
        new_obj.name = 'Youssef'
        new_obj.save()
        key = f"{self.cls_name}.{new_obj.id}"
        with open(FileUtil.saved_file, "r")as f:
            re_dict = json.load(f)
        self.assertIn(key, re_dict)
        self.assertIn('name', re_dict[key])
        self.assertEqual(new_obj.name, re_dict[key]['name'])


class TestAmenity_to_dict(Basic_to_dict):
    """Unittests for testing to_dict method of the Amenity class."""

    def __init__(self, *args, **kwargs):
        """
        Initialize The Class and Object For Amenity Class
        """
        super().__init__(*args, **kwargs)
        self.obj = Amenity()
        sleep(0.05)
        self.obj2 = Amenity(
            **{
                'id': 'a42ee380-c959-450e-ad29-c840a898cfce',
                'created_at': '2017-09-28T21:11:15.504287',
                'updated_at': '2017-09-28T21:11:15.504296',
                'name': 'Yousef Ahmed',
                'age': 19,
                'score': 93.9,
                '__class__': 'Amenity',
            }
        )
        self.cls_name = 'Amenity'
        self.cls = Amenity

    def test_have_special_keys(self):
        """
        Test if class attributes in the return of to_dict method
        """
        self.assertIn("name", self.cls.__dict__)
        self.cls.name = 'Youssef'
        self.assertIn("name", self.cls.__dict__)
        self.assertEqual("Youssef", self.cls.__dict__['name'])


if __name__ == "__main__":
    unittest.main()

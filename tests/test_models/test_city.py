#!/usr/bin/python3

"""
test module for City class
Define unittests for models/City.py
Unittest classes:
    TestCity_instantiation
    TestCity_save
    TestCity_to_dict
"""

from models.engine.Basic_Test_Classes import Basic_Instantiation, Basic_Save
from models.engine.Basic_Test_Classes import Basic_to_dict
from models.engine.available_class import FileUtil
from models.city import City
from time import sleep
import json
import unittest


class TestCity_Instantiation(Basic_Instantiation):
    """Unittests for testing instantiation of the City class."""

    def __init__(self, *args, **kwargs):
        """
        Initialize The Class and Object For City Class
        """
        super().__init__(*args, **kwargs)
        self.obj = City()
        sleep(0.05)
        self.obj2 = City()
        self.cls_name = 'City'
        self.cls = City

    def test_name_cls_attribute(self):
        """
        Make Testes In name class attribute
        """
        self.assertEqual(str, type(self.cls.name))
        self.assertIn("name", dir(self.obj))
        self.assertNotIn("name", self.obj.__dict__)

    def test_state_id_cls_attribute(self):
        """
        Make Testes In state_id class attribute
        """
        self.assertEqual(str, type(self.cls.state_id))
        self.assertIn("state_id", dir(self.obj))
        self.assertNotIn("state_id", self.obj.__dict__)


class TestCity_Save(Basic_Save):
    """Unittests for testing save method of the City class."""

    def __init__(self, *args, **kwargs):
        """
        Initialize The Class and Object For City Class
        """
        super().__init__(*args, **kwargs)
        self.obj = City()
        sleep(0.05)
        self.obj2 = City()
        self.cls_name = 'City'
        self.cls = City

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

    def test_state_id_save(self):
        """
        Test if state_id cls saved in json
        """
        new_obj = self.cls()
        new_obj.state_id = 'CAL'
        new_obj.save()
        key = f"{self.cls_name}.{new_obj.id}"
        with open(FileUtil.saved_file, "r")as f:
            re_dict = json.load(f)
        self.assertIn(key, re_dict)
        self.assertIn('state_id', re_dict[key])
        self.assertEqual(new_obj.state_id, re_dict[key]['state_id'])


class TestCity_to_dict(Basic_to_dict):
    """Unittests for testing to_dict method of the City class."""

    def __init__(self, *args, **kwargs):
        """
        Initialize The Class and Object For City Class
        """
        super().__init__(*args, **kwargs)
        self.obj = City()
        sleep(0.05)
        self.obj2 = City(
            **{
                'id': 'a42ee380-c959-450e-ad29-c840a898cfce',
                'created_at': '2017-09-28T21:11:15.504287',
                'updated_at': '2017-09-28T21:11:15.504296',
                'name': 'Yousef Ahmed',
                'age': 19,
                'score': 93.9,
                '__class__': 'City'
            }
        )
        self.cls_name = 'City'
        self.cls = City

    def test_have_special_keys_name(self):
        """
        Test if class attributes in the return of to_dict method
        """
        self.assertIn("name", self.cls.__dict__)
        self.cls.name = 'Youssef'
        self.assertIn("name", self.cls.__dict__)
        self.assertEqual("Youssef", self.cls.__dict__['name'])

    def test_have_special_keys_state_id(self):
        """
        Test if class attributes in the return of to_dict method
        """
        self.assertIn("state_id", self.cls.__dict__)
        self.cls.state_id = 'CAL'
        self.assertIn("state_id", self.cls.__dict__)
        self.assertEqual("CAL", self.cls.__dict__['state_id'])


if __name__ == "__main__":
    unittest.main()

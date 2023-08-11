#!/usr/bin/python3

"""
test module for User class
Define unittests for models/User.py
Unittest classes:
    TestUser_instantiation
    TestUser_save
    TestUser_to_dict
"""

from models.engine.Basic_Test_Classes import Basic_Instantiation, Basic_Save
from models.engine.Basic_Test_Classes import Basic_to_dict
from models.engine.available_class import FileUtil
from models.user import User
from time import sleep
import json
import unittest


class TestUser_Instantiation(Basic_Instantiation):
    """Unittests for testing instantiation of the User class."""

    def __init__(self, *args, **kwargs):
        """
        Initialize The Class and Object For User Class
        """
        super().__init__(*args, **kwargs)
        self.obj = User()
        sleep(0.05)
        self.obj2 = User()
        self.cls_name = 'User'
        self.cls = User

    def test_email_cls_attribute(self):
        """
        Make Testes In email class attribute
        """
        self.assertEqual(str, type(self.cls.email))
        self.assertIn("email", dir(self.obj))
        self.assertNotIn("email", self.obj.__dict__)

    def test_password_cls_attribute(self):
        """
        Make Testes In password class attribute
        """
        self.assertEqual(str, type(self.cls.password))
        self.assertIn("password", dir(self.obj))
        self.assertNotIn("password", self.obj.__dict__)

    def test_first_name_cls_attribute(self):
        """
        Make Testes In first_name class attribute
        """
        self.assertEqual(str, type(self.cls.first_name))
        self.assertIn("first_name", dir(self.obj))
        self.assertNotIn("first_name", self.obj.__dict__)

    def test_last_name_cls_attribute(self):
        """
        Make Testes In last_name class attribute
        """
        self.assertEqual(str, type(self.cls.last_name))
        self.assertIn("last_name", dir(self.obj))
        self.assertNotIn("last_name", self.obj.__dict__)


class TestUser_Save(Basic_Save):
    """Unittests for testing save method of the User class."""

    def __init__(self, *args, **kwargs):
        """
        Initialize The Class and Object For User Class
        """
        super().__init__(*args, **kwargs)
        self.obj = User()
        sleep(0.05)
        self.obj2 = User()
        self.cls_name = 'User'
        self.cls = User

    def test_email_save(self):
        """
        Test if email cls saved in json
        """
        new_obj = self.cls()
        new_obj.email = 'yousef@gmail.com'
        new_obj.save()
        key = f"{self.cls_name}.{new_obj.id}"
        with open(FileUtil.saved_file, "r")as f:
            re_dict = json.load(f)
        self.assertIn(key, re_dict)
        self.assertIn('email', re_dict[key])
        self.assertEqual(new_obj.email, re_dict[key]['email'])

    def test_password_save(self):
        """
        Test if password cls saved in json
        """
        new_obj = self.cls()
        new_obj.password = '3112004'
        new_obj.save()
        key = f"{self.cls_name}.{new_obj.id}"
        with open(FileUtil.saved_file, "r")as f:
            re_dict = json.load(f)
        self.assertIn(key, re_dict)
        self.assertIn('password', re_dict[key])
        self.assertEqual(new_obj.password, re_dict[key]['password'])

    def test_first_name_save(self):
        """
        Test if first_name cls saved in json
        """
        new_obj = self.cls()
        new_obj.first_name = 'Youssef'
        new_obj.save()
        key = f"{self.cls_name}.{new_obj.id}"
        with open(FileUtil.saved_file, "r")as f:
            re_dict = json.load(f)
        self.assertIn(key, re_dict)
        self.assertIn('first_name', re_dict[key])
        self.assertEqual(new_obj.first_name, re_dict[key]['first_name'])

    def test_last_name_save(self):
        """
        Test if last_name cls saved in json
        """
        new_obj = self.cls()
        new_obj.last_name = 'Ahmed'
        new_obj.save()
        key = f"{self.cls_name}.{new_obj.id}"
        with open(FileUtil.saved_file, "r")as f:
            re_dict = json.load(f)
        self.assertIn(key, re_dict)
        self.assertIn('last_name', re_dict[key])
        self.assertEqual(new_obj.last_name, re_dict[key]['last_name'])


class TestUser_to_dict(Basic_to_dict):
    """Unittests for testing to_dict method of the User class."""

    def __init__(self, *args, **kwargs):
        """
        Initialize The Class and Object For User Class
        """
        super().__init__(*args, **kwargs)
        self.obj = User()
        sleep(0.05)
        self.obj2 = User(
            **{
                'id': 'a42ee380-c959-450e-ad29-c840a898cfce',
                'created_at': '2017-09-28T21:11:15.504287',
                'updated_at': '2017-09-28T21:11:15.504296',
                'name': 'Yousef Ahmed',
                'age': 19,
                'score': 93.9,
                '__class__': 'User'
            }
        )
        self.cls_name = 'User'
        self.cls = User

    def test_have_special_keys_email(self):
        """
        Test if class attributes in the return of to_dict method
        """
        self.assertIn("email", self.cls.__dict__)
        self.cls.email = 'yousef@gmail.com'
        self.assertIn("email", self.cls.__dict__)
        self.assertEqual("yousef@gmail.com", self.cls.__dict__['email'])

    def test_have_special_keys_password(self):
        """
        Test if class attributes in the return of to_dict method
        """
        self.assertIn("password", self.cls.__dict__)
        self.cls.password = '3112004'
        self.assertIn("password", self.cls.__dict__)
        self.assertEqual("3112004", self.cls.__dict__['password'])

    def test_have_special_keys_first_name(self):
        """
        Test if class attributes in the return of to_dict method
        """
        self.assertIn("first_name", self.cls.__dict__)
        self.cls.first_name = 'Yousef'
        self.assertIn("first_name", self.cls.__dict__)
        self.assertEqual('Yousef', self.cls.__dict__['first_name'])

    def test_have_special_keys_last_name(self):
        """
        Test if class attributes in the return of to_dict method
        """
        self.assertIn("last_name", self.cls.__dict__)
        self.cls.last_name = 'Ahmed'
        self.assertIn("last_name", self.cls.__dict__)
        self.assertEqual('Ahmed', self.cls.__dict__['last_name'])


if __name__ == "__main__":
    unittest.main()

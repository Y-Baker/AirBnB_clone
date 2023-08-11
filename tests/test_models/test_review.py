#!/usr/bin/python3

"""
test module for Review class
Define unittests for models/Review.py
Unittest classes:
    TestReview_instantiation
    TestReview_save
    TestReview_to_dict
"""

from models.engine.Basic_Test_Classes import Basic_Instantiation, Basic_Save
from models.engine.Basic_Test_Classes import Basic_to_dict
from models.engine.available_class import FileUtil
from models.review import Review
from time import sleep
import json
import unittest


class TestReview_Instantiation(Basic_Instantiation):
    """Unittests for testing instantiation of the Review class."""

    def __init__(self, *args, **kwargs):
        """
        Initialize The Class and Object For Review Class
        """
        super().__init__(*args, **kwargs)
        self.obj = Review()
        sleep(0.05)
        self.obj2 = Review()
        self.cls_name = 'Review'
        self.cls = Review

    def test_text_cls_attribute(self):
        """
        Make Testes In text class attribute
        """
        self.assertEqual(str, type(self.cls.text))
        self.assertIn("text", dir(self.obj))
        self.assertNotIn("text", self.obj.__dict__)

    def test_place_id_cls_attribute(self):
        """
        Make Testes In place_id class attribute
        """
        self.assertEqual(str, type(self.cls.place_id))
        self.assertIn("place_id", dir(self.obj))
        self.assertNotIn("place_id", self.obj.__dict__)

    def test_user_id_cls_attribute(self):
        """
        Make Testes In user_id class attribute
        """
        self.assertEqual(str, type(self.cls.user_id))
        self.assertIn("user_id", dir(self.obj))
        self.assertNotIn("user_id", self.obj.__dict__)


class TestReview_Save(Basic_Save):
    """Unittests for testing save method of the Review class."""

    def __init__(self, *args, **kwargs):
        """
        Initialize The Class and Object For Review Class
        """
        super().__init__(*args, **kwargs)
        self.obj = Review()
        sleep(0.05)
        self.obj2 = Review()
        self.cls_name = 'Review'
        self.cls = Review

    def test_text_save(self):
        """
        Test if text cls saved in json
        """
        new_obj = self.cls()
        new_obj.text = '4.5-star'
        new_obj.save()
        key = f"{self.cls_name}.{new_obj.id}"
        with open(FileUtil.saved_file, "r")as f:
            re_dict = json.load(f)
        self.assertIn(key, re_dict)
        self.assertIn('text', re_dict[key])
        self.assertEqual(new_obj.text, re_dict[key]['text'])

    def test_place_id_save(self):
        """
        Test if place_id cls saved in json
        """
        new_obj = self.cls()
        new_obj.place_id = 'H-555'
        new_obj.save()
        key = f"{self.cls_name}.{new_obj.id}"
        with open(FileUtil.saved_file, "r")as f:
            re_dict = json.load(f)
        self.assertIn(key, re_dict)
        self.assertIn('place_id', re_dict[key])
        self.assertEqual(new_obj.place_id, re_dict[key]['place_id'])

    def test_user_id_save(self):
        """
        Test if user_id cls saved in json
        """
        new_obj = self.cls()
        new_obj.user_id = 'a-54321'
        new_obj.save()
        key = f"{self.cls_name}.{new_obj.id}"
        with open(FileUtil.saved_file, "r")as f:
            re_dict = json.load(f)
        self.assertIn(key, re_dict)
        self.assertIn('user_id', re_dict[key])
        self.assertEqual(new_obj.user_id, re_dict[key]['user_id'])


class TestReview_to_dict(Basic_to_dict):
    """Unittests for testing to_dict method of the Review class."""

    def __init__(self, *args, **kwargs):
        """
        Initialize The Class and Object For Review Class
        """
        super().__init__(*args, **kwargs)
        self.obj = Review()
        sleep(0.05)
        self.obj2 = Review(
            **{
                'id': 'a42ee380-c959-450e-ad29-c840a898cfce',
                'created_at': '2017-09-28T21:11:15.504287',
                'updated_at': '2017-09-28T21:11:15.504296',
                'name': 'Yousef Ahmed',
                'age': 19,
                'score': 93.9,
                '__class__': 'Review'
            }
        )
        self.cls_name = 'Review'
        self.cls = Review

    def test_have_special_keys_text(self):
        """
        Test if class attributes in the return of to_dict method
        """
        self.assertIn("text", self.cls.__dict__)
        self.cls.text = '4.5-star'
        self.assertIn("text", self.cls.__dict__)
        self.assertEqual("4.5-star", self.cls.__dict__['text'])

    def test_have_special_keys_place_id(self):
        """
        Test if class attributes in the return of to_dict method
        """
        self.assertIn("place_id", self.cls.__dict__)
        self.cls.place_id = 'H-555'
        self.assertIn("place_id", self.cls.__dict__)
        self.assertEqual("H-555", self.cls.__dict__['place_id'])

    def test_have_special_keys_user_id(self):
        """
        Test if class attributes in the return of to_dict method
        """
        self.assertIn("user_id", self.cls.__dict__)
        self.cls.user_id = 'a-54321'
        self.assertIn("user_id", self.cls.__dict__)
        self.assertEqual("a-54321", self.cls.__dict__['user_id'])


if __name__ == "__main__":
    unittest.main()

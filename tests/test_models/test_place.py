#!/usr/bin/python3

"""
test module for Place class
Define unittests for models/Place.py
Unittest classes:
    TestPlace_instantiation
    TestPlace_save
    TestPlace_to_dict
"""

from models.engine.Basic_Test_Classes import Basic_Instantiation, Basic_Save
from models.engine.Basic_Test_Classes import Basic_to_dict
from models.engine.available_class import FileUtil
from models.place import Place
from time import sleep
import json
import unittest


class TestPlace_Instantiation(Basic_Instantiation):
    """Unittests for testing instantiation of the Place class."""

    def __init__(self, *args, **kwargs):
        """
        Initialize The Class and Object For Place Class
        """
        super().__init__(*args, **kwargs)
        self.obj = Place()
        sleep(0.05)
        self.obj2 = Place()
        self.cls_name = 'Place'
        self.cls = Place

    def test_name_cls_attribute(self):
        """
        Make Testes In name class attribute
        """
        self.assertEqual(str, type(self.cls.name))
        self.assertIn("name", dir(self.obj))
        self.assertNotIn("name", self.obj.__dict__)

    def test_description_cls_attribute(self):
        """
        Make Testes In description class attribute
        """
        self.assertEqual(str, type(self.cls.description))
        self.assertIn("description", dir(self.obj))
        self.assertNotIn("description", self.obj.__dict__)

    def test_number_rooms_cls_attribute(self):
        """
        Make Testes In number_rooms class attribute
        """
        self.assertEqual(int, type(self.cls.number_rooms))
        self.assertIn("number_rooms", dir(self.obj))
        self.assertNotIn("number_rooms", self.obj.__dict__)

    def test_number_bathrooms_cls_attribute(self):
        """
        Make Testes In number_bathrooms class attribute
        """
        self.assertEqual(int, type(self.cls.number_bathrooms))
        self.assertIn("number_bathrooms", dir(self.obj))
        self.assertNotIn("number_bathrooms", self.obj.__dict__)

    def test_max_guest_cls_attribute(self):
        """
        Make Testes In max_guest class attribute
        """
        self.assertEqual(int, type(self.cls.max_guest))
        self.assertIn("max_guest", dir(self.obj))
        self.assertNotIn("max_guest", self.obj.__dict__)

    def test_price_by_night_cls_attribute(self):
        """
        Make Testes In price_by_night class attribute
        """
        self.assertEqual(int, type(self.cls.price_by_night))
        self.assertIn("price_by_night", dir(self.obj))
        self.assertNotIn("price_by_night", self.obj.__dict__)

    def test_latitude_cls_attribute(self):
        """
        Make Testes In latitude class attribute
        """
        self.assertEqual(float, type(self.cls.latitude))
        self.assertIn("latitude", dir(self.obj))
        self.assertNotIn("latitude", self.obj.__dict__)

    def test_longitude_cls_attribute(self):
        """
        Make Testes In longitude class attribute
        """
        self.assertEqual(float, type(self.cls.longitude))
        self.assertIn("longitude", dir(self.obj))
        self.assertNotIn("longitude", self.obj.__dict__)

    def test_city_id_cls_attribute(self):
        """
        Make Testes In city_id class attribute
        """
        self.assertEqual(str, type(self.cls.city_id))
        self.assertIn("city_id", dir(self.obj))
        self.assertNotIn("city_id", self.obj.__dict__)

    def test_user_id_cls_attribute(self):
        """
        Make Testes In user_id class attribute
        """
        self.assertEqual(str, type(self.cls.user_id))
        self.assertIn("user_id", dir(self.obj))
        self.assertNotIn("user_id", self.obj.__dict__)

    def test_amenity_ids_cls_attribute(self):
        """
        Make Testes In amenity_ids class attribute
        """
        self.assertEqual(list, type(self.cls.amenity_ids))
        self.assertIn("amenity_ids", dir(self.obj))
        self.assertNotIn("amenity_ids", self.obj.__dict__)
        if len(self.cls.amenity_ids) > 0:
            self.assertEqual(str, type(self.cls.amenity_ids[0]))


class TestPlace_Save(Basic_Save):
    """Unittests for testing save method of the Place class."""

    def __init__(self, *args, **kwargs):
        """
        Initialize The Class and Object For Place Class
        """
        super().__init__(*args, **kwargs)
        self.obj = Place()
        sleep(0.05)
        self.obj2 = Place()
        self.cls_name = 'Place'
        self.cls = Place

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

    def test_description_save(self):
        """
        Test if description cls saved in json
        """
        new_obj = self.cls()
        new_obj.description = 'some details'
        new_obj.save()
        key = f"{self.cls_name}.{new_obj.id}"
        with open(FileUtil.saved_file, "r")as f:
            re_dict = json.load(f)
        self.assertIn(key, re_dict)
        self.assertIn('description', re_dict[key])
        self.assertEqual(new_obj.description, re_dict[key]['description'])

    def test_number_rooms_save(self):
        """
        Test if number_rooms cls saved in json
        """
        new_obj = self.cls()
        new_obj.number_rooms = 30
        new_obj.save()
        key = f"{self.cls_name}.{new_obj.id}"
        with open(FileUtil.saved_file, "r")as f:
            re_dict = json.load(f)
        self.assertIn(key, re_dict)
        self.assertIn('number_rooms', re_dict[key])
        self.assertEqual(new_obj.number_rooms, re_dict[key]['number_rooms'])

    def test_number_bathrooms_save(self):
        """
        Test if number_bathrooms cls saved in json
        """
        new_obj = self.cls()
        new_obj.number_bathrooms = 3
        new_obj.save()
        key = f"{self.cls_name}.{new_obj.id}"
        with open(FileUtil.saved_file, "r")as f:
            re_dict = json.load(f)
        self.assertIn(key, re_dict)
        self.assertIn('number_bathrooms', re_dict[key])
        self.assertEqual(3, re_dict[key]['number_bathrooms'])

    def test_max_guest_save(self):
        """
        Test if max_guest cls saved in json
        """
        new_obj = self.cls()
        new_obj.max_guest = 60
        new_obj.save()
        key = f"{self.cls_name}.{new_obj.id}"
        with open(FileUtil.saved_file, "r")as f:
            re_dict = json.load(f)
        self.assertIn(key, re_dict)
        self.assertIn('max_guest', re_dict[key])
        self.assertEqual(new_obj.max_guest, re_dict[key]['max_guest'])

    def test_price_by_night_save(self):
        """
        Test if price_by_night cls saved in json
        """
        new_obj = self.cls()
        new_obj.price_by_night = 120
        new_obj.save()
        key = f"{self.cls_name}.{new_obj.id}"
        with open(FileUtil.saved_file, "r")as f:
            re_dict = json.load(f)
        self.assertIn(key, re_dict)
        self.assertIn('price_by_night', re_dict[key])
        self.assertEqual(120, re_dict[key]['price_by_night'])

    def test_latitude_save(self):
        """
        Test if latitude cls saved in json
        """
        new_obj = self.cls()
        new_obj.latitude = 3.5
        new_obj.save()
        key = f"{self.cls_name}.{new_obj.id}"
        with open(FileUtil.saved_file, "r")as f:
            re_dict = json.load(f)
        self.assertIn(key, re_dict)
        self.assertIn('latitude', re_dict[key])
        self.assertEqual(new_obj.latitude, re_dict[key]['latitude'])

    def test_longitude_save(self):
        """
        Test if longitude cls saved in json
        """
        new_obj = self.cls()
        new_obj.longitude = 4.0
        new_obj.save()
        key = f"{self.cls_name}.{new_obj.id}"
        with open(FileUtil.saved_file, "r")as f:
            re_dict = json.load(f)
        self.assertIn(key, re_dict)
        self.assertIn('longitude', re_dict[key])
        self.assertEqual(new_obj.longitude, re_dict[key]['longitude'])

    def test_city_id_save(self):
        """
        Test if city_id cls saved in json
        """
        new_obj = self.cls()
        new_obj.city_id = 'california'
        new_obj.save()
        key = f"{self.cls_name}.{new_obj.id}"
        with open(FileUtil.saved_file, "r")as f:
            re_dict = json.load(f)
        self.assertIn(key, re_dict)
        self.assertIn('city_id', re_dict[key])
        self.assertEqual(new_obj.city_id, re_dict[key]['city_id'])

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

    def test_amenity_ids_save(self):
        """
        Test if amenity_ids cls saved in json
        """
        new_obj = self.cls()
        new_obj.amenity_ids = ['a-124', 'b-504', 'x-777']
        new_obj.save()
        key = f"{self.cls_name}.{new_obj.id}"
        with open(FileUtil.saved_file, "r")as f:
            re_dict = json.load(f)
        self.assertIn(key, re_dict)
        self.assertIn('amenity_ids', re_dict[key])
        self.assertEqual(new_obj.amenity_ids, re_dict[key]['amenity_ids'])


class TestPlace_to_dict(Basic_to_dict):
    """Unittests for testing to_dict method of the Place class."""

    def __init__(self, *args, **kwargs):
        """
        Initialize The Class and Object For Place Class
        """
        super().__init__(*args, **kwargs)
        self.obj = Place()
        sleep(0.05)
        self.obj2 = Place(
            **{
                'id': 'a42ee380-c959-450e-ad29-c840a898cfce',
                'created_at': '2017-09-28T21:11:15.504287',
                'updated_at': '2017-09-28T21:11:15.504296',
                'name': 'Yousef Ahmed',
                'age': 19,
                'score': 93.9,
                '__class__': 'Place'
            }
        )
        self.cls_name = 'Place'
        self.cls = Place

    def test_have_special_keys_name(self):
        """
        Test if class attributes in the return of to_dict method
        """
        self.assertIn("name", self.cls.__dict__)
        self.cls.name = 'Youssef'
        self.assertIn("name", self.cls.__dict__)
        self.assertEqual("Youssef", self.cls.__dict__['name'])

    def test_have_special_keys_description(self):
        """
        Test if class attributes in the return of to_dict method
        """
        self.assertIn("description", self.cls.__dict__)
        self.cls.description = 'some details'
        self.assertIn("description", self.cls.__dict__)
        self.assertEqual("some details", self.cls.__dict__['description'])

    def test_have_special_keys_number_rooms(self):
        """
        Test if class attributes in the return of to_dict method
        """
        self.assertIn("number_rooms", self.cls.__dict__)
        self.cls.number_rooms = 30
        self.assertIn("number_rooms", self.cls.__dict__)
        self.assertEqual(30, self.cls.__dict__['number_rooms'])

    def test_have_special_keys_number_bathrooms(self):
        """
        Test if class attributes in the return of to_dict method
        """
        self.assertIn("number_bathrooms", self.cls.__dict__)
        self.cls.number_bathrooms = 3
        self.assertIn("number_bathrooms", self.cls.__dict__)
        self.assertEqual(3, self.cls.__dict__['number_bathrooms'])

    def test_have_special_keys_max_guest(self):
        """
        Test if class attributes in the return of to_dict method
        """
        self.assertIn("max_guest", self.cls.__dict__)
        self.cls.max_guest = 60
        self.assertIn("max_guest", self.cls.__dict__)
        self.assertEqual(60, self.cls.__dict__['max_guest'])

    def test_have_special_keys_price_by_night(self):
        """
        Test if class attributes in the return of to_dict method
        """
        self.assertIn("price_by_night", self.cls.__dict__)
        self.cls.price_by_night = 120
        self.assertIn("price_by_night", self.cls.__dict__)
        self.assertEqual(120, self.cls.__dict__['price_by_night'])

    def test_have_special_keys_latitude(self):
        """
        Test if class attributes in the return of to_dict method
        """
        self.assertIn("latitude", self.cls.__dict__)
        self.cls.latitude = 3.5
        self.assertIn("latitude", self.cls.__dict__)
        self.assertEqual(3.5, self.cls.__dict__['latitude'])

    def test_have_special_keys_longitude(self):
        """
        Test if class attributes in the return of to_dict method
        """
        self.assertIn("longitude", self.cls.__dict__)
        self.cls.longitude = 3.5
        self.assertIn("longitude", self.cls.__dict__)
        self.assertEqual(3.5, self.cls.__dict__['longitude'])

    def test_have_special_keys_city_id(self):
        """
        Test if class attributes in the return of to_dict method
        """
        self.assertIn("city_id", self.cls.__dict__)
        self.cls.city_id = 'california'
        self.assertIn("city_id", self.cls.__dict__)
        self.assertEqual('california', self.cls.__dict__['city_id'])

    def test_have_special_keys_user_id(self):
        """
        Test if class attributes in the return of to_dict method
        """
        self.assertIn("user_id", self.cls.__dict__)
        self.cls.user_id = 'a-54321'
        self.assertIn("user_id", self.cls.__dict__)
        self.assertEqual('a-54321', self.cls.__dict__['user_id'])

    def test_have_special_keys_amenity_ids(self):
        """
        Test if class attributes in the return of to_dict method
        """
        self.assertIn("amenity_ids", self.cls.__dict__)
        self.cls.amenity_ids = ['a-124', 'b-504']
        self.assertIn("amenity_ids", self.cls.__dict__)
        self.assertEqual(['a-124', 'b-504'], self.cls.__dict__['amenity_ids'])


if __name__ == "__main__":
    unittest.main()

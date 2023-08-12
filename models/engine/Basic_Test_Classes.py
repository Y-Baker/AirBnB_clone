#!/usr/bin/python3

"""
test module for a class
Define unittests for models/*.py
Unittest classes:
    Basic_Instantiation
    Basic_Save
    Basic_to_dict
"""

from models import storage
from models.base_model import BaseModel
import unittest
from datetime import datetime
from time import sleep
import os
from models.engine.available_class import FileUtil


class Basic_Instantiation(unittest.TestCase):
    """Unittests for testing instantiation of a specific class."""

    def __init__(self, *args, **kwargs):
        """
        Initialize The Class and Object For All Class
        """
        super().__init__(*args, **kwargs)
        self.obj = BaseModel()
        sleep(0.05)
        self.obj2 = BaseModel()
        self.cls_name = 'BaseModel'
        self.cls = BaseModel

    def test_no_args(self):
        """
        Test No args
        """
        self.assertEqual(self.cls, type(self.obj))

    def test_saved_in_stroge_dict(self):
        """
        Test The New Object in file_stroge.__objects
        """
        saved = storage.all().values()
        obj_dict = []
        for val in saved:
            obj_dict.append(val.to_dict())
        self.assertIn(self.obj.to_dict(), obj_dict)

    def test_id_is_str(self):
        """
        Test if the obj id is string
        """
        self.assertEqual(str, type(self.obj.id))

    def test_created_at_is_datetime(self):
        """
        Test if the obj created_at is datetime-type
        """
        self.assertEqual(datetime, type(self.obj.created_at))

    def test_updated_at_is_datetime(self):
        """
        Test if the obj updated_at is datetime-type
        """
        self.assertEqual(datetime, type(self.obj.updated_at))

    def test_two_obj_unique_id(self):
        """
        Test if two objects have different ids
        """
        self.assertNotEqual(self.obj.id, self.obj2.id)

    def test_time_different_in_created_at(self):
        """
        Test if the second obj created after the first obj
        """
        self.assertLess(self.obj.created_at, self.obj2.created_at)

    def test_time_different_in_updated_at(self):
        """
        Test if the second obj updated after the first obj
        """
        self.assertLess(self.obj.updated_at, self.obj2.updated_at)

    def test_str_representation(self):
        """
        Test if the str representation of a object is correct
        Usage: [<class>] (<id>) {<obj.__dict__>}
        """
        new_obj = self.cls()
        new_obj.id = "54321"
        dt = datetime.now()
        dt_repr = repr(dt)
        new_obj.created_at = new_obj.updated_at = dt
        obj_str = str(new_obj)

        self.assertIn(f"[{self.cls_name}] (54321)", obj_str)
        self.assertIn("'id': '54321'", obj_str)
        self.assertIn("'created_at': " + dt_repr, obj_str)
        self.assertIn("'updated_at': " + dt_repr, obj_str)

    def test_none_arg(self):
        """
        Test If args is None
        """
        new_obj = self.cls(None)
        self.assertNotIn(None, new_obj.__dict__.values())

    def test_with_args(self):
        """
        Test If instantiation with args
        """
        dt = datetime.now()
        dt_iso = dt.isoformat()
        new_obj = self.cls(id="123", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(new_obj.id, "123")
        self.assertEqual(new_obj.created_at, dt)
        self.assertEqual(new_obj.updated_at, dt)

    def test_with_none_kwargs(self):
        """
        Test it instantiation with none value in dict
        """
        with self.assertRaises(TypeError):
            self.cls(id=None, created_at=None, updated_at=None)

    def test_with_none_id(self):
        """
        Test it instantiation with none value in dict
        """
        dt = datetime.now().isoformat()
        new_obj = self.cls(id=None, created_at=dt, updated_at=dt)
        self.assertEqual(str, type(new_obj.id))

    def test_with_none_created_at(self):
        """
        Test it instantiation with none value in dict
        """
        dt = datetime.now().isoformat()
        with self.assertRaises(TypeError):
            self.cls(id="54321", created_at=None, updated_at=dt)

    def test_with_none_updated_at(self):
        """
        Test it instantiation with none value in dict
        """
        dt = datetime.now().isoformat()
        with self.assertRaises(TypeError):
            self.cls(id="12345", created_at=dt, updated_at=None)


class Basic_Save(unittest.TestCase):
    """Unittests for testing save method of a specific class."""

    def __init__(self, *args, **kwargs):
        """
        Initialize The Class and Object For All Class
        """
        super().__init__(*args, **kwargs)
        self.obj = BaseModel()
        sleep(0.05)
        self.obj2 = BaseModel()
        self.cls_name = 'BaseModel'
        self.cls = BaseModel

    def setUp(self):
        """
        set up Method called before each test
        """
        try:
            os.rename(FileUtil.saved_file, "tmp")
        except IOError:
            pass

    def tearDown(self):
        """
        tearDown Method Called after each test
        """
        try:
            os.remove(FileUtil.saved_file)
        except IOError:
            pass
        try:
            os.rename("tmp", FileUtil.saved_file)
        except IOError:
            pass

    def test_simple_save(self):
        """
        Test If updated at change when save the file after a while
        """
        sleep(0.05)
        f_update = self.obj.updated_at
        self.obj.save()
        self.assertLess(f_update, self.obj.updated_at)

    def test_two_saves(self):
        """
        Test Update_at changs when save twice
        """
        sleep(0.05)
        f_update = self.obj.updated_at
        self.obj.save()
        s_update = self.obj.updated_at
        sleep(0.05)
        self.obj.save()
        self.assertLess(f_update, s_update)
        self.assertLess(s_update, self.obj.updated_at)

    def test_save_with_arg_int(self):
        """
        Test save With args
        """
        new_obj = self.cls()
        with self.assertRaises(TypeError):
            new_obj.save(77)

    def test_save_with_arg_str(self):
        """
        Test save With args
        """
        new_obj = self.cls()
        with self.assertRaises(TypeError):
            new_obj.save('hi')

    def test_save_with_arg_None(self):
        """
        Test save With args
        """
        new_obj = self.cls()
        with self.assertRaises(TypeError):
            new_obj.save(None)

    def test_save_with_multi_arg(self):
        """
        Test save With args
        """
        new_obj = self.cls()
        with self.assertRaises(TypeError):
            new_obj.save(77, 'str', None)

    def test_save_with_file(self):
        """
        Test if the file *.json saved
        """
        self.obj.save()
        obj_id = self.cls_name + '.' + self.obj.id
        with open(FileUtil.saved_file, "r")as f:
            self.assertIn(obj_id, f.read())


class Basic_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of a specific class."""

    def __init__(self, *args, **kwargs):
        """
        Initialize The Class and Object For All Class
        """
        super().__init__(*args, **kwargs)
        self.obj = BaseModel()
        sleep(0.05)
        self.obj2 = BaseModel(
            **{
                'id': 'a42ee380-c959-450e-ad29-c840a898cfce',
                'created_at': '2017-09-28T21:11:15.504287',
                'updated_at': '2017-09-28T21:11:15.504296',
                'name': 'Yousef Ahmed',
                'age': 19,
                'score': 93.9,
                '__class__': 'BaseModel',
            }
        )
        self.cls_name = 'BaseModel'
        self.cls = BaseModel

    def test_to_dict_type(self):
        """
        Test The Type of the return value of to_dict Method
        """
        self.assertEqual(dict, type(self.obj.to_dict()))

    def test_num_keys(self):
        """
        Test Number of keys in to_dict dict
        """
        self.assertEqual(7, len(self.obj2.to_dict()))

    def test_have_default_keys(self):
        """
        Test IF to_dict method return correct keys
        """
        self.assertIn("id", self.obj.to_dict())
        self.assertIn("created_at", self.obj.to_dict())
        self.assertIn("updated_at", self.obj.to_dict())
        self.assertIn("__class__", self.obj.to_dict())

    def test_have_added_keys(self):
        """
        Test If to_dict method return the added attribute as keys
        """
        new_obj = self.cls()
        new_obj.full_name = "Yousef Ahmed"
        new_obj.age = 19
        new_obj.score = 93.9

        self.assertEqual("Yousef Ahmed", new_obj.full_name)
        self.assertEqual(19, new_obj.age)
        self.assertEqual(93.9, new_obj.score)
        self.assertIn("full_name", new_obj.to_dict())
        self.assertIn("age", new_obj.to_dict())
        self.assertIn("score", new_obj.to_dict())

    def test_type_in_to_dict(self):
        """
        Test type of to_dict values of the attributes
        """
        re_dict = self.obj.to_dict()
        self.assertEqual(str, type(re_dict["id"]))
        self.assertEqual(str, type(re_dict["created_at"]))
        self.assertEqual(str, type(re_dict["updated_at"]))

    def test_to_dict_output(self):
        """
        Test Output of to_dict Method
        """
        dt = datetime.now()
        new_obj = self.cls()
        new_obj.id = "123456"
        new_obj.created_at = new_obj.updated_at = dt
        re_dict = {
            'id': '123456',
            '__class__': self.cls_name,
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }

        self.assertDictEqual(re_dict, new_obj.to_dict())

    def test_to_dict_or_direct_dict(self):
        """
        Test if return of to_dict Method not equal __dict__ representation
        as __class__ not in __dict__ but in to_dict return
        """
        new_obj = self.cls()
        self.assertNotEqual(new_obj.to_dict(), new_obj.__dict__)

    def test_to_dict_with_arg_int(self):
        """
        Test if to_dict method has args
        """
        with self.assertRaises(TypeError):
            self.obj.to_dict(77)

    def test_to_dict_with_arg_str(self):
        """
        Test if to_dict method has args
        """
        with self.assertRaises(TypeError):
            self.obj.to_dict('str')

    def test_to_dict_with_arg_None(self):
        """
        Test if to_dict method has args
        """
        with self.assertRaises(TypeError):
            self.obj.to_dict(None)

    def test_to_dict_with_multi_args(self):
        """
        Test if to_dict method has args
        """
        with self.assertRaises(TypeError):
            self.obj.to_dict(77, 'str', None)


if __name__ == "__main__":
    pass

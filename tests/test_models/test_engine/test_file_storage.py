#!/usr/bin/python3
"""
test module for file storage
Defines unittests for file_storage.py.
Unittest classes:
"""
import json
import os
import unittest
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models import storage
from models.engine.available_class import FileUtil


class TestFileStorage(unittest.TestCase):
    """
    test cases for file storage class
    """

    @classmethod
    def setUpClass(cls) -> None:
        """
        method to set up class
        """
        cls.base1 = BaseModel(
            **{
                "id": "1002",
                "created_at": "2023-08-08T17:38:28.614516",
                "updated_at": "2023-06-07T22:09:22.546435",
            }
        )
        try:
            os.rename(FileUtil.saved_file, "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(cls):
        """
        tear down class
        """
        try:
            os.remove(FileUtil.saved_file)
        except IOError:
            pass
        try:
            os.rename("tmp", FileUtil.saved_file)
        except IOError:
            pass

    def test_instance(self):
        """
        test instantiation
        """
        self.assertEqual("1002", self.base1.id)

    def test_instance_fileStorage(self):
        """cheks for file storage class instantation"""
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)

    def test_docs(self):
        """Test for docstrings of file storage class"""
        self.assertIsNotNone(FileStorage.all)
        self.assertIsNotNone(FileStorage.new)
        self.assertIsNotNone(FileStorage.save)
        self.assertIsNotNone(FileStorage.reload)

    def test_all(self):
        """
        test method all that retries all objects saved in application memory
        """
        try:
            with open(FileUtil.saved_file) as fp:
                dict1 = json.load(fp)
                dict2 = storage.all()

                for (k1, v), (k2, value) in zip(dict1.items(), dict2.items()):
                    self.assertEqual(v, value.to_dict())
        except FileNotFoundError:
            pass

    def test_new_method(self):
        """
        test method new that sets a new objects in the objects dictionary
        with key class name.obj_id
        """
        self.base1.name = "abdo"
        storage.new(self.base1)
        dict2 = storage.all()
        obj = dict2["BaseModel.1002"]
        self.assertEqual(obj.to_dict(), self.base1.to_dict())
        self.assertEqual("abdo", dict2["BaseModel.1002"].name)

    def test_new_sets_object_in_objects_dictionary_with_correct_key(self):
        file_storage = FileStorage()
        model_key = f"{self.base1.__class__.__name__}.{self.base1.id}"
        file_storage.new(self.base1)
        dictt = file_storage.all()
        self.assertEqual(dictt[model_key].to_dict(), self.base1.to_dict())

    def test_save(self):
        """
        test method for save method in filestorage class
        to check it saves in the file or not
        """
        storage.new(self.base1)
        storage.save()
        with open(FileUtil.saved_file) as fp:
            dict1 = json.load(fp)
            self.assertIn(self.base1.to_dict(), dict1.values())

    def test_reload(self):
        """
        test method for reload method in filestorage class
        to check it reloads in the file or not
        """
        try:
            if os.stat(FileUtil.saved_file).st_size > 0:
                self.assertGreater(len(storage.all()), 0)
        except FileNotFoundError:
            pass

    def test_save_and_reload(self):
        """
        test method for reload method in filestorage class
        to check it reloads in the file or not
        """
        try:
            city = City()
            city.name = "cairo"
            storage.save()
            if os.stat(FileUtil.saved_file).st_size > 0:
                storage.reload()
                dict1 = storage.all()
                self.assertIn(f"City.{city.id}", dict1)
                reloaded_city = dict1[f"City.{city.id}"]
                self.assertEqual(city.id, reloaded_city.id)
                self.assertEqual(city.name, reloaded_city.name)
        except FileNotFoundError:
            pass

    def test_reload_empty_file(self):
        """
        test reloading from an empty file
        """
        objects = {}
        from models.engine.available_class import FileUtil
        my_classes = FileUtil.my_Classes
        try:
            if os.stat('./empty_file.json').st_size > 0:
                with open('./empty_file.json') as fp:
                    stored_data = json.load(fp)
                    for key, value in stored_data.items():
                        class_name = stored_data[key]['__class__']
                        objects[key] \
                            = my_classes[class_name](**stored_data[key])
            self.assertEqual(0, len(objects))

        except FileNotFoundError:
            pass

    def test_save_file_not_exist_empty_dict(self):
        """
        test saving in file hat doesn't exist
        """
        objects = {}
        directory = os.path.dirname('./not_exist.json')
        if not os.path.exists(directory):
            os.makedirs(directory)

        new_dict = {
            key: value.to_dict()
            for key, value in objects.items()
        }
        with open('./not_exist.json', "w") as f:
            json.dump(new_dict, f, indent=4)

    def test_save_file_not_exist_not_empty(self):
        """
        test saving in file hat doesn't exist
        """
        file_path = './not_exist.json'
        objects = {'BaseModel.1002': self.base1}
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        new_dict = {
            key: value.to_dict()
            for key, value in objects.items()
        }
        with open(file_path, "w") as f:
            json.dump(new_dict, f, indent=4)

        self.assertGreater(os.path.getsize(file_path), 0)

    def test_save_file_not_exist_not_empty_then_reload(self):
        """
        test saving in file hat doesn't exist
        """
        file_path = './not_exist.json'
        objects = {'BaseModel.1002': self.base1}
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        new_dict = {
            key: value.to_dict()
            for key, value in objects.items()
        }
        with open(file_path, "w") as f:
            json.dump(new_dict, f, indent=4)

        self.assertGreater(os.path.getsize(file_path), 0)

        from models.engine.available_class import FileUtil
        my_classes = FileUtil.my_Classes
        try:
            if os.stat(file_path).st_size > 0:
                with open(file_path) as fp:
                    stored_data = json.load(fp)
                    for key, value in stored_data.items():
                        class_name = stored_data[key]['__class__']
                        objects[key] \
                            = my_classes[class_name](**stored_data[key])
            self.assertEqual(self.base1.to_dict(),
                             objects['BaseModel.1002'].to_dict())
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    unittest.main()

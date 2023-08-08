#!/usr/bin/python3
"""
test module for baseclass
Defines unittests for base.py.
Unittest classes:
    TestBase_instantiation - line 23
    TestBase_to_json_string - line 110
    TestBase_save_to_file - line 156
    TestBase_from_json_string - line 234
    TestBase_create - line 288
    TestBase_load_from_file - line 340
    TestBase_save_to_file_csv - line 406
    TestBase_load_from_file_csv - line 484
"""
import datetime
import unittest
import uuid

from models.base_model import BaseModel


class TestBaseModelInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    @classmethod
    def setUpClass(cls) -> None:
        """
        set up class method
        """
        cls.base = BaseModel()
        cls.base2 = BaseModel(**{'id': '534b886d-ee20-4d43-bc78-208616fd05af',
                                 'created_at': '2023-08-08T17:38:28.614516',
                                 'updated_at': '2023-08-08T17:38:28.614520',
                                 'name': 'My_First_Model',
                                 'my_number': 89,
                                 '__class__': 'BaseModel'})
        cls.base3 = BaseModel(**{'id': None,
                                 'created_at': '2023-08-08T17:38:28.614516',
                                 'updated_at': '2023-08-08T17:38:28.614520',
                                 'name': 'My_First_Model',
                                 'my_number': 89,
                                 'age': 50,
                                 '__class__': 'BaseModel'})
        cls.base4 = BaseModel(**{
            'created_at': '2023-08-08T17:38:28.614516',
            'updated_at': '2023-08-08T17:38:28.614520',
            'name': 'My_First_Model',
            'my_number': 89,

            '__class__': 'BaseModel'})
        cls.base5 = BaseModel(**{
            'id': '1001',
            'created_at': '2023-08-08',
            'updated_at': '2023-08-08T17:38:28.614520',
            '__class__': 'BaseModel'})

    def test_no_arg(self):
        """
        test no args
        """
        self.assertEqual(type(self.base.id), type(str(uuid.uuid4())))
        self.assertEqual(type(self.base.created_at),
                         type((datetime.datetime.now())))
        self.assertEqual(type(self.base.updated_at),
                         type((datetime.datetime.now())))

    def test_kwargs(self):
        """
        test with kwargs
        """
        self.assertEqual(self.base2.id,
                         '534b886d-ee20-4d43-bc78-208616fd05af')
        self.assertEqual(self.base2.created_at,
                         datetime.datetime
                         .fromisoformat('2023-08-08T17:38:28.614516'))
        self.assertEqual(self.base2.updated_at,
                         datetime.datetime
                         .fromisoformat('2023-08-08T17:38:28.614520'))
        self.assertEqual(self.base2.name,
                         'My_First_Model')
        self.assertEqual(self.base2.my_number,
                         89)
        self.assertEqual(self.base2.__class__.__name__,
                         BaseModel.__name__)

    def test_kwargs_id_None(self):
        """
        test with kwargs
        """
        self.assertEqual(type(self.base3.id), type(str(uuid.uuid4())))
        self.assertEqual(self.base3.created_at,
                         datetime.datetime
                         .fromisoformat('2023-08-08T17:38:28.614516'))
        self.assertEqual(self.base3.updated_at,
                         datetime
                         .datetime.fromisoformat('2023-08-08T17:38:28.614520'))
        self.assertEqual(self.base3.name,
                         'My_First_Model')
        self.assertEqual(self.base3.my_number,
                         89)
        self.assertEqual(self.base3.__class__.__name__,
                         BaseModel.__name__)
        self.assertEqual(self.base3.age, 50)

    def test_kwargs_id_Not_provided(self):
        """
            test with kwargs
        """
        self.assertEqual(type(self.base4.id), type(str(uuid.uuid4())))
        self.assertEqual(self.base4.created_at,
                         datetime.datetime
                         .fromisoformat('2023-08-08T17:38:28.614516'))
        self.assertEqual(self.base4.updated_at,
                         datetime.datetime
                         .fromisoformat('2023-08-08T17:38:28.614520'))
        self.assertEqual(self.base4.name,
                         'My_First_Model')
        self.assertEqual(self.base4.my_number,
                         89)
        self.assertEqual(self.base4.__class__.__name__,
                         BaseModel.__name__)

    def test_kwargs_created_at_not_iso(self):
        """
            test with kwargs
        """
        self.assertEqual(self.base5.id, '1001')
        self.assertEqual(datetime.datetime, self.base5.created_at.__class__)
        self.assertEqual(self.base5.updated_at,
                         datetime.datetime
                         .fromisoformat('2023-08-08T17:38:28.614520'))
        self.assertEqual(self.base5.__class__.__name__,
                         BaseModel.__name__)


class TestBase_to_dict(unittest.TestCase):
    """Unittests for testing to_json_string method of Base class."""

    @classmethod
    def setUpClass(cls) -> None:
        """
        set up class method
        """
        cls.base2 = BaseModel(**{'id': '534b886d-ee20-4d43-bc78-208616fd05af',
                                 'created_at': '2023-08-08T17:38:28.614516',
                                 'updated_at': '2023-08-08T17:38:28.614520',
                                 'name': 'My_First_Model',
                                 'my_number': 89,
                                 '__class__': 'BaseModel'})
        cls.base5 = BaseModel(**{
            'id': '1001',
            'created_at': '2023-08-08',
            'updated_at': '2023-08-08T17:38:28.614520',
            '__class__': 'BaseModel'})

        cls.dict2 = {'id': '534b886d-ee20-4d43-bc78-208616fd05af',
                     'created_at': '2023-08-08T17:38:28.614516',
                     'updated_at': '2023-08-08T17:38:28.614520',
                     'name': 'My_First_Model',
                     'my_number': 89,
                     '__class__': 'BaseModel'}

        cls.dict5 = {'__class__': 'BaseModel',
                     'created_at': '2023-08-08T00:00:00',
                     'id': '1001',
                     'updated_at': '2023-08-08T17:38:28.614520'}

    def test_base_model_to_dict(self):
        """
        test_base_model_to_dict
        """
        self.assertEqual(self.base2.to_dict().__class__, dict)
        self.assertEqual(self.dict2, self.base2.to_dict())
        self.assertEqual(6, len(self.base2.to_dict()))

    def test_base_model_to_dict2(self):
        """
        test_base_model_to_dict2
        """
        self.assertEqual(self.base5.to_dict().__class__, dict)
        self.assertEqual(self.dict5, self.base5.to_dict())
        self.assertEqual(4, len(self.base5.to_dict()))

    def test_base_model_to_str(self):
        """
        test_base_model_to_dict2
        """

        self.assertEqual(270, len(self.base2.__str__()))
        self.assertEqual("[BaseModel] (534b886d-ee20-4d43-bc78-208616fd05af) "
                         "{'id': '534b886d-ee20-4d43-bc78-208616fd05af', "
                         "'created_at': "
                         "datetime.datetime(2023, 8, 8, 17, 38, 28, 614516), "
                         "'updated_at': "
                         "datetime.datetime(2023, 8, 8, 17, 38, 28, 614520), "
                         "'name': 'My_First_Model', "
                         "'my_number': 89}", self.base2.__str__())

    def test_base_model_to_str2(self):
        """
        test_base_model_to_dict2
        """
        self.assertEqual(149, len(self.base5.__str__()))
        self.assertEqual("[BaseModel] (1001) {'id': '1001',"
                         " 'created_at': "
                         "datetime.datetime(2023, 8, 8, 0, 0), "
                         "'updated_at': "
                         "datetime.datetime(2023, 8, 8, 17, 38, 28, 614520)}",
                         self.base5.__str__())

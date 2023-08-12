#!/usr/bin/python3
"""
Test module for baseclass
Defines unittests for base.py.
Unittest classes:
    TestBase_instantiation - line 23
    TestBase_to_json_string - line 110
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
        cls.base1 = BaseModel()
        cls.base2 = BaseModel(
            **{
                "id": "534b886d-ee20-4d43-bc78-208616fd05af",
                "created_at": "2023-08-08T17:38:28.614516",
                "updated_at": "2023-08-08T17:38:28.614520",
                "name": "My_First_Model",
                "my_number": 89,
                "__class__": "BaseModel",
            }
        )
        cls.base3 = BaseModel(
            **{
                "id": None,
                "created_at": "2023-08-08T17:38:28.614516",
                "updated_at": "2023-08-08T17:38:28.614520",
                "name": "My_First_Model",
                "my_number": 89,
                "age": 50,
                "__class__": "BaseModel",
            }
        )
        cls.base4 = BaseModel(
            **{
                "created_at": "2023-08-08T17:38:28.614516",
                "updated_at": "2023-08-08T17:38:28.614520",
                "name": "My_First_Model",
                "my_number": 89,
                "__class__": "BaseModel",
            }
        )
        cls.base5 = BaseModel(
            **{
                "id": "1001",
                "created_at": "2023-08-08",
                "updated_at": "2023-08-08T17:38:28.614520",
                "__class__": "BaseModel",
            }
        )

    def test_save_new_instance_1(self):
        """
        test_save_new_instance_1
        """
        old_date = self.base.updated_at
        self.base.save()

        self.assertNotEqual(old_date, self.base.updated_at)

    def test_no_arg(self):
        """
        test no args
        """
        self.assertEqual(type(self.base.id), type(str(uuid.uuid4())))
        self.assertEqual(type(self.base.created_at),
                         type((datetime.datetime.now())))
        self.assertEqual(type(self.base.updated_at),
                         type((datetime.datetime.now())))

    def test_no_arg2(self):
        """
        test no args 2
        """
        self.assertNotEqual(self.base.id, self.base1.id)

    def test_no_arg3(self):
        """
        test no args 3
        """
        self.assertTrue(hasattr(self.base, 'id'))

    def test_no_arg4(self):
        """
        test no args 4
        """
        self.assertTrue(hasattr(self.base, 'created_at'))

    def test_no_arg5(self):
        """
        test no args 5
        """
        self.assertTrue(hasattr(self.base, 'updated_at'))

    def test_kwargs(self):
        """
        test with kwargs
        """
        self.assertEqual(self.base2.id, "534b886d-ee20-4d43-bc78-208616fd05af")
        self.assertEqual(
            self.base2.created_at,
            datetime.datetime.fromisoformat("2023-08-08T17:38:28.614516"),
        )
        self.assertEqual(
            self.base2.updated_at,
            datetime.datetime.fromisoformat("2023-08-08T17:38:28.614520"),
        )
        self.assertEqual(self.base2.name, "My_First_Model")
        self.assertEqual(self.base2.my_number, 89)
        self.assertEqual(self.base2.__class__.__name__, BaseModel.__name__)

    def test_kwargs_id_None(self):
        """
        test with kwargs
        """
        self.assertEqual(type(self.base3.id), type(str(uuid.uuid4())))
        self.assertEqual(
            self.base3.created_at,
            datetime.datetime.fromisoformat("2023-08-08T17:38:28.614516"),
        )
        self.assertEqual(
            self.base3.updated_at,
            datetime.datetime.fromisoformat("2023-08-08T17:38:28.614520"),
        )
        self.assertEqual(self.base3.name, "My_First_Model")
        self.assertEqual(self.base3.my_number, 89)
        self.assertEqual(self.base3.__class__.__name__, BaseModel.__name__)
        self.assertEqual(self.base3.age, 50)

    def test_kwargs_id_Not_provided(self):
        """
        test with kwargs
        """
        self.assertEqual(type(self.base4.id), type(str(uuid.uuid4())))
        self.assertEqual(
            self.base4.created_at,
            datetime.datetime.fromisoformat("2023-08-08T17:38:28.614516"),
        )
        self.assertEqual(
            self.base4.updated_at,
            datetime.datetime.fromisoformat("2023-08-08T17:38:28.614520"),
        )
        self.assertEqual(self.base4.name, "My_First_Model")
        self.assertEqual(self.base4.my_number, 89)
        self.assertEqual(self.base4.__class__.__name__, BaseModel.__name__)

    def test_kwargs_created_at_not_iso(self):
        """
        test with kwargs
        """
        self.assertEqual(self.base5.id, "1001")
        self.assertEqual(datetime.datetime, self.base5.created_at.__class__)
        self.assertEqual(
            self.base5.updated_at,
            datetime.datetime.fromisoformat("2023-08-08T17:38:28.614520"),
        )
        self.assertEqual(self.base5.__class__.__name__, BaseModel.__name__)

    def test_id_not_uuid_int(self):
        """
        test with kwargs
        """
        base = BaseModel(**{"id": 4654})
        self.assertEqual(4654, base.id)

    def test_id_not_uuid_str(self):
        """
        test with kwargs
        """
        base = BaseModel(**{"id": "4654"})
        self.assertEqual("4654", base.id)

    def test_id_not_uuid_float(self):
        """
        test with kwargs
        """
        base = BaseModel(**{"id": 4654.564})
        self.assertEqual(4654.564, base.id)

    def test_id_not_uuid_bool(self):
        """
        test with kwargs
        """
        base = BaseModel(**{"id": True})
        self.assertEqual(True, base.id)

    def test_id_not_uuid_bool2(self):
        """
        test with kwargs
        """
        base = BaseModel(**{"id": False})
        self.assertEqual(False, base.id)

    def test_id_not_uuid_complex(self):
        """
        test with kwargs
        """
        base = BaseModel(**{"id": complex(1j)})
        self.assertEqual(complex(1j), base.id)

    def test_id_not_uuid_list(self):
        """
        test with kwargs
        """
        base = BaseModel(**{"id": [4654, 654, 879]})
        self.assertEqual([4654, 654, 879], base.id)

    def test_id_not_uuid_tuple(self):
        """
        test with kwargs
        """
        base = BaseModel(**{"id": (4654, 568, 465)})
        self.assertEqual((4654, 568, 465), base.id)

    def test_id_not_uuid_dict(self):
        """
        test with kwargs
        """
        base = BaseModel(**{"id": {"name": "val", "age": 17}})
        self.assertEqual({"name": "val", "age": 17}, base.id)

    def test_id_not_uuid_set(self):
        """
        test with kwargs
        """
        base = BaseModel(**{"id": {4654, 568, 465}})
        self.assertEqual({4654, 568, 465}, base.id)

    def test_created_at_not_date_str(self):
        """
        test_created_at_not_date_str
        """
        with self.assertRaises(ValueError):
            BaseModel(
                **{
                    "id": "654654",
                    "created_at": "okays",
                    "updated_at": "2023-08-08T17:38:28.614516",
                }
            )

    def test_created_at_not_date_float(self):
        """
        test_created_at_not_date_str
        """
        with self.assertRaises(TypeError):
            BaseModel(
                **{
                    "id": "654654",
                    "created_at": 564.4698,
                    "updated_at": "2023-08-08T17:38:28.614516",
                }
            )

    def test_created_at_not_date_int(self):
        """
        test_created_at_not_date_str
        """
        with self.assertRaises(TypeError):
            BaseModel(
                **{
                    "id": "654654",
                    "created_at": 564,
                    "updated_at": "2023-08-08T17:38:28.614516",
                }
            )

    def test_created_at_not_date_bool(self):
        """
        test_created_at_not_date_bool
        """
        with self.assertRaises(TypeError):
            BaseModel(
                **{
                    "id": "654654",
                    "created_at": True,
                    "updated_at": "2023-08-08T17:38:28.614516",
                }
            )

    def test_created_at_not_date_int_1(self):
        """
        test_created_at_not_date_int
        """
        with self.assertRaises(ValueError):
            BaseModel(
                **{
                    "id": "654654",
                    "created_at": "564",
                    "updated_at": "2023-08-08T17:38:28.614516",
                }
            )

    def test_created_at_not_date_float_1(self):
        """
        test_created_at_not_date_float
        """
        with self.assertRaises(ValueError):
            BaseModel(
                **{
                    "id": "654654",
                    "created_at": "5668.154",
                    "updated_at": "2023-08-08T17:38:28.614516",
                }
            )

    def test_updated_at_not_date_str(self):
        """
        test_updated_at_not_date_str
        """
        with self.assertRaises(ValueError):
            BaseModel(
                **{
                    "id": "654654",
                    "updated_at": "okays",
                    "created_at": "2023-08-08T17:38:28.614516",
                }
            )

    def test_updated_at_not_date_float(self):
        """
        test_updated_at_not_date_float
        """
        with self.assertRaises(TypeError):
            BaseModel(
                **{
                    "id": "654654",
                    "updated_at": 564.4698,
                    "created_at": "2023-08-08T17:38:28.614516",
                }
            )

    def test_updated_at_not_date_int(self):
        """
        test_updated_at_not_date_int
        """
        with self.assertRaises(TypeError):
            BaseModel(
                **{
                    "id": "654654",
                    "updated_at": 564,
                    "created_at": "2023-08-08T17:38:28.614516",
                }
            )

    def test_updated_at_not_date_bool(self):
        """
        test_updated_at_not_date_bool
        """
        with self.assertRaises(TypeError):
            BaseModel(
                **{
                    "id": "654654",
                    "updated_at": True,
                    "created_at": "2023-08-08T17:38:28.614516",
                }
            )

    def test_updated_at_not_date_int_1(self):
        """
        test_updated_at_not_date_int
        """
        with self.assertRaises(ValueError):
            BaseModel(
                **{
                    "id": "654654",
                    "updated_at": "564",
                    "created_at": "2023-08-08T17:38:28.614516",
                }
            )

    def test_updated_at_not_date_float_1(self):
        """
        test_updated_at_not_date_float
        """
        with self.assertRaises(ValueError):
            BaseModel(
                **{
                    "id": "654654",
                    "updated_at": "5668.154",
                    "created_at": "2023-08-08T17:38:28.614516",
                }
            )

    def test_unpacking__class__attr_int(self):
        """
        test_unpacking__class__attr_int
        """
        base = BaseModel(
            **{
                "id": "654654",
                "updated_at": "2023-08-08T17:38:28.614516",
                "created_at": "2023-08-08T17:38:28.614516",
                "__class__": 4564,
            }
        )
        self.assertEqual(BaseModel, base.__class__)

    def test_unpacking__class__attr_float(self):
        """
        test_unpacking__class__attr_float
        """
        base = BaseModel(
            **{
                "id": "654654",
                "updated_at": "2023-08-08T17:38:28.614516",
                "created_at": "2023-08-08T17:38:28.614516",
                "__class__": 4564.564,
            }
        )
        self.assertEqual(BaseModel, base.__class__)

    def test_unpacking__class__attr_str(self):
        """
        test_unpacking__class__attr_str
        """
        base = BaseModel(
            **{
                "id": "654654",
                "updated_at": "2023-08-08T17:38:28.614516",
                "created_at": "2023-08-08T17:38:28.614516",
                "__class__": "4564",
            }
        )
        self.assertEqual(BaseModel, base.__class__)

    def test_unpacking__class__attr_bool(self):
        """
        test_unpacking__class__attr_bool
        """
        base = BaseModel(
            **{
                "id": "654654",
                "updated_at": "2023-08-08T17:38:28.614516",
                "created_at": "2023-08-08T17:38:28.614516",
                "__class__": True,
            }
        )
        self.assertEqual(BaseModel, base.__class__)

    def test_unpacking_different_attr_int(self):
        """
        test_unpacking_different_attr_int
        """
        x = 5
        base = BaseModel(
            **{
                "id": "654654",
                "updated_at": "2023-08-08T17:38:28.614516",
                "created_at": "2023-08-08T17:38:28.614516",
                "__class__": True,
                "x": x,
            }
        )
        self.assertEqual(x, base.x)

    def test_unpacking_different_attr_float(self):
        """
        test_unpacking_different_attr_float
        """
        x = 546.4654
        base = BaseModel(
            **{
                "id": "654654",
                "updated_at": "2023-08-08T17:38:28.614516",
                "created_at": "2023-08-08T17:38:28.614516",
                "__class__": True,
                "x": x,
            }
        )
        self.assertEqual(x, base.x)

    def test_unpacking_different_attr_bool(self):
        """
        test_unpacking_different_attr_bool
        """
        x = True
        base = BaseModel(
            **{
                "id": "654654",
                "updated_at": "2023-08-08T17:38:28.614516",
                "created_at": "2023-08-08T17:38:28.614516",
                "__class__": True,
                "x": x,
            }
        )
        self.assertEqual(x, base.x)

    def test_unpacking_different_attr_list(self):
        """
        test_unpacking_different_attr_list
        """
        x = [True, 56, "str"]
        base = BaseModel(
            **{
                "id": "654654",
                "updated_at": "2023-08-08T17:38:28.614516",
                "created_at": "2023-08-08T17:38:28.614516",
                "__class__": True,
                "x": x,
            }
        )
        self.assertEqual(x, base.x)

    def test_unpacking_different_attr_tuple(self):
        """
        test_unpacking_different_attr_tuple
        """
        x = (True, 85964, "basque")
        base = BaseModel(
            **{
                "id": "654654",
                "updated_at": "2023-08-08T17:38:28.614516",
                "created_at": "2023-08-08T17:38:28.614516",
                "__class__": True,
                "x": x,
            }
        )
        self.assertEqual(x, base.x)

    def test_unpacking_different_attr_set(self):
        """
        test_unpacking_different_attr_set
        """
        x = {"asd", 64968, True}
        base = BaseModel(
            **{
                "id": "654654",
                "updated_at": "2023-08-08T17:38:28.614516",
                "created_at": "2023-08-08T17:38:28.614516",
                "__class__": True,
                "x": x,
            }
        )
        self.assertEqual(x, base.x)

    def test_unpacking_different_attr_dict(self):
        """
        test_unpacking_different_attr_dict
        """
        x = {"id": 654, "name": "Ramada", "age": 50}
        base = BaseModel(
            **{
                "id": "654654",
                "updated_at": "2023-08-08T17:38:28.614516",
                "created_at": "2023-08-08T17:38:28.614516",
                "__class__": True,
                "x": x,
            }
        )
        self.assertEqual(x, base.x)


class TestBase_to_dict(unittest.TestCase):
    """Unittests for testing to_json_string method of Base class."""

    @classmethod
    def setUpClass(cls) -> None:
        """
        set up class method
        """
        cls.base2 = BaseModel(
            **{
                "id": "534b886d-ee20-4d43-bc78-208616fd05af",
                "created_at": "2023-08-08T17:38:28.614516",
                "updated_at": "2023-08-08T17:38:28.614520",
                "name": "My_First_Model",
                "my_number": 89,
                "__class__": "BaseModel",
            }
        )
        cls.base5 = BaseModel(
            **{
                "id": "1001",
                "created_at": "2023-08-08",
                "updated_at": "2023-08-08T17:38:28.614520",
                "__class__": "BaseModel",
            }
        )

        cls.dict2 = {
            "id": "534b886d-ee20-4d43-bc78-208616fd05af",
            "created_at": "2023-08-08T17:38:28.614516",
            "updated_at": "2023-08-08T17:38:28.614520",
            "name": "My_First_Model",
            "my_number": 89,
            "__class__": "BaseModel",
        }

        cls.dict5 = {
            "__class__": "BaseModel",
            "created_at": "2023-08-08T00:00:00",
            "id": "1001",
            "updated_at": "2023-08-08T17:38:28.614520",
        }

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
        test_base_model_to_str
        """

        self.assertEqual(270, len(self.base2.__str__()))
        self.assertEqual(
            "[BaseModel] (534b886d-ee20-4d43-bc78-208616fd05af) "
            "{'id': '534b886d-ee20-4d43-bc78-208616fd05af', "
            "'created_at': "
            "datetime.datetime(2023, 8, 8, 17, 38, 28, 614516), "
            "'updated_at': "
            "datetime.datetime(2023, 8, 8, 17, 38, 28, 614520), "
            "'name': 'My_First_Model', "
            "'my_number': 89}",
            self.base2.__str__(),
        )

    def test_base_model_to_str2(self):
        """
        test_base_model_to_str2
        """
        self.assertEqual(149, len(self.base5.__str__()))
        self.assertEqual(
            "[BaseModel] (1001) {'id': '1001',"
            " 'created_at': "
            "datetime.datetime(2023, 8, 8, 0, 0), "
            "'updated_at': "
            "datetime.datetime(2023, 8, 8, 17, 38, 28, 614520)}",
            self.base5.__str__(),
        )

    def test_save_from_unpacking_1(self):
        """
        test_save_from unpacking_1
        """
        base = BaseModel(
            **{
                "id": "1",
                "created_at": "2023-08-08T17:38:28.614520",
                "updated_at": "2023-08-08T17:38:28.614520",
            }
        )
        old_date = base.updated_at
        base.save()
        self.assertNotEqual(old_date, base.updated_at)

    def test_save_from_unpacking_2(self):
        """
        test_save_from unpacking_2


        """
        old_date = self.base5.updated_at
        self.base5.save()
        self.assertNotEqual(old_date, self.base5.updated_at)


if __name__ == "__main__":
    unittest.main()

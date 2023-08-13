#!/usr/bin/python3
"""
module to test console.py
classes of testing:
class TestHelpOutput(unittest.TestCase):
class Test_console_prompting(unittest.TestCase):
class Test_parseline(unittest.TestCase):
class Test_ParseLine_Detected_BaseModel(unittest.TestCase):
class Test_ParseLine_Detected_Amenity(unittest.TestCase):
class Test_ParseLine_Detected_City(unittest.TestCase):
class Test_ParseLine_Detected_Place(unittest.TestCase):
class Test_ParseLine_Detected_Review(unittest.TestCase):
class Test_ParseLine_Detected_State(unittest.TestCase):
class Test_ParseLine_Detected_User(unittest.TestCase):
class Test_ParseLine_not_Detected(unittest.TestCase):
class Test_extract_function_info(unittest.TestCase):

"""
import re
import unittest
from unittest.mock import patch
from console import HBNBCommand
from console import extract_function_info
from console import list_string_to_dict
from console import split_args
from models import storage
from models.user import User
from datetime import datetime

from models.engine.file_storage import FileStorage
import os
from io import StringIO
from models.engine.available_class import FileUtil


class TestHelpOutput(unittest.TestCase):
    @patch("sys.stdout", new_callable=StringIO)
    def test_function_output(self, mock_stdout):
        """
        TestHelpOutput test_function_output
        """
        HBNBCommand().onecmd("help")
        expected_output = """Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  patch_all  quit  show  update"""
        self.assertEqual(expected_output, mock_stdout.getvalue().strip())
        self.assertFalse(HBNBCommand().onecmd("help quit"))

    @patch("sys.stdout", new_callable=StringIO)
    def test_help_EOP(self, mock_stdout):
        """
        TestHelpOutput test_EOF
        """
        HBNBCommand().onecmd("help EOF")
        expected_output = """EOF signal to exit the program"""
        self.assertEqual(expected_output, mock_stdout.getvalue().strip())
        self.assertFalse(HBNBCommand().onecmd("help EOF"))

    @patch("sys.stdout", new_callable=StringIO)
    def test_help_all(self, mock_stdout):
        """
        TestHelpOutput test all
        """
        HBNBCommand().onecmd("help all")
        expected_output = """Prints all string representation of all instances
        based or not on a class name
        Usage: all BaseModel or all"""
        self.assertEqual(expected_output, mock_stdout.getvalue().strip())
        self.assertFalse(HBNBCommand().onecmd("help all"))

    @patch("sys.stdout", new_callable=StringIO)
    def test_help_count(self, mock_stdout):
        """
        TestHelpOutput test count
        """
        HBNBCommand().onecmd("help count")
        expected_output = """Return: the Number of instance Based on Class name
        Usage: Usage: count <class> or <class>.count()"""
        self.assertEqual(expected_output, mock_stdout.getvalue().strip())
        self.assertFalse(HBNBCommand().onecmd("help count"))

    @patch("sys.stdout", new_callable=StringIO)
    def test_help_create(self, mock_stdout):
        """
        TestHelpOutput test create
        """
        HBNBCommand().onecmd("help create")
        expected_output = """Create New instance
        Usage: create BaseModel"""
        self.assertEqual(expected_output, mock_stdout.getvalue().strip())
        self.assertFalse(HBNBCommand().onecmd("help create"))

    @patch("sys.stdout", new_callable=StringIO)
    def test_help_destroy(self, mock_stdout):
        """
        TestHelpOutput test destroy
        """
        HBNBCommand().onecmd("help destroy")
        expected_output = """Deletes an instance based on the class name and id
        Usage: destroy BaseModel <id>"""
        self.assertEqual(expected_output, mock_stdout.getvalue().strip())
        self.assertFalse(HBNBCommand().onecmd("help destroy"))

    @patch("sys.stdout", new_callable=StringIO)
    def test_help_help(self, mock_stdout):
        """
        TestHelpOutput test help help
        """
        HBNBCommand().onecmd("help help")
        expected_output = (
            """List available commands with "help" or \
detailed help with "help cmd"."""
        )
        self.assertEqual(expected_output, mock_stdout.getvalue().strip())
        self.assertFalse(HBNBCommand().onecmd("help help"))

    @patch("sys.stdout", new_callable=StringIO)
    def test_help_patch_all(self, mock_stdout):
        """
        TestHelpOutput test patch_all
        """
        HBNBCommand().onecmd("help patch_all")
        expected_output = """function to update multiple items at same time"""
        self.assertEqual(expected_output, mock_stdout.getvalue().strip())
        self.assertFalse(HBNBCommand().onecmd("help patch_all"))

    @patch("sys.stdout", new_callable=StringIO)
    def test_help_quit(self, mock_stdout):
        """
        TestHelpOutput test help quit
        """
        HBNBCommand().onecmd("help quit")
        expected_output = """Quit command to exit the program."""
        self.assertEqual(expected_output, mock_stdout.getvalue().strip())
        self.assertFalse(HBNBCommand().onecmd("help quit"))

    @patch("sys.stdout", new_callable=StringIO)
    def test_help_show(self, mock_stdout):
        """
        TestHelpOutput test help show
        """
        HBNBCommand().onecmd("help show")
        expected_output = """Print str-representation of an \
instance based on class name, id
        Usage: show BaseModel <id>"""
        self.assertEqual(expected_output, mock_stdout.getvalue().strip())
        self.assertFalse(HBNBCommand().onecmd("help show"))

    @patch("sys.stdout", new_callable=StringIO)
    def test_help_update(self, mock_stdout):
        """
        TestHelpOutput test help update
        """
        HBNBCommand().onecmd("help update")
        expected_output = """Updates an instance based on the class name and id
        by adding or updating attribute
        Usage: update <class name> <id> <attribute name> <attribute value>"""
        self.assertEqual(expected_output, mock_stdout.getvalue().strip())
        self.assertFalse(HBNBCommand().onecmd("help update"))


class Test_console_prompting(unittest.TestCase):
    """Unittests for testing prompting of the HBNB command interpreter."""

    def test_prompt_string(self):
        """
        Test_console_prompting test prompt
        """
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        """
        Test_console_prompting test empty line with nothing
        """
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())

    @patch("sys.stdout", new_callable=StringIO)
    def test_empty_line(self, mock_stdout):
        """test propmtin with empty line"""
        HBNBCommand().onecmd("   ")
        self.assertEqual("", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_empty_line(self, mock_stdout):
        """test propmtin with empty line with multiple spaces"""
        HBNBCommand().onecmd("        ")
        self.assertEqual("", mock_stdout.getvalue())

    def test_available_classes(self):
        """
        Test_console_prompting test available classes is equal
        to fileUtil.my_classes
        """
        hb_instance = HBNBCommand()
        self.assertEqual(hb_instance._HBNBCommand__available_class,
                         FileUtil.my_Classes)


class Test_parseline(unittest.TestCase):
    """unit test for console line"""

    def setUp(self):
        """cmd test class setup"""
        self.hbnbCmd = HBNBCommand()

    def test_parseline_usage_detected(self):
        """
        Test_parseline test_parseline_usage_detected
        """
        line = "BaseModel.show(id)"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "show")
        self.assertEqual(arg, ["BaseModel", "id"])

    def test_parseline_usage_detected1(self):
        """
        Test_parseline test_parseline_usage_detected1
        """
        line = "BaseModel.show(id)"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "show")
        self.assertEqual(arg, ["BaseModel", "id"])

    def test_parseline_usage_not_detected1(self):
        """
        Test_parseline test_parseline_usage_not_detected1
        """
        line = "other_function(arg)"
        result = self.hbnbCmd.parseline(line)
        self.assertEqual(("other_function", "(arg)",
                          "other_function(arg)"), result)

    def test_parseline_usage_not_detected2(self):
        """
        Test_parseline test_parseline_usage_not_detected2
        """
        line = "BaseModel"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "BaseModel")
        self.assertEqual(arg, "")

    def test_parseline_usage_not_detected3(self):
        """
        Test_parseline test_parseline_usage_not_detected2
        """
        line = "BaseModel."
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertIsNone(cmd)
        self.assertEqual(arg, ["BaseModel"])

    def test_parseline_usage_not_detected4(self):
        """
        Test_parseline test_parseline_usage_not_detected2
        """
        line = "BaseModel."
        with self.assertRaises(TypeError) as ex:
            cmd, arg, _ = self.hbnbCmd.parseline(line, "cmd")
            self.assertEqual(
                "parseline() takes 2 positional \
arguments but 3 were given", ex.msg
            )

    def test_parseline_usage_not_detected5(self):
        """
        Test_parseline test_parseline_usage_not_detected2
        """
        line = "show.BaseModel(id)"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual("show", cmd)
        self.assertEqual(".BaseModel(id)", arg)


class Test_ParseLine_Detected_BaseModel(unittest.TestCase):
    """
    Test_ParseLine_Detected_BaseModel
    """

    def setUp(self):
        """cmd test class setup"""
        self.hbnbCmd = HBNBCommand()

    def test_parseline_usage_detected_BaseModel_super1(self):
        """
        Test_ParseLine_Detected_BaseModel
        test_parseline_usage_detected_BaseModel
        """
        line = "show BaseModel id"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "show")
        self.assertEqual(arg, "BaseModel id")

    def test_parseline_usage_detected_BaseModel_super2(self):
        """
        Test_ParseLine_Detected_BaseModel
        test_parseline_usage_detected_BaseModel
        """
        line = "show BaseModel id key value"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "show")
        self.assertEqual(arg, "BaseModel id key value")

    def test_parseline_usage_detected_BaseModel_super3(self):
        """
        Test_ParseLine_Detected_BaseModel
        test_parseline_usage_detected_BaseModel
        """
        line = "create BaseModel"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "create")
        self.assertEqual(arg, "BaseModel")

    def test_parseline_usage_detected_BaseModel_super4(self):
        """
        Test_ParseLine_Detected_BaseModel
        test_parseline_usage_detected_BaseModel
        """
        line = "all BaseModel"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "all")
        self.assertEqual(arg, "BaseModel")

    def test_parseline_usage_detected_BaseModel_super5(self):
        """
        Test_ParseLine_Detected_BaseModel
        test_parseline_usage_detected_BaseModel
        """
        line = "count BaseModel"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "count")
        self.assertEqual(arg, "BaseModel")

    def test_parseline_usage_detected_BaseModel_super6(self):
        """
        Test_ParseLine_Detected_BaseModel
        test_parseline_usage_detected_BaseModel
        """
        line = "destroy BaseModel id"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "destroy")
        self.assertEqual(arg, "BaseModel id")

    def test_parseline_usage_detected_BaseModel_super7(self):
        """
        Test_ParseLine_Detected_BaseModel
        test_parseline_usage_detected_BaseModel
        """
        line = "show BaseModel id"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "show")
        self.assertEqual(arg, "BaseModel id")

    def test_parseline_usage_detected_BaseModel_super8(self):
        """
        Test_ParseLine_Detected_BaseModel
        test_parseline_usage_detected_BaseModel
        """
        line = "update BaseModel id key value"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "update")
        self.assertEqual(arg, "BaseModel id key value")

    def test_parseline_usage_detected_BaseModel3(self):
        """
        Test_ParseLine_Detected_BaseModel
        test_parseline_usage_detected_BaseModel
        """
        line = "BaseModel.show(id, key, value)"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "show")
        self.assertEqual(arg, ["BaseModel", "id", 'key', 'value'])

    def test_parseline_usage_detected_BaseModel4(self):
        """
        Test_ParseLine_Detected_BaseModel
        test_parseline_usage_detected_BaseModel
        """
        line = "BaseModel.all(id)"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "all")
        self.assertEqual(arg, ["BaseModel", "id"])

    def test_parseline_usage_detected_BaseModel5(self):
        """
        Test_ParseLine_Detected_BaseModel
        test_parseline_usage_detected_BaseModel
        """
        line = "BaseModel.all()"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "all")
        self.assertEqual(arg, ["BaseModel"])

    def test_parseline_usage_detected_BaseModel6(self):
        """
        Test_ParseLine_Detected_BaseModel
        test_parseline_usage_detected_BaseModel
        """
        line = "BaseModel.count()"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "count")
        self.assertEqual(arg, ["BaseModel"])

    def test_parseline_usage_detected_BaseModel7(self):
        """
        Test_ParseLine_Detected_BaseModel
        test_parseline_usage_detected_BaseModel
        """
        line = "BaseModel.create()"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, None)
        self.assertEqual(arg, ["BaseModel"])

    def test_parseline_usage_detected_BaseModel8(self):
        """
        Test_ParseLine_Detected_BaseModel
        test_parseline_usage_detected_BaseModel
        """
        line = "BaseModel.present()"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "present")
        self.assertEqual(arg, ["BaseModel"])

    def test_parseline_usage_detected_BaseModel9(self):
        """
        Test_ParseLine_Detected_BaseModel
        test_parseline_usage_detected_BaseModel
        """
        line = "BaseModel.update()"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "update")
        self.assertEqual(arg, ["BaseModel"])

    def test_parseline_usage_detected_BaseModel10(self):
        """
        Test_ParseLine_Detected_BaseModel
        test_parseline_usage_detected_BaseModel
        """
        line = "BaseModel.update(id key value extra)"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "update")
        self.assertEqual(arg, ["BaseModel", 'id', 'key', 'value', 'extra'])


class Test_ParseLine_Detected_Amenity(unittest.TestCase):
    """
    Test_ParseLine_Detected_Amenity
    """

    def setUp(self):
        """cmd test class setup"""
        self.hbnbCmd = HBNBCommand()

    def test_parseline_usage_detected_Amenity_super1(self):
        """
        Test_ParseLine_Detected_Amenity
        test_parseline_usage_detected_Amenity
        """
        line = "show Amenity id"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "show")
        self.assertEqual(arg, "Amenity id")

    def test_parseline_usage_detected_Amenity_super2(self):
        """
        Test_ParseLine_Detected_Amenity
        test_parseline_usage_detected_Amenity
        """
        line = "show Amenity id key value"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "show")
        self.assertEqual(arg, "Amenity id key value")

    def test_parseline_usage_detected_Amenity_super3(self):
        """
        Test_ParseLine_Detected_Amenity
        test_parseline_usage_detected_Amenity
        """
        line = "create Amenity"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "create")
        self.assertEqual(arg, "Amenity")

    def test_parseline_usage_detected_Amenity_super4(self):
        """
        Test_ParseLine_Detected_Amenity
        test_parseline_usage_detected_Amenity
        """
        line = "all Amenity"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "all")
        self.assertEqual(arg, "Amenity")

    def test_parseline_usage_detected_Amenity_super5(self):
        """
        Test_ParseLine_Detected_Amenity
        test_parseline_usage_detected_Amenity
        """
        line = "count Amenity"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "count")
        self.assertEqual(arg, "Amenity")

    def test_parseline_usage_detected_Amenity_super6(self):
        """
        Test_ParseLine_Detected_Amenity
        test_parseline_usage_detected_Amenity
        """
        line = "destroy Amenity id"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "destroy")
        self.assertEqual(arg, "Amenity id")

    def test_parseline_usage_detected_Amenity_super7(self):
        """
        Test_ParseLine_Detected_Amenity
        test_parseline_usage_detected_Amenity
        """
        line = "show Amenity id"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "show")
        self.assertEqual(arg, "Amenity id")

    def test_parseline_usage_detected_Amenity_super8(self):
        """
        Test_ParseLine_Detected_Amenity
        test_parseline_usage_detected_Amenity
        """
        line = "update Amenity id key value"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "update")
        self.assertEqual(arg, "Amenity id key value")

    def test_parseline_usage_detected_Amenity3(self):
        """
        Test_ParseLine_Detected_Amenity
        test_parseline_usage_detected_Amenity
        """
        line = "Amenity.show(id, key, value)"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "show")
        self.assertEqual(arg, ["Amenity", "id", 'key', 'value'])

    def test_parseline_usage_detected_Amenity4(self):
        """
        Test_ParseLine_Detected_Amenity
        test_parseline_usage_detected_Amenity
        """
        line = "Amenity.all(id)"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "all")
        self.assertEqual(arg, ["Amenity", "id"])

    def test_parseline_usage_detected_Amenity5(self):
        """
        Test_ParseLine_Detected_Amenity
        test_parseline_usage_detected_Amenity
        """
        line = "Amenity.all()"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "all")
        self.assertEqual(arg, ["Amenity"])

    def test_parseline_usage_detected_Amenity6(self):
        """
        Test_ParseLine_Detected_Amenity
        test_parseline_usage_detected_Amenity
        """
        line = "Amenity.count()"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "count")
        self.assertEqual(arg, ["Amenity"])

    def test_parseline_usage_detected_Amenity7(self):
        """
        Test_ParseLine_Detected_Amenity
        test_parseline_usage_detected_Amenity
        """
        line = "Amenity.create()"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, None)
        self.assertEqual(arg, ["Amenity"])

    def test_parseline_usage_detected_Amenity8(self):
        """
        Test_ParseLine_Detected_Amenity
        test_parseline_usage_detected_Amenity
        """
        line = "Amenity.present()"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "present")
        self.assertEqual(arg, ["Amenity"])

    def test_parseline_usage_detected_Amenity9(self):
        """
        Test_ParseLine_Detected_Amenity
        test_parseline_usage_detected_Amenity
        """
        line = "Amenity.update()"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "update")
        self.assertEqual(arg, ["Amenity"])

    def test_parseline_usage_detected_Amenity10(self):
        """
        Test_ParseLine_Detected_Amenity
        test_parseline_usage_detected_Amenity
        """
        line = "Amenity.update(id key value extra)"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "update")
        self.assertEqual(arg, ["Amenity", 'id', 'key', 'value', 'extra'])


class Test_ParseLine_Detected_City(unittest.TestCase):
    """
    Test_ParseLine_Detected_City
    """

    def setUp(self):
        """cmd test class setup"""
        self.hbnbCmd = HBNBCommand()

    def test_parseline_usage_detected_City_super1(self):
        """
        Test_ParseLine_Detected_City
        test_parseline_usage_detected_City
        """
        line = "show City id"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "show")
        self.assertEqual(arg, "City id")

    def test_parseline_usage_detected_City_super2(self):
        """
        Test_ParseLine_Detected_City
        test_parseline_usage_detected_City
        """
        line = "show City id key value"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "show")
        self.assertEqual(arg, "City id key value")

    def test_parseline_usage_detected_City_super3(self):
        """
        Test_ParseLine_Detected_City
        test_parseline_usage_detected_City
        """
        line = "create City"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "create")
        self.assertEqual(arg, "City")

    def test_parseline_usage_detected_City_super4(self):
        """
        Test_ParseLine_Detected_City
        test_parseline_usage_detected_City
        """
        line = "all City"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "all")
        self.assertEqual(arg, "City")

    def test_parseline_usage_detected_City_super5(self):
        """
        Test_ParseLine_Detected_City
        test_parseline_usage_detected_City
        """
        line = "count City"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "count")
        self.assertEqual(arg, "City")

    def test_parseline_usage_detected_City_super6(self):
        """
        Test_ParseLine_Detected_City
        test_parseline_usage_detected_City
        """
        line = "destroy City id"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "destroy")
        self.assertEqual(arg, "City id")

    def test_parseline_usage_detected_City_super7(self):
        """
        Test_ParseLine_Detected_City
        test_parseline_usage_detected_City
        """
        line = "show City id"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "show")
        self.assertEqual(arg, "City id")

    def test_parseline_usage_detected_City_super8(self):
        """
        Test_ParseLine_Detected_City
        test_parseline_usage_detected_City
        """
        line = "update City id key value"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "update")
        self.assertEqual(arg, "City id key value")

    def test_parseline_usage_detected_City3(self):
        """
        Test_ParseLine_Detected_City
        test_parseline_usage_detected_City
        """
        line = "City.show(id, key, value)"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "show")
        self.assertEqual(arg, ["City", "id", 'key', 'value'])

    def test_parseline_usage_detected_City4(self):
        """
        Test_ParseLine_Detected_City
        test_parseline_usage_detected_City
        """
        line = "City.all(id)"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "all")
        self.assertEqual(arg, ["City", "id"])

    def test_parseline_usage_detected_City5(self):
        """
        Test_ParseLine_Detected_City
        test_parseline_usage_detected_City
        """
        line = "City.all()"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "all")
        self.assertEqual(arg, ["City"])

    def test_parseline_usage_detected_City6(self):
        """
        Test_ParseLine_Detected_City
        test_parseline_usage_detected_City
        """
        line = "City.count()"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "count")
        self.assertEqual(arg, ["City"])

    def test_parseline_usage_detected_City7(self):
        """
        Test_ParseLine_Detected_City
        test_parseline_usage_detected_City
        """
        line = "City.create()"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, None)
        self.assertEqual(arg, ["City"])

    def test_parseline_usage_detected_City8(self):
        """
        Test_ParseLine_Detected_City
        test_parseline_usage_detected_City
        """
        line = "City.present()"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "present")
        self.assertEqual(arg, ["City"])

    def test_parseline_usage_detected_City9(self):
        """
        Test_ParseLine_Detected_City
        test_parseline_usage_detected_City
        """
        line = "City.update()"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "update")
        self.assertEqual(arg, ["City"])

    def test_parseline_usage_detected_City10(self):
        """
        Test_ParseLine_Detected_City
        test_parseline_usage_detected_City
        """
        line = "City.update(id key value extra)"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "update")
        self.assertEqual(arg, ["City", 'id', 'key', 'value', 'extra'])


class Test_ParseLine_Detected_Place(unittest.TestCase):
    """
    Test_ParseLine_Detected_Place
    """

    def setUp(self):
        """cmd test class setup"""
        self.hbnbCmd = HBNBCommand()

    def test_parseline_usage_detected_Place_super1(self):
        """
        Test_ParseLine_Detected_Place
        test_parseline_usage_detected_Place
        """
        line = "show Place id"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "show")
        self.assertEqual(arg, "Place id")

    def test_parseline_usage_detected_Place_super2(self):
        """
        Test_ParseLine_Detected_Place
        test_parseline_usage_detected_Place
        """
        line = "show Place id key value"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "show")
        self.assertEqual(arg, "Place id key value")

    def test_parseline_usage_detected_Place_super3(self):
        """
        Test_ParseLine_Detected_Place
        test_parseline_usage_detected_Place
        """
        line = "create Place"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "create")
        self.assertEqual(arg, "Place")

    def test_parseline_usage_detected_Place_super4(self):
        """
        Test_ParseLine_Detected_Place
        test_parseline_usage_detected_Place
        """
        line = "all Place"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "all")
        self.assertEqual(arg, "Place")

    def test_parseline_usage_detected_Place_super5(self):
        """
        Test_ParseLine_Detected_Place
        test_parseline_usage_detected_Place
        """
        line = "count Place"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "count")
        self.assertEqual(arg, "Place")

    def test_parseline_usage_detected_Place_super6(self):
        """
        Test_ParseLine_Detected_Place
        test_parseline_usage_detected_Place
        """
        line = "destroy Place id"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "destroy")
        self.assertEqual(arg, "Place id")

    def test_parseline_usage_detected_Place_super7(self):
        """
        Test_ParseLine_Detected_Place
        test_parseline_usage_detected_Place
        """
        line = "show Place id"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "show")
        self.assertEqual(arg, "Place id")

    def test_parseline_usage_detected_Place_super8(self):
        """
        Test_ParseLine_Detected_Place
        test_parseline_usage_detected_Place
        """
        line = "update Place id key value"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "update")
        self.assertEqual(arg, "Place id key value")

    def test_parseline_usage_detected_Place3(self):
        """
        Test_ParseLine_Detected_Place
        test_parseline_usage_detected_Place
        """
        line = "Place.show(id, key, value)"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "show")
        self.assertEqual(arg, ["Place", "id", 'key', 'value'])

    def test_parseline_usage_detected_Place4(self):
        """
        Test_ParseLine_Detected_Place
        test_parseline_usage_detected_Place
        """
        line = "Place.all(id)"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "all")
        self.assertEqual(arg, ["Place", "id"])

    def test_parseline_usage_detected_Place5(self):
        """
        Test_ParseLine_Detected_Place
        test_parseline_usage_detected_Place
        """
        line = "Place.all()"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "all")
        self.assertEqual(arg, ["Place"])

    def test_parseline_usage_detected_Place6(self):
        """
        Test_ParseLine_Detected_Place
        test_parseline_usage_detected_Place
        """
        line = "Place.count()"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "count")
        self.assertEqual(arg, ["Place"])

    def test_parseline_usage_detected_Place7(self):
        """
        Test_ParseLine_Detected_Place
        test_parseline_usage_detected_Place
        """
        line = "Place.create()"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, None)
        self.assertEqual(arg, ["Place"])

    def test_parseline_usage_detected_Place8(self):
        """
        Test_ParseLine_Detected_Place
        test_parseline_usage_detected_Place
        """
        line = "Place.present()"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "present")
        self.assertEqual(arg, ["Place"])

    def test_parseline_usage_detected_Place9(self):
        """
        Test_ParseLine_Detected_Place
        test_parseline_usage_detected_Place
        """
        line = "Place.update()"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "update")
        self.assertEqual(arg, ["Place"])

    def test_parseline_usage_detected_Place10(self):
        """
        Test_ParseLine_Detected_Place
        test_parseline_usage_detected_Place
        """
        line = "Place.update(id key value extra)"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "update")
        self.assertEqual(arg, ["Place", 'id', 'key', 'value', 'extra'])


class Test_ParseLine_Detected_Review(unittest.TestCase):
    """
    Test_ParseLine_Detected_Review
    """

    def setUp(self):
        """cmd test class setup"""
        self.hbnbCmd = HBNBCommand()

    def test_parseline_usage_detected_Review_super1(self):
        """
        Test_ParseLine_Detected_Review
        test_parseline_usage_detected_Review
        """
        line = "show Review id"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "show")
        self.assertEqual(arg, "Review id")

    def test_parseline_usage_detected_Review_super2(self):
        """
        Test_ParseLine_Detected_Review
        test_parseline_usage_detected_Review
        """
        line = "show Review id key value"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "show")
        self.assertEqual(arg, "Review id key value")

    def test_parseline_usage_detected_Review_super3(self):
        """
        Test_ParseLine_Detected_Review
        test_parseline_usage_detected_Review
        """
        line = "create Review"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "create")
        self.assertEqual(arg, "Review")

    def test_parseline_usage_detected_Review_super4(self):
        """
        Test_ParseLine_Detected_Review
        test_parseline_usage_detected_Review
        """
        line = "all Review"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "all")
        self.assertEqual(arg, "Review")

    def test_parseline_usage_detected_Review_super5(self):
        """
        Test_ParseLine_Detected_Review
        test_parseline_usage_detected_Review
        """
        line = "count Review"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "count")
        self.assertEqual(arg, "Review")

    def test_parseline_usage_detected_Review_super6(self):
        """
        Test_ParseLine_Detected_Review
        test_parseline_usage_detected_Review
        """
        line = "destroy Review id"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "destroy")
        self.assertEqual(arg, "Review id")

    def test_parseline_usage_detected_Review_super7(self):
        """
        Test_ParseLine_Detected_Review
        test_parseline_usage_detected_Review
        """
        line = "show Review id"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "show")
        self.assertEqual(arg, "Review id")

    def test_parseline_usage_detected_Review_super8(self):
        """
        Test_ParseLine_Detected_Review
        test_parseline_usage_detected_Review
        """
        line = "update Review id key value"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "update")
        self.assertEqual(arg, "Review id key value")

    def test_parseline_usage_detected_Review3(self):
        """
        Test_ParseLine_Detected_Review
        test_parseline_usage_detected_Review
        """
        line = "Review.show(id, key, value)"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "show")
        self.assertEqual(arg, ["Review", "id", 'key', 'value'])

    def test_parseline_usage_detected_Review4(self):
        """
        Test_ParseLine_Detected_Review
        test_parseline_usage_detected_Review
        """
        line = "Review.all(id)"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "all")
        self.assertEqual(arg, ["Review", "id"])

    def test_parseline_usage_detected_Review5(self):
        """
        Test_ParseLine_Detected_Review
        test_parseline_usage_detected_Review
        """
        line = "Review.all()"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "all")
        self.assertEqual(arg, ["Review"])

    def test_parseline_usage_detected_Review6(self):
        """
        Test_ParseLine_Detected_Review
        test_parseline_usage_detected_Review
        """
        line = "Review.count()"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "count")
        self.assertEqual(arg, ["Review"])

    def test_parseline_usage_detected_Review7(self):
        """
        Test_ParseLine_Detected_Review
        test_parseline_usage_detected_Review
        """
        line = "Review.create()"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, None)
        self.assertEqual(arg, ["Review"])

    def test_parseline_usage_detected_Review8(self):
        """
        Test_ParseLine_Detected_Review
        test_parseline_usage_detected_Review
        """
        line = "Review.present()"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "present")
        self.assertEqual(arg, ["Review"])

    def test_parseline_usage_detected_Review9(self):
        """
        Test_ParseLine_Detected_Review
        test_parseline_usage_detected_Review
        """
        line = "Review.update()"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "update")
        self.assertEqual(arg, ["Review"])

    def test_parseline_usage_detected_Review10(self):
        """
        Test_ParseLine_Detected_Review
        test_parseline_usage_detected_Review
        """
        line = "Review.update(id key value extra)"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "update")
        self.assertEqual(arg, ["Review", 'id', 'key', 'value', 'extra'])


class Test_ParseLine_Detected_State(unittest.TestCase):
    """
    Test_ParseLine_Detected_State
    """

    def setUp(self):
        """cmd test class setup"""
        self.hbnbCmd = HBNBCommand()

    def test_parseline_usage_detected_State_super1(self):
        """
        Test_ParseLine_Detected_State
        test_parseline_usage_detected_State
        """
        line = "show State id"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "show")
        self.assertEqual(arg, "State id")

    def test_parseline_usage_detected_State_super2(self):
        """
        Test_ParseLine_Detected_State
        test_parseline_usage_detected_State
        """
        line = "show State id key value"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "show")
        self.assertEqual(arg, "State id key value")

    def test_parseline_usage_detected_State_super3(self):
        """
        Test_ParseLine_Detected_State
        test_parseline_usage_detected_State
        """
        line = "create State"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "create")
        self.assertEqual(arg, "State")

    def test_parseline_usage_detected_State_super4(self):
        """
        Test_ParseLine_Detected_State
        test_parseline_usage_detected_State
        """
        line = "all State"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "all")
        self.assertEqual(arg, "State")

    def test_parseline_usage_detected_State_super5(self):
        """
        Test_ParseLine_Detected_State
        test_parseline_usage_detected_State
        """
        line = "count State"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "count")
        self.assertEqual(arg, "State")

    def test_parseline_usage_detected_State_super6(self):
        """
        Test_ParseLine_Detected_State
        test_parseline_usage_detected_State
        """
        line = "destroy State id"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "destroy")
        self.assertEqual(arg, "State id")

    def test_parseline_usage_detected_State_super7(self):
        """
        Test_ParseLine_Detected_State
        test_parseline_usage_detected_State
        """
        line = "show State id"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "show")
        self.assertEqual(arg, "State id")

    def test_parseline_usage_detected_State_super8(self):
        """
        Test_ParseLine_Detected_State
        test_parseline_usage_detected_State
        """
        line = "update State id key value"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "update")
        self.assertEqual(arg, "State id key value")

    def test_parseline_usage_detected_State3(self):
        """
        Test_ParseLine_Detected_State
        test_parseline_usage_detected_State
        """
        line = "State.show(id, key, value)"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "show")
        self.assertEqual(arg, ["State", "id", 'key', 'value'])

    def test_parseline_usage_detected_State4(self):
        """
        Test_ParseLine_Detected_State
        test_parseline_usage_detected_State
        """
        line = "State.all(id)"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "all")
        self.assertEqual(arg, ["State", "id"])

    def test_parseline_usage_detected_State5(self):
        """
        Test_ParseLine_Detected_State
        test_parseline_usage_detected_State
        """
        line = "State.all()"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "all")
        self.assertEqual(arg, ["State"])

    def test_parseline_usage_detected_State6(self):
        """
        Test_ParseLine_Detected_State
        test_parseline_usage_detected_State
        """
        line = "State.count()"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "count")
        self.assertEqual(arg, ["State"])

    def test_parseline_usage_detected_State7(self):
        """
        Test_ParseLine_Detected_State
        test_parseline_usage_detected_State
        """
        line = "State.create()"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, None)
        self.assertEqual(arg, ["State"])

    def test_parseline_usage_detected_State8(self):
        """
        Test_ParseLine_Detected_State
        test_parseline_usage_detected_State
        """
        line = "State.present()"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "present")
        self.assertEqual(arg, ["State"])

    def test_parseline_usage_detected_State9(self):
        """
        Test_ParseLine_Detected_State
        test_parseline_usage_detected_State
        """
        line = "State.update()"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "update")
        self.assertEqual(arg, ["State"])

    def test_parseline_usage_detected_State10(self):
        """
        Test_ParseLine_Detected_State
        test_parseline_usage_detected_State
        """
        line = "State.update(id key value extra)"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "update")
        self.assertEqual(arg, ["State", 'id', 'key', 'value', 'extra'])


class Test_ParseLine_Detected_User(unittest.TestCase):
    """
    Test_ParseLine_Detected_User
    """

    def setUp(self):
        """cmd test class setup"""
        self.hbnbCmd = HBNBCommand()

    def test_parseline_usage_detected_User_super1(self):
        """
        Test_ParseLine_Detected_User
        test_parseline_usage_detected_User
        """
        line = "show User id"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "show")
        self.assertEqual(arg, "User id")

    def test_parseline_usage_detected_User_super2(self):
        """
        Test_ParseLine_Detected_User
        test_parseline_usage_detected_User
        """
        line = "show User id key value"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "show")
        self.assertEqual(arg, "User id key value")

    def test_parseline_usage_detected_User_super3(self):
        """
        Test_ParseLine_Detected_User
        test_parseline_usage_detected_User
        """
        line = "create User"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "create")
        self.assertEqual(arg, "User")

    def test_parseline_usage_detected_User_super4(self):
        """
        Test_ParseLine_Detected_User
        test_parseline_usage_detected_User
        """
        line = "all User"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "all")
        self.assertEqual(arg, "User")

    def test_parseline_usage_detected_User_super5(self):
        """
        Test_ParseLine_Detected_User
        test_parseline_usage_detected_User
        """
        line = "count User"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "count")
        self.assertEqual(arg, "User")

    def test_parseline_usage_detected_User_super6(self):
        """
        Test_ParseLine_Detected_User
        test_parseline_usage_detected_User
        """
        line = "destroy User id"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "destroy")
        self.assertEqual(arg, "User id")

    def test_parseline_usage_detected_User_super7(self):
        """
        Test_ParseLine_Detected_User
        test_parseline_usage_detected_User
        """
        line = "show User id"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "show")
        self.assertEqual(arg, "User id")

    def test_parseline_usage_detected_User_super8(self):
        """
        Test_ParseLine_Detected_User
        test_parseline_usage_detected_User
        """
        line = "update User id key value"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "update")
        self.assertEqual(arg, "User id key value")

    def test_parseline_usage_detected_User3(self):
        """
        Test_ParseLine_Detected_User
        test_parseline_usage_detected_User
        """
        line = "User.show(id, key, value)"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "show")
        self.assertEqual(arg, ["User", "id", 'key', 'value'])

    def test_parseline_usage_detected_User4(self):
        """
        Test_ParseLine_Detected_User
        test_parseline_usage_detected_User
        """
        line = "User.all(id)"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "all")
        self.assertEqual(arg, ["User", "id"])

    def test_parseline_usage_detected_User5(self):
        """
        Test_ParseLine_Detected_User
        test_parseline_usage_detected_User
        """
        line = "User.all()"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "all")
        self.assertEqual(arg, ["User"])

    def test_parseline_usage_detected_User6(self):
        """
        Test_ParseLine_Detected_User
        test_parseline_usage_detected_User
        """
        line = "User.count()"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "count")
        self.assertEqual(arg, ["User"])

    def test_parseline_usage_detected_User7(self):
        """
        Test_ParseLine_Detected_User
        test_parseline_usage_detected_User
        """
        line = "User.create()"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, None)
        self.assertEqual(arg, ["User"])

    def test_parseline_usage_detected_User8(self):
        """
        Test_ParseLine_Detected_User
        test_parseline_usage_detected_User
        """
        line = "User.present()"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "present")
        self.assertEqual(arg, ["User"])

    def test_parseline_usage_detected_User9(self):
        """
        Test_ParseLine_Detected_User
        test_parseline_usage_detected_User
        """
        line = "User.update()"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "update")
        self.assertEqual(arg, ["User"])

    def test_parseline_usage_detected_User10(self):
        """
        Test_ParseLine_Detected_User
        test_parseline_usage_detected_User
        """
        line = "User.update(id key value extra)"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "update")
        self.assertEqual(arg, ["User", 'id', 'key', 'value', 'extra'])


class Test_ParseLine_not_Detected(unittest.TestCase):
    """
    Test_ParseLine_not_Detected
    """

    def setUp(self):
        """cmd test class setup"""
        self.hbnbCmd = HBNBCommand()

    def test_parseline_usage_not_detected1(self):
        """
        Test_ParseLine_not_Detected
        test_parseline_usage_not_detected1
        """
        line = "show.User(id)"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "show")
        self.assertEqual(arg, ".User(id)")

    def test_parseline_usage_not_detected2(self):
        """
        Test_ParseLine_not_Detected
        test_parseline_usage_not_detected2
        """
        line = "show.User(id)"
        cmd, arg, _ = self.hbnbCmd.parseline(line)
        self.assertEqual(cmd, "show")
        self.assertEqual(arg, ".User(id)")


class Test_extract_function_info(unittest.TestCase):
    """Test_extract_function_info"""

    def test_extract_function_info_detected(self):
        """
        test_extract_function_info
        gets called when line contains a Class.command(args)
        """
        cmd, args = extract_function_info("User.all()")
        self.assertEqual("all", cmd)
        self.assertEqual(["User"], args)

    def test_extract_function_info_no_paranthesis(self):
        """
        test_extract_function_info
        gets called when line contains a Class.command(args)
        """
        cmd, args = extract_function_info("User.all")
        self.assertEqual(None, cmd)
        self.assertEqual(["User"], args)

    def test_extract_function_info_create(self):
        """
        test_extract_function_info
        gets called when line contains a Class.command(args)
        """
        cmd, args = extract_function_info("User.create()")
        self.assertEqual(None, cmd)
        self.assertEqual(["User"], args)

    def test_extract_function_info_update(self):
        """
        test_extract_function_info
        gets called when line contains a Class.command(args)
        """
        cmd, args = extract_function_info("User.update()")
        self.assertEqual("update", cmd)
        self.assertEqual(["User"], args)

    def test_extract_function_info_update_with_id(self):
        """
        test_extract_function_info
        gets called when line contains a Class.command(args)
        """
        cmd, args = extract_function_info("User.update(id)")
        self.assertEqual("update", cmd)
        self.assertEqual(['User', 'id'], args)

    def test_extract_function_info_update_with_multiple_args(self):
        """
        test_extract_function_info
        gets called when line contains a Class.command(args)
        """
        cmd, args = extract_function_info("User.update(id, key, val)")
        self.assertEqual("update", cmd)
        self.assertEqual(['User', 'id', 'key', 'val'], args)

    def test_extract_function_info_update_with_dict(self):
        """
        test_extract_function_info
        gets called when line contains a Class.command(args)
        """
        line = "User.update('id', {'id': '5645', 'name': 'khames', 'age': 89})"
        cmd, args = extract_function_info(line)
        self.assertEqual("patch_all", cmd)
        expected = ['User', 'id', '{id:',
                    '5645', 'name:', 'khames', 'age:', '89}']
        self.assertEqual(expected, args)


class Test_Console_exit(unittest.TestCase):
    """
    Test_Console_exit
    Unittests for testing exiting from the HBNB command interpreter.
    """

    def test_quit_exits(self):
        """
        Test if Quit Exit
        """
        self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF_exits(self):
        """
        Test IF EOF exits
        """
        self.assertTrue(HBNBCommand().onecmd("EOF"))


class Test_list_string_to_dict(unittest.TestCase):
    """Test_list_string_to_dict"""

    def test_list_string_to_dict_not_list_none(self):
        """
        test_list_string_to_dict_not_list
        """
        dct = list_string_to_dict(None)
        self.assertIsNone(dct)

    def test_list_string_to_dict_not_list_dict(self):
        """
        test_list_string_to_dict_not_list
        """
        dct = list_string_to_dict({'id': 15})
        self.assertIsNone(dct)

    def test_list_string_to_dict_not_list_set(self):
        """
        test_list_string_to_dict_not_list
        """
        dct = list_string_to_dict({'id', 15})
        self.assertIsNone(dct)

    def test_list_string_to_dict_not_list_int(self):
        """
        test_list_string_to_dict_not_list
        """
        dct = list_string_to_dict(15)
        self.assertIsNone(dct)

    def test_list_string_to_dict_not_list_float(self):
        """
        test_list_string_to_dict_not_list
        """
        dct = list_string_to_dict(150.5)
        self.assertIsNone(dct)

    def test_list_string_to_dict_not_list_str(self):
        """
        test_list_string_to_dict_not_list
        """
        dct = list_string_to_dict('name')
        self.assertIsNone(dct)

    def test_list_string_to_dict_not_list_bool(self):
        """
        test_list_string_to_dict_not_list
        """
        dct = list_string_to_dict(True)
        self.assertIsNone(dct)

    @patch("sys.stdout", new_callable=StringIO)
    def test_list_string_to_dict_list(self, mock_stdout):
        """
        test_list_string_to_dict_list
        """
        dct = list_string_to_dict(['id'])
        self.assertIsNone(dct)
        self.assertEqual("** value missing **", mock_stdout.getvalue().strip())

    @patch("sys.stdout", new_callable=StringIO)
    def test_list_string_to_dict_list(self, mock_stdout):
        """
        test_list_string_to_dict_list
        """
        dct = list_string_to_dict([])
        self.assertIsNone(dct)
        self.assertEqual("** attribute name missing **",
                         mock_stdout.getvalue().strip())

    @patch("sys.stdout", new_callable=StringIO)
    def test_list_string_to_dict_list_val_miss(self, mock_stdout):
        """
        test_list_string_to_dict_list
        """
        dct = list_string_to_dict(['id'])
        self.assertIsNone(dct)
        self.assertEqual("** value missing **", mock_stdout.getvalue().strip())

    @patch("sys.stdout", new_callable=StringIO)
    def test_list_string_to_dict_list_val_miss1(self, mock_stdout):
        """
        test_list_string_to_dict_list
        """
        dct = list_string_to_dict(['{id:'])
        self.assertIsNone(dct)
        self.assertEqual("** value missing **", mock_stdout.getvalue().strip())

    @patch("sys.stdout", new_callable=StringIO)
    def test_list_string_to_dict_list_val_miss2(self, mock_stdout):
        """
        test_list_string_to_dict_list
        """
        dct = list_string_to_dict(['{id:', '89', 'name:'])
        self.assertIsNone(dct)
        self.assertEqual("** value missing **", mock_stdout.getvalue().strip())

    @patch("sys.stdout", new_callable=StringIO)
    def test_list_string_to_dict_list_val_miss3(self, mock_stdout):
        """
        test_list_string_to_dict_list
        """
        dct = list_string_to_dict(['{id:', '89', 'name:', 'khames', 'age'])
        self.assertIsNone(dct)
        self.assertEqual("** value missing **", mock_stdout.getvalue().strip())

    @patch("sys.stdout", new_callable=StringIO)
    def test_list_string_to_dict_list_val_missing_key(self, mock_stdout):
        """
        test_list_string_to_dict_list
        """
        dct = list_string_to_dict(['{id:', '89',
                                   'name:', 'khames',
                                   'age:', '89', 'key'])
        self.assertIsNone(dct)
        self.assertEqual("** value missing **", mock_stdout.getvalue().strip())

    @patch("sys.stdout", new_callable=StringIO)
    def test_list_string_to_dict_list_val_miss3(self, mock_stdout):
        """
        test_list_string_to_dict_list
        """
        dct = list_string_to_dict(['{}'])
        self.assertIsNone(dct)
        self.assertEqual("** attribute name missing **",
                         mock_stdout.getvalue().strip())

    def test_list_string_to_dict_list_valid_list(self):
        """
        test_list_string_to_dict_list_valid_list
        """
        dct = list_string_to_dict(["{first_name:", "John", "age:", "89}"])
        self.assertIsNotNone(dct)
        self.assertEqual({"first_name": "John", "age": 89}, dct)


class Test_split_args(unittest.TestCase):
    """
    class to test split args function
    """

    def test_split_args(self):
        """
        test split_args functionality
        """
        line = 'update user'
        actual_val = split_args(line)
        expected_val = ['update', 'user']
        self.assertEqual(expected_val, actual_val)

    def test_split_args1(self):
        """
        test split_args functionality
        """
        line = 'update user "id", "key" "val"'
        actual_val = split_args(line)
        expected_val = ['update', 'user', 'id', 'key', 'val']
        self.assertEqual(expected_val, actual_val)


class Test_patch_all(unittest.TestCase):
    """
    unit test cases for do_patch_all method
    """

    @classmethod
    def setUpClass(cls):
        """
        setup class
        """
        try:
            os.rename("saved_object.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}
        cls.hnbnCmd = HBNBCommand()
        cls.user = User()
        cls.ids = cls.user.id
        cls.created = cls.user.created_at
        cls.updated = cls.user.updated_at

        cls.user.save()

    @classmethod
    def tearDown(cls):
        """
        tear down class
        """
        try:
            os.remove("saved_object.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "saved_object.json")
        except IOError:
            pass

    @patch("sys.stdout", new_callable=StringIO)
    def test__patch_all(self, mock_stdout):
        """
        test_patch_all
        """
        ids = self.ids
        dct = {
            'first_name': 'mohamed',
            'last_name': 'ahmed',
            'age': 31
        }
        line = f"User.update({ids}, {dct})"
        self.hnbnCmd.onecmd(line)

        self.hnbnCmd.onecmd(f'User.show({ids})')
        data_string = mock_stdout.getvalue()

        # Regular expressions to extract values
        id_match = re.search(r"'id': '(.+?)'", data_string)
        first_name_match = re.search(r"'first_name': '(.+?)'", data_string)
        last_name_match = re.search(r"'last_name': '(.+?)'", data_string)
        age_match = re.search(r"'age': (\d+)", data_string)

        # Extracted values
        id_value = id_match.group(1)
        first_name_value = first_name_match.group(1)
        last_name_value = last_name_match.group(1)
        age_value = int(age_match.group(1))
        self.assertEqual(ids, id_value)
        self.assertEqual("mohamed", first_name_value)
        self.assertEqual("ahmed", last_name_value)
        self.assertEqual(31, age_value)


class Test_Create(unittest.TestCase):
    """
    Unittests for testing create fun
    """

    def setUp(self):
        """
        Call Before Every Test
        """
        try:
            os.rename(FileUtil.saved_file, "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

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

    def test_create_missing_class(self):
        """
        Test With no class name
        """
        mss = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(mss, f.getvalue().strip())

    def test_create_invalid_class(self):
        """
        Test With not exits class
        """
        mss = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Mymodel"))
            self.assertEqual(mss, f.getvalue().strip())

    def test_create_invalid_Method(self):
        """Test invalid Method dot"""
        mss = "*** Unknown syntax: MyModel.create()"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("MyModel.create()"))
            self.assertEqual(mss, f.getvalue().strip())
        mss = "*** Unknown syntax: User.create()"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("User.create()"))
            self.assertEqual(mss, f.getvalue().strip())

    def test_create_objects(self):
        """Test create"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertLess(0, len(f.getvalue().strip()))
            self.assertEqual(str, type(f.getvalue()))
            key = "BaseModel.{}".format(f.getvalue().strip())
            self.assertIn(key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertLess(0, len(f.getvalue().strip()))
            self.assertEqual(str, type(f.getvalue()))
            key = "User.{}".format(f.getvalue().strip())
            self.assertIn(key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertLess(0, len(f.getvalue().strip()))
            self.assertEqual(str, type(f.getvalue()))
            key = "State.{}".format(f.getvalue().strip())
            self.assertIn(key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertLess(0, len(f.getvalue().strip()))
            self.assertEqual(str, type(f.getvalue()))
            key = "City.{}".format(f.getvalue().strip())
            self.assertIn(key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertLess(0, len(f.getvalue().strip()))
            self.assertEqual(str, type(f.getvalue()))
            key = "Amenity.{}".format(f.getvalue().strip())
            self.assertIn(key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertLess(0, len(f.getvalue().strip()))
            self.assertEqual(str, type(f.getvalue()))
            key = "Place.{}".format(f.getvalue().strip())
            self.assertIn(key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertLess(0, len(f.getvalue().strip()))
            self.assertEqual(str, type(f.getvalue()))
            key = "Review.{}".format(f.getvalue().strip())
            self.assertIn(key, storage.all().keys())


class Test_Show(unittest.TestCase):
    """Unittest for show fun"""

    def setUp(self):
        """
        Call Before Every Test
        """
        try:
            os.rename(FileUtil.saved_file, "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

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

    def test_show_missing_class(self):
        """
        Test With no class name
        """
        mss = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(mss, f.getvalue().strip())
        mss = "*** Unknown syntax: .show()"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(".show()"))
            self.assertEqual(mss, f.getvalue().strip())

    def test_show_invalid_class(self):
        """
        Test With not exits class
        """
        mss = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show MyModel"))
            self.assertEqual(mss, f.getvalue().strip())
        mss = "*** Unknown syntax: MyModel.show()"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("MyModel.show()"))
            self.assertEqual(mss, f.getvalue().strip())

    def test_show_missing_id(self):
        """Test id missing"""
        mss = "** instance id missing **"

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel"))
            self.assertEqual(mss, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show User"))
            self.assertEqual(mss, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show State"))
            self.assertEqual(mss, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show City"))
            self.assertEqual(mss, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Amenity"))
            self.assertEqual(mss, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Place"))
            self.assertEqual(mss, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Review"))
            self.assertEqual(mss, f.getvalue().strip())

    def test_show_missing_id_dot_Method(self):
        """test id missing dot method"""
        mss = "** instance id missing **"

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.show()"))
            self.assertEqual(mss, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("User.show()"))
            self.assertEqual(mss, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("State.show()"))
            self.assertEqual(mss, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("City.show()"))
            self.assertEqual(mss, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Amenity.show()"))
            self.assertEqual(mss, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Place.show()"))
            self.assertEqual(mss, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Review.show()"))
            self.assertEqual(mss, f.getvalue().strip())

    def test_show_no_instance_found(self):
        """Test with no istance"""
        mss = "** no instance found **"

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel 1"))
            self.assertEqual(mss, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show User 2"))
            self.assertEqual(mss, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show State 3"))
            self.assertEqual(mss, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show City 4"))
            self.assertEqual(mss, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Amenity 5"))
            self.assertEqual(mss, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Place 6"))
            self.assertEqual(mss, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Review 7"))
            self.assertEqual(mss, f.getvalue().strip())

    def test_show_no_instance_found_dot_Method(self):
        """Test no instance dot method"""
        mss = "** no instance found **"

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.show(1)"))
            self.assertEqual(mss, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("User.show(2)"))
            self.assertEqual(mss, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("State.show(3)"))
            self.assertEqual(mss, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("City.show(4)"))
            self.assertEqual(mss, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Amenity.show(5)"))
            self.assertEqual(mss, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Place.show(6)"))
            self.assertEqual(mss, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Review.show(7)"))
            self.assertEqual(mss, f.getvalue().strip())

    def test_show_objects(self):
        """test with classic method"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["BaseModel.{}".format(obj_id)]
            command = "show BaseModel {}".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["User.{}".format(obj_id)]
            command = "show User {}".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["State.{}".format(obj_id)]
            command = "show State {}".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["Place.{}".format(obj_id)]
            command = "show Place {}".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["City.{}".format(obj_id)]
            command = "show City {}".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["Amenity.{}".format(obj_id)]
            command = "show Amenity {}".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["Review.{}".format(obj_id)]
            command = "show Review {}".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), f.getvalue().strip())

    def test_show_objects_dot_method(self):
        """Test with dot method"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["BaseModel.{}".format(obj_id)]
            command = "BaseModel.show({})".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["User.{}".format(obj_id)]
            command = "User.show({})".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["State.{}".format(obj_id)]
            command = "State.show({})".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["Place.{}".format(obj_id)]
            command = "Place.show({})".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["City.{}".format(obj_id)]
            command = "City.show({})".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["Amenity.{}".format(obj_id)]
            command = "Amenity.show({})".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["Review.{}".format(obj_id)]
            command = "Review.show({})".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), f.getvalue().strip())


class Test_destroy(unittest.TestCase):
    """Unittest for destroy fun"""

    def setUp(self):
        """
        Call Before Every Test
        """
        try:
            os.rename(FileUtil.saved_file, "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

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

    def test_destroy_missing_class(self):
        """
        Test With no class name
        """
        correct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(correct, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(".destroy()"))
            self.assertEqual(correct, f.getvalue().strip())

    def test_destroy_invalid_class(self):
        """
        Test With not exits class
        """
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy MyModel"))
            self.assertEqual(correct, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("MyModel.destroy()"))
            self.assertEqual(correct, f.getvalue().strip())

    def test_destroy_id_missing(self):
        """Test id missing"""
        correct = "** instance id missing **"

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel"))
            self.assertEqual(correct, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy User"))
            self.assertEqual(correct, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy State"))
            self.assertEqual(correct, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy City"))
            self.assertEqual(correct, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy Amenity"))
            self.assertEqual(correct, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy Place"))
            self.assertEqual(correct, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy Review"))
            self.assertEqual(correct, f.getvalue().strip())

    def test_destroy_id_missing_dot_Method(self):
        """test id missing dot method"""
        correct = "** instance id missing **"

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.destroy()"))
            self.assertEqual(correct, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("User.destroy()"))
            self.assertEqual(correct, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("State.destroy()"))
            self.assertEqual(correct, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("City.destroy()"))
            self.assertEqual(correct, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Amenity.destroy()"))
            self.assertEqual(correct, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Place.destroy()"))
            self.assertEqual(correct, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Review.destroy()"))
            self.assertEqual(correct, f.getvalue().strip())

    def test_destroy_invalid_id_dot_Method(self):
        """test id missing dot method"""
        correct = "** no instance found **"

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel 1"))
            self.assertEqual(correct, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy User 1"))
            self.assertEqual(correct, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy State 1"))
            self.assertEqual(correct, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy City 1"))
            self.assertEqual(correct, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy Amenity 1"))
            self.assertEqual(correct, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy Place 1"))
            self.assertEqual(correct, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy Review 1"))
            self.assertEqual(correct, f.getvalue().strip())

    def test_destroy_invalid_id_dot_Method(self):
        """Test no instance dot method"""
        correct = "** no instance found **"

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.destroy(1)"))
            self.assertEqual(correct, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("User.destroy(1)"))
            self.assertEqual(correct, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("State.destroy(1)"))
            self.assertEqual(correct, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("City.destroy(1)"))
            self.assertEqual(correct, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Amenity.destroy(1)"))
            self.assertEqual(correct, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Place.destroy(1)"))
            self.assertEqual(correct, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Review.destroy(1)"))
            self.assertEqual(correct, f.getvalue().strip())

    def test_destroy_objects_space_notation(self):
        """test with classic method"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            testID = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["BaseModel.{}".format(testID)]
            command = "destroy BaseModel {}".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            testID = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["User.{}".format(testID)]
            command = "show User {}".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            testID = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["State.{}".format(testID)]
            command = "show State {}".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            testID = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["Place.{}".format(testID)]
            command = "show Place {}".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            testID = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["City.{}".format(testID)]
            command = "show City {}".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            testID = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["Amenity.{}".format(testID)]
            command = "show Amenity {}".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            testID = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["Review.{}".format(testID)]
            command = "show Review {}".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())

    def test_destroy_objects_dot_notation(self):
        """Test with dot method"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            testID = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["BaseModel.{}".format(testID)]
            command = "BaseModel.destroy({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            testID = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["User.{}".format(testID)]
            command = "User.destroy({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            testID = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["State.{}".format(testID)]
            command = "State.destroy({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            testID = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["Place.{}".format(testID)]
            command = "Place.destroy({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            testID = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["City.{}".format(testID)]
            command = "City.destroy({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            testID = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["Amenity.{}".format(testID)]
            command = "Amenity.destroy({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            testID = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["Review.{}".format(testID)]
            command = "Review.destory({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())


if __name__ == "__main__":
    unittest.main()

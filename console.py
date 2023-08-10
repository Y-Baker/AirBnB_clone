#!/usr/bin/python3

"""contains the entry point of the command interpreter"""

import cmd
from shlex import split
from models import storage
from models.engine.available_class import FileUtil
import re


class HBNBCommand(cmd.Cmd):
    """The Command Interpreter for AirBnB Project"""

    prompt = '(hbnb)' + ' '
    __available_class = FileUtil.my_Classes

    def emptyline(self):
        """Do Nothing for empty string
        why: because super(cmd) excute the last command for empty line"""
        pass

    def parseline(self, line):
        """
        Called Before Every line execute
        Used to Check For Usage: <Class_Name>.<Command_Interpreter>(<args>)
        """
        available_cls = [f"{_}." for _ in self.__class__.__available_class]
        for cls in available_cls:
            if cls in line:
                cmd, arg = extract_function_info(line)
                return cmd, arg, line
        return super().parseline(line)

    def do_create(self, line):
        """
        Create New instance
        Usage: create BaseModel
        """
        args = split_args(line)
        if args and len(args) > 0:
            if args[0] in HBNBCommand.__available_class:
                created_obj = HBNBCommand.__available_class[args[0]]()
                created_obj.save()
                print(created_obj.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """
        Print str-representation of an instance based on class name, id
        Usage: show BaseModel <id>
        """
        available_instance = storage.all()

        args = split_args(line)
        if not args or len(args) < 1:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__available_class:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in available_instance:
            print("** no instance found **")
        else:
            obj = available_instance[f"{args[0]}.{args[1]}"]
            print(obj)

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        Usage: destroy BaseModel <id>
        """
        available_instance = storage.all()

        args = split_args(line)
        if not args or len(args) < 1:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__available_class:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in available_instance:
            print("** no instance found **")
        else:
            del available_instance[f"{args[0]}.{args[1]}"]
            storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on a class name
        Usage: all BaseModel or all
        """
        available_instance = storage.all()

        args = split_args(line)
        if len(args) == 0:
            list_obj = [str(obj) for obj in available_instance.values()]
            print(list_obj)
        elif len(args) > 0:
            if args[0] in HBNBCommand.__available_class:
                list_obj = []
                for key, value in available_instance.items():
                    if key.split('.')[0] == args[0]:
                        list_obj.append(str(value))
                print(list_obj)
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        available_instance = storage.all()

        args = split_args(line)
        if not args or len(args) < 1:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__available_class:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in available_instance:
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            obj = available_instance[f"{args[0]}.{args[1]}"]
            if args[2] in obj.__dict__:
                data_type = type(obj.__dict__[args[2]])
                args[3] = data_type(args[3])
            obj.__dict__[args[2]] = args[3]
            obj.save()

    def do_count(self, line):
        """
        Return: the Number of instance Based on Class name
        Usage: Usage: count <class> or <class>.count()
        """
        available_instance = storage.all()

        args = split_args(line)
        count = 0
        if args and len(args) > 0:
            if args[0] in HBNBCommand.__available_class:
                for obj in available_instance.values():
                    if args[0] == obj.__class__.__name__:
                        count += 1
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

        print(count)

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, args):
        """EOF signal to exit the program"""
        return True


def split_args(line):
    """This Function will Separate args and return a list of the arguments"""

    if type(line) == str:
        args = [_.strip(",") for _ in split(line)]
        return args
    return line


def extract_function_info(line):
    """
    Find the Function Name and The input args
    ex: User.show(<id>)
    to: fun: show, arg = [User, id]
    """

    line_args = line.split('.')
    args = [line_args[0]]

    match = re.match(r"(\w+)\(", line_args[1])
    if match:
        cmd = match.group(1)
    else:
        return None, args

    if cmd == "create":
        return None, args

    args_str = re.search(r"\((.*?)\)", line_args[1]).group(1)
    if args_str:
        args_without_class = [arg.strip(',') for arg in split(args_str)]
        args.extend(args_without_class)

    return cmd, args


if __name__ == '__main__':
    HBNBCommand().cmdloop()

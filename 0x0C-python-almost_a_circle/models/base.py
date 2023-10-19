#!/usr/bin/python3
"""
This module provides a class which will be
the base class.
"""
import json
import os


class Base:
    """
    The Base class has a private attribute
    which will be used to set ``id`` when
    it is not given.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the Base class based on
        the value of the ``id`` argument.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation
        of list_dictionaries.

        Args:
            list_dictionaries: list of dictionaries

        Returns:
            JSON string representation of list_dictionaries
            or []
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries, default=str)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
        A class method that writes the JSON string
        representation of list_objs to a file.

        Args:
            cls: the class
            list_objs: list of instances that inherit
            from Base
        Returns:
            .json file
        """
        if list_objs is None:
            list_objs = []

        # convert each instance in list_objs to a JSON string
        list_dicts = [obj.to_dictionary() for obj in list_objs]

        # construct the required filename
        filename = cls.__name__ + ".json"

        # Write the JSON data to file
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        A static method that returns the list of the JSON
        representation.

        Args:
            json_string (str): a JSON string representing a list of
            dictionaries

        Returns:
            list: list of dictionaries represented by the JSON string
        """
        if json_string is None or json_string == "":
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with attributes set based on the given dictionary.

        Args:
            cls: the class (Rectangle or Square)
            **dictionary: A dictionary of attributes to set on the instance.

        Returns:
            An instance with attributes set according to the dictionary.
        """
        # Create "dummy" instance
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            raise ValueError("Unsupported class")

        # Call update on the dummy instance to apply the new real values
        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a JSON file.

        Args:
            cls: the class (Rectangle or Square)

        Returns:
            list: A list of instances of the specified class.
        """
        filename = cls.__name__ + ".json"

        if not os.path.exists(filename):
            return []

        with open(filename, 'r', encoding='utf-8') as file:
            json_string = file.read()
            dict_list = cls.from_json_string(json_string)

        instance_list = [cls.create(**dictionary) for dictionary in dict_list]

        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serialize and save a list of objects to a CSV file.

        Args:
            cls: The class (Rectangle or Square).
            list_objs: A list of instances to be serialized and saved.

        Returns:
            None
        """
        filename = cls.__name__ + ".csv"

        with open(filename, 'w', encoding='utf-8') as file:
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    data = [str(obj.id), str(obj.width), str(obj.height),
                            str(obj.x), str(obj.y)]
                    file.write(",".join(data) + "\n")
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    data = [str(obj.id), str(obj.size), str(obj.x), str(obj.y)]
                    file.write(",".join(data) + "\n")

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialize and load a list of objects from a CSV file.

        Args:
            cls: The class (Rectangle or Square).

        Returns:
            A list of instances loaded from the CSV file.
        """
        filename = cls.__name__ + ".csv"

        if not os.path.exists(filename):
            return []

        instance_list = []

        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split(",")
                if cls.__name__ == "Rectangle":
                    obj = cls(int(data[1]), int(data[2]))
                    obj.id = int(data[0])
                    obj.x = int(data[3])
                    obj.y = int(data[4])
                elif cls.__name__ == "Square":
                    obj = cls(int(data[1]))
                    obj.id = int(data[0])
                    obj.x = int(data[2])
                    obj.y = int(data[3])
                instance_list.append(obj)

        return instance_list

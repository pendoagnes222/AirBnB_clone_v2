#!/usr/bin/python3
""" file storage class """
import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """ File Storage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return all objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ Update dictionary """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects.update({key: obj})

    def save(self):
        """ Serializes __objects to the JSON file """
        with open(FileStorage.__file_path, 'w') as fp:
            dic = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(dic, fp)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:
            with open(FileStorage.__file_path) as fp:
                dic = json.load(fp)
                do = {k: eval(v["__class__"])(**v) for k, v in dic.items()}
                FileStorage.__objects = do
        except:
            pass

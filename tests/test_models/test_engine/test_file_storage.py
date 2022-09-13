#!/usr/bin/python3
"""
Define unittests for FileStorage class (models/engine/file_storage.py)
"""
import unittest
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel
import os
import json


class TestFileStorage_attr_type(unittest.TestCase):
    """Test attributes and instances type of FileStorage class"""

    def test_intance_type(self):
        self.assertEqual(FileStorage, type(FileStorage()))

    def test_attr_type(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))


class TestFileStorage_storage(unittest.TestCase):
    """Test creation of storage variable"""

    def reaload_without_file(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

        s = FileStorage()
        s.reload()

        self.assertEqual(FileStorage, type(s))

    def test_storage_type(self):
        self.assertEqual(FileStorage, type(storage))


class TestFileStorage_new_all(unittest.TestCase):
    """Test new and all methods of FileStorage class"""

    # Test type
    def test_all(self):
        self.assertEqual(dict, type(storage.all()))

    def test_new(self):
        b = BaseModel(id="b-new")
        storage.new(b)
        objects_dict = storage.all()
        keys = objects_dict.keys()
        b_key = "BaseModel." + b.id
        self.assertTrue(b_key in keys)


class TestFileStorage_save_reload(unittest.TestCase):
    """Test save and reload methods of FileStorage class"""

    @classmethod
    def clean(self):
        """Remove 'file.json'"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_save(self):
        TestFileStorage_save_reload.clean()

        c_date = '2017-09-28T21:05:54.119427'
        u_date = '2017-09-28T21:05:54.119572'
        id_val = "b_save"

        b = BaseModel(id=id_val, created_at=c_date, updated_at=u_date,)
        storage.new(b)
        storage.save()

        objects_dict = storage.all()
        keys = objects_dict.keys()
        b_key = "BaseModel." + b.id
        b_dict = b.to_dict()

        with open("file.json", "r") as file:
            json_text = file.read()
        json_dict = eval(json_text)
        self.assertTrue(b_key in json_dict.keys())
        self.assertEqual(json_dict[b_key], b_dict)

        TestFileStorage_save_reload.clean()

    def test_reload(self):
        TestFileStorage_save_reload.clean()
        b_key = "BaseModel.b_reaload"
        b_dict = {
            '__class__': 'BaseModel',
            'id': 'b_reaload',
            'name': "Holberton"}

        json_dict = {b_key: b_dict}

        with open("file.json", "w") as file:
            json.dump(json_dict, file)

        storage.reload()
        object_dict = storage.all()
        self.assertTrue(b_key in object_dict.keys())
        self.assertEqual(object_dict[b_key].name, "Holberton")

        TestFileStorage_save_reload.clean()

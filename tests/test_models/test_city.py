#!/usr/bin/python3
"""
Define unittests for City class (models/city.py)
"""
import unittest
from models.base_model import BaseModel
from models.city import City
from models import storage
import datetime
from time import sleep
import os


class TestCity(unittest.TestCase):
    """Test instantiation of City class."""

    # Testing type
    def test_type(self):
        c = City()
        self.assertEqual(City, type(c))

    def test_type_public_attr(self):
        c = City()
        self.assertEqual(str, type(c.id))
        self.assertEqual(str, type(c.state_id))
        self.assertEqual(str, type(c.name))

    def test_type_created_at(self):
        c = City()
        self.assertEqual(datetime.datetime, type(c.created_at))

    def test_type_update_at(self):
        c = City()
        self.assertEqual(datetime.datetime, type(c.updated_at))

    # Testing id
    def test_unique_id(self):
        c1 = City()
        c2 = City()
        self.assertNotEqual(c1.id, c2.id)

    # Testing dates
    def test_consecutive_created_at(self):
        c1 = City()
        sleep(0.02)
        c2 = City()
        self.assertLess(c1.created_at, c2.created_at)

    def test_consecutive_updated_at(self):
        c1 = City()
        sleep(0.02)
        c2 = City()
        self.assertLess(c1.updated_at, c2.updated_at)

    # Testing new attributes creation
    def test_new_attr(self):
        c = City()
        c.name = "Holberton"
        c.email = "ejemplo@gato.com"
        self.assertTrue(hasattr(c, "name") and hasattr(c, "email"))

    # Test update storage variable
    def test_bm_updated_storage(self):
        c = City()
        c_key = "City." + c.id
        keys = storage.all().keys()
        self.assertTrue(c_key in keys)

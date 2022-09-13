#!/usr/bin/python3
"""
Define unittests for Place class (models/place.py)
"""
import unittest
from models.base_model import BaseModel
from models.place import Place
from models import storage
import datetime
from time import sleep
import os


class TestPlace(unittest.TestCase):
    """Test instantiation of Place class."""

    # Testing type
    def test_type(self):
        p = Place()
        self.assertEqual(Place, type(p))

    def test_type_public_attr(self):
        p = Place()
        self.assertEqual(str, type(p.id))
        self.assertEqual(str, type(p.city_id))
        self.assertEqual(str, type(p.user_id))
        self.assertEqual(str, type(p.name))
        self.assertEqual(str, type(p.description))
        self.assertEqual(int, type(p.number_rooms))
        self.assertEqual(int, type(p.number_bathrooms))
        self.assertEqual(int, type(p.max_guest))
        self.assertEqual(int, type(p.price_by_night))
        self.assertEqual(float, type(p.latitude))
        self.assertEqual(float, type(p.longitude))
        self.assertEqual(list, type(p.amenity_ids))

    def test_type_created_at(self):
        p = Place()
        self.assertEqual(datetime.datetime, type(p.created_at))

    def test_type_update_at(self):
        p = Place()
        self.assertEqual(datetime.datetime, type(p.updated_at))

    # Testing id
    def test_unique_id(self):
        p1 = Place()
        p2 = Place()
        self.assertNotEqual(p1.id, p2.id)

    # Testing dates
    def test_consecutive_created_at(self):
        p1 = Place()
        sleep(0.02)
        p2 = Place()
        self.assertLess(p1.created_at, p2.created_at)

    def test_consecutive_updated_at(self):
        p1 = Place()
        sleep(0.02)
        p2 = Place()
        self.assertLess(p1.updated_at, p2.updated_at)

    # Testing new attributes creation
    def test_new_attr(self):
        p = Place()
        p.name = "Holberton"
        p.email = "ejemplo@gato.com"
        self.assertTrue(hasattr(p, "name") and hasattr(p, "email"))

    # Test update storage variable
    def test_bm_updated_storage(self):
        p = Place()
        p_key = "Place." + p.id
        keys = storage.all().keys()
        self.assertTrue(p_key in keys)

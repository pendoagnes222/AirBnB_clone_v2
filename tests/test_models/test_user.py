#!/usr/bin/python3
"""
Define unittests for User class (models/user.py)
"""
import unittest
from models.base_model import BaseModel
from models.user import User
from models import storage
import datetime
from time import sleep
import os


class TestUsers(unittest.TestCase):
    """Test instantiation of User class."""

    # Testing type
    def test_type(self):
        u = User()
        self.assertEqual(User, type(u))

    def test_type_id(self):
        u = User()
        self.assertEqual(str, type(u.id))

    def test_type_public_attr(self):
        u = User()
        self.assertEqual(str, type(u.email))
        self.assertEqual(str, type(u.password))
        self.assertEqual(str, type(u.first_name))
        self.assertEqual(str, type(u.last_name))

    def test_type_created_at(self):
        u = User()
        self.assertEqual(datetime.datetime, type(u.created_at))

    def test_type_update_at(self):
        u = User()
        self.assertEqual(datetime.datetime, type(u.updated_at))

    # Testing id
    def test_unique_id(self):
        u1 = User()
        u2 = User()
        self.assertNotEqual(u1.id, u2.id)

    # Testing dates
    def test_consecutive_created_at(self):
        u1 = User()
        sleep(0.02)
        u2 = User()
        self.assertLess(u1.created_at, u2.created_at)

    def test_consecutive_updated_at(self):
        u1 = User()
        sleep(0.02)
        u2 = User()
        self.assertLess(u1.updated_at, u2.updated_at)

    # Testing new attributes creation
    def test_new_attr(self):
        u = User()
        u.name = "Holberton"
        u.my_number = "ejemplo@gato.com"
        self.assertTrue(hasattr(u, "name") and hasattr(u, "my_number"))
    
    def test_bm_updated_storage(self):
        u = User()
        u_key = "User." + u.id
        keys = storage.all().keys()
        self.assertTrue(u_key in keys)

# test_railwaydb.py
"""
Tests for RailwayDB module.
"""

import unittest
from railwaydb import RailwayDB

class TestRailwayDB(unittest.TestCase):
    """Test cases for RailwayDB class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RailwayDB()
        self.assertIsInstance(instance, RailwayDB)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RailwayDB()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

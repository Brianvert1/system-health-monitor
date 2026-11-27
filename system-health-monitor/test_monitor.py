import unittest
from monitor import warnings

class WarningTests(unittest.TestCase):
    def test_threshold(self):
        report = dict(cpu_percent=85, memory_percent=20, disk_percent=90)
        self.assertEqual(len(warnings(report, 85)), 2)

    def test_healthy(self):
        report = dict(cpu_percent=10, memory_percent=20, disk_percent=30)
        self.assertEqual(warnings(report, 85), [])

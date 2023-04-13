import pygame
import unittest
from queue import Queue
from ConfigurationStateManager import ConfigurationStateManager
from os import environ
from Renderables import *


environ["SDL_VIDEODRIVER"] = "dummy"

class RenderableTestCase(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.display = pygame.display.set_mode((640, 480))
        self.config = ConfigurationStateManager(Queue(), Queue())

    def test_base_case_functionality(self):
        self.assertEqual(True, True, "Base RenderableTestCase assert failed")


class GenericDerivedTestCase(RenderableTestCase):
    def test_derived_case_functionality(self):
        self.assertEqual(True, True, "Generic derived test case assert failed")

class StringLineTest(RenderableTestCase):
    def test_width_percent_too_large(self):
        with self.assertRaises(ValueError):
            StringLine(101, 50).draw(self.display, self.config)

    def test_y_percent_too_high(self):
        with self.assertRaises(ValueError):
            StringLine(10, 101).draw(self.display, self.config)

    def test_y_percent_too_low(self):
        with self.assertRaises(ValueError):
            StringLine(10, -1).draw(self.display, self.config)

    def test_width_fills_screen(self):
        self.assertIsInstance(StringLine(100, 50).draw(self.display, self.config),
                              StringLine,
                              "StringLine did not return self when width = 100%")

    def test_y_zero(self):
        self.assertIsInstance(StringLine(50, 0).draw(self.display, self.config),
                              StringLine,
                              "StringLine did not return self when y = 0")

    def test_y_one_hundred(self):
        self.assertIsInstance(StringLine(50, 100).draw(self.display, self.config),
                              StringLine,
                              "StringLine did not return self when y = 100")

    def test_average_case(self):
        self.assertIsInstance(StringLine(50, 50).draw(self.display, self.config),
                              StringLine,
                              "StringLine did not return self in average use case")

class FretLineTest(RenderableTestCase):
    def test_x_percent_too_large(self):
        with self.assertRaises(ValueError):
            FretLine(101, 5).draw(self.display, self.config)

    def test_x_percent_too_small(self):
        with self.assertRaises(ValueError):
            FretLine(-1, 5).draw(self.display, self.config)

    def test_x_percent_zero(self):
        self.assertIsInstance(FretLine(0, 5).draw(self.display, self.config),
                              FretLine,
                              "FretLine did not return self when x_percent = 0")

    def test_x_percent_one_hundred(self):
        self.assertIsInstance(FretLine(100, 5).draw(self.display, self.config),
                              FretLine,
                              "FretLine did not return self when x_percent = 100")

    def test_height_percent_too_large(self):
        with self.assertRaises(ValueError):
            FretLine(50, 11).draw(self.display, self.config)

    def test_height_percent_too_small(self):
        with self.assertRaises(ValueError):
            FretLine(50, -1).draw(self.display, self.config)

    def test_height_percent_max(self):
        self.assertIsInstance(FretLine(50, 10).draw(self.display, self.config),
                              FretLine,
                              "FretLine did not return self when height_percent = 10 (max)")

    def test_height_percent_min(self):
        self.assertIsInstance(FretLine(50, 0).draw(self.display, self.config),
                              FretLine,
                              "FretLine did not return self when height_percent = 0 (min)")

    def test_average_case(self):
        self.assertIsInstance(FretLine(50, 5).draw(self.display, self.config),
                              FretLine,
                              "FretLine did not return self in average use case")

class FretMarkTest(RenderableTestCase):
    def test_x_percent_too_large(self):
        with self.assertRaises(ValueError):
            FretMark(100, 50).draw(self.display, self.config)

    def test_x_percent_too_small(self):
        with self.assertRaises(ValueError):
            FretMark(0, 50).draw(self.display, self.config)

    def test_x_percent_min(self):
        self.assertIsInstance(FretMark(0.005, 50).draw(self.display, self.config),
                              FretMark,
                              "FretMark did not return self when x_percent = 0.005 (min)")

    def test_x_percent_max(self):
        self.assertIsInstance(FretMark(99.995, 50).draw(self.display, self.config),
                              FretMark,
                              "FretMark did not return self when x_percent = 99.995 (max)")

    def test_y_percent_too_large(self):
        with self.assertRaises(ValueError):
            FretMark(50, 100).draw(self.display, self.config)

    def test_y_percent_too_small(self):
        with self.assertRaises(ValueError):
            FretMark(50, 0).draw(self.display, self.config)

    def test_y_percent_min(self):
        self.assertIsInstance(FretMark(50, 0.005).draw(self.display, self.config),
                              FretMark,
                              "FretMark did not return self when y_percent = 0.005 (min)")

    def test_y_percent_max(self):
        self.assertIsInstance(FretMark(50, 99.995).draw(self.display, self.config),
                              FretMark,
                              "FretMark did not return self when y_percent = 99.995 (max)")

    def test_average_case(self):
        self.assertIsInstance(FretMark(50, 50).draw(self.display, self.config),
                              FretMark,
                              "FretMark did not return self in average use case")



if __name__ == "__main__":
    unittest.main()
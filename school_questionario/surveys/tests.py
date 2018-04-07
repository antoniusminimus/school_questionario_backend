import unittest

from django.test import TestCase

# Create your tests here.
from surveys.models import Survey


class SurveysTests(TestCase):

    def test_subject_class(self):
        self.assertTrue(Survey)

    def test_subject_class_unique_name(self):
        pass


if __name__ == '__main__':
    unittest.main

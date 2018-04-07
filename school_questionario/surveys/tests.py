import unittest

from django.test import TestCase

# Create your tests here.
from surveys.models import Survey


class SurveysTests(TestCase):

    def test_subject_class(self):
        self.assertTrue(Survey)


if __name__ == '__main__':
    unittest.main

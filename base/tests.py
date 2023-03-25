from django.test import TestCase
from .models import Author
# Create your tests here.




def preparing_str_for_db(author_names):
    return [x.strip(' ').lower() for x in author_names]


class TestExample(TestCase):

    def test_preparing_str_for_db(self):
        self.assertEqual(preparing_str_for_db([' Mihail Stankevich  ', ' Alex']), ['mihail stankevich', 'alex'])
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelsTest(TestCase):

    def test_create_user_with_email_seccesfull(self):
        """test create user with email succesfull"""
        email = "email@mail.com"
        password = "password123"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_name_normalized(self):
        """test username to be normalized"""

        email = "test@MAIL.Com"

        user = get_user_model().objects.create_user(email, "passwd")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test creating user with no email error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """test super user creation"""
        user = get_user_model().objects.create_superuser('super', 'test12')

        self.assertTrue(user.is_superuser, True)
        self.assertTrue(user.is_staff, True)

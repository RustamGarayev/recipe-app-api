from django.test import TestCase
from django.contrib.auth import get_user_model


# User = get_user_model
class ModelTests(TestCase):
    """Test creating new user with an email successful"""
    def test_create_user_with_email_successful(self):
        email = 'test@gmail.com'
        password = 'Test12345'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test the email for a new user is normalized """
        email = 'test@Fmail.com'
        user = get_user_model().objects.create_user(
            email, 'test12345'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                None, 'test12345'
            )

    # def test_password_has_enough_charachters(self):
    #    """Test creating user with invalid password raises error"""
    #    with self.assertRaises(ValueError):
    #        get_user_model().objects.create_user(
    #            'test@gmail.com', 'test'
    #        )

    def test_create_new_superuser(self):
        """ Test creating new Superuser """
        user = get_user_model().objects.create_superuser(
            'test@gmail.com', 'test12345556'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

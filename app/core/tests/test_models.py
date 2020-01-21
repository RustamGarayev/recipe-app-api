from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='test@londonappdev.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)

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

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)

    def test_tag_str(self):
        """Test the ingredient string representation"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):
        """Test the recipe string representation"""
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title='Steak and mushroom sauce',
            time_minute=5,
            price=5.00
        )

        self.assertEqual(str(recipe), recipe.title)

'''
Users application tests
'''

# Import all requirements
from django.test import TestCase
from django.contrib.auth import get_user_model


# Custom User Tests class
class CustomUserTests(TestCase):

    def test_create_user(self):
        # Create a User for testing
        User = get_user_model()
        user = User.objects.create_user(
            email='testuser@example.com',
            password='Testpass1234567890',
        )
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

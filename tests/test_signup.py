import unittest
from models.signup import SignUp, Driver, Rider


class TestSignUp(unittest.TestCase):

    def test_combined_name(self):
        person = SignUp('Kabarozi', 'Dorothy', 256775401173,
                        234, 3)

        self.assertEqual(person.combined_name(), 'Kabarozi Dorothy')
        self.assertGreater(person.promo_code, 1)

    def test_validate_email(self):
        self.assertEqual(SignUp.validate_email(
            'kizdorothy@gmail.com'), 'kizdorothy@gmail.com')

    def test_add(self):
        rider = Rider('Dar', 'kato-details')
        rider.add('Kato', 'Kampala')
        self.assertEqual(len(rider.rider_details), 1)

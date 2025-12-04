"""

"""
import unittest
from unittest import TestCase
from unittest.mock import patch
from oo_18_die import Die, Die6, Die20


class TestDie(TestCase):

    def test_initialization(self):
        """Test of de dobbelsteen correct wordt aangemaakt."""

        # basis testen
        # Maak een object aan
        # Test of de eigenschappen juist zijn
        d = Die(6)
        self.assertEqual(d.sides, 6)
        self.assertIsNone(d.value)
        self.assertEqual(str(d), "D6")

    def test_read_only_properties(self):
        """Test of sides en value read-only zijn."""

        # exception testen
        # Doe iets waarvan je zeker weet dat het een exception moet geven
        # Controleer dat het effectief een exception geeft
        d = Die(6)
        with self.assertRaises(AttributeError):
            d.sides = 10
        with self.assertRaises(AttributeError):
            d.value = 5

    def test_roll(self):
        """Test het rollen van de dobbelsteen."""

        # function testen
        # Voer een functie uit en controleer of het goed werkt
        d = Die(6)
        for _ in range(1000):
            self.assertIn(d.roll(), range(1, 7))


    def test_equality(self):
        """Test de __eq__ methode."""
        d1 = Die(6)
        d2 = Die(6)

        # Nog niet gerold: moet ValueError geven
        with self.assertRaises(ValueError):
            _ = d1 == d2

        # Forceer resultaten via mock
        with patch('random.randint', side_effect=[3, 3]):
            d1.roll()
            d2.roll()
            self.assertEqual(d1, d2)

        with patch('random.randint', return_value=4):
            d2.roll()  # d2 is nu 4, d1 was 3
            self.assertNotEqual(d1, d2)

    def test_addition(self):
        """Test optellen van twee dobbelstenen (__add__)."""
        d1 = Die(6)
        d2 = Die(6)

        # Nog niet gerold
        with self.assertRaises(ValueError):
            _ = d1 + d2

        with patch('random.randint', side_effect=[2, 5]):
            d1.roll()
            d2.roll()
            self.assertEqual(d1 + d2, 7)

    def test_radd(self):
        """Test optellen van int en dobbelsteen (int + Die)."""
        d = Die(6)
        with patch('random.randint', return_value=3):
            d.roll()
            # Test __radd__ (5 + d)
            self.assertEqual(5 + d, 8)

    def test_multiplication(self):
        """
        Test vermenigvuldiging (__mul__).
        Die * 3 betekent: rol de die 3 keer en tel op.
        """
        d = Die(6)

        # Mock randint om altijd 2 terug te geven
        with patch('random.randint', return_value=2):
            # 3 keer rollen, elke keer 2 -> totaal 6
            result = d * 3
            self.assertEqual(result, 6)

        # Test met verkeerd type
        with self.assertRaises(TypeError):
            _ = d * "string"

    def test_subclasses(self):
        """Korte test of de subclasses correct initialiseren."""
        d6 = Die6()
        self.assertEqual(d6.sides, 6)

        d20 = Die20()
        self.assertEqual(d20.sides, 20)


if __name__ == '__main__':
    unittest.main()
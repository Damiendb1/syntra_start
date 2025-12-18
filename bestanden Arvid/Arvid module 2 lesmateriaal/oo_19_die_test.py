"""
Unit testing is een testmethode waarbij afzonderlijke stukjes code, zoals functies, methoden of classes,
geïsoleerd worden getest om te controleren of ze naar verwachting werken.

Unit testing biedt verschillende draagt bij tot de kwaliteit en stabiliteit van software.

Foutdetectie: Bugs worden opgespoord voordat ze zich verspreiden naar andere delen van de code.
Betere codekwaliteit: Unit tests dwingen ontwikkelaars om hun code modulair en testbaar te schrijven.
Snellere ontwikkelcycli: Fouten worden sneller gevonden en opgelost, wat leidt tot efficiëntere softwareontwikkeling.
Minder kosten op lange termijn: Hoe eerder een bug wordt ontdekt, hoe minder duur het is om deze te verhelpen.
Betere documentatie: Unit tests fungeren als een vorm van documentatie over hoe functies bedoeld zijn te werken.

Er zijn ontwikkelteams waar je eerst je unittest moet schrijven en pas daarna de eigenlijke functies of class.
Dit verplicht te ontwikkelaar om eerst na te denken hoe iets moet werken en wat de mogelijke resultaten zijn.
"""



# In een standaard Python installatie is de module unittest beschikbaar.
import unittest

# importeer de module waar een "unit of work" zit die je wil testen.
# We gaan de function pants_size en de classes van Die testen


# Maak een subclass van unittest.TestCase
# De naam van jouw nieuw klasse mag je volledig kiezen.
# Voeg aan die klasse methods toe waarvan de naam begint met 'test_'
# Bij het uitvoeren van de unittest worden alle methoden die starten met 'test_' uitgevoerd.
# Deze methoden moeten geen argumenten nemen en een waarde teruggeven.
# Dus ze zijn allemaal van deze vorm
#   def test_something(self) -> None:
#        test1

# We voegen ter illustratie een eenvoudige function toe
# Normaal gezien staan de test en de function in verschillende bestanden.
def pants_size(size: int) -> str:
    """
    Function to determine a size-label of pants based on the size.
    :param size: Pants size.
    :return: Size label.
    """
    if size < 15:
        return "S"
    if size < 25:
        return "L"
    return "XL"


class PantsSize(unittest.TestCase):
    def test_size(self):
        # Deze method zal als test worden uitgevoerd

        # Schrijf voor elke goede test waarde van de function een test
        # assertEqual(expected, actual) controleert of de verwachte waarde
        # overeenkomt met de waarde die de function teruggeeft.
        self.assertEqual("S", pants_size(10))
        self.assertEqual("L", pants_size(20))
        self.assertEqual("XL", pants_size(30))
        # Het is niet zo relevant welke parameter eerst komt, de verwachte waarde
        # of de berekende waarde.
        self.assertEqual( pants_size(30), "XL")

        # bovenstaande tests slagen allemaal
        # Stel dat de function pants_size een bug bevat.
        # De waarde 15 zou ook S moeten teruggeven
        # Dan zal deze test mislukken.

        # self.assertEqual("S", pants_size(15))

        # Een test die faalt, kan twee zaken betekenen:
        # 1. De function is foutief geschreven. Er zit een ug in
        # 2. De function werkt zoals verwacht, maar de test is fout.
        # In beide gevallen moet je code aanpassen: ofwel jouw function, ofwel jouw test.


# Het uitschrijven van een unittest is een stap in de ontwikkelingsprocessen van een softwareproject.
# Als je tests schrijft voor de function pants_size(), kan je bedenken:
# Wat moet de function doen bij negatieve getallen?
# Wat moet de function doen bij float waarde als input?
# Wat moet de function doen als de input een string is?
# Het is dan aan de programmeur om deze vragen te beantwoorden en de functie eventueel robuuster te maken
#    - controle dat de input een getal is, anders een ValueError geven
#    - controleer of de input een positief getal is, anders een ValueError geven
#    - controleer of de input een getal tussen 5 en 150, anders een ValueError geven



from oo.oo_18_die import Die, Die6, Die20

class TestDie(unittest.TestCase):

    def test_superclass_die(self):
        d = Die(9)
        self.assertEqual(d.sides, 9)
        # Er zijn naast assertEqual ook andere assert-methoden.
        self.assertIsNone(d._last_roll)
        self.assertNotEqual(d.sides, 5)

    def test_die6(self):
        d6 = Die6()
        for _ in range(100):
            self.assertTrue(0< d6.roll() < 7)
        # Bij het schrijven van tests moet je altijd ervoor zorgen dat
        # het verwachte resultaat vastligt.
        # Een rol van een D6 zal niet steeds 5 zijn.
        # Onderstaande test zal meestal mislukken. Maar heeft 1/6 kans om te slagen.

        # res = d6.roll()
        # self.assertEqual(res, 5)

    def test_die_property(self):
        d = Die(23)
        # d.sides is een property die niet van waarde veranderd mag worden.
        # De property setter voor 'sides' geeft een AttributeError.
        # Om the controleren of het aanpassen van sides een exception geeft,
        # kan je deze code gebruiken.
        with self.assertRaises(AttributeError):
            d.sides = 10


if __name__ == '__main__':
    unittest.main()

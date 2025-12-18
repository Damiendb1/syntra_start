# Een deur is een object met drie verschillende mogelijke toestanden.
#    opened, closed, locked
# De toestand mag enkel gewijzigd worden d.m.v. de functions open(), close(), lock()


# We maken 3 constantes voor de mogelijke toestanden.
OPENED = "opened"
CLOSED = "closed"
LOCKED = "locked"


class Door:
    """
    Class for a door
    """

    def __init__(self, number: int):
        self.number = number
        # We veronderstellen dat een deur steeds start in status open.
        # We maken status protected door er een _ onder te zetten.
        self._status = OPENED

    # de toestand kan wel opgevraagd worden
    @property
    def toestand(self):
        return self._status

    # de toestand mag niet gewijzigd worden
    @toestand.setter
    def toestand(self, value):
        raise AttributeError("Je mag status enkel wijzigen let open(), ....")

    def open(self):
        """
        You can open a door when it is not locked
        """
        if self._status == OPENED:
            return
        if self._status == CLOSED:
            self._status = OPENED

        if self._status == LOCKED:
            self._status = LOCKED

    def close(self):
        if self.toestand == OPENED:
            self._status = CLOSED
        if self._status == CLOSED:
            self._status = OPENED

        if self._status == LOCKED:
            self._status = LOCKED

    def lock(self):
        pass

    def __lt__(self, other):
        # number is een publiek (niet-protected) class attribute
        # zowel self als other hebber en toegang toe.
        return self.number < other.number

    def __eq__(self, other):
        # Stel dat twee deuren gelijk zijn als het toestand gelijk is
        # _status is protected. Enkel self heeft er toegang toe
        return self.toestand > other.toestand  # ==> Dit is correct
        # return self._status > other.toestand  # ==> Dit is correct maar ziet er raar uit
        # return self._status > other._status  # Dit hoort niet.  You SHOULD not do this.


d = Door(4)
d._status = CLOSED
print(d.address)
d.status = "Arvid"
print(d.toestand)
print(d.state_description)
print(d._status)
print(status)

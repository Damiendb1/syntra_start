# De datetime module helpt je werken met datums, tijden, en tijdsduren.
# * De huidige datum/tijd ophalen
# * Datums formatteren
# * Verschillen tussen datums berekenen
# * Tijden plannen of simuleren

import datetime  # Importeer de module

# De huidige datum en  tijd
print(datetime.datetime.now())

# De huidige datum
print(datetime.date.today())

today = datetime.date.today()
b_day = datetime.date(2007, 12, 16)
diff = today - b_day
print(diff)
print(f"Nog {diff.days} dagen tot Kerstmis!")

# Datum formatteren
# strftime() – string formatting
now = datetime.datetime.now()
formatted = now.strftime("%d-%m-%Y %H:%M")
print(f"Geformatteerde tijd: {formatted}")
"""
%Y	Volledig jaar	2025
%y	Jaar (2 cijfers)	25
%m	Maand (01–12)	10
%B	Volledige maandnaam	oktober
%d	Dag van de maand (01–31)	07
%A	Volledige weekdagnaam	dinsdag
%a	Afgekorte weekdagnaam	di
%H	Uur (24-uurs formaat)	21
%I	Uur (12-uurs formaat)	09
%p	AM of PM	PM
%M	Minuten (00–59)	24
%S	Seconden (00–59)	00
%j	Dag van het jaar (001–366)	280
%W	Weeknummer van het jaar (maandag-start)	40
%Z	Tijdzone	CEST
%c	Volledige lokale datum/tijd	di 07 okt 2025 21:24:00
%x	Lokale datum	07/10/25
%X	Lokale tijd	
"""

# String omzetten naar datum
date_str = "25-12-2025"
date = datetime.datetime.strptime(date_str, "%d-%m-%Y")
print(f"Omgezette datum: {date.date()}")

# tijd verschillen
from datetime import datetime, timedelta

now = datetime.now()

# Tijdsverschillen maken
one_day = timedelta(days=1)
one_week = timedelta(weeks=1)
two_hour = timedelta(hours=2)
thirty_minutes = timedelta(minutes=30)

# Rekenen met datums
tomorrow = now + one_day
yesterday = now - one_day
next_week = now + one_week
in_two_hours = now + two_hour

print(f"Nu: {now}")
print(f"Morgen: {tomorrow}")
print(f"Gisteren: {yesterday}")
print(f"Volgende week: {next_week}")
print(f"Over 2 uur: {in_two_hours}")




deadline = now + timedelta(days=7, hours=3, minutes=30)
print(f"Deadline: {deadline}")


# opdracht 1: Vraag de gebruiker om een datum (DAG/MAAND/JAAR) in te geven.
# Blijf vragen tot het formaat goed is.

# opdracht 2: Opdracht 1 + bepaal of de datum in het verleden of in de toekomst ligt.
# opdracht 3: Opdracht 1 + bepaal of de datum in de hersft, winter,lente of zomer ligt.
# opdracht 4: Opdracht 1 + als de datum in het verleden ligt, zeg dan hoeveel jaar het geleden is.



def work_on_car(age:int):
    try:
        try:
            a = 1/0
            print("Ik open de motorkap")
        except ZeroDivisionError:
            print("domme deling")

        print("Ik veeg het jaarplaatje proper")
        if age > 10:
            raise ValueError()
        print("Ik repareer de auto")

    except ValueError:
        pass

    finally:
        print("Ik was mijn handen")


work_on_car(7)

filename = "filedefsdsdgsg"

try:
    file = open(filename,"r")
except FileNotFoundError:
    print("Bestand niet gevonden")
except PermissionError:
    print("Geen toegang")
else:
    try:
        for line in file:
            print(line[:-1])
    except IOError:
        print("Fout bij lezen van bestand")





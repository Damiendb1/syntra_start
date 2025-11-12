import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)s %(levelname)s %(message)s')
def vraag_getal_1_10():
    while True:
        n = input("geef een getal tussen 1 en 10: ")
        if n.lower() == "stop":
            logging.info("programma gestopt")
            return

        try:
            n = int(n)
            if 1 <= n <= 10:
                logging.info(f"{n}getal ligt tussen 1 en 10")
            else:
                logging.error(f"{n}geen geheeel getal")
                pass
        except ValueError:
            logging.error(f"{n}geen is geen geheleen getal")

vraag_getal_1_10()





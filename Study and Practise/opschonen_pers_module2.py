import csv

in_path = r"C:\datadev2\personsmodule2.csv"
out_path = r"C:\datadev2\personsmodule4_clean.csv"

with open(in_path, "r", encoding="utf-8", newline="") as f_in, \
     open(out_path, "w", encoding="utf-8", newline="") as f_out:

    reader = csv.reader(f_in)
    writer = csv.writer(f_out,delimiter=";")

    writer.writerow(["name", "gender", "type"])

    for row in reader:
        if not row:
            continue
        name = row[0].strip()
        gender = row[1].strip().upper()
        type_ = row[2].strip().upper()
        writer.writerow([name, gender, type_])

print("Nieuwe bestand geschreven", out_path)

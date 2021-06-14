import csv

studenti = {"123": 8, "124": 10, "555": 9}
info = []
file_to_open = 'studenti.csv'          #Datoteku studenti.csv smo zamijenili novim imenom, da nam je dalje lakše koristiti u programu
with open(file_to_open) as f:
    student_info = csv.DictReader(f)
    info = list(student_info)          #Ovdje smo predstavili kao listu dokument
    print("Podaci o studentima")
    print("                   ")
    for i, row in enumerate(info):       #Na ovaj način smo omogućili iteriranje
        i += 1
        print('{}. \t {} \t {}, ocjena: {}'.format(           #Formatirali smo stringove tj.
            i, row['ime'], row['prezime'], row['ocjena']))    #izvdojili smo ispis pojedinih članova kolone preko for petlje
                                                             # i to tako što ispisujemo samo kolone sa imenima, prezimenima i ocjenama

    with open(file_to_open, 'w') as updated_file:
        fieldnames = ['ime', 'prezime', 'index', 'ocjena']    # Otvara se datoteka i u nju se upisuju elementi prvog reda (imena polja) ime, prezime..
        csv_writer = csv.DictWriter(                          #fieldnames je promjenjiva u koju se podaci smjestaju koju ćemo kasnije koristiti za upis
            updated_file, fieldnames=fieldnames, delimiter=',')

        csv_writer.writeheader()
        for mod_row in info:
            for index, ocjena in studenti.items():          # Provjeravajući indexe studenata, tj. ona mjesta sa istim indexom kao u "studenti"
                if mod_row['index'] == index:
                    mod_row['ocjena'] = int(                 # sada ta mjesta poprimaju nove vrijednosti, aritmetičku vrijednost prethodne ocjene i nove
                        (int(mod_row['ocjena']) + ocjena) / 2)
            csv_writer.writerow(mod_row)                     #To se sve sada upisuje u datoteku studenti.csv

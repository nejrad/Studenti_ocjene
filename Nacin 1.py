import csv            #Zadatak je bio ažurirati csv file koji čuva podatke o studentima
adresa="studenti.csv"
with open (adresa) as d:
    r=csv.reader(d)
    tabela=list(r) #Na ovaj način smo predstavili učitan .csv file kao listu, s kojom je lakše raditi
studenti = {"123": 8, "124": 10, "555": 9}

print("Podaci o studentima")
print("                   ")
for i in range(1,len(tabela)): #i brojač ovdje ide do dužine liste koja je uzeta iz fajla
    print(str(i)+".  ",tabela[i][0],'  ',tabela[i][1],", ocjena:",tabela[i][3])
    # Za svaku iteraciju printaju se podaci iz fajla, tabela[i][0] znači i-ta vrijednost i prvog reda kolone,
    # (kod nas je to ime) iz csv,
    # tabela[i][1] bi bila iz druge kolone to je kod nas prezime,
    # brojač ide od broja 1 da bi se preskočio red gdje pišu imena kolona (ime, prezime itd)
    if studenti.get(tabela[i][2])!=None:
        # Ako je vrijednost ključa tj indexa (ocjena 8,10,9) različita od nonetype tj. ako ona postoji računa se prosjek
        tabela[i][3]=(int(tabela[i][3])+studenti[tabela[i][2]])//2
        #uzima se vrijednost iz ovog iz tabele i uzima se onda vrijednost i iz students dictionary i računa to za svaki red

with open(adresa,mode="w",newline='')as d:
    w=csv.writer(d)
    w.writerows(tabela)
    # upišu se vrijednosti naše nove update-ovane tabele u isti fajl
    # (adresa je gore deklarisana pod istim imenom tj studenti.csv, da je drugačije bilo, tada bi se napravio novi fajl)

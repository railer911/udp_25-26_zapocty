import statistics
def top5_studenti(subor):
    try:
        studenti = []
        with open(subor, "r") as f:
            for riadok in f:
                meno, priezvisko, body = riadok.strip().split(";")
                celemeno = meno + " " + priezvisko
                studenti.append((int(body), celemeno))
        studenti.sort(reverse=True)
        return studenti[:5]
    
    except FileNotFoundError:
        print("Súbor neexistuje!")
        return []

def spp(subor):
    try:
        studenti = []
        bodyspolu = []
        studentipodpriemer = []
        with open(subor, "r") as f:
            for riadok in f:
                meno, priezvisko, body = riadok.strip().split(";")
                celemeno = meno + " " + priezvisko
                body = int(body)
                studenti.append((body, celemeno))
                bodyspolu.append(body)
        priemer = statistics.mean(bodyspolu)
        for body, meno in studenti:
            if body < priemer:
                studentipodpriemer.append((body, meno))
        studentipodpriemer.sort(reverse=True)
        percento=(int((len(studenti))-int(len(studentipodpriemer)))/int(len(studenti)))*100
        percento=round(percento,2)
        priemer=round(priemer,2)
        return priemer, studentipodpriemer, percento
    
    except FileNotFoundError:
        print("Súbor neexistuje!")
        return []

def ulozto(subor,novysubor):
    try:
        studenti = []
        with open(subor, "r") as f:
            for riadok in f:
                meno, priezvisko, body = riadok.strip().split(";")
                celemeno = meno + " " + priezvisko
                studenti.append((int(body), celemeno))
        studenti.sort(reverse=True)
        with open(novysubor,"w") as file:
            for body, meno in studenti:
                file.write(meno," so ziskom ",body," bodov\n")
    except FileNotFoundError:
        print("Súbor neexistuje!")
        return []
    
su=input("Napíš meno vstupneho suboru (nazov_suboru.txt): ")
print("1. Najlepšia pätica")
print("2. Všetci študenti pod priemerom")
print("2. Uloženie do externého txt súboru")
print("4. Koniec")

while True:
    vybermoznosti=int(input("Vyber si ktorú funkciu chceš vykonať: (1-4) "))

    if vybermoznosti == 1:
        print("Jupí vybral si si top 5 študentov!")
        jednicka = top5_studenti(su)
        print("Toto sú najlepší:")
        for i, (body, meno) in enumerate(jednicka, start=1):
            print(i,"." ,meno, "-", body, "bodov")

    elif vybermoznosti == 2:
        print("Jupí vybral si si studentov pod priemerom!")
        priemer,podpriemer,perc = spp(su)
        print("Studenti pod priemerom boli: ")
        for body,meno in podpriemer:
            print(meno, body)
        print("Priemer bol",str(priemer)+" bodov")
        print("Pod priemerom bolo "+str(perc)+"% študentov")

    elif vybermoznosti == 3:
        print("Jupí vybral si si uloženie do suboru!")
        output=input("Nazov noveho fajlu (novy_subor.txt): ")
        ulozto(su,output)
        print("ulozene")

    elif vybermoznosti == 4:
        print("koncim, caw, cc")
        break

    else:

        print("skus to znova")

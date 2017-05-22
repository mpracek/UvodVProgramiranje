import urllib .request

podatki = urllib.request.urlopen('http://www.flashscores.co.uk/')
print(podatki)




"Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32"
def verjetnost(ekipa, rezultati, kraj):
    '''Pove nam približno verjetnost, s katero bo prišlo do zmage, remija oziroma poraza glede na prejšnje rezultate ekipe.
    V rezultat vpišemo niz Z, P, R, kjer je Z zmaga, P poraz in R remi.
    V kraj vpišemo niz domač ali gost.'''
    verjetnost1 = 0
    for rezultat in rezultati:
        if rezultat == 'Z':
            verjetnost1 += 0.19
        elif rezultat == 'R':
            verjetnost1 += 0.1
        elif rezultat == 'P':
            verjetnost1 += 0.05
        else:
            return None
    for _ in kraj:
        if kraj == 'domač':
            verjetnost1 * 1
        elif kraj == 'gost':
            verjetnost1 * 0.75
    if verjetnost1 < 0.5:
        return ekipa, verjetnost1, 'poraz ali remi'
    else:
        return ekipa, verjetnost1, 'zmaga'
     
        
def seznam_stav(izhodna_datoteka, ekipa, rezultati, kraj):
    '''V verjetnost vpišemo, kar nam vrne funkcija verjetnost, izhodna datoteka pa je datoteka, v katero bomo slikali'''
    with open (izhodna_datoteka, 'a') as dat:
        print(verjetnost(ekipa, rezultati, kraj), file = dat)

def slovar_stav(vhodna_datoteka, izhodna_datoteka):
    '''Vrne slovar stav'''
    SlovarStav = {}
    with open (vhodna_datoteka) as dat2:
        with open (izhodna_datoteka, 'a') as dat3:
            for vrstica in dat2:
                SlovarStav[vrstica[1]] = SlovarStav[vrstica[0][2]]
        print(SlovarStav, file = 'dat3')
                
        
def uredi_po_vrednostih(slovar):
    pari_vrednost_kljuc = []
    for kljuc, vrednost in slovar.items():
        pari_vrednost_kljuc.append((-vrednost, kljuc))
    urejeno_po_vrednostih = []
    for vrednost, kljuc in sorted(pari_vrednost_kljuc):
        urejeno_po_vrednostih.append((kljuc, -vrednost))
    return urejeno_po_vrednostih

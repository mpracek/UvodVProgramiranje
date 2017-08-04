"Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32"
import os


def verjetnost(ekipa, rezultati, kraj):
    '''Pove nam približno verjetnost, s katero bo prišlo do zmage, remija oziroma poraza glede na prejšnje rezultate ekipe.
    V rezultat vpišemo niz Z, P, R, kjer je Z zmaga, P poraz in R remi.
    V kraj vpišemo niz domač ali gost.'''
    if len(rezultati) != 5:
        return None
    else: 
        verjetnost1 = 0
        for rezultat in rezultati:
            if rezultat == 'Z':
                verjetnost1 += 0.19
            elif rezultat == 'R':
                verjetnost1 += 0.1
            elif rezultat == 'P':
                verjetnost1 += 0.05
            else:
                verjetnost1 = verjetnost1
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
    '''V izhodno datoteko zapišemo, verjetost nekega dogodka.'''
    with open (izhodna_datoteka, 'a') as dat:
        print(verjetnost(ekipa, rezultati, kraj), file = dat)        


def slovar_stav(vhodna_datoteka, izhodna_datoteka):
    '''Verjetnosti uredi v slovar.
>>> verjetnost('Hiša', 'PPRZZ', 'domač')
('Hiša', 0.5800000000000001, 'zmaga')
    slovar = {0.5800000000000001 :'Hiša', 'zmaga'}'''

    SlovarStav = {}
    with open (vhodna_datoteka) as dat2:
        with open (izhodna_datoteka, 'a') as dat3:
            for vrstica in dat2:
                SlovarStav[vrstica[1]] = SlovarStav[vrstica[0][2]]
        print(SlovarStav, file = dat3)
                
def skupna_stava(vhodna_datoteka):
    '''Pokaže nam verjetnost, da se zgodijo vsi dogodki'''
    with open(vhodna_datoteka) as vhod:
        verjetnost_celote = 1
        for vrstica in vhod:
            razdelitev = vrstica.split(',')
            verjetnost_celote = verjetnost_celote * float(razdelitev[1])
    return verjetnost_celote

def celota(vhodna_datoteka):
    with open(vhodna_datoteka, 'a') as vhod:
       print(skupna_stava(vhodna_datoteka), file = vhod)

def izbris(vhodna_datoteka):
    os.remove(vhodna_datoteka)

def poraz():
    return  'P'

def remi():
    return  'R'

def zmaga():
    return 'Z'


    
          
            
        

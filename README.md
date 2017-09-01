# Mali stavni pomočnik

## Uvod v programiranje, projektna naloga

Verjetnost dogodka je program, ki nam da *približno* verjetnost dogodkov v športu.

### Navodila za uporabo

Program glede na zadnjih 5 rezultatov in to, kje ekipa igra naslednjo tekmo predvidi mogoč razplet naslednje tekme/ dvoboja.

Verjetnost nad 0.75 nam pove verjetno zmago, manjša pa nam napove verjeten poraz ali remi.
V vmesniku *zapišemo* ime tekmovalca ali ekipe, *izberemo* njihovih zadnjih 5 *rezultatov* ter *kje bo tekmovalec ali ekipa odigral naslednjo tekmo*, doma ali v gosteh. Za posamične športe, kot je tenis, kjer imamo večinoma turnirski način igre, vedno izberemo igra doma. 
Ko dokončamo svojo izbiro kliknemo *dodaj*.
Preden lahko vpišemo nov dogodek, kliknemo na *nov dogodek*.
Nadaljujemo z vnašanjem dokler želimo, nato kliknemo *izpiši*.
Na koncu še *izbrišemo* preostale rezultate.

### Pogoste napake
Najbolj pogosta napaka, ki se nam lahko zgodi, je da ne izberemo zadnjih 5 rezultatov oziroma kje klub igra.
Napake, ki nam lahko delajo več problemov so povezane z gumbi *Dodaj*, *Nov dogodek*, ter *izpiši*.
Če po tem, ko izberemo *Dodaj* ne izberemo še *Nov dogodek*, bo naša verjetnost lahko presegla 1, kar je matematično nemogoče.
Problem nam lahko dela tudi gumb *Izpiši*. Če ga izberemo dvakrat zapovrstjo, nam bo vrgel napako, saj nam gumb *Izpiši* verjetnost, da se zgodijo vsi dogodki, ki smo jih predvideli hkrati zapiše v isto datoteko kot ostale rezultate, zapis pa je druge oblike kot zapis dogodkov.

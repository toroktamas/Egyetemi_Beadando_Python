#!/usr/bin/pyhon3
# -*- coding:utf-8 -*-


"""
Egy sor egy sora a konyvtarnak.
novenyek{
     1:["Rozsa","Nagy",2,2017.11.10,true]
}
"""

from datetime import datetime , timedelta

lista_neve = str(input("Kerem adja meg a fajl nevet: "))
n = 0
novenyek = {}
with open(lista_neve, "rt+",encoding="utf-8") as f:
     for s in f:
          sor = s.replace("\n","").split(";")
          novenyek[n] = sor
          n+=1
          
"""
Meg kell tudni valtoztatni a konyvtarat.
Meg kell vizsgalni hogy mikor kell locsolni es kiirni amit most kell.
"""

"""
Locsolas ellenorzo.
"""
ma = datetime.today()
for a in novenyek.values():
     nap = a[3].replace(" ", "").split(".")
     valtozonap = datetime(year=int(nap[0]), month=int(nap[1]), day=int(nap[2]), hour=0, minute=0, second=0,microsecond=0)
     datum = timedelta(valtozonap.day-ma.day)
     if ( int(datum.days) >= int(a[2])):
          print("Meg kell locsoloni a {0}t".format(a[0]))
          a[3] = str("{0}. {1}. {2}.".format(ma.year, ma.month, ma.day))
          if a[4] == "true":
               print("\033[0;31;48m Csak vedokesztyuben kozelitsd meg! \n")
               print("\033[0;37;48m")

"""
Kiiratom szepen a novenyeket ami a listaban van.
"""

for k,j in novenyek.items():
     print("{0}. Noveny neve: {1} fenyigeny: {2}, vizigeny: {3}, utolso locsolas: {4}, szuros: {5}".format(k+1 ,j[0] ,j[1] ,j[2] ,j[3] ,j[4]))

hozzaad = str(input("Szeretne hozzaadni a konyvtarhoz uj novenyt? (igen/nem) "))
valtoztat = str(input("Szeretne megvaltoztatni a jelenlegi novenyek listajat? (igen/nem) "))
for j,k in novenyek.items():
     if valtoztat == "igen":
          valtoztat_sor  = int(input("Hanyadik sort szeretne megvaltoztatni? (Kerem szanot irjon be.) "))
          if valtoztat_sor-1 == j:
               valtoztat_mit = str(input("Mit szeretne megvaltoztatni vagy torolni. (Noveny neve, fenyigeny, vizigeny, utolso locsolas, szure) ")) 
               if valtoztat_mit == "Noveny neve":
                    val = str(input("Torli vagy valtoztatja? (torol/valtoztat) "))
                    if val == "valtoztat":
                         valtozik = str(input("Kerem irja be az uj adatot: "))
                         j[0] = valtozik
                    if val == "torol":
                         valtozik = " "
               if valtoztat_mit == "fenyigeny":
                    val = str(input("Torli vagy valtoztatja? (torol/valtoztat) "))
                    if val == "valtoztat":
                         valtozik = str(input("Kerem irja be az uj adatot: "))
                         j[1] = valtozik
                    if val == "torol":
                         valtozik = " "
               if valtoztat_mit == "vizigeny":
                    val = str(input("Torli vagy valtoztatja? (torol/valtoztat) "))
                    if val == "valtoztat":
                         valtozik = str(input("Kerem irja be az uj adatot: "))
                         j[2] = valtozik
                    if val == "torol":
                         valtozik = " "
                         
               if valtoztat_mit == "utolso locsolas":
                    val = str(input("Torli vagy valtoztatja? (torol/valtoztat) "))
                    if val == "valtoztat":
                         valtozik = str(input("Kerem irja be az uj adatot: "))
                         j[3] = valtozik
                    if val == "torol":
                         valtozik = " "
               if valtoztat_mit == "szure":
                    val = str(input("Torli vagy valtoztatja? (torol/valtoztat) "))
                    if val == "valtoztat":
                         valtozik = str(input("Kerem irja be az uj adatot: "))
                         j[4] = valtozik
                    if val == "torol":
                         valtozik = " "
uj_novenyek = {}
szam = 0
if hozzaad == "igen":
     novenynev = str(input("Kerem adja meg a noveny nevet: "))
     fenyigeny = str(input("Kerem adja meg a fenyigenyt: "))
     vizigeny = str(input("Kerem adja meg hogy hany naponta kell locsolni: "))
     utosolocsolas = str(input("Kerem adja meg az utolso locsolas datumat (ev.honap.nap): "))
     szure = str(input("Kerem adja meg hogy szur-e (true/false): "))
     for i,m in novenyek.items():
          if i == szam:
               uj_novenyek[szam] = m
               szam+=1
          else:
               uj_novenyek[szam] = [novenynev,vizigeny,fenyigeny,utosolocsolas,szure]
     sa = 0
     with open(lista_neve,"wt+", encoding="utf-8") as f:
          for a in uj_novenyek.values():
               for k in a:
                    if k != " " and sa <= 5:
                         f.write("{0};".format(k))
               f.write("\n")
               sa = 0

"""
Fajl kiirasa fajlba ugyanabba amibe beolvastam.
"""
sa = 0
with open(lista_neve,"wt+", encoding="utf-8") as f:
     for a in novenyek.values():
          for k in a:
               if ((k != " ") and (sa <= 5)):
                    sa +=1
                    f.write("{0};".format(k))
          f.write("\n")
          sa = 0


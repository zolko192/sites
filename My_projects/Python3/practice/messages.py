#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

""" Készíts egy új SMS_tarolo osztályt! Az osztály olyan objektumokat példányosít majd, amelyek hasonlítanak
a telefonon lévő bejövő / kimenő üzenet tárolókra:
bejovo_uzenetek = SMS_tarolo()
Ez a tároló több SMS üzenetet tárol (tehát a belső állapota az üzenetek listája lesz). Minden üzenetet egy
rendezett 4-es reprezentáljon:
(olvasott_e, kuldo_szama, erkezesi_ido, SMS_szovege)
A bejövő üzenetek tárolójának az alábbi metódusokat kell biztosítania:
bejovo_uzenetek.beerkezo_uzenet_hozzaadasa(kuldo_szama, erkezesi_ido, SMS_szovege)
# Készít egy új rendezett 4-est az SMS számára,
# és beszúrja őket a tárolóba a többi üzenet után.
# Az üzenet készítésénél az olvasott_e állapotát
#
hamisra (False) állítja.
bejovo_uzenetek.uzenetek_szama()
# Visszatér a bejovo_uzenetek tárolóban lévő SMS-ek számával
bejovo_uzenetek.olvasatlan_uzenetek_indexeinek_lekerese()
# Visszatér az összes olvasatlan SMS indexét tartalmazó listával.
bejovo_uzenetek.uzenet_lekerese(i)
# Visszatér az uzenet[i]-hez tartozó (kuldo_szama, erkezesi_ido, SMS_szovege) 4-
˓ → essel.
# Az üzenet státuszát olvasottra állítja.
# Ha nincs üzenet az i. indexen, akkor a visszatérési érték None.
bejovo_uzenetek.torol(i)
# Kitörli az i. pozícióban álló üzenetet.
bejovo_uzenetek.mindent_torol()
# Kitörli az összes üzenetet a bejövő SMS-ek
˓ → tárolójából.
Írd meg az osztályt, készíts egy SMS tároló objektumot, írj teszteket a metódusokhoz és implementáld őket! """

class Messages(object):
	
	def __init__(self):
		print("Készülőben!");

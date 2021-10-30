#!/usr/bin/python3

oraber = 1195
napi = 8
delelott_heti = 5
delutan_heti = 6
ora_potlek = 4
tappenz = ((oraber / 100) * 70) * 40
muszakpotlek = ((oraber / 100) * 60) * ora_potlek
delelott = (napi * oraber) * delelott_heti
delutan = ((napi * oraber) + muszakpotlek) * delutan_heti
brutto = (delelott + delutan) + tappenz
netto = brutto - (brutto / 100) * 33
print (" A Bruttó fizetése: {0} Ft \n A Nettó fizetése: {1} Ft".format(brutto, netto))

import xml.etree.ElementTree as ET
from _elementtree import Element
from typing import Union
from xml.etree.ElementTree import Element


class Pracownik:
    def __init__(self, imie, nazwisko, stanowisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stanowisko = stanowisko
        self.pensja = pensja

class Firma:
    def __init__(self):
        self.lista = []
    def zatrudnij(self, pracownik):
        self.lista.append(pracownik)
    def zwolnij(self, pracownik):
        self.lista.remove(pracownik)
    def listapracownikow(self):
        res = []
        for x in self.lista:
            res.append({'imie' : x.imie, 'nazwisko' : x.nazwisko, 'stanowisko' : x.stanowisko, 'pensja' : x.pensja})
        return res


adam = Pracownik('Adam', 'Kowalski', 'kierownik', "2000")
karol = Pracownik('Karol', 'Iksinski', 'Wyrobnik ciasteczek', "300")

korporacja_ciastkarska = Firma()

korporacja_ciastkarska.zatrudnij(adam)
korporacja_ciastkarska.zatrudnij(karol)

print(korporacja_ciastkarska.listapracownikow())

korporacja_ciastkarska.zwolnij(adam)
print(korporacja_ciastkarska.listapracownikow())

element = ET.Element('pracownicy')
pracownik1 = ET.SubElement(element, 'adam', {"imie" : adam.imie, "nazwisko": adam.nazwisko, "stanowisko": adam.stanowisko, "pensja": adam.pensja} )
pracownik2 = ET.SubElement(element, 'karol', {"imie" : karol.imie, "nazwisko": karol.nazwisko, "stanowisko": karol.stanowisko, "pensja": karol.pensja})

tree = ET.ElementTree(element)
tree.write("pracownicy.xml")

zpliku = ET.parse("pracownicy.xml")
root = zpliku.getroot()


print("Dane odczytane z XML")
for x in root:
    print(x.attrib['imie'], x.attrib['nazwisko'])

from threading import *
import sys
import random

# Klasse fuer das Verschuesseln
class VersThr (Thread):

    def __init__(self,unver):
        Thread.__init__(self)
        self.unver = unver
        self.ver = ""

    def run(self):
        for character in self.unver:
            index1 = clear.index(character)
            self.ver = self.ver + unclear[index1]


#Klasse fuer das Entverschuesseln

class EntVersThr (Thread):

    def __init__(self,ver):
        Thread.__init__(self)
        self.ver = ver
        self.unver = ""

    def run(self):
        for character in self.ver:
            index1 = unclear.index(character)
            self.unver = self.unver + clear[index1]


class verstartup(object):

    def __init__(self):
        self.eingabe = raw_input("Geben Sie den zu verschluesselnden Satz ein \n")
        self.anzahl = raw_input("Geben Sie ein, wie viele Thread an der Verschluesselung arbeiten sollen \n")
        self.eingabe = self.eingabe.upper()
        print self.eingabe


    def startver(self):
        self.mythreads = []
        self.position = 0
        self.qoute = float(len(self.eingabe)) / float(self.anzahl)
        self.verschu = ""
        for x in range(0,int(self.anzahl)):
            part = self.eingabe[int(self.position):int(self.position+self.qoute)]
            self.position += float(self.qoute)
            if len(part) != 0:
                thread = ""
                thread = VersThr(part)
                thread.start()
                self.mythreads.append(thread)
        for thread in self.mythreads:
            self.verschu = self.verschu + thread.ver
            thread.join()

        print "Fertig Verschuesselt: " + self.verschu


class entverstartup(object):
    def __init__(self):
        self.eingabe = raw_input("Geben Sie den zu entschluesselnden Zeichenfolge ein \n")
        self.anzahl = raw_input("Geben Sie ein, wie viele Thread an der Entschluesselung arbeiten sollen \n")
        self.eingabe = self.eingabe.upper()
        print self.eingabe

    def startunver(self):
        self.mythreads = []
        self.position = 0
        self.qoute = float(len(self.eingabe)) / float(self.anzahl)
        self.unverschu = ""
        for x in range(0, int(self.anzahl)):
            part = self.eingabe[int(self.position):int(self.position + self.qoute)]
            self.position += float(self.qoute)
            if len(part) != 0:
                thread = ""
                thread = EntVersThr(part)
                thread.start()
                self.mythreads.append(thread)
        for thread in self.mythreads:
            self.unverschu = self.unverschu + thread.unver
            thread.join()

        print "Fertig Entschuesselt: " + self.unverschu

#Definition der Verschlueselungs Listen

clear = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
        ,"!","$","%","&","/","(",")","=","?","}","]","[","{","^","@",":",",",";","_","-","<",">","|","#","'","+","*","~","-"
        ,"0","1","2","3","4","5","6","7","8","9","0"," "]
unclear = []

# Erstellen einer Zufallszahl und eine Verschiebungsliste anhand der Zufallszahl

inde = 0
randzahl = random.randint(1,50)
for x in range(0,len(clear)):
    inde += 1
    if inde+randzahl == len(clear):
        inde = randzahl * -1

    unclear.append(clear[inde+randzahl])
print randzahl
print clear
print unclear


#Main Methode Haupt-Loop

while True :
    print ""
    ein = raw_input("Geben Sie ein was Sie machen wollen \n1 => Verschluesseln  2 => Entschluesseln  3 => Exit \n")

    try:
        ein = int(ein)
    except ValueError:
        ein = 0

    if ein == 1:
        verstarting = verstartup()
        verstarting.startver()
    elif ein == 2:
        entverstarting = entverstartup()
        entverstarting.startunver()
    elif ein == 3:
        sys.exit(0)
    else:
        print "Unbekannter Befehl"
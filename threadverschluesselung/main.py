from threading import *
import sys
import random

class VersThr (Thread):

    """
    Diese Klasse steht einen Thread her,
    der einen String verschluesselt

    :ivar String unver:    String, in dem der unverschuesselte Text steht
    :ivar String ver:      String, in dem der verschuesselte Text steht
    :ivar int index1:      Int, der den Zielindex darstellt
    :param String unver:   String, in dem der unverschuesselte Text steht

    """

    def __init__(self,unver):
        """
        Initialisiert die Superklasse,speichert den Parameter in die Instanzvariable
        und erstellt eine weitere Instanzvariable.

        :param ver:     String, in dem der verschuesselte Text steht
        """
        Thread.__init__(self)
        self.unver = unver
        self.ver = ""

    def run(self):
        """
        Nimmt jeden Character aus dem Text und speichert den verschluesselten Character dazu

        :return: None
        """
        for character in self.unver:
            index1 = clear.index(character)
            self.ver = self.ver + unclear[index1]


class EntVersThr (Thread):

    """
    Diese Klasse steht einen Thread her,
    der einen String entschluesselt

    :ivar String unver:    String, in dem der unverschuesselte Text steht
    :ivar String ver:      String, in dem der verschuesselte Text steht
    :ivar int index1:      Int, der den Zielindex darstellt
    :param String ver:     String, in dem der verschuesselte Text steht

    """

    def __init__(self,ver):
        """
        Initialisiert die Superklasse,speichert den Parameter in die Instanzvariable
        und erstellt eine weitere Instanzvariable.

        :param ver:     String, in dem der verschuesselte Text steht
        """
        Thread.__init__(self)
        self.ver = ver
        self.unver = ""

    def run(self):
        """
        Nimmt jeden Character aus dem Text und speichert den unverschluesselten Character dazu

        :return: None
        """
        for character in self.ver:
            index1 = unclear.index(character)
            self.unver = self.unver + clear[index1]


class verstartup(object):
    """
    Diese Klasse berechnet alle wichtigen Wert, um den Text in gleichgrosse Teile aufzuteilen,
    damit alle Threads gleichmaessig ausgelastet sind,
    fragt alle Eingabe des Benutzers ab,
    startet die Threads mit entsprechenden Parametern,
    schliesst alle Threads und gibt den verschuesselten Text aus

    :ivar String eingabe:   String, in dem die Benutzereingabe steht
    :ivar int anzahl:       Int, in dem steht, wie viele Threads erstellt werden soll
    :ivar List mythreads:   Liste, in dem die erstellen Threads gespeichert werden
    :ivar int position:    Int, in dem steht, wie weit der zu verschuesselnde Text schon verteilt wurde
    :ivar Float qoute:      Float, in dem steht, wie viele Character jeder Thread bekommen muss
    :ivar String verschu:   String, in dem der fertig verschuesselte Text steht
    :ivar String part:      String, in dem steht, welche Character der naechste Thread bekommt

    """
    def __init__(self):

        """
        Erstellt einige Instanzvariablen, fragt den Benutzer ueber den Text ab,
        die Anzahl der Threads und schreibt die Eingabe auf Grossbuchstaben um

        """

        self.eingabe = raw_input("Geben Sie den zu verschluesselnden Satz ein \n")
        self.anzahl = raw_input("Geben Sie ein, wie viele Thread an der Verschluesselung arbeiten sollen \n")
        self.eingabe = self.eingabe.upper()
        self.verschu = ""
        self.mythreads = []
        self.position = 0


    def startver(self):

        """
        Errechnet die Qoute fuer jeden Thread,
        erstellt den Thread spezifischen Text, startet einen Thread mit diesem Text,
        speichert die Thread ab, wartet bis alle Threads fertig sind,
        speichert das Ergebnis von jedem Thread ab und gibt das Ergebnis aus

        :return: None
        """
        self.qoute = float(len(self.eingabe)) / float(self.anzahl)
        for x in range(0,int(self.anzahl)):
            part = self.eingabe[int(self.position):int(self.position+self.qoute)]
            self.position += float(self.qoute)
            if len(part) != 0:
                thread = VersThr(part)
                thread.start()
                self.mythreads.append(thread)
        for thread in self.mythreads:
            self.verschu = self.verschu + thread.ver
            thread.join()

        print "Fertig Verschuesselt: " + self.verschu


class entverstartup(object):
    """
        Diese Klasse berechnet alle wichtigen Wert, um den Text in gleichgrosse Teile aufzuteilen,
        damit alle Threads gleichmaessig ausgelastet sind,
        fragt alle Eingabe des Benutzers ab,
        startet die Threads mit entsprechenden Parametern,
        schliesst alle Threads und gibt den entschuesselten Text aus

        :ivar String eingabe:   String, in dem die Benutzereingabe steht
        :ivar int anzahl:       Int, in dem steht, wie viele Threads erstellt werden soll
        :ivar List mythreads:   Liste, in dem die erstellen Threads gespeichert werden
        :ivar int position:    Int, in dem steht, wie weit der zu entschuesselnde Text schon verteilt wurde
        :ivar Float qoute:      Float, in dem steht, wie viele Character jeder Thread bekommen muss
        :ivar String unverschu:   String, in dem der fertig entschuesselte Text steht
        :ivar String part:      String, in dem steht, welche Character der naechste Thread bekommt

        """

    def __init__(self):

        """
        Erstellt einige Instanzvariablen, fragt den Benutzer ueber den Text ab,
        die Anzahl der Threads und schreibt die Eingabe auf Grossbuchstaben um

        """

        self.eingabe = raw_input("Geben Sie den zu entschluesselnden Zeichenfolge ein \n")
        self.anzahl = raw_input("Geben Sie ein, wie viele Thread an der Entschluesselung arbeiten sollen \n")
        self.eingabe = self.eingabe.upper()
        self.mythreads = []
        self.position = 0
        self.unverschu = ""


    def startunver(self):

        """
        Errechnet die Qoute fuer jeden Thread,
        erstellt den Thread spezifischen Text, startet einen Thread mit diesem Text,
        speichert die Thread ab, wartet bis alle Threads fertig sind,
        speichert das Ergebnis von jedem Thread ab und gibt das Ergebnis aus

        :return: None
        """
        self.qoute = float(len(self.eingabe)) / float(self.anzahl)
        for x in range(0, int(self.anzahl)):
            part = self.eingabe[int(self.position):int(self.position + self.qoute)]
            self.position += float(self.qoute)
            if len(part) != 0:
                thread = EntVersThr(part)
                thread.start()
                self.mythreads.append(thread)
        for thread in self.mythreads:
            self.unverschu = self.unverschu + thread.unver
            thread.join()

        print "Fertig Entschuesselt: " + self.unverschu

#Definition der klaren Liste

clear = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
        ,"!","$","%","&","/","(",")","=","?","}","]","[","{","^","@",":",",",";","_","-","<",">","|","#","'","+","*","~","-"
        ,"0","1","2","3","4","5","6","7","8","9","0"," "]
unclear = []

# Erstellen einer Zufallszahl und Definition der Verschuesselungs-Liste anhand der Zufallszahl

def createversch (randzahl):
    inde = 0
    for x in range(0,len(clear)):
        inde += 1
        if inde+randzahl == len(clear):
            inde = randzahl * -1

        unclear.append(clear[inde+randzahl])

#   Debug Information
#print randzahl
#print clear
#print unclear


# "Main Methode" Haupt-Loop

createversch(random.randint(1,50))
print len(unclear)
while True :
    ein = raw_input("Geben Sie ein was Sie machen wollen \n1 => Verschluesseln  2 => Entschluesseln  3 => Setzen der Verschiebungszahl und Neuberechnung der Verschluesselung 4=> Exit \n")

    try:
        ein = int(ein)
    except ValueError:
        ein = 0

    if ein == 1:
        verstart = verstartup()
        verstart.startver()
    elif ein == 2:
        entverstart = entverstartup()
        entverstart.startunver()
    elif ein == 3:
        zahl = raw_input("Geben Sie die Verschiebungszahl ein, die zwischen 0 und %d liegt \n" % int(len(unclear)-2))

        try:
            zahl = int(zahl)
            unclear = []
            createversch(zahl)
            print "Verschuesselung neu generiert."
        except ValueError:
            print "Das war keine Zahl. Versuchen Sie es nochmal mit einer Zahl."

    elif ein == 4:
        sys.exit(0)
    else:
        print "Unbekannter Befehl"
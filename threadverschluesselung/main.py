from threading import *
import sys

class VersThr (Thread):
    unver = ""
    ver = ""
    def __init__(self,unver):
        Thread.__init__(self)
        self.unver = unver

    def run(self):
        print "'" + str(self.unver) + "'\n"
        self.ver = self.ver + self.unver


#

class startup(object):
    eingabe = ""
    ausgabe = ""
    anzahl = 0
    mythreads = []

    def __init__(self):
        self.eingabe = raw_input("Geben Sie das zu verschluesselnde Wort ein \n")
        #print self.eingabe
        self.anzahl = raw_input("Geben Sie ein, wie viele Thread an der Verschluesselung arbeiten sollen \n")
        #print self.anzahl

    def startver(self):
        position = 0
        qoute = float(len(self.eingabe)) / float(self.anzahl)
        for x in range(0,int(self.anzahl)):
            part = self.eingabe[int(position):int(position+qoute)]
            position += float(qoute)
            if len(part) != 0:
                thread = ""
                thread = VersThr(part)
                thread.start()
                self.mythreads.append(thread)
        #print self.mythreads
        for thread in self.mythreads:
            print thread.unver
            thread.join()


"""

thread = VersThr("ghg")
thread.start()
print "Bla: " + str(thread)

"""

#Main Methode Haupt-Loop

while True :
    print "Geben Sie ein was Sie machen wollen"
    ein = raw_input("1 => Verschluesseln  2 => Entschluesseln  3 => Exit \n")

    try:
        ein = int(ein)
    except ValueError:
        ein = 0

    if ein == 1:
        starting = startup()
        starting.startver()
    elif ein == 2:
        print "Placeholder"
    elif ein == 3:
        sys.exit(0)
    else:
        print "Unbekannter Befehl"
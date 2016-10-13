from threading import *

class startup(object):
    eingabe = ""
    anzahl = 0
    threads = []

    def __init__(self):
        self.eingabe = raw_input("Geben Sie das zu verschluesselnde Wort ein \n")
        #print self.eingabe
        self.anzahl = raw_input("Geben Sie ein, wie viele Thread an der Verschluesselung arbeiten sollen \n")
        #print self.anzahl

    def startver(self):
        teil = []
        for i in range(0,int(self.anzahl)):
            #part = eingabe[]
        qoute = len(self.eingabe) / int(self.anzahl)
        print "Qoute: "+ str(qoute)
        for x in range(0,int(self.anzahl)):
            thread = VerschluesselungThr(self.eingabe).start()
            self.threads += [thread]



class VerschluesselungThr (Thread):
    unver = ""
    ver = ""
    def __init__(self,unver):
        Thread.__init__(self)
        self.unver = unver
        print "bla: " + str(self.unver)


    def run(self):
        pass


starting = startup()
starting.startver()
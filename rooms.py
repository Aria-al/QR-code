import QR_unit

class Rooms:
    def __init__( self ):
        self.dictDesc = dict()

        
    def loadFromDisk( self, strFilename = "rooms.txt"):
        f = open(strFilename)
        while 1:
            line = f.readline()
            if line == "":
                break
            print("DBG: Rooms.loadFromDisk: line: '%s'" % line )
            strName = "203" # TODO
            strDesc = "desc de la salle TODO" # TODO
            self.dictDesc[strName]=strDesc
            
        f.close()
        
        
    def getDesc( self, strName ):
        try:
            return self.dictDesc[strName]
        except BaseException as err:
            print( "WRN: Rooms.getDesc: err: %s" % err)
        return 
    

    def Dic (self, strFilename = "rooms.txt") :
        salle = {}
        a = open("rooms.txt")
        while 1:
            line = a.readline()
            if line == "" :
                break
            strKey, strValue = line.split(";")
            self.dictDesc[strKey] = strValue
            salle.update({strKey:strValue})
        a.close()
        return (salle)

      
# class Rooms - end

rooms = Rooms()
rooms.Dic()

def makeQR () :
    QR_unit.QR_treatment.create(203)
    
def auto_test():
    name = "203"
    print("salle %s => %s" % (name, rooms.getDesc(name) ) )

if __name__ == "__main__":
    auto_test()

def Creation ():
    a = open("rooms.txt")
    while 1 :
        line = a.readline()
        if line == "":
            break
        key, tobedump = line.split(";")
        QR_unit.QR_treatment.create(key)
    a.close()


# Will help to automate the production of all the QR codes


def referencer_2 ():
    rooms.Dic()
    datafromQR = QR_unit.QR_treatment.read()
    key = rooms.getDesc(datafromQR)
    print (key)


# Helps to link the key in the QR code to one of the value in the text document


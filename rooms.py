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

    def Dic ( strFilename = "rooms.txt" ):
        l = open("rooms.txt")
        room = {}
        while 1 :
            issue = l.readline()
            if issue == "":
                break
            strKey, strValue = issue.split ( ";" ) 
            strKey = str( str( strKey ))
            strValue = str( str( strValue ))
            room.update( { strKey : strValue })
        return room

      
# class Rooms - end

rooms = Rooms()
rooms.loadFromDisk()

def makeQR () :
    QR_unit.QR_treatment.create(203)
    
def auto_test():
    name = "203"
    print("salle %s => %s" % (name, rooms.getDesc(name) ) )

if __name__ != "__main__":
    auto_test()

def Creation (key):
    pass

# Will help to automate the production of all the QR codes


def referencer ():
    room = Rooms.Dic()
    datafromQR = QR_unit.QR_treatment.read()
    print ( room.get( datafromQR))

# Helps to link the key in the QR code to one of the value in the text document


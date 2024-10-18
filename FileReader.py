import threading
import time

class FileReader:
    filename : str
    Creatures : list

    def __init__(self,filename):
        self.filename = filename
        self.running = True
        self.readData()
        t = threading.Thread(target=self.ThreadFunction)
        t.start()

    def readData(self):
        """This function needs to Gather and update the creatures."""
        with open(self.filename) as f:
            lines = f.readlines()
        res = ""
        for line in lines:
            res +=line
        creatureData = res.split("# ")
        #print(creatureData)
        self.Creatures = []
        for entry in creatureData:
            if (entry !=""):
                name = entry.split(" (")[0]
                maxHp = int(entry.split(" (")[1].split(")")[0])
                currentHp = maxHp - entryHealthSearch(entry)
                # Make the Creatures
                self.Creatures.append(Creature(name,maxHp,currentHp))

    def getCreatures(self):
        return self.Creatures

    def ThreadFunction(self):
        while(self.running):
            self.readData()
            time.sleep(.1)

    def stop(self):    
        self.running = False

def entryHealthSearch(entry : str):
    lst = entry.split("\n")[1:]
    curr : int = 0
    for line in lst:
        if line != "":
            curr = int(line)
        else:
            break
    return curr


class Creature:
    """Represents a dnd creature"""
    name : str
    hp : int
    max_hp : int

    def __init__(self,name : str,max_hp : int,hp : int):
        self.hp = hp
        self.max_hp = max_hp
        self.name = name

    def getHpPercent(self):
        return self.hp / self.max_hp

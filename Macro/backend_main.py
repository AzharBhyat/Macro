import keyboard
import pickle


dataFp = "keydata.json"
savesFp = "./Saves/"

global currentState

def recordKeys():
    recordedData = keyboard.record(until='esc')
    with open(dataFp, 'wb') as file:
        pickle.dump(recordedData, file)
    return

def playKeys(saveFile):
    with open(saveFile, "rb" )as file:
        data = pickle.load(file)
        keyboard.play(data)
    return


def _main(mode): 
    if(mode == "record"):
        print("Recording")
        recordKeys()

def Play(file):
    playKeys(file)
    return

def Save(fileName):
    saveFile = open(savesFp+fileName+".json", "wb")
    pickle.dump(pickle.load(open(dataFp, "rb")), saveFile)

    saveFile.close()
    return

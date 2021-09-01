import pyautogui as gui
import time
import json

def keypress(gui,code):
    gui.keyDown(code)
    gui.keyUp(code)

print("Opening Zoom")
#To open ZOOM
gui.keyDown("winleft")
gui.keyUp("winleft")
time.sleep(5)
gui.write("zoom")
gui.keyDown("\n")
gui.keyUp("\n")
time.sleep(10)
print("Done")


#Resize zoom
print("Resizing The window ")
gui.keyDown("winleft")
cheat = ["up","up","down","left","up"]
for code in cheat:
    keypress(gui,code)
gui.keyUp("winleft")
time.sleep(2)
print("Done")

print("Clicking Join Meeting")
gui.click(331,254)
time.sleep(3)
print("Done")


# meeting details
print("Loading Data from File")
data = json.load(open('cmeeting.json'))
print("Done")

print("Writing Meeting ID and Name")
gui.write(str(data["M_Id"]))
keypress(gui,"tab")
keypress(gui,"tab")
gui.hotkey("ctrl","a")
keypress(gui,"backspace")
gui.write(str(data["name"]))
keypress(gui,"tab")
keypress(gui,"tab")
while(True):
    try:
        if(not gui.pixelMatchesColor(802,621,(14,114,235),4)):
            keypress(gui,"space")
    except:
        print("retrying tick part")
    else:
        break
keypress(gui,"tab")
keypress(gui,"space")
print("Done")
time.sleep(10)


#now in password screen:
print("Writing Password")
gui.write(data["p"])
keypress(gui,"tab")
keypress(gui,"space")
print("Done")
print("Entered Zoom Meeting")

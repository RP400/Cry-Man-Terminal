# This is now a created import
# Imports
from guizero import App, Text, TextBox, PushButton
from mcpi import minecraft
from time import sleep
# Save's
#        X    Y    Z 
Save1 = 0.5, 0.0, 0.7
#        X    Y    Z 
Save2 = 0.5, 0.0, 0.7
#        X    Y    Z 
Save3 = 0.5, 0.0, 0.7
# Function loop #1
def MagicBearFIP():
    mc = minecraft.Minecraft.create()
    Si = str(input("T-T <(Would you like to go to a saved spot?) (y/n): "))
    if Si in ("y", "n"):
        if Si == "y":
            sleep(0.5)
            ISi = str(input("T-T <(Wich saved spot would you like to go to?): "))
            if ISi == "Save1":
                print("""T-T <(Teleporting...)""")
                sleep(4)
                mc.player.setPos(Save1)
                getp = mc.player.getPos()
                xp1 = round(getp.x, 1)
                yp1 = round(getp.y, 1)
                zp1 = round(getp.z, 1)
                Fullxyz = xp1, yp1, zp1
                sleep(0.5)
                if Fullxyz == Save1:
                    print("T-T <(Teleport Sucessful!)")
                else:
                   print("T-T <(Teleport Unsucessful!) (Type A Valid Coord In Your Save)") 
            elif ISi == "Save2":
                print("""T-T <(Teleporting...)""")
                sleep(4)
                mc.player.setPos(Save2)
                getp2 = mc.player.getPos()
                xp2 = round(getp2.x, 1)
                yp2 = round(getp2.y, 1)
                zp2 = round(getp2.z, 1)
                Fullxyz2 = xp2, yp2, zp2
                sleep(0.5)
                if Fullxyz2 == Save2:
                    print("T-T <(Teleport Sucessful!)")
                else:
                   print("T-T <(Teleport Unsucessful!) (Type A Valid Coord In Your Save)") 
            elif ISi == "Save3":
                print("""T-T <(Teleporting...)""")
                sleep(4)
                mc.player.setPos(Save3)
                getp3 = mc.player.getPos()
                xp3 = round(getp3.x, 1)
                yp3 = round(getp3.y, 1)
                zp3 = round(getp3.z, 1)
                Fullxyz3 = xp3, yp3, zp3
                sleep(0.5)
                if Fullxyz3 == Save3:
                    print("T-T <(Teleport Sucessful!)")
                else:
                   print("T-T <(Teleport Unsucessful!) (Type A Valid Coord In Your Save)") 
            else:
                print("""T-T <(Not a valid save. Please Retry) (/!\ This is case sensitive, remember your caps /!\)""")
        if Si == "n":
            print("T-T <(Some basic spots):\n\t1) Spawn = 0.5, 0.0, 0.7\n\t2) The Sky = 0.5, 100, 0.7")
            while True:
                try:
                    x = float(input("T-T <(Where would you like to go?) (type your X): "))
                    break
                except ValueError:
                    print("T-T <(Oops! That was not a valid coord. Try again...)")
            while True:
                try:
                    y = float(input("T-T <(Where would you like to go?) (type your Y): "))
                    break
                except ValueError:
                    print("T-T <(Oops! That was not a valid coord. Try again...)")
            while True:
                try:
                    z = float(input("T-T <(Where would you like to go?) (type your Z): "))
                    break
                except ValueError:
                    print("T-T <(Oops! That was not a valid coord. Try again...)")     
            xyzf = round(x), round(y), round(z)
            print("""T-T <(Teleporting...)""")
            sleep(4)
            mc.player.setPos(xyzf)
            pos = mc.player.getPos()
            xp = round(pos.x, 1)
            yp = round(pos.y, 1)
            zp = round(pos.z, 1)
            playerpos = xp, yp, zp
            sleep(1)
            if playerpos == xyzf:
                print("""T-T <(Teleport succesful!)""")
            else:
                print("""T-T <(Teleport unsuccesful!)""")
            sleep(1)
    else:
        print("T-T <(That wasnt a valid letter. Please answer with y/n)")
# Function loop #2
def MagicBearFcStart():
    while True:
        while True:
            try:
                x = print("T-T <(Loading...)")
                sleep(1)
                MagicBearFIP()
                break
            except ConnectionRefusedError:
                print("T-T <(Oh! A Minecraft world doesn't seem to be open. Open one and try again)")
                i2 = input("T-T <(Retry ?) (y/n): ")
                if i2 in ("y", "n"):
                    if i2 == "y":
                        print(""" """)
                    if i2 == "n":
                        print("T-T <(Goodbye!)")
                        sleep(1)
                        quit()
        o = input("""T-T <(Again?) (y/n): """)
        if o in ("y", "n"):
            if o == "n":
                print("""T-T <(Goodbye!)""")
                sleep(1)
                break
            if o == "n":
                print("""T-T <(Going again...)""")
                sleep(1)
 # Merged function loop #1
MagicBearFcStart()
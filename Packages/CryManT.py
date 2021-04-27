# Imports
from mcpi import minecraft
from time import sleep
# Save's
#       X in here   Y in here    Z in here
Save1 = round(0.5), round(0.0), round(0.7)
#       X in here   Y in here    Z in here
Save2 = round(0.5), round(0.0), round(0.7)
#       X in here   Y in here    Z in here
Save3 = round(0.5), round(0.0), round(0.7)
# Function loop #1
def MagicBearFIP():
    mc = minecraft.Minecraft.create()
    Si = str(input("T-T <(Would you like to go to a saved spot?) (y/n): "))
    if Si == "y":
        sleep(0.5)
        ISi = str(input("T-T <(Wich saved spot would you like to go to?): "))
        if ISi == "Save1":
            print("""T-T <(Teleporting...)""")
            sleep(4)
            posS = mc.player.setPos(Save1)
            getp = mc.player.getPos()
            xp1 = int(float(getp.x))
            yp1 = int(float(getp.y))
            zp1 = int(float(getp.z))
            Fullxyz = round(xp1), round(yp1), round(zp1)
            sleep(0.5)
            if Fullxyz == Save1:
                print("T-T <(Teleport Sucessful!)")
            else:
               print("T-T <(Teleport Unsucessful!) (Type A Valid Coord In Your Save)") 
        elif ISi == "Save2":
            print("""T-T <(Teleporting...)""")
            sleep(4)
            posS = mc.player.setPos(Save2)
            getp2 = mc.player.getPos()
            xp2 = int(float(getp2.x))
            yp2 = int(float(getp2.y))
            zp2 = int(float(getp2.z))
            Fullxyz2 = round(xp2), round(yp2), round(zp2)
            sleep(0.5)
            if Fullxyz2 == Save2:
                print("T-T <(Teleport Sucessful!)")
            else:
               print("T-T <(Teleport Unsucessful!) (Type A Valid Coord In Your Save)") 
        elif ISi == "Save3":
            print("""T-T <(Teleporting...)""")
            sleep(4)
            posS = mc.player.setPos(Save3)
            getp3 = mc.player.getPos()
            xp3 = int(float(getp3.x))
            yp3 = int(float(getp3.y))
            zp3 = int(float(getp3.z))
            Fullxyz3 = round(xp3), round(yp3), round(zp3)
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
        sp = mc.player.setPos(xyzf)
        pos = mc.player.getPos()
        xp = int(float(pos.x))
        yp = int(float(pos.y))
        zp = int(float(pos.z))
        playerpos = round(xp), round(yp), round(zp)
        sleep(1)
        if playerpos == xyzf:
            print("""T-T <(Teleport succesful!)""")
        else:
            print("""T-T <(Teleport unsuccesful!)""")
        sleep(1)
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
                if i2 == "y":
                    print(""" """)
                if i2 == "n":
                    print("T-T <(Goodbye!)")
                    sleep(1)
                    quit()
        o = input("""T-T <(Want to go again?) (y/n): """)
        if o == "n":
            print("""T-T <(Goodbye!)""")
            sleep(1)
            break
        if o == "y":
            print("""T-T <(Going again...)""")
            sleep(1)
 # Merged function loop #1
MagicBearFcStart()
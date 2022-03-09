# Imports
from guizero import App, Text, TextBox, PushButton
from time import sleep
import sys

def do_this_when_closed():
    if app.yesno("Close", "Do you want to quit?"):
        app.destroy()

def QuitQ():
    sys.exit()

def do_nothing():
    print("T-T <(Launching...)")
    sleep(0.7)
    goI = input("T-T <(Would you like to close the launcher as well? (y/n)): ").lower()
    if goI in ["y", "n"]:
        if goI == "y":
            print("T-T <(Closing...)")
            sleep(0.5)
            app.destroy()
            import TransferCMT
            sys.exit()
        else:
            print("T-T <(Why?)")
            sleep(0.5)
            import TransferCMT
            sys.exit()
    else:
        print("T-T <(Oops, that wasnt the right letter, please type a 'y' or a 'n'. )")
    app.destroy()

# A frustrating loop
while True:
    # Gui 
    app = App(title="CryManT Launcher")
    text = Text(app, text="T-T <(Launch): ", align="left")
    button = PushButton(app, text="Launch", command=do_nothing, align="left")
    text = Text(app, text=" :(Quit)> T-T", align="right")
    button = PushButton(app, text="Quit", command=QuitQ, align="right")
    app.when_closed = do_this_when_closed
    app.display()

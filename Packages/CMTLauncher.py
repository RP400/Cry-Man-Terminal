#Launcher {

# Imports
from guizero import App, Text, TextBox, PushButton
from time import sleep
# A frustrating loop
while True:
    def do_nothing():
        print("T-T <(Launching...)")
        sleep(0.7)
        goI = input("T-T <(Would you like to close the launcher aswell? (y/n)): ")
        if goI in ("y", "n"):
            if goI == "y":
                print("T-T <(Closing...)")
                sleep(0.5)
                app.destroy()
                import TransferCMT
                exit()
            if goI == "n":
                print("T-T <(Why?)")
                sleep(0.5)
                import TransferCMT
                exit()
        else:
            print("T-T <(Oops, that wasnt the right word. Make sure its spelt correctly but just in lower case.)")
        app.destroy()
    def QuitQ():
        quit()
    def do_this_when_closed():
        if app.yesno("Close", "Do you want to quit?"):
            app.destroy()
# Gui 
    app = App(title="CryManT Launcher")
    text = Text(app, text="T-T <(Launch): ", align="left")
    button = PushButton(app, text="Launch", command=do_nothing, align="left")
    text = Text(app, text=" :(Quit)> T-T", align="right")
    button = PushButton(app, text="Quit", command=QuitQ, align="right")
    app.when_closed = do_this_when_closed
    app.display()
#           }
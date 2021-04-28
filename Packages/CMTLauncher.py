#Launcher {

# Imports
from guizero import App, Text, TextBox, PushButton
from time import sleep
def do_nothing():
    print("T-T <(Launching...)")
    sleep(0.2)
    sleep(0.5)
    import TransferCMT.py
    app.destroy()
def QuitQ():
    quit()
def do_this_when_closed():
    if app.yesno("Close", "Do you want to quit?"):
        app.destroy()
# Gui
app = App(title="CryManT Launcher")
text = Text(app, text="T-T <(Launch me!): ", align="left")
button = PushButton(app, text="Launch", command=do_nothing, align="left")
text = Text(app, text=" :(Quit)> T-T", align="right")
button = PushButton(app, text="Quit", command=QuitQ, align="right")
app.when_closed = do_this_when_closed
app.display()
#           }

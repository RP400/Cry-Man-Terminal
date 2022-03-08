# How Do I Set It Up?</br>
To install open the terminal and type the following commands:
```bash
cd ~
pip3 install guizero
git clone https://github.com/RP400/Cry-Man-Terminal
```
then, to run use this command:
```bash
python3 ~/Cry-Man-Terminal/Packages/CMTLauncher.py</br>
```
Now have fun!

# How Do I Add Saved Spots?
Open the `Cry-Man-Terminal/Packages/CMTRaw.py` with your editor of choice (if you can't decide I would recommend Thonny Python IDE),</br>
you will see something like this starting on line 6:</br>
```py
# Save's
#        X    Y    Z 
Save1 = 0.5, 0.0, 0.7
#        X    Y    Z 
Save2 = 0.5, 0.0, 0.7
#        X    Y    Z 
Save3 = 0.5, 0.0, 0.7
```
Choose a `Save`,
delete the default coords,</br>
type in the coords you want to save (like this: `Save2 = 0.5, 0.0, 0.7`)</br>
now save the file and run the code,</br>
type `y` for yes to go to a saved spot,</br>
type in the save you put it in e.g: `Save2`</br>
And you're done!


# Updates (1):</br>
- Better imports (Thanks to @robotech21 for suggesting this fix)</br>

# CryManT GithubVersion: 1.1.3 Original Version: 2.1.3

import pyttsx3

engine = pyttsx3.init()

with open('/home/shweta/Documents/python/rdfile.txt') as f:
    # lines = f.readlines.()
    lines = f.read().splitlines()
   

    engine.say(lines)
    engine.runAndWait()
    engine.runAndWait()
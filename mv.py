
import os

startpunkt = ''
zielpunkt = ''
batchmode = ''
fileformat = ''
name = ''

startpunkt = input("Wo befindet sich die Datei? ")
batchmode = input("Wollen Sie mehrere Dateien verschieben? Ja oder Nein >> ")

if batchmode == "Ja" or batchmode == "ja":
    fileformat = input("Welches Fileformat moechten Sie verschieben? ")
    zielpunkt = input("Wo ist das Zielverzeichnis? ")
    move = ''
    move = 'mv ~/' +startpunkt + fileformat + ' ~/' +zielpunkt
    os.system("touch move.txt")
    script_out = open('move.txt', 'w')
    script_out.write(move)
    script_out.close()
    convert = 'cp move.txt move.sh && sudo chmod +x move.sh && ./move.sh'
    os.system(convert)
    os.system('rm move.txt && rm move.sh')

else:
    name = input("Wie lautet der exacte Name der Datei? ")
    zielpunkt = input("Wo ist das Zielverzeichnis? ")
    move = ''
    move = 'mv ~/' +startpunkt + name + ' ~/' +zielpunkt
    os.system('touch move.txt')
    script_out = open('move.txt', 'w')
    script_out.write(move)
    script_out.close()
    convert = 'cp move.txt move.sh && sudo chmod +x move.sh && ./move.sh'
    os.system(convert)
    os.system('rm move.txt && rm move.sh')



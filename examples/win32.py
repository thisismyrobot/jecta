import msvcrt
import time


#windows code for files dropped onto cmd on XP 
def getch_files_cmd():
    path = u''

    #block on first '"'
    while msvcrt.getch() != chr(34):
        pass

    #get path after '"'
    while 1:
        char = msvcrt.getch()
        if char == chr(34):
            break
        else:
            path += char

    return path

while 1:
    print "recieved path: %s" % getch_files_cmd()
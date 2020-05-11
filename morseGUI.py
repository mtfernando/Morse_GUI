import sys
import time
from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO

RPi.GPIO.setmode(RPi.GPIO.BCM)

#Hardware
ledRed = LED(14)
ledGreen = LED(15)
ledBlue = LED(18)

def split(word): 
    return [char for char in word]

#A unit is 0.25 seconds.
#Dot in morse is one unit.
#Line in morse are three units.
#Space between morse charactes in same letter is one unit.
#Space between letters are three units.
#Space between words are seven units.

def blinkDot(count = 1):
    #The flash will be repeated according to the given count.

    for i in range(count):
        ledRed.on()
        ledGreen.on()
        ledBlue.on()

        time.sleep(0.25) #Active for 0.25 seconds indicating a dot.

        ledRed.off()
        ledGreen.off()
        ledBlue.off()

        time.sleep(0.25) #Seperation between morse blinks is 0.25 seconds of inactivity.

def blinkLine(count=1):
    #The flash will be repeated according to the given count.
    for i in range(count):
        ledRed.on()
        ledGreen.on()
        ledBlue.on()

        time.sleep(0.75) #Active for 0.25 seconds indicating a line.

        ledRed.off()
        ledGreen.off()
        ledBlue.off()

        time.sleep(0.25) #Seperation between morse blinks is 0.25 seconds of inactivity.

def wordSep():
    time.sleep(0.625) #Seperation between words

def letterSep():
    time.sleep(0.5) #Seperation between letters
    
def flash1():
    blinkDot()
    blinkLine(3)

def flash2():
    blinkDot(2)
    blinkLine(3)

def flash3():
    blinkDot(3)
    blinkLine(2)

def flash4():
    blinkDot(4)
    blinkLine()

def flash5():
    blinkDot(5)

def flash6():
    blinkLine()
    blinkDot(4)

def flash7():
    blinkline(2)
    blinkDot(3)

def flash8():
    blinkLine(3)
    blinkDot(2)

def flash9():
    blinkLine(4)
    blinkDot()

def flash0():
    blinkLine(5)    
    
def flashA():
    blinkDot()
    blinkLine()

def flashB():
    blinkLine()
    blinkDot(3)

def flashC():
    blinkLine()
    blinkDot()
    blinkLine()
    blinkDot()

def flashD():
    blinkLine()
    blinkDot(2)

def flashE():
    blinkDot()

def flashF():
    blinkDot(2)
    blinkLine()
    blinkDot()

def flashG():
    blinkLine()
    blinkLine()
    blinkDot()

def flashH():
    blinkDot(4)

def flashI():
    blinkDot(2)

def flashJ():
    blinkDot()
    blinkLine(2)

def flashK():
    blinkLine()
    blinkDot()
    blinkLine()

def flashL():
    blinkDot()
    blinkLine()
    blinkDot(2)

def flashM():
    blinkLine(2)

def flashN():
    blinkLine()
    blinkDot()

def flashO():
    blinkLine(3)

def flashP():
    blinkDot()
    blinkLine(2)
    blinkDot()

def flashQ():
    blinkLine(2)
    blinkDot()
    blinkLine()

def flashR():
    blinkDot()
    blinkLine()
    blinkDot()

def flashS():
    blinkDot(3)

def flashT():
    blinkLine()

def flashU():
    blinkDot(2)
    blinkLine()

def flashV():
    blinkDot(3)
    blinkLine()

def flashW():
    blinkDot()
    blinkLine(2)

def flashX():
    blinkLine()
    blinkDot(2)
    blinkLine()

def flashY():
    blinkLine()
    blinkDot()
    blinkLine(2)

def flashZ():
    blinkLine(2)
    blinkDot(2)
    
def blink():
    text = user_text.get()

    if (len(text)<13):
        textout = Label(win, text="Blinking... "+text).pack()
        charList = split(text.lower())
        print(charList)
        for elem in charList:
            if (elem=='a'):
                flashA()
                letterSep()
            elif (elem=='b'):
                flashB()
                letterSep()
            elif (elem=='c'):
                flashC()
                letterSep()
            elif (elem=='d'):
                flashD()
                letterSep()
            elif (elem=='e'):
                flashE()
                letterSep()
            elif (elem=='f'):
                flashF()
                letterSep()
            elif (elem=='g'):
                flashG()
                letterSep()
            elif (elem=='h'):
                flashH()
                letterSep()
            elif (elem=='i'):
                flashI()
                letterSep()
            elif(elem=='j'):
                flashJ()
                letterSep()
            elif(elem=='k'):
                flashK()
                letterSep()
            elif(elem=='l'):
                flashL()
                letterSep()
            elif(elem=='m'):
                flashM()
                letterSep()
            elif(elem=='n'):
                flashN()
                letterSep()
            elif(elem=='o'):
                flashO()
                letterSep()
            elif(elem=='p'):
                flashP()
                letterSep()
            elif(elem=='q'):
                flashQ()
                letterSep()
            elif(elem=='r'):
                flashR()
                letterSep()
            elif(elem=='s'):
                flashS()
                letterSep()
            elif(elem=='t'):
                flashT()
                letterSep()
            elif(elem=='u'):
                flashU()
                letterSep()
            elif(elem=='v'):
                flashV()
                letterSep()
            elif(elem=='w'):
                flashW()
                letterSep()
            elif(elem=='x'):
                flashX()
                letterSep()
            elif(elem=='y'):
                flashY()
                letterSep()
            elif(elem=='z'):
                flashZ()
                letterSep()
            elif(elem=='0'):
                flash0()
                letterSep()
            elif(elem=='1'):
                flash1()
                letterSep()
            elif(elem=='2'):
                flash2()
                letterSep()
            elif(elem=='3'):
                flash3()
                letterSep()
            elif(elem=='4'):
                flash4()
                letterSep()
            elif(elem=='5'):
                flash5()
                letterSep()
            elif(elem=='6'):
                flash6()
                letterSep()
            elif(elem=='7'):
                flash7()
                letterSep()
            elif(elem=='8'):
                flash8()
            elif(elem=='9'):
                flash9()
                letterSep()
                letterSep()
            elif(elem==' '):
                wordSep()
            else:
                continue;

    else:
        textout = Label(win, text="INVALID! MAX 12 CHAR.", fg='red').pack()

def close():
    RPi.GPIO.cleanup()
    win.destroy()    
#GUI Definitions
win = Tk()
win.title("Morse Blinker")
myFont = tkinter.font.Font(family = 'Calibri', size = 14, weight = "bold")

#Widgets
user_text = StringVar()
welcomeLabel = Label(win, text="Welcome to the Morse Blinker!").pack()
entryLabel = Label(win, text="Please enter a word (max 12 char):").pack()
textbox = Entry(win, textvariable=user_text).pack()
entrybutton = Button(win, text="Blink!", command=blink).pack()

exitButton = Button(win, text = "Exit", font = myFont, command = close, bg = 'red')
exitButton.pack()
win.protocol("WM_DELETE_WINDOW", close)

win.mainloop()

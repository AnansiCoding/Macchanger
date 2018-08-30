#!/usr/bin/env python3

# This Program has almost all the features of mac changer in terminal
# Christopher Valdez
# August 23, 2018
# mac.py version 1.0

#To do list
#[1] find a way to internally find computer's wifi and ethernet names to get rid of user input

import sys
import os
import time

import dialogue
from addressBin import *

if __name__ == '__main__':
    os.system('clear')
    def main():
        dialogue.main()
        user_input = input("Make your choice ==> ")
        os.system('clear')
        if user_input == ('1'):
            showMac()
        if user_input == ('2'):
            randomMac()
        if user_input == ('3'):
            customMac()
        if user_input == ('4'):
            resetMac()
        if user_input == ('5'):
            closeProgram()
        if user_input == ('5150'):
            findRef()
        else:
            main()    
    def showMac():      #Start of show Mac option
        dialogue.connectionType()
        connectionType = input("Enter your connection type ==> ")
        os.system('clear')
        if connectionType == ('1'):
            showWifi()
        if connectionType == ('2'):
            showEth()
        if connectionType == ('3'):
            os.system('clear')
            main()
        else:
            dialogue.inputError()
            os.system('clear')
            showMac()
    def showWifi():
        print("The following is your Mac-Address for "+(wifi)+"\n")
        showWifiAddress()
        continueInput = input("\n\nPress any key to continue, or B to go back. ")
        if continueInput.lower() == ('b'):
            os.system('clear')
            showMac()
        else:
            os.system('clear')
            main()
    def showEth():
        print("The following is your Mac-Address for "+(eth)+"\n")
        showEthAddress()
        continueInput = input("\n\nPress any key to continue, or B to go back. ")
        if continueInput.lower() == ('b'):
            os.system('clear')
            showMac()
        else:
            os.system('clear')
            main()
    def randomMac():        #Start of random mac option
        dialogue.connectionType()
        connectionType = input("Enter your connection type ==> ")
        os.system('clear')
        if connectionType == ('1'):
            randomWifi()
        if connectionType == ('2'):
            randomEth()  
        if connectionType == ('3'):
            os.system('clear')
            main()
        else:
            dialogue.inputError()
            os.system('clear')
            randomMac()
    def randomWifi():
        dialogue.randomMac()
        randomType = input("Make your choice ==> ")
        os.system('clear')
        if randomType == ('1'):
            print("Your Mac-Address has been randomly set.\n")
            wifiDown()
            os.system('sudo macchanger -r '+(wifi))
            wifiUp()
            networkManagerRestart()
            continueInput = input("\n\nPress any key to continue, or B to go back. ")
            if continueInput.lower() == ('b'):
                os.system('clear')
                randomWifi()
            else:
                os.system('clear')
                main()
        if randomType == ('2'):
            print("Everything but vendor bytes have been randomly set.\n")
            wifiDown()
            os.system('sudo macchanger -e  '+(wifi))
            wifiUp()
            networkManagerRestart()
            continueInput = input("\n\nPress any key to continue, or B to go back. ")
            if continueInput.lower() == ('b'):
                os.system('clear')
                randomWifi()
            else:
                os.system('clear')
                main()
        if randomType == ('3'):
            print("Random vendor Mac-Address of the same kind has been set.\n")
            wifiDown()
            os.system('sudo macchanger -a '+(wifi))
            wifiUp()
            networkManagerRestart()
            continueInput = input("\n\nPress any key to continue, or B to go back. ")
            if continueInput.lower() == ('b'):
                os.system('clear')
                randomWifi()
            else:
                os.system('clear')
                main()
        if randomType == ('4'):
            print("Completly random vendor Mac-Address has been set.\n")
            wifiDown()
            os.system('sudo macchanger -A '+(wifi))
            wifiUp()
            networkManagerRestart()
            continueInput = input("\n\nPress any key to continue, or B to go back. ")
            if continueInput.lower() == ('b'):
                os.system('clear')
                randomWifi()
            else:
                os.system('clear')
                main()
        if randomType == ('5'):
            print("Here is a list of known vendors.\n")
            print("When finished press Q to quit.\n")
            continueInput = input("Press any key to show list.")
            os.system('macchanger -l | less')
            os.system('clear')
            continueInput = input("\n\nPress any key to continue, or B to go back. ")
            if continueInput.lower() == ('b'):
                os.system('clear')
                randomWifi()
            else:
                os.system('clear')
                main()
        if randomType == ('6'):
            os.system('clear')
            randomMac()
        else:
            dialogue.inputError()
            os.system('clear')
            randomWifi()
    def randomEth():
        dialogue.randomMac()
        randomType = input("Make your choice ==> ")
        os.system('clear')
        if randomType == ('1'):
            print("Your Mac-Address has been randomly set.\n")
            ethDown()
            os.system('sudo macchanger -r '+(eth))
            ethUp()
            networkManagerRestart()
            continueInput = input("\n\nPress any key to continue, or B to go back. ")
            if continueInput.lower() == ('b'):
                os.system('clear')
                randomEth()
            else:
                os.system('clear')
                main()
        if randomType == ('2'):
            print("Everything but vendor bytes have been randomly set.\n")
            ethDown()
            os.system('sudo macchanger -e '+(eth))
            ethUp()
            networkManagerRestart()
            continueInput = input("\n\nPress any key to continue, or B to go back. ")
            if continueInput.lower() == ('b'):
                os.system('clear')
                randomEth()
            else:
                os.system('clear')
                main()
        if randomType == ('3'):
            print("Random vendor Mac-Address of the same kind has been set.\n")
            ethDown()
            os.system('sudo macchanger -a '+(eth))
            ethUp()
            networkManagerRestart()
            continueInput = input("\n\nPress any key to continue, or B to go back. ")
            if continueInput.lower() == ('b'):
                os.system('clear')
                randomEth()
            else:
                os.system('clear')
                main()
        if randomType == ('4'):
            print("Completly random vendor Mac-Address has been set.\n")
            ethDown()
            os.system('sudo macchanger -A '+(eth))
            ethUp()
            networkManagerRestart()
            continueInput = input("\n\nPress any key to continue, or B to go back. ")
            if continueInput.lower() == ('b'):
                os.system('clear')
                randomEth()
            else:
                os.system('clear')
                main()
        if randomType == ('5'):
            print("Here is a list of known vendors.\n")
            print("When finished press Q to quit.\n")
            continueInput = input("Press any key to show list.")
            os.system('macchanger -l | less')
            os.system('clear')
            continueInput = input("\n\nPress any key to continue, or B to go back. ")
            if continueInput.lower() == ('b'):
                os.system('clear')
                randomEth()
            else:
                os.system('clear')
                main()
        if randomType == ('6'):
            os.system('clear')
            randomMac()
        else:
            dialogue.inputError()
            os.system('clear')
            randomEth()
    def customMac():        #Start of custom mac option
        dialogue.connectionType()
        connectionType=input("Enter your connection type ==> ")
        os.system('clear')
        if connectionType == ('1'):
            customWifi()
        if connectionType == ('2'):
            customEth()
        if connectionType == ('3'):
            os.system('clear')
            main()
        else:
            dialogue.inputError()
            os.system('clear')
            customMac()
    def customWifi():
        customWifiMac = input("\nEnter a new Mac-Address or B to go Back ==> ")
        if customWifiMac.lower() == ('b'):
            os.system('clear')
            customMac()
        else:
            wifiDown()
            time.sleep(1)
            os.system('sudo macchanger -m '+(customWifiMac)+' '+(wifi))
            time.sleep(1)
            wifiUp()
            networkManagerRestart()
            print("\nMac-Address has been change to "+(customWifiMac))
            continueInput=input("\n\nPress any key to continue, or B to go back. ")
            if continueInput.lower() == ('b'):
                os.system('clear')
                customWifi()
            else:
                os.system('clear')
                main()
    def customEth():
        customEthMac = input("\nEnter a new Mac-Address or B to go Back ==> ")
        if customEthMac.lower() == ('b'):
            os.system('clear')
            customMac()
        else:
            ethDown()
            time.sleep(1)
            os.system('sudo macchanger -m '+(customEthMac)+' '+(eth))
            time.sleep(1)
            ethUp()
            networkManagerRestart()
            print("\nMac-Address has been change to "+(customEthMac))
            continueInput = input("\n\nPress any key to continue, or B to go back. ")
            if continueInput.lower() == ('b'):
                os.system('clear')
                customEth()
            else:
                os.system('clear')
                main()          
    def resetMac():     #Start of reset mac option
        dialogue.connectionType()
        connectionType = input("Enter your connection type ==> ")
        os.system('clear')
        if connectionType == ('1'):
            resetWifi()
        if connectionType == ('2'):
            resetEth()
        if connectionType == ('3'):
            os.system('clear')
            main()
        else:
            dialogue.inputError()
            os.system('clear')
            resetMac()
    def resetWifi():
        resetQuestion = input("You would like to reset your Mac-Address Y/n ==> ")
        if resetQuestion.lower() == ('y'):
            print("Your Mac-Address is being reset\n")
            wifiDown()
            os.system('sudo macchanger -p '+(wifi))
            wifiUp()
            networkManagerRestart()
            print("\nMac-Address has been reset")
            continueInput=input("\n\nPress any key to continue, or B to go back. ")
            if continueInput.lower()==('b'):
                os.system('clear')
                resetMac()
            else:
                os.system('clear')
                main()
        if resetQuestion.lower() == ('n'):
            os.system('clear')
            resetMac()
        else:
            dialogue.inputError()
            os.system('clear')
            resetWifi()
    def resetEth():
        resetQuestion = input("You would like to reset your Mac-Address Y/n ==> ")
        if resetQuestion.lower() == ('y'):
            print("Your Mac-Address is being reset\n")
            ethDown()
            os.system('sudo macchanger -p '+(eth))
            ethUp()
            networkManagerRestart()
            print("\nMac-Address has been reset")
            continueInput = input("\n\nPress any key to continue, or B to go back. ")
            if continueInput.lower() == ('b'):
                os.system('clear')
                resetMac()
            else:
                os.system('clear')
                main()
        if resetQuestion.lower() == ('n'):
            os.system('clear')
            resetMac()
        else:
            dialogue.inputError()
            os.system('clear')
            resetEth()
    def closeProgram():     #start of close program
        exit_answer = input("Are you sure? Y/n ==> ")
        if exit_answer.lower() == ('y'):
            os.system('clear')
            sys.exit(0)
        if exit_answer.lower() == ('n'):
            os.system('clear')
            main()
        else :
            dialogue.inputError()
            os.system('clear')
            closeProgram()
    def findRef():
        dialogue.findRef()
        time.sleep(5)
        os.system('clear')
        main()

    main()      #Run main program

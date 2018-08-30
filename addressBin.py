import os

#In the below variable enter your wifi and ethernet names.
#To find the names of you wifi and ethernet use ifconfig

wifi = str('wlan0')
eth = str('eth0')

if __name__ == '__main__':
    pass
else:
    def showWifiAddress():
        os.system('macchanger -s '+(wifi))
    def showEthAddress():
        os.system('macchanger -s '+(eth))
    def wifiDown():
        os.system('sudo ifconfig '+(wifi)+' down')
    def wifiUp():
        os.system('sudo ifconfig '+(wifi)+' up')
    def networkManagerRestart():
        os.system('sudo service network-manager restart')
    def ethDown():
        os.system('sudo ifconfig '+(eth)+' down')
    def ethUp():
        os.system('sudo ifconfig '+(eth)+' up')

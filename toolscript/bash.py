#!/usr/bin/env python
"""""""""""""""""""""
Simple bash commands
"""""""""""""""""""""
# IMPORTS
import os, time

# AUTHORINFO
__author__ = "Joel Chapon"
__email___ = "joel.chapon@student.kdg.be"
__status__ = "Finished"

# FUNCTIONS
def call_update():
    command = "sudo apt update -y"
    os.system(command)
    command = "sudo apt upgrade -y"
    os.system(command)

def install_package():
    print('\n1 = MariaDB')
    print('2 = Xrdp')
    print('3 = Thunar')
    print('4 = Gedit')

    try:
        choice = int(input('What package would you like to install? '))
        if choice == 1:
            command = "sudo apt install mariadb-server -y"
            os.system(command)
            command = "sudo mysql_secure_installation"
            os.system(command)
        if choice == 2:
            command = "sudo apt-get install xrdp -y"
            os.system(command)
            vnc_setup()
        if choice == 3:
            command = "sudo apt-get install thunar -y"
            os.system(command)
        if choice == 4:
            command = "sudo apt-get install gedit -y"
            os.system(command)
        else:
            print('Give a numnber between 1 and 4!')
            install_package()
    except NameError:
        print('Please give a number')
        install_package()

def vnc_setup():
    print('Navigate to Interface > VNC > Yes')
    time.sleep(5)
    command = "sudo raspi-config"
    os.system(command)

def call_shutdown():
    command = "sudo shutdown -h now"
    os.system(command)

def show_info():
    command = "uname -a"
    os.system(command)
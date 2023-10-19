import subprocess
import ctypes
from ctypes import *
import time
from subprocess import *
import signal
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app = QApplication([])



main_win = QWidget()
main_win.setWindowTitle('Palera1n commands')
main_win.setFixedSize(300, 400)
label2 = QLabel('Commands')
rootless_boot = QPushButton('Rootless boot')
rootfull_boot = QPushButton('Rootfull boot')
fakefs = QPushButton('Create FakeFS')
bindfs = QPushButton('Create BindFS')
force_revert = QPushButton('Delete Jailbreak')
pongo_shell = QPushButton('Pongo shell')
custom_args = QPushButton('Custom arguments')


    
Vlayout1 = QVBoxLayout()

Hlayout1 = QHBoxLayout()
Hlayout2 = QHBoxLayout()
Hlayout3 = QHBoxLayout()
Hlayout4 = QHBoxLayout()
Hlayout5 = QHBoxLayout()
Hlayout6 = QHBoxLayout()
Hlayout7 = QHBoxLayout()
Hlayout8 = QHBoxLayout()



HlayoutM = QHBoxLayout()

Hlayout1.addWidget(label2)
Hlayout2.addWidget(rootless_boot)
Hlayout3.addWidget(rootfull_boot)
Hlayout4.addWidget(fakefs)
Hlayout5.addWidget(bindfs)
Hlayout6.addWidget(force_revert)
Hlayout7.addWidget(pongo_shell)
Hlayout8.addWidget(custom_args)


HlayoutM.addLayout(Vlayout1)

Vlayout1.addLayout(Hlayout1)
Vlayout1.addLayout(Hlayout2)
Vlayout1.addLayout(Hlayout3)
Vlayout1.addLayout(Hlayout4)
Vlayout1.addLayout(Hlayout5)
Vlayout1.addLayout(Hlayout6)
Vlayout1.addLayout(Hlayout7)
Vlayout1.addLayout(Hlayout8)


main_win.setLayout(HlayoutM)


def rootless_boot_event():
    result = subprocess.run('./palera1n-macos-x86_64 -v', shell=True, text=True)
rootless_boot.clicked.connect(rootless_boot_event)

def rootfull_boot_event():
    result = subprocess.run('./palera1n-macos-x86_64 -f -v', shell=True, text=True)
rootfull_boot.clicked.connect(rootfull_boot_event)

def fakefs_event():
    result = subprocess.run('./palera1n-macos-x86_64 -fc -v', shell=True, text=True)
fakefs.clicked.connect(fakefs_event)

def bindfs_event():
    result = subprocess.run('./palera1n-macos-x86_64 -Bf -v', shell=True, text=True)
bindfs.clicked.connect(bindfs_event)

def force_revert_event():
    result = subprocess.run('./palera1n-macos-x86_64 --force-revert -f -v', shell=True, text=True)
    output_field.append(result.stdout)
force_revert.clicked.connect(force_revert_event)

def pongo_shell_event():
    result = subprocess.run('./palera1n-macos-x86_64 -p -v', shell=True, text=True)
pongo_shell.clicked.connect(pongo_shell_event)

def custom_args_event():
    args, ok, = QInputDialog.getText(main_win, "Type args with spaces", "Arguments:")
    if ok and args != '!cancel':
        commargs = './palera1n-macos-x86_64 ' + args
        result = subprocess.run(commargs, shell=True, text=True)
custom_args.clicked.connect(custom_args_event)



main_win.show()
app.exec()

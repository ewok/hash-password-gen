#!/usr/bin/env python2
# -*- coding: utf-8 -*-
__author__ = 'ewok'

import sys
from PyQt4 import QtGui

import mainform

app = None


def main():
    app = QtGui.QApplication(sys.argv)
    form = mainform.MainForm()
    form.app = app  # передаю ссылку на аппликэйшн для доступа к клипборду
    form.show()
    app.exec_()

if __name__ == "__main__":
    sys.exit(main())

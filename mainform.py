#! /usr/bin/env python2
# -*- coding: utf-8 -*-
__author__ = 'ewok'

from PyQt4 import QtCore, QtGui, uic

from utils import generate_password


# прототип главной формы
class MainForm(QtGui.QMainWindow):
    # конструктор
    def __init__(self):
        super(MainForm, self).__init__()

        # динамически загружает визуальное представление формы
        uic.loadUi("mainform.ui", self)

        # связывает событие нажатия на кнопку с методом
        self.connect(self.buttonCopy, QtCore.SIGNAL("clicked()"),
                     self.copyPassToClipboard)

        for obj in self.lineMasterPassword, self.lineSalt:
            self.connect(obj, QtCore.SIGNAL("textEdited(QString)"), self.update_generated_password)

        self.connect(self.spinPasswordLength, QtCore.SIGNAL("valueChanged(int)"), self.update_generated_password)

        for obj in self.radioShaSum, self.radioMd5Sum:
            self.connect(obj, QtCore.SIGNAL("clicked()"), self.update_generated_password)

    def copyPassToClipboard(self):
        clipboard = self.app.clipboard()
        clipboard.setText(self.plainGeneratedPassword.toPlainText())

    def update_generated_password(self):
        method = ['sha1sum']
        if self.radioShaSum.isChecked():
            method = ['sha1sum']
        elif self.radioMd5Sum.isChecked():
            method = ['md5sum']

        self.plainGeneratedPassword.setPlainText(generate_password(self.lineMasterPassword.text(),
                                                                   self.lineSalt.text(),
                                                                   method,
                                                                   self.spinPasswordLength.value()))
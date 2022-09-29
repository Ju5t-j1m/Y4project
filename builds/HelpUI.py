# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HelpUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class UiHelp(object):
    def __init__(self):
        self.buttonBox = None
        self.label = None
        self.label_2 = None
        self.label_3 = None

    def setup_ui(self, Help):
        Help.setObjectName("Help")
        Help.setFixedSize(400, 480)
        Help.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Help.setSizeGripEnabled(False)
        Help.setModal(False)

        self.buttonBox = QtWidgets.QDialogButtonBox(Help)
        self.buttonBox.setGeometry(QtCore.QRect(30, 450, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")

        self.label = QtWidgets.QLabel(Help)
        self.label.setGeometry(QtCore.QRect(298, 0, 100, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo res.png"))
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Help)
        self.label_2.setGeometry(QtCore.QRect(1, 0, 291, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(False)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Help)
        self.label_3.setGeometry(QtCore.QRect(2, 70, 391, 391))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.label_3.setObjectName("label_3")

        self.retranslate_ui(Help)
        self.buttonBox.accepted.connect(Help.accept)
        self.buttonBox.rejected.connect(Help.reject)
        QtCore.QMetaObject.connectSlotsByName(Help)

    def retranslate_ui(self, Help):
        _translate = QtCore.QCoreApplication.translate
        Help.setWindowTitle(_translate("Help", "Help"))
        self.label_2.setText(_translate("Help", "<html><head/><body><p><span style=\" text-decoration: underline; "
                                                "color:#0055ff;\">V3 HSED J.N "
                                                "https://github.com/Ju5t-j1m/Y4project</span><span style=\" "
                                                "color:#0055ff;\"><br/></span><span style=\" font-style:italic; "
                                                "color:#000000;\">This program was made with python3.8 + the PyQt "
                                                "toolkit<br/></span><span style=\" color:#000000;\">By Jimmy Norman ("
                                                "976690) BSc Swansea University<br/>Produced in pursuit of MSc Cyber "
                                                "Security<br/>Licensed under MIT License</span></p></body></html>"))
        self.label_3.setText(_translate("Help", "<html><head/><body><p><span style=\" font-weight:600; "
                                                "text-decoration: underline;\">Help/Information<br/></span><span "
                                                "style=\" font-weight:600; color:#ff0000;\">!!THIS PROGRAM SHOULD NOT "
                                                "BE USED AS A MEANS TO SECURE FILES!!</span><span style=\" "
                                                "font-weight:600; text-decoration: underline;\"><br/></span>The "
                                                "purpose of this program is to encode and decode a hard to detect "
                                                "steganograpohic standard to HTML files. The objective of "
                                                "steganography is secrecy not security<br/><span style=\" "
                                                "font-weight:600; text-decoration: "
                                                "underline;\"><br/>Encoding<br/></span>To encode a file, "
                                                "load or paste a file into the first scrolling window and enter the "
                                                "plaintext you would like to encode in the box below, then press "
                                                "\'<span style=\" font-weight:600;\">Encode</span>\'. The result "
                                                "displays in the \'<span style=\" font-weight:600;\">Encoded "
                                                "HTML</span>\' box<span style=\" font-weight:600; text-decoration: "
                                                "underline;\"><br/>Decoding<br/></span>To decode a file an encoded "
                                                "file must be present or loaded into the \'<span style=\" "
                                                "font-weight:600;\">Encoded HTML</span>\' box, once this box has your "
                                                "desired HTML to decode press the \'Decode\' button. The results are "
                                                "displayed in the small box below<span style=\" font-weight:600; "
                                                "text-decoration: underline;\"><br/>Saving<br/></span>Encoded HTML "
                                                "and decoded messages can be saved to a file by pressing the "
                                                "associated buttons<br/><span style=\" font-weight:600; "
                                                "text-decoration: underline;\">Algorithm Operation<br/></span>Due to "
                                                "the nature of the algorithm the length of the plaintext must be "
                                                "smaller or equal to the length in lines of the \'<span style=\" "
                                                "font-weight:600;\">Base HTML</span>\'. This algorithm also supports "
                                                "a selection of common characters these "
                                                "are:<br/><br/>Alphabetical<span style=\" font-weight:600;\">["
                                                "a-z]</span><br/>Uppercase<span style=\" font-weight:600;\">["
                                                "A-Z]</span><br/>Digits<span style=\" font-weight:600;\">["
                                                "0-9]<br/></span>Symbols<span style=\" font-weight:600;\">[\' \', "
                                                "\'!\', \'$\', \'%\', \'&amp;\', \'*\', \'(\', \')\', \':\', \';\', "
                                                "\'-\', \'+\', \'=\', \'?\', \'@\', \'.\']<br/><br/>Thank you for "
                                                "using my program<br/>contact@: "
                                                "jimnor05@gmail.com/976690@swansea.ac.uk</span></p></body></html>"))
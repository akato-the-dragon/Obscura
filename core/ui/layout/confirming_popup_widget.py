# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirming_popup_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_confirming_popup_widget(object):
    def setupUi(self, confirming_popup_widget):
        if not confirming_popup_widget.objectName():
            confirming_popup_widget.setObjectName(u"confirming_popup_widget")
        confirming_popup_widget.resize(400, 150)
        self.confirming_popup_layout = QVBoxLayout(confirming_popup_widget)
        self.confirming_popup_layout.setSpacing(10)
        self.confirming_popup_layout.setObjectName(u"confirming_popup_layout")
        self.confirming_popup_layout.setContentsMargins(15, 15, 15, 15)
        self.title_layout = QVBoxLayout()
        self.title_layout.setObjectName(u"title_layout")
        self.title_label = QLabel(confirming_popup_widget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.title_layout.addWidget(self.title_label)

        self.description_label = QLabel(confirming_popup_widget)
        self.description_label.setObjectName(u"description_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.description_label.sizePolicy().hasHeightForWidth())
        self.description_label.setSizePolicy(sizePolicy)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.title_layout.addWidget(self.description_label)


        self.confirming_popup_layout.addLayout(self.title_layout)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setSpacing(10)
        self.buttons_layout.setObjectName(u"buttons_layout")
        self.buttons_layout.setContentsMargins(15, -1, 15, -1)
        self.continue_button = QPushButton(confirming_popup_widget)
        self.continue_button.setObjectName(u"continue_button")

        self.buttons_layout.addWidget(self.continue_button)

        self.cancel_button = QPushButton(confirming_popup_widget)
        self.cancel_button.setObjectName(u"cancel_button")

        self.buttons_layout.addWidget(self.cancel_button)


        self.confirming_popup_layout.addLayout(self.buttons_layout)


        self.retranslateUi(confirming_popup_widget)

        QMetaObject.connectSlotsByName(confirming_popup_widget)
    # setupUi

    def retranslateUi(self, confirming_popup_widget):
        self.title_label.setText(QCoreApplication.translate("confirming_popup_widget", u"<ttile>", None))
        self.description_label.setText(QCoreApplication.translate("confirming_popup_widget", u"<description>", None))
        self.continue_button.setText(QCoreApplication.translate("confirming_popup_widget", u"\u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u044c", None))
        self.cancel_button.setText(QCoreApplication.translate("confirming_popup_widget", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
        pass
    # retranslateUi


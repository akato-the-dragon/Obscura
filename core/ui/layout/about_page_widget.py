# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about_page_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_about_page_widget(object):
    def setupUi(self, about_page_widget):
        if not about_page_widget.objectName():
            about_page_widget.setObjectName(u"about_page_widget")
        about_page_widget.resize(840, 500)
        self.about_page_layout = QVBoxLayout(about_page_widget)
        self.about_page_layout.setSpacing(10)
        self.about_page_layout.setObjectName(u"about_page_layout")
        self.about_page_layout.setContentsMargins(15, 15, 15, 15)
        self.title_label = QLabel(about_page_widget)
        self.title_label.setObjectName(u"title_label")

        self.about_page_layout.addWidget(self.title_label)

        self.text_edit = QTextEdit(about_page_widget)
        self.text_edit.setObjectName(u"text_edit")
        self.text_edit.setFrameShape(QFrame.NoFrame)
        self.text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.text_edit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.text_edit.setReadOnly(True)

        self.about_page_layout.addWidget(self.text_edit)


        self.retranslateUi(about_page_widget)

        QMetaObject.connectSlotsByName(about_page_widget)
    # setupUi

    def retranslateUi(self, about_page_widget):
        self.title_label.setText(QCoreApplication.translate("about_page_widget", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        pass
    # retranslateUi


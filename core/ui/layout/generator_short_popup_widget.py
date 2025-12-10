# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'generator_short_popup_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_generator_short_popup_widget(object):
    def setupUi(self, generator_short_popup_widget):
        if not generator_short_popup_widget.objectName():
            generator_short_popup_widget.setObjectName(u"generator_short_popup_widget")
        generator_short_popup_widget.resize(500, 100)
        self.generator_short_popup_layout = QVBoxLayout(generator_short_popup_widget)
        self.generator_short_popup_layout.setSpacing(5)
        self.generator_short_popup_layout.setObjectName(u"generator_short_popup_layout")
        self.generator_short_popup_layout.setContentsMargins(15, 10, 15, 10)
        self.title_label = QLabel(generator_short_popup_widget)
        self.title_label.setObjectName(u"title_label")

        self.generator_short_popup_layout.addWidget(self.title_label)

        self.password_layout = QHBoxLayout()
        self.password_layout.setObjectName(u"password_layout")
        self.password_line_edit = QLineEdit(generator_short_popup_widget)
        self.password_line_edit.setObjectName(u"password_line_edit")
        self.password_line_edit.setMinimumSize(QSize(0, 25))
        self.password_line_edit.setEchoMode(QLineEdit.Password)
        self.password_line_edit.setReadOnly(True)

        self.password_layout.addWidget(self.password_line_edit)

        self.show_button = QPushButton(generator_short_popup_widget)
        self.show_button.setObjectName(u"show_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_button.sizePolicy().hasHeightForWidth())
        self.show_button.setSizePolicy(sizePolicy)
        self.show_button.setMinimumSize(QSize(25, 25))
        self.show_button.setMaximumSize(QSize(25, 25))
        self.show_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.password_layout.addWidget(self.show_button)

        self.generate_button = QPushButton(generator_short_popup_widget)
        self.generate_button.setObjectName(u"generate_button")
        sizePolicy.setHeightForWidth(self.generate_button.sizePolicy().hasHeightForWidth())
        self.generate_button.setSizePolicy(sizePolicy)
        self.generate_button.setMinimumSize(QSize(25, 25))
        self.generate_button.setMaximumSize(QSize(25, 25))
        self.generate_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.password_layout.addWidget(self.generate_button)

        self.copy_button = QPushButton(generator_short_popup_widget)
        self.copy_button.setObjectName(u"copy_button")
        self.copy_button.setMinimumSize(QSize(0, 25))
        self.copy_button.setMaximumSize(QSize(16777215, 25))
        self.copy_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.password_layout.addWidget(self.copy_button)

        self.close_button = QPushButton(generator_short_popup_widget)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setMinimumSize(QSize(0, 25))
        self.close_button.setMaximumSize(QSize(16777215, 25))
        self.close_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.password_layout.addWidget(self.close_button)


        self.generator_short_popup_layout.addLayout(self.password_layout)


        self.retranslateUi(generator_short_popup_widget)

        QMetaObject.connectSlotsByName(generator_short_popup_widget)
    # setupUi

    def retranslateUi(self, generator_short_popup_widget):
        self.title_label.setText(QCoreApplication.translate("generator_short_popup_widget", u"\u0411\u044b\u0441\u0442\u0440\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.show_button.setText("")
        self.generate_button.setText("")
        self.copy_button.setText(QCoreApplication.translate("generator_short_popup_widget", u"\u0421\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.close_button.setText(QCoreApplication.translate("generator_short_popup_widget", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
        pass
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'remove_master_popup_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_remove_master_popup_widget(object):
    def setupUi(self, remove_master_popup_widget):
        if not remove_master_popup_widget.objectName():
            remove_master_popup_widget.setObjectName(u"remove_master_popup_widget")
        remove_master_popup_widget.resize(400, 175)
        self.remove_master_popup_layout = QVBoxLayout(remove_master_popup_widget)
        self.remove_master_popup_layout.setSpacing(10)
        self.remove_master_popup_layout.setObjectName(u"remove_master_popup_layout")
        self.remove_master_popup_layout.setContentsMargins(15, 15, 15, 10)
        self.title_label = QLabel(remove_master_popup_widget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.remove_master_popup_layout.addWidget(self.title_label)

        self.password_layout = QHBoxLayout()
        self.password_layout.setSpacing(10)
        self.password_layout.setObjectName(u"password_layout")
        self.password_layout.setContentsMargins(30, -1, 45, -1)
        self.password_label = QLabel(remove_master_popup_widget)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.password_layout.addWidget(self.password_label)

        self.password_line_edit = QLineEdit(remove_master_popup_widget)
        self.password_line_edit.setObjectName(u"password_line_edit")
        self.password_line_edit.setMinimumSize(QSize(0, 25))
        self.password_line_edit.setMaximumSize(QSize(16777215, 25))
        self.password_line_edit.setEchoMode(QLineEdit.Password)

        self.password_layout.addWidget(self.password_line_edit)

        self.show_button = QPushButton(remove_master_popup_widget)
        self.show_button.setObjectName(u"show_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_button.sizePolicy().hasHeightForWidth())
        self.show_button.setSizePolicy(sizePolicy)
        self.show_button.setMinimumSize(QSize(25, 25))
        self.show_button.setMaximumSize(QSize(25, 25))
        self.show_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.show_button.setFocusPolicy(Qt.TabFocus)

        self.password_layout.addWidget(self.show_button)


        self.remove_master_popup_layout.addLayout(self.password_layout)

        self.error_label = QLabel(remove_master_popup_widget)
        self.error_label.setObjectName(u"error_label")

        self.remove_master_popup_layout.addWidget(self.error_label)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setSpacing(10)
        self.buttons_layout.setObjectName(u"buttons_layout")
        self.buttons_layout.setContentsMargins(45, -1, 45, -1)
        self.remove_button = QPushButton(remove_master_popup_widget)
        self.remove_button.setObjectName(u"remove_button")
        self.remove_button.setMinimumSize(QSize(0, 30))
        self.remove_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.buttons_layout.addWidget(self.remove_button)

        self.cancel_button = QPushButton(remove_master_popup_widget)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setMinimumSize(QSize(0, 30))
        self.cancel_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.buttons_layout.addWidget(self.cancel_button)


        self.remove_master_popup_layout.addLayout(self.buttons_layout)


        self.retranslateUi(remove_master_popup_widget)

        QMetaObject.connectSlotsByName(remove_master_popup_widget)
    # setupUi

    def retranslateUi(self, remove_master_popup_widget):
        self.title_label.setText(QCoreApplication.translate("remove_master_popup_widget", u"\u0421\u043d\u044f\u0442\u044c \u043c\u0430\u0441\u0442\u0435\u0440 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.password_label.setText(QCoreApplication.translate("remove_master_popup_widget", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.show_button.setText("")
        self.error_label.setText(QCoreApplication.translate("remove_master_popup_widget", u"<error>", None))
        self.remove_button.setText(QCoreApplication.translate("remove_master_popup_widget", u"\u0421\u043d\u044f\u0442\u044c", None))
        self.cancel_button.setText(QCoreApplication.translate("remove_master_popup_widget", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        pass
    # retranslateUi


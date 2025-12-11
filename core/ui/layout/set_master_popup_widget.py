# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'set_master_popup_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_set_master_popup_widget(object):
    def setupUi(self, set_master_popup_widget):
        if not set_master_popup_widget.objectName():
            set_master_popup_widget.setObjectName(u"set_master_popup_widget")
        set_master_popup_widget.resize(450, 250)
        self.set_master_popup_layout = QVBoxLayout(set_master_popup_widget)
        self.set_master_popup_layout.setSpacing(10)
        self.set_master_popup_layout.setObjectName(u"set_master_popup_layout")
        self.set_master_popup_layout.setContentsMargins(15, 15, 15, 10)
        self.title_label = QLabel(set_master_popup_widget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.set_master_popup_layout.addWidget(self.title_label)

        self.password_content_layout = QGridLayout()
        self.password_content_layout.setObjectName(u"password_content_layout")
        self.password_content_layout.setHorizontalSpacing(10)
        self.password_content_layout.setVerticalSpacing(20)
        self.password_content_layout.setContentsMargins(15, -1, 30, 15)
        self.repeat_password_label = QLabel(set_master_popup_widget)
        self.repeat_password_label.setObjectName(u"repeat_password_label")
        self.repeat_password_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.password_content_layout.addWidget(self.repeat_password_label, 2, 0, 1, 1)

        self.password_line_edit = QLineEdit(set_master_popup_widget)
        self.password_line_edit.setObjectName(u"password_line_edit")
        self.password_line_edit.setMinimumSize(QSize(0, 25))
        self.password_line_edit.setMaximumSize(QSize(16777215, 25))
        self.password_line_edit.setEchoMode(QLineEdit.Password)

        self.password_content_layout.addWidget(self.password_line_edit, 1, 1, 1, 1)

        self.password_label = QLabel(set_master_popup_widget)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.password_content_layout.addWidget(self.password_label, 1, 0, 1, 1)

        self.repeat_password_line_edit = QLineEdit(set_master_popup_widget)
        self.repeat_password_line_edit.setObjectName(u"repeat_password_line_edit")
        self.repeat_password_line_edit.setMinimumSize(QSize(0, 25))
        self.repeat_password_line_edit.setMaximumSize(QSize(16777215, 25))
        self.repeat_password_line_edit.setEchoMode(QLineEdit.Password)

        self.password_content_layout.addWidget(self.repeat_password_line_edit, 2, 1, 1, 1)

        self.current_password_label = QLabel(set_master_popup_widget)
        self.current_password_label.setObjectName(u"current_password_label")
        self.current_password_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.password_content_layout.addWidget(self.current_password_label, 0, 0, 1, 1)

        self.current_password_line_edit = QLineEdit(set_master_popup_widget)
        self.current_password_line_edit.setObjectName(u"current_password_line_edit")
        self.current_password_line_edit.setMinimumSize(QSize(0, 25))
        self.current_password_line_edit.setMaximumSize(QSize(16777215, 25))
        self.current_password_line_edit.setEchoMode(QLineEdit.Password)

        self.password_content_layout.addWidget(self.current_password_line_edit, 0, 1, 1, 1)

        self.show_button = QPushButton(set_master_popup_widget)
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

        self.password_content_layout.addWidget(self.show_button, 0, 2, 1, 1)


        self.set_master_popup_layout.addLayout(self.password_content_layout)

        self.error_label = QLabel(set_master_popup_widget)
        self.error_label.setObjectName(u"error_label")

        self.set_master_popup_layout.addWidget(self.error_label)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setSpacing(10)
        self.buttons_layout.setObjectName(u"buttons_layout")
        self.buttons_layout.setContentsMargins(45, -1, 45, -1)
        self.set_button = QPushButton(set_master_popup_widget)
        self.set_button.setObjectName(u"set_button")
        self.set_button.setMinimumSize(QSize(0, 30))
        self.set_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.buttons_layout.addWidget(self.set_button)

        self.cancel_button = QPushButton(set_master_popup_widget)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setMinimumSize(QSize(0, 30))
        self.cancel_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.buttons_layout.addWidget(self.cancel_button)


        self.set_master_popup_layout.addLayout(self.buttons_layout)


        self.retranslateUi(set_master_popup_widget)

        QMetaObject.connectSlotsByName(set_master_popup_widget)
    # setupUi

    def retranslateUi(self, set_master_popup_widget):
        self.title_label.setText(QCoreApplication.translate("set_master_popup_widget", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u043c\u0430\u0441\u0442\u0435\u0440 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.repeat_password_label.setText(QCoreApplication.translate("set_master_popup_widget", u"\u041f\u043e\u0432\u0442\u043e\u0440\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c:", None))
        self.password_label.setText(QCoreApplication.translate("set_master_popup_widget", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.current_password_label.setText(QCoreApplication.translate("set_master_popup_widget", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0439 \u043f\u0430\u0440\u043e\u043b\u044c:", None))
        self.show_button.setText("")
        self.error_label.setText(QCoreApplication.translate("set_master_popup_widget", u"<error>", None))
        self.set_button.setText(QCoreApplication.translate("set_master_popup_widget", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.cancel_button.setText(QCoreApplication.translate("set_master_popup_widget", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        pass
    # retranslateUi


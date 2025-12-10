# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'generator_popup_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_generator_popup_widget(object):
    def setupUi(self, generator_popup_widget):
        if not generator_popup_widget.objectName():
            generator_popup_widget.setObjectName(u"generator_popup_widget")
        generator_popup_widget.resize(500, 300)
        self.generator_popup_layout = QVBoxLayout(generator_popup_widget)
        self.generator_popup_layout.setSpacing(30)
        self.generator_popup_layout.setObjectName(u"generator_popup_layout")
        self.generator_popup_layout.setContentsMargins(15, 15, 15, 10)
        self.title_label = QLabel(generator_popup_widget)
        self.title_label.setObjectName(u"title_label")

        self.generator_popup_layout.addWidget(self.title_label)

        self.parameters_layout = QGridLayout()
        self.parameters_layout.setObjectName(u"parameters_layout")
        self.parameters_layout.setHorizontalSpacing(10)
        self.parameters_layout.setVerticalSpacing(15)
        self.parameters_layout.setContentsMargins(30, -1, 90, -1)
        self.lenght_spin_box = QSpinBox(generator_popup_widget)
        self.lenght_spin_box.setObjectName(u"lenght_spin_box")
        self.lenght_spin_box.setMinimumSize(QSize(0, 25))
        self.lenght_spin_box.setMaximumSize(QSize(16777215, 25))
        self.lenght_spin_box.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lenght_spin_box.setMinimum(4)
        self.lenght_spin_box.setMaximum(64)
        self.lenght_spin_box.setValue(8)

        self.parameters_layout.addWidget(self.lenght_spin_box, 0, 1, 1, 1)

        self.use_upper_register_label = QLabel(generator_popup_widget)
        self.use_upper_register_label.setObjectName(u"use_upper_register_label")
        self.use_upper_register_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.parameters_layout.addWidget(self.use_upper_register_label, 2, 0, 1, 1)

        self.use_chars_label = QLabel(generator_popup_widget)
        self.use_chars_label.setObjectName(u"use_chars_label")
        self.use_chars_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.parameters_layout.addWidget(self.use_chars_label, 1, 0, 1, 1)

        self.lenght_label = QLabel(generator_popup_widget)
        self.lenght_label.setObjectName(u"lenght_label")
        self.lenght_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.parameters_layout.addWidget(self.lenght_label, 0, 0, 1, 1)

        self.use_symbols_label = QLabel(generator_popup_widget)
        self.use_symbols_label.setObjectName(u"use_symbols_label")
        self.use_symbols_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.parameters_layout.addWidget(self.use_symbols_label, 3, 0, 1, 1)

        self.use_chars_check_box = QCheckBox(generator_popup_widget)
        self.use_chars_check_box.setObjectName(u"use_chars_check_box")
        self.use_chars_check_box.setMinimumSize(QSize(0, 25))
        self.use_chars_check_box.setMaximumSize(QSize(16777215, 25))
        self.use_chars_check_box.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.parameters_layout.addWidget(self.use_chars_check_box, 1, 1, 1, 1)

        self.use_upper_register_check_box = QCheckBox(generator_popup_widget)
        self.use_upper_register_check_box.setObjectName(u"use_upper_register_check_box")
        self.use_upper_register_check_box.setMinimumSize(QSize(0, 25))
        self.use_upper_register_check_box.setMaximumSize(QSize(16777215, 25))
        self.use_upper_register_check_box.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.parameters_layout.addWidget(self.use_upper_register_check_box, 2, 1, 1, 1)

        self.use_symbols_check_box = QCheckBox(generator_popup_widget)
        self.use_symbols_check_box.setObjectName(u"use_symbols_check_box")
        self.use_symbols_check_box.setMinimumSize(QSize(0, 25))
        self.use_symbols_check_box.setMaximumSize(QSize(16777215, 25))
        self.use_symbols_check_box.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.parameters_layout.addWidget(self.use_symbols_check_box, 3, 1, 1, 1)


        self.generator_popup_layout.addLayout(self.parameters_layout)

        self.password_layout = QHBoxLayout()
        self.password_layout.setSpacing(5)
        self.password_layout.setObjectName(u"password_layout")
        self.password_line_edit = QLineEdit(generator_popup_widget)
        self.password_line_edit.setObjectName(u"password_line_edit")
        self.password_line_edit.setMinimumSize(QSize(0, 25))
        self.password_line_edit.setMaximumSize(QSize(16777215, 25))
        self.password_line_edit.setEchoMode(QLineEdit.Password)
        self.password_line_edit.setReadOnly(True)

        self.password_layout.addWidget(self.password_line_edit)

        self.show_button = QPushButton(generator_popup_widget)
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

        self.generate_button = QPushButton(generator_popup_widget)
        self.generate_button.setObjectName(u"generate_button")
        sizePolicy.setHeightForWidth(self.generate_button.sizePolicy().hasHeightForWidth())
        self.generate_button.setSizePolicy(sizePolicy)
        self.generate_button.setMinimumSize(QSize(25, 25))
        self.generate_button.setMaximumSize(QSize(25, 25))
        self.generate_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.password_layout.addWidget(self.generate_button)

        self.copy_button = QPushButton(generator_popup_widget)
        self.copy_button.setObjectName(u"copy_button")
        self.copy_button.setMinimumSize(QSize(0, 25))
        self.copy_button.setMaximumSize(QSize(16777215, 25))
        self.copy_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.password_layout.addWidget(self.copy_button)

        self.close_button = QPushButton(generator_popup_widget)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setMinimumSize(QSize(0, 25))
        self.close_button.setMaximumSize(QSize(16777215, 25))
        self.close_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.password_layout.addWidget(self.close_button)


        self.generator_popup_layout.addLayout(self.password_layout)


        self.retranslateUi(generator_popup_widget)

        QMetaObject.connectSlotsByName(generator_popup_widget)
    # setupUi

    def retranslateUi(self, generator_popup_widget):
        self.title_label.setText(QCoreApplication.translate("generator_popup_widget", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u044f \u043f\u0430\u0440\u043e\u043b\u044f", None))
        self.use_upper_register_label.setText(QCoreApplication.translate("generator_popup_widget", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u0432\u0435\u0440\u0445\u043d\u0438\u0439 \u0440\u0435\u0433\u0438\u0441\u0442\u0440:", None))
        self.use_chars_label.setText(QCoreApplication.translate("generator_popup_widget", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u0431\u0443\u043a\u0432\u044b:", None))
        self.lenght_label.setText(QCoreApplication.translate("generator_popup_widget", u"\u0414\u043b\u0438\u043d\u0430 \u043f\u0430\u0440\u043e\u043b\u044f:", None))
        self.use_symbols_label.setText(QCoreApplication.translate("generator_popup_widget", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u0441\u043f\u0435\u0446. \u0441\u0438\u043c\u0432\u043e\u043b\u044b:", None))
        self.use_chars_check_box.setText("")
        self.use_upper_register_check_box.setText("")
        self.use_symbols_check_box.setText("")
        self.show_button.setText("")
        self.generate_button.setText("")
        self.copy_button.setText(QCoreApplication.translate("generator_popup_widget", u"\u0421\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.close_button.setText(QCoreApplication.translate("generator_popup_widget", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
        pass
    # retranslateUi


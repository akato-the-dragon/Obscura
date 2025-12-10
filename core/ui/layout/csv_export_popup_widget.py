# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'csv_export_popup_widget.ui'
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
    QProgressBar, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_csv_export_popup_widget(object):
    def setupUi(self, csv_export_popup_widget):
        if not csv_export_popup_widget.objectName():
            csv_export_popup_widget.setObjectName(u"csv_export_popup_widget")
        csv_export_popup_widget.resize(450, 200)
        self.csv_export_popup_layout = QVBoxLayout(csv_export_popup_widget)
        self.csv_export_popup_layout.setSpacing(0)
        self.csv_export_popup_layout.setObjectName(u"csv_export_popup_layout")
        self.csv_export_popup_layout.setContentsMargins(0, 0, 0, 0)
        self.centered_layout = QVBoxLayout()
        self.centered_layout.setSpacing(30)
        self.centered_layout.setObjectName(u"centered_layout")
        self.centered_layout.setContentsMargins(15, 15, 15, 15)
        self.title_label = QLabel(csv_export_popup_widget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.centered_layout.addWidget(self.title_label)

        self.csv_file_layout = QHBoxLayout()
        self.csv_file_layout.setSpacing(10)
        self.csv_file_layout.setObjectName(u"csv_file_layout")
        self.csv_file_layout.setContentsMargins(15, -1, 15, -1)
        self.csv_file_label = QLabel(csv_export_popup_widget)
        self.csv_file_label.setObjectName(u"csv_file_label")
        self.csv_file_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.csv_file_layout.addWidget(self.csv_file_label)

        self.csv_file_line_edit = QLineEdit(csv_export_popup_widget)
        self.csv_file_line_edit.setObjectName(u"csv_file_line_edit")
        self.csv_file_line_edit.setMinimumSize(QSize(0, 25))

        self.csv_file_layout.addWidget(self.csv_file_line_edit)

        self.csv_file_browser_button = QPushButton(csv_export_popup_widget)
        self.csv_file_browser_button.setObjectName(u"csv_file_browser_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.csv_file_browser_button.sizePolicy().hasHeightForWidth())
        self.csv_file_browser_button.setSizePolicy(sizePolicy)
        self.csv_file_browser_button.setMinimumSize(QSize(25, 25))
        self.csv_file_browser_button.setMaximumSize(QSize(25, 25))
        self.csv_file_browser_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.csv_file_layout.addWidget(self.csv_file_browser_button)


        self.centered_layout.addLayout(self.csv_file_layout)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setSpacing(10)
        self.buttons_layout.setObjectName(u"buttons_layout")
        self.buttons_layout.setContentsMargins(45, -1, 45, -1)
        self.export_button = QPushButton(csv_export_popup_widget)
        self.export_button.setObjectName(u"export_button")
        self.export_button.setMinimumSize(QSize(0, 30))
        self.export_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.buttons_layout.addWidget(self.export_button)

        self.cancel_button = QPushButton(csv_export_popup_widget)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setMinimumSize(QSize(0, 30))
        self.cancel_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.buttons_layout.addWidget(self.cancel_button)


        self.centered_layout.addLayout(self.buttons_layout)


        self.csv_export_popup_layout.addLayout(self.centered_layout)

        self.progress_bar = QProgressBar(csv_export_popup_widget)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setMaximumSize(QSize(16777215, 8))
        self.progress_bar.setTextVisible(False)

        self.csv_export_popup_layout.addWidget(self.progress_bar)


        self.retranslateUi(csv_export_popup_widget)

        QMetaObject.connectSlotsByName(csv_export_popup_widget)
    # setupUi

    def retranslateUi(self, csv_export_popup_widget):
        self.title_label.setText(QCoreApplication.translate("csv_export_popup_widget", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442 \u0438\u0437 csv \u0444\u0430\u0439\u043b\u0430", None))
        self.csv_file_label.setText(QCoreApplication.translate("csv_export_popup_widget", u"\u041f\u0443\u0442\u044c \u043a \u0444\u0430\u0439\u043b\u0443:", None))
        self.csv_file_browser_button.setText(QCoreApplication.translate("csv_export_popup_widget", u"...", None))
        self.export_button.setText(QCoreApplication.translate("csv_export_popup_widget", u"\u0418\u043c\u043f\u043e\u0440\u0442", None))
        self.cancel_button.setText(QCoreApplication.translate("csv_export_popup_widget", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        pass
    # retranslateUi


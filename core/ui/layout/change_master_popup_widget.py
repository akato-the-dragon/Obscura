# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'change_master_popup_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QProgressBar, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_change_master_popup_widget(object):
    def setupUi(self, change_master_popup_widget):
        if not change_master_popup_widget.objectName():
            change_master_popup_widget.setObjectName(u"change_master_popup_widget")
        change_master_popup_widget.resize(450, 125)
        self.change_master_popup_layout = QVBoxLayout(change_master_popup_widget)
        self.change_master_popup_layout.setSpacing(0)
        self.change_master_popup_layout.setObjectName(u"change_master_popup_layout")
        self.change_master_popup_layout.setContentsMargins(0, 0, 0, 0)
        self.centered_layout = QVBoxLayout()
        self.centered_layout.setSpacing(15)
        self.centered_layout.setObjectName(u"centered_layout")
        self.centered_layout.setContentsMargins(15, 15, 15, 15)
        self.title_label = QLabel(change_master_popup_widget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.centered_layout.addWidget(self.title_label)

        self.tip_label = QLabel(change_master_popup_widget)
        self.tip_label.setObjectName(u"tip_label")

        self.centered_layout.addWidget(self.tip_label)


        self.change_master_popup_layout.addLayout(self.centered_layout)

        self.progress_bar = QProgressBar(change_master_popup_widget)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setMaximumSize(QSize(16777215, 16))
        self.progress_bar.setTextVisible(False)

        self.change_master_popup_layout.addWidget(self.progress_bar)


        self.retranslateUi(change_master_popup_widget)

        QMetaObject.connectSlotsByName(change_master_popup_widget)
    # setupUi

    def retranslateUi(self, change_master_popup_widget):
        self.title_label.setText(QCoreApplication.translate("change_master_popup_widget", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430 \u043d\u043e\u0432\u043e\u0433\u043e \u043c\u0430\u0441\u0442\u0435\u0440 \u043f\u0430\u0440\u043e\u043b\u044f", None))
        self.tip_label.setText(QCoreApplication.translate("change_master_popup_widget", u"\u041d\u0435 \u0437\u0430\u043a\u0440\u044b\u0432\u0430\u0439\u0442\u0435 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0443", None))
        pass
    # retranslateUi


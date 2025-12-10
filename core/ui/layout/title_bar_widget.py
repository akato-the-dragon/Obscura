# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'title_bar_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QWidget)

from core.ui.element.button import FadingButton
from core.ui.element.widget import StatusWidget

class Ui_title_bar_widget(object):
    def setupUi(self, title_bar_widget):
        if not title_bar_widget.objectName():
            title_bar_widget.setObjectName(u"title_bar_widget")
        title_bar_widget.resize(1000, 40)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(title_bar_widget.sizePolicy().hasHeightForWidth())
        title_bar_widget.setSizePolicy(sizePolicy)
        title_bar_widget.setMinimumSize(QSize(500, 40))
        title_bar_widget.setMaximumSize(QSize(16777215, 40))
        self.title_bar_layout = QHBoxLayout(title_bar_widget)
        self.title_bar_layout.setSpacing(10)
        self.title_bar_layout.setObjectName(u"title_bar_layout")
        self.title_bar_layout.setContentsMargins(0, 0, 0, 0)
        self.blackout_widget = QWidget(title_bar_widget)
        self.blackout_widget.setObjectName(u"blackout_widget")
        self.blackout_layout = QHBoxLayout(self.blackout_widget)
        self.blackout_layout.setSpacing(5)
        self.blackout_layout.setObjectName(u"blackout_layout")
        self.blackout_layout.setContentsMargins(0, 0, 0, 0)
        self.title_layout = QHBoxLayout()
        self.title_layout.setSpacing(5)
        self.title_layout.setObjectName(u"title_layout")
        self.title_layout.setContentsMargins(5, -1, -1, -1)
        self.status_widget = StatusWidget(self.blackout_widget)
        self.status_widget.setObjectName(u"status_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.status_widget.sizePolicy().hasHeightForWidth())
        self.status_widget.setSizePolicy(sizePolicy1)
        self.status_widget.setMinimumSize(QSize(25, 25))
        self.status_widget.setMaximumSize(QSize(25, 25))

        self.title_layout.addWidget(self.status_widget)

        self.name_label = QLabel(self.blackout_widget)
        self.name_label.setObjectName(u"name_label")

        self.title_layout.addWidget(self.name_label)


        self.blackout_layout.addLayout(self.title_layout)

        self.version_label = QLabel(self.blackout_widget)
        self.version_label.setObjectName(u"version_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.version_label.sizePolicy().hasHeightForWidth())
        self.version_label.setSizePolicy(sizePolicy2)
        self.version_label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.version_label.setMargin(5)

        self.blackout_layout.addWidget(self.version_label)

        self.separator_line = QFrame(self.blackout_widget)
        self.separator_line.setObjectName(u"separator_line")
        sizePolicy1.setHeightForWidth(self.separator_line.sizePolicy().hasHeightForWidth())
        self.separator_line.setSizePolicy(sizePolicy1)
        self.separator_line.setMinimumSize(QSize(0, 25))
        self.separator_line.setMaximumSize(QSize(16777215, 25))
        self.separator_line.setFrameShape(QFrame.Shape.VLine)
        self.separator_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.blackout_layout.addWidget(self.separator_line)

        self.control_layout = QHBoxLayout()
        self.control_layout.setSpacing(0)
        self.control_layout.setObjectName(u"control_layout")
        self.minimize_button = FadingButton(self.blackout_widget)
        self.minimize_button.setObjectName(u"minimize_button")
        sizePolicy1.setHeightForWidth(self.minimize_button.sizePolicy().hasHeightForWidth())
        self.minimize_button.setSizePolicy(sizePolicy1)
        self.minimize_button.setMinimumSize(QSize(35, 40))
        self.minimize_button.setMaximumSize(QSize(35, 40))
        self.minimize_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.minimize_button.setFocusPolicy(Qt.NoFocus)

        self.control_layout.addWidget(self.minimize_button)

        self.maximize_button = FadingButton(self.blackout_widget)
        self.maximize_button.setObjectName(u"maximize_button")
        sizePolicy1.setHeightForWidth(self.maximize_button.sizePolicy().hasHeightForWidth())
        self.maximize_button.setSizePolicy(sizePolicy1)
        self.maximize_button.setMinimumSize(QSize(35, 40))
        self.maximize_button.setMaximumSize(QSize(35, 40))
        self.maximize_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.maximize_button.setFocusPolicy(Qt.NoFocus)

        self.control_layout.addWidget(self.maximize_button)

        self.close_button = FadingButton(self.blackout_widget)
        self.close_button.setObjectName(u"close_button")
        sizePolicy1.setHeightForWidth(self.close_button.sizePolicy().hasHeightForWidth())
        self.close_button.setSizePolicy(sizePolicy1)
        self.close_button.setMinimumSize(QSize(35, 40))
        self.close_button.setMaximumSize(QSize(35, 40))
        self.close_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.close_button.setFocusPolicy(Qt.NoFocus)

        self.control_layout.addWidget(self.close_button)


        self.blackout_layout.addLayout(self.control_layout)


        self.title_bar_layout.addWidget(self.blackout_widget)


        self.retranslateUi(title_bar_widget)

        QMetaObject.connectSlotsByName(title_bar_widget)
    # setupUi

    def retranslateUi(self, title_bar_widget):
        self.name_label.setText(QCoreApplication.translate("title_bar_widget", u"Obscura", None))
        self.version_label.setText(QCoreApplication.translate("title_bar_widget", u"\u0412\u0435\u0440. <version>", None))
        self.minimize_button.setText("")
        self.maximize_button.setText("")
        self.close_button.setText("")
        pass
    # retranslateUi


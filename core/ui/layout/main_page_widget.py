# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_page_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

from core.ui.element.button import FadingButton

class Ui_main_page_widget(object):
    def setupUi(self, main_page_widget):
        if not main_page_widget.objectName():
            main_page_widget.setObjectName(u"main_page_widget")
        main_page_widget.resize(840, 500)
        self.main_page_layout = QVBoxLayout(main_page_widget)
        self.main_page_layout.setSpacing(0)
        self.main_page_layout.setObjectName(u"main_page_layout")
        self.main_page_layout.setContentsMargins(0, 0, 0, 0)
        self.top_widget = QWidget(main_page_widget)
        self.top_widget.setObjectName(u"top_widget")
        self.top_widget.setMinimumSize(QSize(0, 50))
        self.top_layout = QHBoxLayout(self.top_widget)
        self.top_layout.setSpacing(10)
        self.top_layout.setObjectName(u"top_layout")
        self.top_layout.setContentsMargins(5, 0, 5, 0)
        self.title_label = QLabel(self.top_widget)
        self.title_label.setObjectName(u"title_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)

        self.top_layout.addWidget(self.title_label)

        self.search_layout = QHBoxLayout()
        self.search_layout.setSpacing(5)
        self.search_layout.setObjectName(u"search_layout")
        self.search_line_edit = QLineEdit(self.top_widget)
        self.search_line_edit.setObjectName(u"search_line_edit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.search_line_edit.sizePolicy().hasHeightForWidth())
        self.search_line_edit.setSizePolicy(sizePolicy1)
        self.search_line_edit.setMinimumSize(QSize(200, 30))
        self.search_line_edit.setFocusPolicy(Qt.TabFocus)

        self.search_layout.addWidget(self.search_line_edit)

        self.search_button = FadingButton(self.top_widget)
        self.search_button.setObjectName(u"search_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.search_button.sizePolicy().hasHeightForWidth())
        self.search_button.setSizePolicy(sizePolicy2)
        self.search_button.setMinimumSize(QSize(30, 30))
        self.search_button.setMaximumSize(QSize(30, 30))
        self.search_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.search_button.setFocusPolicy(Qt.TabFocus)

        self.search_layout.addWidget(self.search_button)


        self.top_layout.addLayout(self.search_layout)

        self.add_button = FadingButton(self.top_widget)
        self.add_button.setObjectName(u"add_button")
        sizePolicy2.setHeightForWidth(self.add_button.sizePolicy().hasHeightForWidth())
        self.add_button.setSizePolicy(sizePolicy2)
        self.add_button.setMinimumSize(QSize(40, 40))
        self.add_button.setMaximumSize(QSize(40, 40))
        self.add_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add_button.setFocusPolicy(Qt.TabFocus)

        self.top_layout.addWidget(self.add_button)


        self.main_page_layout.addWidget(self.top_widget)

        self.passwords_table_widget = QTableWidget(main_page_widget)
        if (self.passwords_table_widget.columnCount() < 3):
            self.passwords_table_widget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.passwords_table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.passwords_table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.passwords_table_widget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.passwords_table_widget.setObjectName(u"passwords_table_widget")
        self.passwords_table_widget.setFrameShape(QFrame.NoFrame)
        self.passwords_table_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.passwords_table_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.passwords_table_widget.horizontalHeader().setCascadingSectionResizes(False)
        self.passwords_table_widget.horizontalHeader().setHighlightSections(True)
        self.passwords_table_widget.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.passwords_table_widget.horizontalHeader().setStretchLastSection(True)
        self.passwords_table_widget.verticalHeader().setVisible(False)

        self.main_page_layout.addWidget(self.passwords_table_widget)

        self.bottom_widget = QWidget(main_page_widget)
        self.bottom_widget.setObjectName(u"bottom_widget")
        self.bottom_widget.setMinimumSize(QSize(0, 30))
        self.bottom_layout = QHBoxLayout(self.bottom_widget)
        self.bottom_layout.setSpacing(5)
        self.bottom_layout.setObjectName(u"bottom_layout")
        self.bottom_layout.setContentsMargins(5, 0, 5, 0)
        self.choosed_label = QLabel(self.bottom_widget)
        self.choosed_label.setObjectName(u"choosed_label")
        sizePolicy.setHeightForWidth(self.choosed_label.sizePolicy().hasHeightForWidth())
        self.choosed_label.setSizePolicy(sizePolicy)
        self.choosed_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.bottom_layout.addWidget(self.choosed_label)

        self.delete_button = FadingButton(self.bottom_widget)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.delete_button.setFocusPolicy(Qt.TabFocus)

        self.bottom_layout.addWidget(self.delete_button)


        self.main_page_layout.addWidget(self.bottom_widget)


        self.retranslateUi(main_page_widget)

        QMetaObject.connectSlotsByName(main_page_widget)
    # setupUi

    def retranslateUi(self, main_page_widget):
        self.title_label.setText(QCoreApplication.translate("main_page_widget", u"\u041f\u0430\u0440\u043e\u043b\u0438", None))
        self.search_button.setText("")
        self.add_button.setText("")
        ___qtablewidgetitem = self.passwords_table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("main_page_widget", u"\u0421\u0430\u0439\u0442", None));
        ___qtablewidgetitem1 = self.passwords_table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("main_page_widget", u"\u041b\u043e\u0433\u0438\u043d", None));
        ___qtablewidgetitem2 = self.passwords_table_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("main_page_widget", u"\u041f\u0430\u0440\u043e\u043b\u044c", None));
        self.choosed_label.setText(QCoreApplication.translate("main_page_widget", u"\u0412\u044b\u0431\u0440\u0430\u043d\u043e:", None))
        self.delete_button.setText(QCoreApplication.translate("main_page_widget", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        pass
    # retranslateUi


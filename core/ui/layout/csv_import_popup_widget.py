# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'csv_import_popup_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QProgressBar,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_csv_import_popup_widget(object):
    def setupUi(self, csv_import_popup_widget):
        if not csv_import_popup_widget.objectName():
            csv_import_popup_widget.setObjectName(u"csv_import_popup_widget")
        csv_import_popup_widget.resize(450, 325)
        self.csv_import_popup_layout = QVBoxLayout(csv_import_popup_widget)
        self.csv_import_popup_layout.setSpacing(0)
        self.csv_import_popup_layout.setObjectName(u"csv_import_popup_layout")
        self.csv_import_popup_layout.setContentsMargins(0, 0, 0, 0)
        self.centered_layout = QVBoxLayout()
        self.centered_layout.setSpacing(15)
        self.centered_layout.setObjectName(u"centered_layout")
        self.centered_layout.setContentsMargins(15, 15, 15, 15)
        self.title_label = QLabel(csv_import_popup_widget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.centered_layout.addWidget(self.title_label)

        self.csv_file_layout = QHBoxLayout()
        self.csv_file_layout.setSpacing(10)
        self.csv_file_layout.setObjectName(u"csv_file_layout")
        self.csv_file_layout.setContentsMargins(15, -1, 15, -1)
        self.csv_file_label = QLabel(csv_import_popup_widget)
        self.csv_file_label.setObjectName(u"csv_file_label")
        self.csv_file_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.csv_file_layout.addWidget(self.csv_file_label)

        self.csv_file_line_edit = QLineEdit(csv_import_popup_widget)
        self.csv_file_line_edit.setObjectName(u"csv_file_line_edit")
        self.csv_file_line_edit.setMinimumSize(QSize(0, 25))

        self.csv_file_layout.addWidget(self.csv_file_line_edit)

        self.csv_file_browser_button = QPushButton(csv_import_popup_widget)
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

        self.column_remap_group_box = QGroupBox(csv_import_popup_widget)
        self.column_remap_group_box.setObjectName(u"column_remap_group_box")
        self.column_remap_group_box.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.column_remap_layout = QGridLayout(self.column_remap_group_box)
        self.column_remap_layout.setObjectName(u"column_remap_layout")
        self.column_remap_layout.setHorizontalSpacing(10)
        self.column_remap_layout.setVerticalSpacing(20)
        self.column_remap_layout.setContentsMargins(30, 15, 75, 15)
        self.site_url_label = QLabel(self.column_remap_group_box)
        self.site_url_label.setObjectName(u"site_url_label")
        self.site_url_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.column_remap_layout.addWidget(self.site_url_label, 0, 0, 1, 1)

        self.login_label = QLabel(self.column_remap_group_box)
        self.login_label.setObjectName(u"login_label")
        self.login_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.column_remap_layout.addWidget(self.login_label, 1, 0, 1, 1)

        self.password_label = QLabel(self.column_remap_group_box)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.column_remap_layout.addWidget(self.password_label, 2, 0, 1, 1)

        self.site_url_combo_box = QComboBox(self.column_remap_group_box)
        self.site_url_combo_box.setObjectName(u"site_url_combo_box")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.site_url_combo_box.sizePolicy().hasHeightForWidth())
        self.site_url_combo_box.setSizePolicy(sizePolicy1)
        self.site_url_combo_box.setMinimumSize(QSize(0, 25))

        self.column_remap_layout.addWidget(self.site_url_combo_box, 0, 1, 1, 1)

        self.login_combo_box = QComboBox(self.column_remap_group_box)
        self.login_combo_box.setObjectName(u"login_combo_box")
        sizePolicy1.setHeightForWidth(self.login_combo_box.sizePolicy().hasHeightForWidth())
        self.login_combo_box.setSizePolicy(sizePolicy1)
        self.login_combo_box.setMinimumSize(QSize(0, 25))

        self.column_remap_layout.addWidget(self.login_combo_box, 1, 1, 1, 1)

        self.password_combo_box = QComboBox(self.column_remap_group_box)
        self.password_combo_box.setObjectName(u"password_combo_box")
        sizePolicy1.setHeightForWidth(self.password_combo_box.sizePolicy().hasHeightForWidth())
        self.password_combo_box.setSizePolicy(sizePolicy1)
        self.password_combo_box.setMinimumSize(QSize(0, 25))

        self.column_remap_layout.addWidget(self.password_combo_box, 2, 1, 1, 1)


        self.centered_layout.addWidget(self.column_remap_group_box)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setSpacing(10)
        self.buttons_layout.setObjectName(u"buttons_layout")
        self.buttons_layout.setContentsMargins(45, -1, 45, -1)
        self.import_button = QPushButton(csv_import_popup_widget)
        self.import_button.setObjectName(u"import_button")
        self.import_button.setMinimumSize(QSize(0, 30))
        self.import_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.buttons_layout.addWidget(self.import_button)

        self.cancel_button = QPushButton(csv_import_popup_widget)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setMinimumSize(QSize(0, 30))
        self.cancel_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.buttons_layout.addWidget(self.cancel_button)


        self.centered_layout.addLayout(self.buttons_layout)


        self.csv_import_popup_layout.addLayout(self.centered_layout)

        self.progress_bar = QProgressBar(csv_import_popup_widget)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setMaximumSize(QSize(16777215, 16))
        self.progress_bar.setTextVisible(False)

        self.csv_import_popup_layout.addWidget(self.progress_bar)


        self.retranslateUi(csv_import_popup_widget)

        QMetaObject.connectSlotsByName(csv_import_popup_widget)
    # setupUi

    def retranslateUi(self, csv_import_popup_widget):
        self.title_label.setText(QCoreApplication.translate("csv_import_popup_widget", u"\u0418\u043c\u043f\u043e\u0440\u0442 \u0438\u0437 csv \u0444\u0430\u0439\u043b\u0430", None))
        self.csv_file_label.setText(QCoreApplication.translate("csv_import_popup_widget", u"\u041f\u0443\u0442\u044c \u043a \u0444\u0430\u0439\u043b\u0443:", None))
        self.csv_file_browser_button.setText(QCoreApplication.translate("csv_import_popup_widget", u"...", None))
        self.column_remap_group_box.setTitle(QCoreApplication.translate("csv_import_popup_widget", u"\u0420\u0435\u043c\u0430\u043f\u043f\u0438\u043d\u0433 \u043a\u043e\u043b\u043e\u043d\u043e\u043a", None))
        self.site_url_label.setText(QCoreApplication.translate("csv_import_popup_widget", u"site_url:", None))
        self.login_label.setText(QCoreApplication.translate("csv_import_popup_widget", u"login:", None))
        self.password_label.setText(QCoreApplication.translate("csv_import_popup_widget", u"password:", None))
        self.import_button.setText(QCoreApplication.translate("csv_import_popup_widget", u"\u0418\u043c\u043f\u043e\u0440\u0442", None))
        self.cancel_button.setText(QCoreApplication.translate("csv_import_popup_widget", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        pass
    # retranslateUi


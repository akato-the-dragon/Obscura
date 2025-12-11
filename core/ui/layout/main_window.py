# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)

class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(840, 520)
        main_window.setMinimumSize(QSize(500, 0))
        self.exit_action = QAction(main_window)
        self.exit_action.setObjectName(u"exit_action")
        self.import_csv_action = QAction(main_window)
        self.import_csv_action.setObjectName(u"import_csv_action")
        self.create_password = QAction(main_window)
        self.create_password.setObjectName(u"create_password")
        self.create_quick_password = QAction(main_window)
        self.create_quick_password.setObjectName(u"create_quick_password")
        self.action_version = QAction(main_window)
        self.action_version.setObjectName(u"action_version")
        self.action_version.setEnabled(False)
        self.service_status_action = QAction(main_window)
        self.service_status_action.setObjectName(u"service_status_action")
        self.service_status_action.setEnabled(False)
        self.github_page_action = QAction(main_window)
        self.github_page_action.setObjectName(u"github_page_action")
        self.download_extension_action = QAction(main_window)
        self.download_extension_action.setObjectName(u"download_extension_action")
        self.export_csv_action = QAction(main_window)
        self.export_csv_action.setObjectName(u"export_csv_action")
        self.set_master_action = QAction(main_window)
        self.set_master_action.setObjectName(u"set_master_action")
        self.remove_master_action = QAction(main_window)
        self.remove_master_action.setObjectName(u"remove_master_action")
        self.master_status_action = QAction(main_window)
        self.master_status_action.setObjectName(u"master_status_action")
        self.master_status_action.setEnabled(False)
        self.extension_status_action = QAction(main_window)
        self.extension_status_action.setObjectName(u"extension_status_action")
        self.extension_status_action.setEnabled(False)
        self.main_widget = QWidget(main_window)
        self.main_widget.setObjectName(u"main_widget")
        self.main_layout = QVBoxLayout(self.main_widget)
        self.main_layout.setSpacing(0)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.stacked_widget = QStackedWidget(self.main_widget)
        self.stacked_widget.setObjectName(u"stacked_widget")

        self.main_layout.addWidget(self.stacked_widget)

        main_window.setCentralWidget(self.main_widget)
        self.menu_bar = QMenuBar(main_window)
        self.menu_bar.setObjectName(u"menu_bar")
        self.menu_bar.setGeometry(QRect(0, 0, 840, 21))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_bar.sizePolicy().hasHeightForWidth())
        self.menu_bar.setSizePolicy(sizePolicy)
        self.general_menu = QMenu(self.menu_bar)
        self.general_menu.setObjectName(u"general_menu")
        self.service_menu = QMenu(self.general_menu)
        self.service_menu.setObjectName(u"service_menu")
        self.passwords_menu = QMenu(self.menu_bar)
        self.passwords_menu.setObjectName(u"passwords_menu")
        self.generator_menu = QMenu(self.menu_bar)
        self.generator_menu.setObjectName(u"generator_menu")
        self.help_menu = QMenu(self.menu_bar)
        self.help_menu.setObjectName(u"help_menu")
        main_window.setMenuBar(self.menu_bar)

        self.menu_bar.addAction(self.general_menu.menuAction())
        self.menu_bar.addAction(self.passwords_menu.menuAction())
        self.menu_bar.addAction(self.generator_menu.menuAction())
        self.menu_bar.addAction(self.help_menu.menuAction())
        self.general_menu.addAction(self.service_menu.menuAction())
        self.general_menu.addSeparator()
        self.general_menu.addAction(self.exit_action)
        self.service_menu.addAction(self.service_status_action)
        self.service_menu.addAction(self.extension_status_action)
        self.passwords_menu.addAction(self.import_csv_action)
        self.passwords_menu.addAction(self.export_csv_action)
        self.generator_menu.addAction(self.create_password)
        self.generator_menu.addAction(self.create_quick_password)
        self.help_menu.addAction(self.github_page_action)
        self.help_menu.addSeparator()
        self.help_menu.addAction(self.download_extension_action)
        self.help_menu.addSeparator()
        self.help_menu.addAction(self.action_version)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        self.exit_action.setText(QCoreApplication.translate("main_window", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.import_csv_action.setText(QCoreApplication.translate("main_window", u"\u0418\u043c\u043f\u043e\u0440\u0442 \u0438\u0437 csv...", None))
        self.create_password.setText(QCoreApplication.translate("main_window", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c...", None))
        self.create_quick_password.setText(QCoreApplication.translate("main_window", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0431\u044b\u0441\u0442\u0440\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.action_version.setText(QCoreApplication.translate("main_window", u"\u0412\u0435\u0440\u0441\u0438\u044f: <version>", None))
        self.service_status_action.setText(QCoreApplication.translate("main_window", u"\u0421\u0435\u0440\u0432\u0438\u0441: <service_status>", None))
        self.github_page_action.setText(QCoreApplication.translate("main_window", u"\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 github", None))
        self.download_extension_action.setText(QCoreApplication.translate("main_window", u"\u0421\u043a\u0430\u0447\u0430\u0442\u044c \u0440\u0430\u0441\u0448\u0438\u0440\u0435\u043d\u0438\u0435", None))
        self.export_csv_action.setText(QCoreApplication.translate("main_window", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442 \u0432 csv...", None))
        self.set_master_action.setText(QCoreApplication.translate("main_window", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.remove_master_action.setText(QCoreApplication.translate("main_window", u"\u0421\u043d\u044f\u0442\u044c", None))
        self.master_status_action.setText(QCoreApplication.translate("main_window", u"\u0421\u0442\u0430\u0442\u0443\u0441: <master_status>", None))
        self.extension_status_action.setText(QCoreApplication.translate("main_window", u"\u0420\u0430\u0441\u0448\u0438\u0440\u0435\u043d\u0438\u0435: <extension_status>", None))
        self.general_menu.setTitle(QCoreApplication.translate("main_window", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
        self.service_menu.setTitle(QCoreApplication.translate("main_window", u"\u0421\u0435\u0440\u0432\u0438\u0441", None))
        self.passwords_menu.setTitle(QCoreApplication.translate("main_window", u"\u041f\u0430\u0440\u043e\u043b\u0438", None))
        self.generator_menu.setTitle(QCoreApplication.translate("main_window", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0442\u043e\u0440", None))
        self.help_menu.setTitle(QCoreApplication.translate("main_window", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
        pass
    # retranslateUi


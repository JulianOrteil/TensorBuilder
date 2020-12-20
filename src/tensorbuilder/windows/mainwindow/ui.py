# Copyright 2020 Julian_Orteil

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Main window widget builder module.

This module builds and configures the widgets of the main window.

'UiMainWindow' is the primary builder class for the main window. The
class is a mixin, so it can be inherited in any order. the 'setup_ui'
function should be called to build the widgets.

Importing everything from this module will only import the variables as
defined by the '__all__' attribute.
"""


from __future__ import absolute_import
from __future__ import annotations
from __future__ import division
from __future__ import print_function


__all__ = ["UiMainWindow"]


from PyQt5.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import (
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget
)


class UiMainWindow(object):
    """The primary builder class of the main window.

    Call :meth:`setup_ui()` to build the widgets of the window.

    Example Usage:
        >>> from PyQt5.QtWidgets import QMainWindow
        >>>
        >>> from tensorbuilder.windows.mainwindow.ui import UiMainWindow
        >>>
        >>> class MainWindow(Ui_MainWindow, QMainWindow):
        >>>     ...
    """

    _central_widget: QWidget
    _central_layout: QGridLayout

    _main_container: QFrame

    _navbar: QFrame
    _navbar_layout: QVBoxLayout
    _home_button: QPushButton
    _builder_button: QPushButton
    _configuration_button: QPushButton
    _help_button: QPushButton
    _copyright_label: QLabel

    _menubar: QFrame
    _menubar_layout: QHBoxLayout
    _app_logo: QLabel
    _menubar_main_container: QFrame

    def setup_ui(self, TensorBuilder: QMainWindow):
        """Creates and configures the widgets of the main window."""

        # Setup the window
        TensorBuilder.resize(1920, 1080)

        icon = QIcon()
        icon.addPixmap(
            QPixmap(":/images/images/tensorbuilder-icon.png"),
            QIcon.Normal,
            QIcon.Off
        )

        TensorBuilder.setWindowIcon(icon)
        TensorBuilder.setMinimumSize(QSize(800, 600))  # Conform to Microsoft standards
        TensorBuilder.setObjectName("TensorBuilder")

        size_policy = QSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(TensorBuilder.sizePolicy().hasHeightForWidth())

        TensorBuilder.setSizePolicy(size_policy)
        TensorBuilder.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgba(255, 255, 255, 0);\n"
            "    padding: 5px 0px 5px 25px;\n"
            "    text-align: left;\n"
            "}\n"
            "\n"
            "QPushButton::hover {\n"
            "    background-color: rgba(255, 255, 255, 50);\n"
            "    border-radius: 10px;\n"
            "}\n"
            "\n"
            "QPushButton::pressed {\n"
            "    background-color: rgba(255, 255, 255, 127);\n"
            "}\n"
            "\n"
            "#central_widget {\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 172, 0, 255), stop:1 rgba(255, 37, 0, 255));\n"
            "}\n"
            "\n"
            "#copyright_label {\n"
            "    color: gray;\n"
            "}\n"
            "\n"
            "#main_container {\n"
            "    background-color: white;\n"
            "    border-top-left-radius: 15px;\n"
            "}\n"
            "\n"
            "#searchbox {\n"
            "    border-bottom: 1px solid rgb(190, 190, 190);\n"
            "    border-left: none;\n"
            "    border-right: none;\n"
            "    border-top: none;\n"
            "    margin-left: 5px;\n"
            "    margin-right: 5px;\n"
            "    padding-left: 10px;\n"
            "}`"
        )

        # Create and configure the central widget
        self._central_widget = QWidget(TensorBuilder)
        self._central_widget.setObjectName("central_widget")

        size_policy = QSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self._central_widget.sizePolicy().hasHeightForWidth())

        self._central_widget.setSizePolicy(size_policy)

        self._central_layout = QGridLayout(self._central_widget)
        self._central_layout.setContentsMargins(0, 0, 0, 0)
        self._central_layout.setObjectName("central_layout")
        self._central_layout.setSpacing(0)

        # Create the main container
        self._setup_main_container()

        # Create the navbar
        self._setup_navbar()

        # Create the menubar
        self._setup_menubar()

        # Add widgets to the central layout
        self._central_layout.addWidget(self._menubar, 0, 0, 1, 2)
        self._central_layout.addWidget(self._main_container, 1, 1, 1, 1)
        self._central_layout.addWidget(self._navbar, 1, 0, 1, 1)

        TensorBuilder.setCentralWidget(self._central_widget)

        self._retranslate_ui(TensorBuilder)
        QMetaObject.connectSlotsByName(TensorBuilder)

    def _setup_main_container(self) -> None:
        # Create the main container
        self._main_container = QFrame(self._central_widget)
        self._main_container.setFrameShadow(QFrame.Raised)
        self._main_container.setFrameShape(QFrame.StyledPanel)
        self._main_container.setObjectName("main_container")

        size_policy = QSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )
        size_policy.setHorizontalStretch(6)
        size_policy.setVerticalStretch(25)
        size_policy.setHeightForWidth(self._main_container.sizePolicy().hasHeightForWidth())

        self._main_container.setSizePolicy(size_policy)

    def _setup_navbar(self) -> None:
        # Create the navbar
        self._navbar = QFrame(self._main_container)
        self._navbar.setFrameShadow(QFrame.Raised)
        self._navbar.setFrameShape(QFrame.StyledPanel)
        self._navbar.setMinimumSize(QSize(275, 0))
        self._navbar.setObjectName("navbar")

        size_policy = QSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )
        size_policy.setHorizontalStretch(1)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self._navbar.sizePolicy().hasHeightForWidth())

        self._navbar.setSizePolicy(size_policy)

        self._navbar_layout = QVBoxLayout(self._navbar)
        self._navbar_layout.setContentsMargins(0, 25, 0, 15)
        self._navbar_layout.setObjectName("navbar_layout")
        self._navbar_layout.setSpacing(15)

        # Create the home button
        self._home_button = QPushButton(self._navbar)

        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)

        self._home_button.setFont(font)

        home_icon = QIcon()
        home_icon.addPixmap(
            QPixmap(":/images/images/home_icon.png"),
            QIcon.Normal,
            QIcon.Off
        )

        self._home_button.setIcon(home_icon)
        self._home_button.setIconSize(QSize(20, 20))
        self._home_button.setObjectName("home_button")

        size_policy = QSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Fixed
        )
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self._home_button.sizePolicy().hasHeightForWidth())

        self._home_button.setSizePolicy(size_policy)

        # Create the builder button
        self._builder_button = QPushButton(self._navbar)

        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)

        self._builder_button.setFont(font)

        builder_icon = QIcon()
        builder_icon.addPixmap(
            QPixmap(":/images/images/builder_icon.png"),
            QIcon.Normal,
            QIcon.Off
        )

        self._builder_button.setIcon(builder_icon)
        self._builder_button.setIconSize(QSize(20, 20))
        self._builder_button.setObjectName("builder_button")

        size_policy = QSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Fixed
        )
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self._builder_button.sizePolicy().hasHeightForWidth())

        self._builder_button.setSizePolicy(size_policy)

        # Create the configuration button
        self._configuration_button = QPushButton(self._navbar)

        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)

        self._configuration_button.setFont(font)

        configuration_icon = QIcon()
        configuration_icon.addPixmap(
            QPixmap(":/images/images/configuration_icon.png"),
            QIcon.Normal,
            QIcon.Off
        )

        self._configuration_button.setIcon(configuration_icon)
        self._configuration_button.setIconSize(QSize(20, 20))
        self._configuration_button.setObjectName("configuration_button")

        size_policy = QSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Fixed
        )
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self._configuration_button.sizePolicy().hasHeightForWidth())

        self._configuration_button.setSizePolicy(size_policy)

        # Create the help button
        self._help_button = QPushButton(self._navbar)

        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)

        self._help_button.setFont(font)

        help_icon = QIcon()
        help_icon.addPixmap(
            QPixmap(":/images/images/help_icon.png"),
            QIcon.Normal,
            QIcon.Off
        )

        self._help_button.setIcon(help_icon)
        self._help_button.setIconSize(QSize(20, 20))
        self._help_button.setObjectName("help_button")

        size_policy = QSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Fixed
        )
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self._help_button.sizePolicy().hasHeightForWidth())

        self._help_button.setSizePolicy(size_policy)

        navbar_vertical_spacer = QSpacerItem(
            20,
            40,
            QSizePolicy.Minimum,
            QSizePolicy.Expanding
        )

        self._copyright_label = QLabel(self._navbar)
        self._copyright_label.setAlignment(Qt.AlignCenter)

        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)

        self._copyright_label.setFont(font)
        self._copyright_label.setObjectName("copyright_label")

        # Add widgets to navbar layout
        self._navbar_layout.addWidget(self._home_button)
        self._navbar_layout.addWidget(self._builder_button)
        self._navbar_layout.addWidget(self._configuration_button)
        self._navbar_layout.addWidget(self._help_button)
        self._navbar_layout.addItem(navbar_vertical_spacer)
        self._navbar_layout.addWidget(self._copyright_label)

    def _setup_menubar(self) -> None:
        # Create the menubar
        self._menubar = QFrame(self._central_widget)
        self._menubar.setFrameShadow(QFrame.Raised)
        self._menubar.setFrameShape(QFrame.StyledPanel)
        self._menubar.setObjectName("menubar")

        size_policy = QSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )
        size_policy.setHorizontalStretch(1)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self._menubar.sizePolicy().hasHeightForWidth())

        self._menubar.setSizePolicy(size_policy)

        self._menubar_layout = QHBoxLayout(self._menubar)
        self._menubar_layout.setContentsMargins(0, 0, 0, 0)
        self._menubar_layout.setObjectName("menubar_layout")
        self._menubar_layout.setSpacing(0)

        # Create the app logo
        self._app_logo = QLabel(self._menubar)
        self._app_logo.setObjectName("app_logo")
        self._app_logo.setPixmap(  # TODO: Scale the pixmap
            QPixmap(":/images/images/tensorbuilder-logo-horizontal-black-white.png")
        )
        self._app_logo.setText('')

        size_policy = QSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )
        size_policy.setHorizontalStretch(1)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self._app_logo.sizePolicy().hasHeightForWidth())

        self._app_logo.setSizePolicy(size_policy)

        # Create the menubar main container
        self._menubar_main_container = QFrame(self._menubar)
        self._menubar_main_container.setFrameShadow(QFrame.Raised)
        self._menubar_main_container.setFrameShape(QFrame.StyledPanel)
        self._menubar_main_container.setObjectName("menubar_main_container")

        size_policy = QSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )
        size_policy.setHorizontalStretch(6)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self._menubar_main_container.sizePolicy().hasHeightForWidth())

        self._menubar_main_container.setSizePolicy(size_policy)

        # Add widgets to the menu layout
        self._menubar_layout.addWidget(self._app_logo)
        self._menubar_layout.addWidget(self._menubar_main_container)

    def _retranslate_ui(self, TensorBuilder: QMainWindow) -> None:
        _translate = QCoreApplication.translate

        TensorBuilder.setWindowTitle(_translate("TensorBuilder", "TensorBuilder"))
        self._home_button.setText(_translate("TensorBuilder", "Home"))
        self._builder_button.setText(_translate("TensorBuilder", "Network Builder"))
        self._configuration_button.setText(_translate("TensorBuilder", "Configuration"))
        self._help_button.setText(_translate("TensorBuilder", "Help"))
        self._copyright_label.setText(
            _translate("TensorBuilder", "Copyright 2020, Julian_Orteil\nAll Rights Reserved")
        )

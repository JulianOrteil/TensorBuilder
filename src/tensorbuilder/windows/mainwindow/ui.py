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

'UiMainWindow' is the primary builder class for the main window. It is
meant to be inherited before the window type (i.e. 'QMainWindow') and
the 'setup_ui' function should be called to build the widgets.
"""


from __future__ import absolute_import
from __future__ import annotations
from __future__ import division
from __future__ import print_function


from PyQt5.QtCore import QObject, QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QGridLayout, QMainWindow, QSizePolicy, QWidget


class UiMainWindow(QObject):
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

    def _setup_main_container() -> None:
        pass

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

"""Handles the user interactions for the main window.

'MainWindow' is the primary functions controller of the window. When the
user interacts with the widgets of the window, the interaction will be
handled here.

Importing everything from this module will only import the variables as
defined by the '__all__' attribute.
"""


from __future__ import absolute_import
from __future__ import annotations
from __future__ import division
from __future__ import print_function


__all__ = ["MainWindow"]


from loguru import logger
from PyQt5.QtCore import QObject, pyqtSlot

from .model import MainWindowModel
from .view import MainWindowView


class MainWindow(QObject):
    """Processes the user interactions of the main window.

    User interactions are intercepted by the view of the window,
    however, they are processed in this class.

    When a display update is requested from somewhere in the
    application, it should be slotted to a function to process in this
    class.

    Example Usage:
        >>> from tensorbuilder.windows.mainwindow.controller import MainWindow
        >>>
        >>> mainwindow = MainWindow()
    """

    _model: MainWindowModel
    _view: MainWindowView

    def __init__(self) -> None:
        logger.debug(f"Initializing {__name__}.{__class__.__name__}")
        super().__init__()

        self._model = MainWindowModel()
        self._view = MainWindowView()

        # Connect signals to slots
        self._connect_signals()

        logger.success(f"Successfully initialized {__name__}.{__class__.__name__}")

    def _connect_signals(self) -> None:
        logger.debug("Connecting main window controller signals")

        self._view.home_button_clicked.connect(self._on_home_button_clicked)
        self._view.builder_button_clicked.connect(self._on_builder_button_clicked)
        self._view.configuration_button_clicked.connect(self._on_configuration_button_clicked)
        self._view.help_button_clicked.connect(self._on_help_button_clicked)

    @pyqtSlot()
    def _on_home_button_clicked(self) -> None:
        logger.info("User clicked on the home button")

    @pyqtSlot()
    def _on_builder_button_clicked(self) -> None:
        logger.info("User clicked on the builder button")

    @pyqtSlot()
    def _on_configuration_button_clicked(self) -> None:
        logger.info("User clicked on the configuration button")

    @pyqtSlot()
    def _on_help_button_clicked(self) -> None:
        logger.info("User clicked on the help button")

    def close(self) -> None:
        """Closes the window."""

        self._view.close()

    def show(self) -> None:
        """Shows the window."""

        self._view.show()

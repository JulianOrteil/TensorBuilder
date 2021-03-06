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

"""Main window display handler.

'MainWindowView' manages display events for the main window. When a
display change needs to occur, this class is where the interface should
exist to perform that change.

Importing everything from this module will only import the variables as
defined by the '__all__' attribute.
"""


from __future__ import absolute_import
from __future__ import annotations
from __future__ import division
from __future__ import print_function


__all__ = ["MainWindowView"]


from typing import Optional

from loguru import logger
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

from tensorbuilder.utils import QMainWindow
from .ui import UiMainWindow


class MainWindowView(UiMainWindow, QMainWindow):
    """Manages display events for the main window.

    When the user interacts with the main window, depending on that
    event, it is intercepted and handled in this class. Also, any
    display changes should be managed within this class.

    Attributes:
        home_button_clicked (:obj:`pyqtSignal`):
            The signal fired when the home button has been clicked.
            Nothing is sent through the signal
        builder_button_clicked (:obj:`pyqtSignal`):
            The signal fired when the builder button has been clicked.
            Nothing is sent through the signal
        configuration_button_clicked (:obj:`pyqtSignal`):
            The signal fired when the configuration button has been
            clicked. Nothing is sent through the signal
        help_button_clicked (:obj:`pyqtSignal`):
            The signal fired when the help button has been clicked.
            Nothing is sent through the signal

    Example Usage:
        >>> from tensorbuilder.windows.mainwindow.view import MainWindowView
        >>>
        >>> class MainWindow(object):
        ...     _view: MainWindowView
        ...
        ...     def __init__(self) -> None:
        ...         super().__init__()
        ...
        ...         self._view = MainWindowView()
        ...
    """

    home_button_clicked = pyqtSignal()
    builder_button_clicked = pyqtSignal()
    configuration_button_clicked = pyqtSignal()
    help_button_clicked = pyqtSignal()

    def __init__(
        self,
        parent: Optional[QObject] = None
    ) -> None:
        logger.debug(f"Initializing {__name__}.{__class__.__name__}")
        super().__init__(parent=parent)

        # Build the window widgets
        self.setup_ui(self)

        # Connect signals to slots
        self._connect_signals()

        logger.success(f"Successfully initialized {__name__}.{__class__.__name__}")

    def _connect_signals(self) -> None:
        logger.debug("Connecting main window view signals")

        self._home_button.clicked.connect(self._on_home_button_clicked)
        self._builder_button.clicked.connect(self._on_builder_button_clicked)
        self._configuration_button.clicked.connect(self._on_configuration_button_clicked)
        self._help_button.clicked.connect(self._on_help_button_clicked)

    @pyqtSlot()
    def _on_home_button_clicked(self) -> None:
        self.home_button_clicked.emit()

    @pyqtSlot()
    def _on_builder_button_clicked(self) -> None:
        self.builder_button_clicked.emit()

    @pyqtSlot()
    def _on_configuration_button_clicked(self) -> None:
        self.configuration_button_clicked.emit()

    @pyqtSlot()
    def _on_help_button_clicked(self) -> None:
        self.help_button_clicked.emit()

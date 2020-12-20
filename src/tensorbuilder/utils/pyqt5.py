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

"""Reimplemented or extended functionality of certain 'PyQt5' objects.

'QMainWindow' extends the functionality of PyQt5's 'QMainWindow' by
introducing 'pyqtSignal's that emit when certain user events occur.
Currently, the events emitted are: mouse hover events, mouse click
events, window close events, and keypress events.

Importing everything from this module will only import the variables as
defined by the '__all__' attribute.
"""


from __future__ import absolute_import
from __future__ import annotations
from __future__ import division
from __future__ import print_function


__all__ = ["QMainWindow"]


from typing import Optional, Union

from PyQt5.QtCore import QEvent, Qt, pyqtSignal
from PyQt5.QtGui import QCloseEvent, QKeyEvent, QMouseEvent
from PyQt5.QtWidgets import QMainWindow as _QMainWindow, QWidget


class QMainWindow(_QMainWindow):
    """An extended class of PyQt5's :obj:`QMainWindow`.

    This class extends the functionality of the :obj:`QMainWindow` by
    adding :obj:`pyqtSignal`s that emit when certain user events occur.

    This class is meant to be inherited. If the parent class also has a
    widget builder class, this class should then be inherited after the
    builder class.

    Args:
        parent (:obj:`QWidget`, optional):
            The parent widget for this class. If the parent is
            :obj:`None`, then this class will be considered to be a
            top-level widget.
            Defaults to :obj:`None`.

    Attributes:
        closed (:obj:`pyqtSignal`):
            The signal fired when the window is to be closed. The
            :obj:`QCloseEvent` is sent through the signal.
        keypressed (:obj:`pyqtSignal`):
            The signal fired when the user presses a key with the window
            focused. The :obj:`QKeyEvent` is sent through the signal.
        mouse_hover_changed (:obj:`pyqtSignal`):
            The signal fired when the mouse enters or leaves a widget in
            which :term:`installEventFilter(self)` has been called.
            :term:`self` should be the class in which this class is
            subclassed. A tuple of :obj:`(sender, QMouseEvent)` is sent
            through the signal.
        mouse_released (:obj:`pyqtSignal`):
            The signal fired when a mouse button has been released. The
            :obj:`QMouseEvent` is sent through the signal.

    Example Usage:
        >>> from tensorbuilder.utils.pyqt5 import QMainWindow
        >>> from tensorbuilder.examplewindow.ui import UiExampleWindow
        >>>
        >>> # Example usage without builder class
        >>> class ExampleWindow1(QMainWindow):
        ...     pass
        ...
        >>>
        >>> # Example usage with builder class
        >>> class ExampleWindow2(UiExampleWindow, QMainWindow):
        ...     pass
        ...
    """

    closed = pyqtSignal(QCloseEvent)
    keypressed = pyqtSignal(QKeyEvent)
    mouse_hover_changed = pyqtSignal(tuple)
    mouse_released = pyqtSignal(QMouseEvent)

    def __init__(
        self,
        parent: Optional[QWidget] = None
    ) -> None:
        super().__init__(parent=parent)

    def closeEvent(self, event: QCloseEvent) -> None:
        self.closed.emit(event)

    def eventFilter(self, sender: QWidget, event: QEvent) -> bool:
        if event.type() in (QEvent.Enter, QEvent.Leave):
            self.mouse_hover_changed.emit((sender, event))
            return True
        return False

    def keyPressEvent(self, event: QKeyEvent) -> None:
        self.keypressed.emit(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self.mouse_released.emit(event)

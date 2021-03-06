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

"""The data model for the main window.

'MainWindowModel' stores the data for the main window.

Importing everything from this module will only import the variables as
defined by the '__all__' attribute.
"""


from __future__ import absolute_import
from __future__ import annotations
from __future__ import division
from __future__ import print_function


__all__ = ["MainWindowModel"]


from dataclasses import dataclass


@dataclass
class MainWindowModel:
    """Stores the data for the main window.

    Attributes:
        .

    Example Usage:
        >>> from tensorbuilder.windows.mainwindow.model import MainWindowModel
        >>>
        >>> class MainWindow(MainWindowModel):
        ...     pass
    """

    pass

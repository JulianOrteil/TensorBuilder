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

"""The interactable windows of the application.

'MainWindow' is the main interactable window of the application. The
window is what the user will primarily interact with.

Importing everything from this module will only import the variables as
defined by the '__all__' attribute.
"""


from __future__ import absolute_import
from __future__ import annotations
from __future__ import division
from __future__ import print_function


__all__ = ["MainWindow"]


from .mainwindow import MainWindow

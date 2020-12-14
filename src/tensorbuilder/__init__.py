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

"""Neural network building made exceptionally easy.

'TensorBuilder' is an application designed to allow for insanely easy
building of custom neural networks for any application. Similar to block
programming, 'TensorBuilder' will allow you to develop neural networks,
from scratch by dragging and dropping 'blocks'. These blocks will then
build the network you design in code behind-the-scenes.

You can then take these models and plug them into your custom training
pipelines to train like you would have if you programmed the model
yourself.

Currently, the application will support only TensorFlow as a backend to
build the networks in; however, other backends like ONNX and PyTorch
will be supported.
"""


from __future__ import absolute_import
from __future__ import annotations
from __future__ import division
from __future__ import print_function


__authors__ = "Julian_Orteil"
__copyright__ = "Copyright 2020, Julian_Orteil"
__credits__ = ["Julian_Orteil"]
__license__ = "Apache 2.0"
__maintainers__ = ["Julian_Orteil"]
__version__ = "0.0.1alpha"


import argparse
import sys
from multiprocessing import freeze_support

from loguru import logger
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QApplication


class Application(QObject):
    pass


class Loader(QObject):
    pass


def parse_args() -> argparse.Namespace:
    """Parses the arguments supplied to the application at launch.

    Returns:
        args (:obj:`Namespace`):
            The parsed arguments supplied to the application at launch.
    """

    # Create the parser
    parser = argparse.ArgumentParser(
        prog="TensorBuilder",
        description="Neural network building made exceptionally easy.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("-v", "--version", help="print the version of the app and then exit.")
    parser.add_argument(
        "-V",
        "--verbose",
        help=(
            "depending on the OS, open a Powershell window or "
            "terminal and display the output of the app."
        )
    )

    return parser.parse_args()


@logger.catch
def main() -> int:
    """The entry function of the application.

    This function is wrapped using loguru's :term:`catch()` decorator
    effectively allowing the application to catch and log every
    exception raised in the MainThread.

    Returns:
        return_code (:obj:`int`):
            The error status code of the application to pass to
            :term:`sys.exit()`.
    """

    # Allow multiprocessing when the application is frozen
    freeze_support()

    # Direct all uncaught exceptions to loguru for handling
    # Most should be caught by the decorater above; however, they may be
    # some that are not
    sys.excepthook = lambda *args: logger.opt(exception=args).error("An uncaught error occurred:\n")

    # Parse command arguments
    args = parse_args()

    # Launch the application
    qapp = QApplication(sys.argv)
    app = Application(args)

    qapp.aboutToQuit.connect(app.quit)

    return qapp.exec_()

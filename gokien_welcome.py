#!/usr/bin/env python
# -*- coding: utf8 -*-
#
# This file is part of the gokien project.
#
# Copyright (C) 2013 Long T. Dam <longdt90@gmail.com>
# Copyright (C) 2013 Trung Ngo <ndtrung4419@gmail.com>
#
# gokien is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# gokien is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with gokien.  If not, see <http://www.gnu.org/licenses/>.
#

import check_first_run
import sys

if not check_first_run.is_first_run():
    sys.exit(0)


import os
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import QWebView
import string
import xdg.IconTheme
import logging
from gi.repository import Gio

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_DIR = os.path.join(ROOT_DIR, 'templates/')  # Don't forget the last slash
HTML_PATH = os.path.join(ROOT_DIR, 'templates/welcome.html')


def _(string):
    """
    Placeholder for GNU gettext.
    """
    return string


class WelcomeSreen(QWebView):

    def __init__(self, width, height):
        QWebView.__init__(self)
        self.app = QApplication.instance()
        self.html = self.parseHtml(HTML_PATH)
        self.setHtml(self.html, baseUrl=QUrl('file://' + HTML_DIR))
        self.setFixedSize(width, height)
        # Move to the center
        screenGeometry = app.desktop().screenGeometry()
        self.move((screenGeometry.width() - width) / 2,
                 (screenGeometry.height() - height) / 2)
        # Remove the border
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Use the titleChanged signal as a means of communication between
        # the JavaScript context and the Python context
        self.titleChanged.connect(self.performAction)
        self.seeMeNoMore = True

    def parseHtml(self, file_path):
        """
        Parse the template file.
        """
        subs = {
            "title": _('Welcome to GokienOS'),
            "show": _('Open this dialog in the next startup'),
            "close": _('Close'),
            "working": _('Working'),
            "document": _('Document'),
            "spreadsheet": _('Spreadsheet'),
            "presentation": _('Presentation'),
            "networking": _('Networking'),
            "web_browser": _('Web Browser'),
            "chat": _('Chat'),
            "extra": _('Extra'),
            "help": _('Help')
        }

        apps = [
            'firefox',
            'empathy',
            'libreoffice-writer',
            "libreoffice-writer",
            "libreoffice-calc",
            "libreoffice-impress",
            "help"
        ]
        s = Gio.Settings.new('org.gnome.desktop.interface')
        theme = s.get_string('icon-theme')
        for app in apps:
            # TODO Determine current theme
            subs['icon_' + app.replace('-', '_')] = \
                xdg.IconTheme.getIconPath(app, theme=theme)

        template = open(file_path, 'r').read()
        html = string.Template(template).safe_substitute(subs)

        logging.debug(html)
        return html

    def performAction(self, title):
        """
        Perform the action specified by the JavaScript context.
        """
        if title == 'close':
            self.app.exit()
        else:
            os.system(title)
        print(title)


def main():
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    app = QApplication(sys.argv)
    welcomeScreen = WelcomeSreen(654, 350)
    welcomeScreen.show()
    app.exec_()

    # Create the lock file if the user does not want to see us anymore
    if welcomeScreen.seeMeNoMore:
        with open(check_first_run.lock_file_path, "w") as f:
            pass


if __name__ == '__main__':
    main()

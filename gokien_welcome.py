#!/usr/bin/env python

import sys
import os
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import QWebView
import string as String
import xdg.IconTheme
import logging

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_DIR = os.path.join(ROOT_DIR, 'templates/') # Don't forget the last slash
HTML_PATH = os.path.join(ROOT_DIR, 'templates/welcome.html')

def _(string):
    """
        Placeholder for GNU gettext
    """
    return string

class WelcomeSreen(QWebView):
    def __init__(self, app, width, height):
        QWebView.__init__(self)
        self.app = app
        self._html = self._parse_html(HTML_PATH)
        self.setHtml(self._html, baseUrl = QUrl('file://' + HTML_DIR))
        self.setFixedSize(width, height)
        # Move to the center
        screen_geometry = app.desktop().screenGeometry()
        self.move((screen_geometry.width() - width) / 2, 
            (screen_geometry.height() - height) / 2)
        # Remove the border
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        # Handle event titleChanged 
        self.titleChanged.connect(self._title_changed)
        

    def _parse_html(self, file_path):
        """
            Parse the template file and return the resultant content
        """
        subs = {}
        # Codename and version
        subs['title'] = _('Welcome to GokienOS')
        subs['show'] = _('Open this dialog in the next startup')
        subs['close'] = _('Close')
        subs['working'] = _('Working')
        subs['document'] = _('Document')
        subs['spreadsheet'] = _('Spreadsheet')
        subs['presentation'] = _('Presentation')
        subs['networking'] = _('Networking')
        subs['web_browser'] = _('Web Browser') 
        subs['chat'] = _('Chat')
        subs['extra'] = _('Extra')
        subs['help'] = _('Help')
        



        firefox_icon = xdg.IconTheme.getIconPath('firefox', theme='Leon')
        empathy_icon = xdg.IconTheme.getIconPath('empathy', theme='Leon')

        subs['icon_firefox'] = firefox_icon
        subs['icon_empathy'] = empathy_icon
        logging.debug(firefox_icon)
        
        template = open(file_path, 'r').read()
        html = String.Template(template).safe_substitute(subs)

        print html
        return html


    
    def _title_changed(self,title):
        """
            Handle the signal titleChanged
        """
        if title == 'close':
            self.app.exit()
        else:
            os.system(title);
        print(title)


def main(sys_argv):
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    app = QApplication(sys_argv)
    gokien_welcome_screen = WelcomeSreen(app, 654, 350)
    gokien_welcome_screen.show()
    app.exec_()

if __name__ == '__main__':
    main(sys.argv)

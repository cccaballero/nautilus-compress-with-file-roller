"""

"Compress with File-Roller" Nautilus extension

Copyright (c) 2018 Carlos Cesar Caballero Diaz.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

"""

import os
import subprocess
from distutils.spawn import find_executable

# A way to get unquote working with python 2 and 3
try:
    from urllib import unquote
except ImportError:
    from urllib.parse import unquote

import gi
from gi.repository import Nautilus, GObject


class OpenTerminalExtension(Nautilus.MenuProvider, GObject.GObject):
    def __init__(self):
        self.file_roller_exists = self._file_roller_exists()

    def _file_roller_exists(self):
        return find_executable('file-roller') is not None
        
    def _open_file_roller(self, files):
        filenames = []
        for file in files:
            filenames.append(unquote(file.get_uri()[7:]))
        subprocess.Popen(['file-roller', '-d'] + filenames)
    
    def menu_activate_cb(self, menu, files):
        self._open_file_roller(files)
        
    def menu_background_activate_cb(self, menu, file): 
        self._open_file_roller([file])
        
    def get_file_items(self, window, files):
        if not self.file_roller_exists:
            return
        for file in files:
            if file.get_uri_scheme() != 'file':
                return
        
        item = Nautilus.MenuItem(name='NautilusPython::openfileroller_file_item',
                                 label='Compress with File-Roller...' ,
                                 tip='Compress File(s)')
        item.connect('activate', self.menu_activate_cb, files)
        return item,

    def get_background_items(self, window, file):
        if not self.file_roller_exists:
            return
        item = Nautilus.MenuItem(name='NautilusPython::openfileroller_file_item2',
                                 label='Compress with File-Roller...' ,
                                 tip='Compress %s' % file.get_name())
        item.connect('activate', self.menu_background_activate_cb, file)
        return item,


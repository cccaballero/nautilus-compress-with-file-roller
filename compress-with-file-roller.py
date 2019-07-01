"""

"Compress with File-Roller" Nautilus extension

"THE SODA-WARE LICENSE":
As long as you retain this notice you can do whatever you want 
with this stuff. If we meet some day, and you think
this stuff is worth it, you can buy me a soda in return. 

Carlos Cesar Caballero Diaz.

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


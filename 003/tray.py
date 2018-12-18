"""
System tray commands example script.
"""
import os
from collections import namedtuple

import pystray
from pystray import MenuItem, Menu
from PIL import Image

HERE = os.path.dirname(__file__)
ICO_PATH = os.path.join(HERE, os.pardir, 'icon.png')  # needs your own icon.png

CommandItem = namedtuple('CommandItem', 'text, action, default')

COMMANDS = [
    CommandItem('hello', 'echo hello', True),
    CommandItem('world', 'echo world', False),
]

def create_commands(commands_dict):
    def create_callable(command):
        def run (*_):
            # you probably want to replace this with
            # the subprocess module later:
            os.system(command)

        return run

    commands = [MenuItem(text, create_callable(command), default=default)
                for text, command, default in COMMANDS]
    return commands

def main():
    tray = pystray.Icon('tray-test')
    image = Image.open(ICO_PATH)
    tray.icon = image
    menu = Menu(*create_commands(COMMANDS))
    tray.menu = menu
    tray.run(show)

def show(icon):
    icon.visible = True


if __name__ == '__main__':
    main()
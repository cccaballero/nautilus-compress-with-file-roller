# nautilus-compress-with-file-roller

This extension includes an option to the Nautilus file manager contextual menu for compressing files using the File-Roller tool, just like it worked before Gnome removed it.

## Why?

Because I like it and I was really annoyed by Gnome removing all the options provided by File-Roller when compressing files in the Gnome Desktop.

## How install it?

First you need to install the Python bindings for the Nautilus extension framework, if you are in a debian based distribution just:

    apt install python-nautilus

And then you can download the extension and include it in the `~/.local/share/nautilus-python/extensions` folder:

    curl https://raw.githubusercontent.com/cccaballero/nautilus-compress-with-file-roller/master/compress-with-file-roller.py --create-dirs -o ~/.local/share/nautilus-python/extensions/compress-with-file-roller.py

After that, you need to restart nautilus to changes take effect, you can use:

    killall nautilus

Or restart the user session.


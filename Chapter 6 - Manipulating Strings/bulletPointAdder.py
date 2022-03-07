#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

# Automate the Boring Stuff by Al Sweigart
# pg 147

"""
OBJECTIVES: 
1. Paste text from the clipboard.
2. Do something to it.
3. Copy the new text to the clipboard
"""

import pyperclip
text = pyperclip.paste()

# TODO: Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):     # loop through all indexis for "lines" list
    lines[i] = '* ' + lines[i]  # add star to each string in "lines" list
text = '\n'.join(lines)
pyperclip.copy(text)

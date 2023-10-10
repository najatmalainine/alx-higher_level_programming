#!/usr/bin/python3
"""Search and update func"""


def append_after(filename="", search_string="", new_string=""):
    """Appends `new_string` after lines that
    include `search_string` in the file."""

    # Open the file in read and write mode ('r+')
    with open(filename, mode="r+", encoding="utf-8") as f:
        new_text = ""

        # Iterate through each line in the file
        for line in f:
            new_text += line  # Copy the original line to the `new_text`

            if search_string in line:
                new_text += new_string

        f.seek(0)

        f.write(new_text)

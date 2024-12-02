import math

BORDER_LENGTH = 86
EXTRA_SPACE_LENGTH = 2
HEADER_BORDER = "="

methods = [
    "HEAD",
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE"
]

def create_border(title):
    if len(title) % 2 != 0:
        title += " "

    border_side_length = int((BORDER_LENGTH / 2) - (len(title) / 2) - (EXTRA_SPACE_LENGTH / 2))

    return (HEADER_BORDER * border_side_length) + (" " * int(EXTRA_SPACE_LENGTH / 2)) + title + (" " * int(EXTRA_SPACE_LENGTH / 2)) + (HEADER_BORDER * border_side_length)

for method in methods:
    print(create_border(method))
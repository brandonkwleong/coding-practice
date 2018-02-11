#!/usr/local/python3

# Question:
# Given an absolute path for a file (Unix-style), simplify it.
#
# Example 1: /home/ ==> /home
# Example 2: /a/./b/../../c/ ==> /c

def simplifyPath(self, path):
    pl = path.split("/")

    # If the last record is blank, remove it (meaning trailing slash)
    if pl[-1] == '':
        pl.pop()

    finalPath = []

    # Always start from index 1, as first value is always a slash
    for val in pl[1:]:

        # Same directory
        if val == ".":
            continue

        # Parent directory
        elif val == "..":

            # If the value is the root node, going to the
            # parent does nothing
            if len(finalPath) == 0:
                continue
            finalPath.pop()

        # Blank - handles multiple slash case
        elif val == "":
            continue

        # Otherwise, append the directory name
        else:
            finalPath.append(val)

    if len(finalPath) == 0:
        return "/"

    return "/{}".format("/".join(finalPath))


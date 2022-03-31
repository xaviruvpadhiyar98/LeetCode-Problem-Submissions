# Simplify Path

"""
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

    The path starts with a single slash '/'.
    Any two directories are separated by a single slash '/'.
    The path does not end with a trailing '/'.
    The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')

Return the simplified canonical path.
"""

# Example 1:
# Input: path = "/home/"
# Output: "/home"
# Example 2:
# Input: path = "/a/./b/../../c/"
# Output: "/a/c"


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        # Split the path into a list of strings
        for p in path.split("/"):
            # If the path is empty or the path is a single slash, skip
            if p == "..":
                # If the stack is empty, skip
                if stack:
                    stack.pop()
            # If the path is a double slash, skip
            elif p != "." and p:
                stack.append(p)
        # Join the list of strings into a path
        return "/" + "/".join(stack)

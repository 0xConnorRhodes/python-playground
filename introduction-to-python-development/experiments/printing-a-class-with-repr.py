#!/usr/bin/env python 3

class Todo:
    """
    Takes name and status
    """

    def __init__(self, name, completed=False):
        self.name = name
        self.completed = completed

    def __repr__(self):
        return f"{self.name} {self.completed}"

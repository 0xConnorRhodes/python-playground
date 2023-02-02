#!/usr/bin/env python3

class Car:
    """
    Car models a car with tires and an engine
    """

    def __init__(self, engine, tires):
        self.engine = engine
        self.tires = tires

    def drive(self):
        if self.tires < 4:
            print("CRASH")
        elif self.engine == "v6":
            print("vroooooom")
        elif self.engine == "v8":
            print("vrooooooooom")
        elif self.engine == "v12":
            print("vroooooooooooom")


# Virtual Pet

A recreation of the Virtual Pet that I built as part of the Manchester Codes Software Engineer Fasttrack course. This time as a Python project.

## General info

The idea of this virtual pet game is to look after your pet by feeding and exercising it regularly.

As your pet ages it needs to be fed and exercised and it will tell you what it wants at any time.

Make sure you pay attention to its needs because if you don't ... it will die.

## Areas covered

At stages throughout this project I:

* Followed the principles of Test Driven Development (TDD)
* Used Python's built-in unittest module to run the tests
* Used the Python interpreter to run code in the terminal 
* Had plenty of practice refactoring code at every stage of the build
* Learned about Python exceptions and how to throw them and test for them, including assertRaises() as a context manager

## Technologies and languages

* Python 3.8
* Python's in-built unittest module
* Git & GitHub

## Features

* The pet is born with an age of 0
* Start values for hunger and fitness can be configured in the constants at the top of the file. Current value are 0 and 10
* As the pet ages, its hunger and fitness values change at different rates, again these are configured in constants at the top.
* Feeding reduces hunger by an amount defined in the constants
* Walking increases fitness, also by an amount defined in the constants
* Triggers are set for hunger and fitness at which point the pet will ask for food, a walk, or both
* If the pet gets too hungry or too unfit it will die (Triggers are configured)
* The pet will die when it gets to a maximum age that can be configured (default = 30)
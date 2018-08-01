# python-automatic-web-testing

## Description

This repository provides a tool to generate website tests in a fast and effective way. For a large number of projects the worst problem of their tests is their nonexistence. It's difficult to cover all the circumstances with this type of tests, but it is an easy and fast way to start.


## Table of Contents

1. [Installation](#installation)  
2. [Usage](#usage)  
   1. [JSON Files](#json-files)
   1. [Actions](#actions)
      1. [GO](#go)
      1. [CLICK](#click)
      1. [CHECK](#check)
      1. [WAIT](#wait)
      1. [FILL](#fill)
      1. [SELECT](#select)
3. [TODO](#todo)  
4. [Contributing](#contributing)  
           
        
    

## Installation

To run that repository, you will need:

* Python, likely version 3.5.
* Selenium, you can install it using: `pip install -U selenium`

## Usage

You can use this tool in two different ways:

* Creating JSON files and saving them in a directory

* Executing actions in python code

## JSON Files

The JSON files must have the following structure

Key | Value
--- | -----
name | Name of the test
resolution | Dictionary with two keys: *width* and *height* and two ints as values
actions | List of actions 

## Actions

The actions have the same syntax for the JSON files and for python dictionaries if you want to pass them directly.
all the actions have the *'type'* parameter, the rest of parameters depends of the type.

**Types:** 'GO','CLICK','CHECK','WAIT','FILL','SELECT'

### GO
Make the browser go to an url

**Parameters:**

Key | Value
--- | -----
type | 'GO'
url | (string) Url to go 

### CLICK
Make the browser click on an element

**Parameters:**

Key | Value
--- | -----
type | 'CLICK'
xpath | (string) xpath that identifies the element

### CHECK
Check if a value is in an element, print by screen if the check is correct

**Parameters:**

Key | Value
--- | -----
type | 'CHECK'
xpath | (string) xpath that identifies the element
values | (list of strings) list of possible values

### WAIT
Delay execution for a given number of seconds

**Parameters:**

Key | Value
--- | -----
type | 'WAIT'
sleep_time | (int) number of seconds

### FILL
Make the browser fill an element with a text

**Parameters:**

Key | Value
--- | -----
type | 'FILL'
xpath | (string) xpath that identifies the element
text | (string) text to be wrote in the element
send | (boolean) if True enter will be pressed at the end of sending text

### SELECT
Make the browser select an option of an element, of value, text or index only one is necessary.
If more than one is given the priority is value > text > index

**Parameters:**

Key | Value
--- | -----
type | 'SELECT'
xpath | (string) xpath that identifies the element
value | (string or int) search in the options for the value and select it
text | (string) search in the options for the text and select it
index | (int) select the given index



## TODO:

* Create a browser extension that acts as an interface for the creation of JSON files
* Add support to other browsers


## Contributing
  Feel free to contribute the way you want!

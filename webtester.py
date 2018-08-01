from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import os
import json


def remove_extra_keys(method):
    """Decorator to remove the keys that aren't necessary for the actions functions: click, check, wait, ..."""
    def wrap(*args, **kwargs):
        extra_keys = ['type', ]
        for key in extra_keys:
            try:
                del kwargs[key]
            except KeyError:
                pass

        return method(*args, **kwargs)

    return wrap


def treat_exceptions(method):
    """Decorator to treat the exceptions and give more informative error messages"""
    def wrap(*args, **kwargs):
        try:
            return method(*args, **kwargs)
        except NoSuchElementException:
            raise Exception('No such element with xpath: {}'.format(kwargs['xpath']))

    return wrap


class WebTester(object):
    """Class that contains the functions to read the tests and interact with the web"""

    GO_ACTION = 'GO'
    CLICK_ACTION = 'CLICK'
    CHECK_ACTION = 'CHECK'
    WAIT_ACTION = 'WAIT'
    FILL_FORM_ACTION = 'FILL'
    SELECT_FORM_ACTION = 'SELECT'

    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_action(self, action):
        """
        Return the function for a certain action
        :param action: (string) Represents one of the actions
        :return: function object or raise an Exception if the action string is not valid
        """
        actions = {
            self.GO_ACTION: self.go,
            self.CLICK_ACTION: self.click,
            self.CHECK_ACTION: self.check,
            self.WAIT_ACTION: self.wait,
            self.FILL_FORM_ACTION: self.fill,
            self.SELECT_FORM_ACTION: self.select
        }
        try:
            return actions[action]
        except KeyError:
            raise Exception('{0} is not a valid action, the valid actions are: {1}'.format(action,
                                                                                           ", ".join(actions.keys())))

    def set_resolution(self, width, height):
        """
        Set the resolution of the browser screen
        :param width: (int) the desired width
        :param height: (int) the desired height
        :return: None
        """
        self.driver.set_window_size(width, height, self.driver.window_handles[0])

    @remove_extra_keys
    @treat_exceptions
    def go(self, url):
        """
        Make the browser go to an url
        :param url: (string) url to go 
        :return: None
        """
        self.driver.get(url)

    @remove_extra_keys
    @treat_exceptions
    def click(self, xpath):
        """
        Make the browser click on an element
        :param xpath: (string) xpath that identifies the element 
        :return: None
        """
        self.driver.find_element_by_xpath(xpath=xpath).click()
    
    @remove_extra_keys
    @treat_exceptions
    def fill(self, xpath, text, send=False):
        """
        Make the browser fill an element with a text
        :param xpath: (string) xpath that identifies the element 
        :param text: (string) text to be wrote in the element
        :param send: (boolean) if True enter will be pressed at the end of sending text
        :return: None
        """
        element = self.driver.find_element_by_xpath(xpath)
        element.clear()
        element.send_keys(text + '\n' if send else text)

    @remove_extra_keys
    @treat_exceptions
    def select(self, xpath, value=None, text=None, index=None):
        """
        Make the browser select an option of an element, of value, text or index only one is necessary.
        If more than one is given the priority is value > text > index
        :param xpath: (string) xpath that identifies the element 
        :param value: (string or int) search in the options for the value and select it
        :param text: (string) search in the options for the text and select it
        :param index: (int) select the given index
        :return: None
        """
        field = webdriver.support.ui.Select(self.driver.find_element_by_xpath(xpath))
        if value:
            field.select_by_value(value)
        elif text:
            field.select_by_visible_text(text)
        elif index:
            field.select_by_index(index)

    @remove_extra_keys
    @treat_exceptions
    def check(self, xpath, values):
        """
        Check if a value is in an element, print by screen if the check is correct
        :param xpath:  (string) xpath that identifies the element 
        :param values: (list of strings) list of possible values
        :return: None
        """
        text = self.driver.find_element_by_xpath(xpath=xpath).text
        check = False
        for value in values:
            if value in text:
                check = True

        if not check:
            print('Incorrect check: {0} in {1}'.format(text, str(values)))

        print('Correct check: {0} in {1}'.format(text, str(values)))

    @remove_extra_keys
    @treat_exceptions
    def wait(self, sleep_time):
        """
        Delay execution for a given number of seconds
        :param sleep_time: (int) Number of seconds
        :return: None
        """
        time.sleep(sleep_time)

    def test_actions(self, actions):
        """
        Execute a list of actions
        :param actions: (list of dictionaries) actions to be done
        :return: None 
        """
        try:
            for action in actions:
                self.get_action(action['type'])(**action)
        except Exception as e:
            print('Exception: {}'.format(str(e)))

    def test_files(self, location):
        """
        Open all the files in a location and test the data in them
        :param location: (string) folder where the files are located
        :return: None
        """
        for filename in os.listdir(location):
            with open(location + '/' + filename) as json_file:
                data = json.load(json_file)
                self.test_data(data)

    def test_data(self, data):
        """
        Start a test on a certain data
        :param data: (dictionary) Dictionary containing the keys
                    name : (string) name of the test
                    resolution: (dictionary) resolution in which the test will be executed
                        width: (int) width of the resolution
                        height: (int) height of the resolution
                    actions: (list of dictionaries) list of actions to be executed
        :return: None
        """
        print('-'*30)
        print('Starting test: {}'.format(data['name']))
        self.set_resolution(data['resolution']['width'], data['resolution']['height'])
        self.test_actions(data['actions'])
        print('Test finished')
        print('-'*30)


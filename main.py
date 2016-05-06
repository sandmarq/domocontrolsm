#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

"""
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.logger import Logger
from kivy.config import Config


import kivyviews
import threading
from flask import Flask

# Logging initialization
Logger.info('Application: This is a test')

# TODO Add logging
# CRITICAL = 50
# ERROR = 40
# WARNING = 30
# INFO = 20
# DEBUG = 10

# TODO Socket server for receiving data from wifi IoT devices

# TODO Data handler PyOWM and order data work flow

# review check this code for the web site
# Server Flask
serverweb = Flask(__name__)


@serverweb.route("/")
def hello():
    return "DomoControlSM"


@serverweb.route("/weather")
def hello1():
    return "Weather"


@serverweb.route("/alarms")
def hello2():
    return "Alarms"


@serverweb.route("/radio")
def hello3():
    return "Radio"


@serverweb.route("/automation")
def hello4():
    return "Automation"


# Create the server web and run it in a background daemon thread.
server_thread = threading.Thread(target=serverweb.run, kwargs=dict(host='0.0.0.0'))
server_thread.daemon = True
server_thread.start()


# Declare screens classes
class MainScreen(Screen):
    """
    Initialization fo the class
    """
    pass


class WeatherScreen(Screen):
    """
    Initialization fo the class
    """
    pass


class AlarmsScreen(Screen):
    """
    Initialization fo the class
    """
    pass


class RadioScreen(Screen):
    """
    Initialization fo the class
    """
    pass


class AutomationScreen(Screen):
    """
    Initialization fo the class
    """
    pass


class ConfigurationScreen(Screen):
    """
    Initialization fo the class
    """
    pass


# Create the screen manager
sm = ScreenManager()

# Main screen
mainscreen = MainScreen(name='main')
mainview = kivyviews.MainView()
mainscreen.add_widget(mainview)
sm.add_widget(mainscreen)

# Weather Screen
weatherscreen = WeatherScreen(name='weatherinfo')
weatherview = kivyviews.WeatherView()
weatherscreen.add_widget(weatherview)
sm.add_widget(weatherscreen)

# Alarms Screen
alarmsscreen = AlarmsScreen(name='alarmsinfo')
alarmsview = kivyviews.AlarmsView()
alarmsscreen.add_widget(alarmsview)
sm.add_widget(alarmsscreen)

# Radio Screen
radioscreen = RadioScreen(name='radioinfo')
radioview = kivyviews.RadioView()
radioscreen.add_widget(radioview)
sm.add_widget(radioscreen)

# Automation Screen
automationscreen = AutomationScreen(name='automationinfo')
automationview = kivyviews.AutomationView()
automationscreen.add_widget(automationview)
sm.add_widget(automationscreen)

# Configuration Screen
configurationscreen = ConfigurationScreen(name='configuration')
configurationview = kivyviews.ConfigView()
configurationscreen.add_widget(configurationview)
sm.add_widget(configurationscreen)


class DomocontrolsmApp(App):
    use_kivy_settings = False
    """
    Initialization of the app
    """
    def build_config(self, config):
        config.setdefaults('kivy', {
            'log_dir': './',
            'log_enable': 1,
            'log_level': 'debug',
            'log_name': 'domocontrolsm'
        })

    def build(self):
        self.icon = 'img/10d.png'
        self.title = 'DomoControlSM'
        return sm


if __name__ == '__main__':
    DomocontrolsmApp().run()

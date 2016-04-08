#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

"""
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

import kivyviews


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
    """
    Initialization of the app
    """
    icon = 'img/10d.png'
    title = 'DomoControlSM'

    def build(self):
        return sm


if __name__ == '__main__':
    DomocontrolsmApp().run()

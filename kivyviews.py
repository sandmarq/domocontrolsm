"""

"""
import locale

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

import asettings
import misc
import weatherinfo


class MainView(GridLayout):
    """

    """

    def __init__(self, **kwargs):
        kwargs['rows'] = 8
        kwargs['spacing'] = 15
        kwargs['padding'] = 15
        super(MainView, self).__init__(**kwargs)
        Window.clearcolor = (0.2, 0.2, 0.2, 1)

        self.clocklabel = DisplayLabelTime(id="clock_label",
                                           text="Clock",
                                           font_size=75,
                                           height=150,
                                           halign='left',
                                           valign='top')
        self.add_widget(self.clocklabel)

        self.datelabel = DisplayLabelDate(id="date_label",
                                          text="Date",
                                          font_size=40)
        self.add_widget(self.datelabel)

        self.g1 = GridLayout(rows=2)

        self.g2 = GridLayout(cols=2)

        self.labelweather = LabelWeather(id="labelweather",
                                         text="Weather")
        self.g2.add_widget(self.labelweather)

        self.i1 = Image(source='img/10d.png',
                        # size=self.texture_size,
                        size_hint=(0.2, 0.2))
        self.g2.add_widget(self.i1)

        self.g1.add_widget(self.g2)

        self.b1 = ButtonWeather(id="weather",
                                text="Weather",
                                on_release=lambda a: self.openweather())

        self.g1.add_widget(self.b1)

        self.add_widget(self.g1)

        self.b2 = ButtonAlarms(id="alarms",
                               text="alarms",
                               on_release=lambda a: self.openalarms())
        self.add_widget(self.b2)

        self.b3 = Button(id="alarms",
                         text="Radio",
                         on_release=lambda a: self.openradio())
        self.add_widget(self.b3)

        self.b4 = ButtonAutomation(id="domotique",
                                   text="domo",
                                   on_release=lambda a: self.openautomation())

        self.add_widget(self.b4)

        self.b5 = ButtonConfiguration(id="configuration",
                                      text="config",
                                      on_release=lambda a: self.openconfig())

        self.add_widget(self.b5)

        self.add_widget(ButtonQuit(text="Quit", on_release=lambda a: self.quitapp()))

    def openweather(self):
        App.get_running_app().root.current = 'weatherinfo'

    def openalarms(self):
        App.get_running_app().root.current = 'alarmsinfo'

    def openradio(self):
        App.get_running_app().root.current = 'radioinfo'

    def openautomation(self):
        App.get_running_app().root.current = 'automationinfo'

    def openconfig(self):
        App.get_running_app().root.current = 'configuration'

    def quitapp(self):
        quit()


class WeatherView(GridLayout):
    def __init__(self, **kwargs):
        kwargs['cols'] = 2
        kwargs['rows'] = 6
        kwargs['spacing'] = 15
        kwargs['padding'] = 15
        super(WeatherView, self).__init__(**kwargs)
        Window.clearcolor = (0.2, 0.2, 0.2, 1)

        # 1
        self.g11 = GridLayout(rows=2)
        self.l111 = Label(text="En ce moment")
        self.g11.add_widget(self.l111)
        self.g111 = GridLayout(cols=2)
        self.g1111 = GridLayout(cols=1,
                                rows=1)
        self.i1111 = Image(source='img/10d.png',
                           allow_stretch=True,
                           keep_ratio=True,
                           size_hint=(0.2, 0.2))
        self.g1111.add_widget(self.i1111)
        self.g111.add_widget(self.g1111)
        self.g1112 = GridLayout(cols=1,
                                rows=5)

        for count0 in range(1, 6):
            self.labeltext = "info" + str(count0)
            self.l1111 = Label(text=self.labeltext)
            self.g1112.add_widget(self.l1111)

        self.g111.add_widget(self.g1112)
        self.g11.add_widget(self.g111)
        self.add_widget(self.g11)

        # 2 - 3 - 4 - 5

        self.text1 = ["Aujourd'hui", "Demain", "Après demain", "Après après demain"]

        for count1 in range(4):
            self.g12 = GridLayout(rows=2)
            self.l121 = Label(text=self.text1[count1])
            self.g12.add_widget(self.l121)
            self.g121 = GridLayout(cols=2)
            self.g1211 = GridLayout(cols=1,
                                    rows=1)
            self.i1211 = Image(source='img/10d.png',
                               allow_stretch=True,
                               keep_ratio=True,
                               size_hint=(0.2, 0.2))
            self.g1211.add_widget(self.i1211)
            self.g121.add_widget(self.g1211)
            self.g1212 = GridLayout(cols=1,
                                    rows=5)

            for count2 in range(1, 6):
                self.labeltext = "Info" + str(count2)
                self.l1211 = Label(text=self.labeltext)
                self.g1212.add_widget(self.l1211)

            self.g121.add_widget(self.g1212)
            self.g12.add_widget(self.g121)
            self.add_widget(self.g12)

        # 6
        self.g16 = GridLayout(rows=5,
                              cols=2)

        for count3 in range(1, 8):
            self.l161 = Label(text="")
            self.g16.add_widget(self.l161)

        self.b161 = Button(text="Back", on_release=lambda a: self.backmain())
        self.g16.add_widget(self.b161)
        self.add_widget(self.g16)

    def backmain(self):
        App.get_running_app().root.current = 'main'


class AlarmsView(GridLayout):
    def __init__(self, **kwargs):
        kwargs['rows'] = 6
        kwargs['spacing'] = 15
        kwargs['padding'] = 15
        # kwargs['col_default_width'] = 100
        super(AlarmsView, self).__init__(**kwargs)
        Window.clearcolor = (0.2, 0.2, 0.2, 1)

        self.b1 = Button(text="Back", on_release=lambda a: self.backmain())
        self.add_widget(self.b1)

    def backmain(self):
        App.get_running_app().root.current = 'main'


class RadioView(GridLayout):
    def __init__(self, **kwargs):
        kwargs['rows'] = 6
        kwargs['spacing'] = 15
        kwargs['padding'] = 15
        # kwargs['col_default_width'] = 100
        super(RadioView, self).__init__(**kwargs)
        Window.clearcolor = (0.2, 0.2, 0.2, 1)

        self.b1 = Button(text="Back", on_release=lambda a: self.backmain())
        self.add_widget(self.b1)

    def backmain(self):
        App.get_running_app().root.current = 'main'


class AutomationView(GridLayout):
    def __init__(self, **kwargs):
        kwargs['rows'] = 6
        kwargs['spacing'] = 15
        kwargs['padding'] = 15
        # kwargs['col_default_width'] = 100
        super(AutomationView, self).__init__(**kwargs)
        Window.clearcolor = (0.2, 0.2, 0.2, 1)

        self.b1 = Button(text="Back", on_release=lambda a: self.backmain())
        self.add_widget(self.b1)

    def backmain(self):
        App.get_running_app().root.current = 'main'


class ConfigView(GridLayout):
    def __init__(self, **kwargs):
        kwargs['rows'] = 6
        kwargs['cols'] = 2
        kwargs['spacing'] = 15
        kwargs['padding'] = 15
        # kwargs['col_default_width'] = 100
        super(ConfigView, self).__init__(**kwargs)
        Window.clearcolor = (0.2, 0.2, 0.2, 1)

        self.l1 = Label(text='Langue', halign='right', valign='middle')
        self.add_widget(self.l1)
        self.t1 = TextInput(text='fr_CA')
        self.add_widget(self.t1)

        self.l2 = Label(text='Degree', halign='right', valign='middle')
        self.add_widget(self.l2)
        self.t2 = TextInput(text='celsius')
        self.add_widget(self.t2)

        self.l3 = Label(text='Api Key', halign='right', valign='middle')
        self.add_widget(self.l3)
        self.t3 = TextInput(text='990178913a09744af3a45e8323bcba20')
        self.add_widget(self.t3)

        self.l4 = Label(text='City', halign='right', valign='middle')
        self.add_widget(self.l4)
        self.t4 = TextInput(text='Montreal')
        self.add_widget(self.t4)

        self.l5 = Label(text='Country', halign='right', valign='middle')
        self.add_widget(self.l5)
        self.t5 = TextInput(text='ca')
        self.add_widget(self.t5)

        self.l6 = Label(text='', halign='right', valign='middle')
        self.add_widget(self.l6)
        self.b1 = Button(text="Back", on_release=lambda a: self.backmain())
        self.add_widget(self.b1)

    def backmain(self):
        App.get_running_app().root.current = 'main'


class DisplayLabelTime(Label):
    """
    Kivy Label class overwritten for additional functionality.
    Display current time and refresh it every 500ms
    """

    def __init__(self, **kwargs):
        """
        Initialization fo the class et background process
        :param kwargs:
        :return:
        """
        super(DisplayLabelTime, self).__init__(**kwargs)
        Clock.schedule_once(self.update_time)
        Clock.schedule_interval(self.update_time, 0.5)

    def update_time(self, dt):
        """
        Update the text of the label time of screen
        :param dt:
        :return:
        """
        self.text = misc.get_time()


class DisplayLabelDate(Label):
    """
    Kivy Label class overwritten for additional functionality.
    Display current date and refresh it every 500ms
    """

    def __init__(self, **kwargs):
        """
        Initialization fo the class et background process
        :param kwargs:
        :return:
        """
        super(DisplayLabelDate, self).__init__(**kwargs)
        Clock.schedule_once(self.update_date)
        Clock.schedule_interval(self.update_date, 0.5)

    def update_date(self, dt):
        """
        Update the text of the label date of screen
        :param dt:
        :return:
        """
        self.text = misc.get_date()


class LabelWeather(Label):
    """
    Kivy Button class overwritten for additional functionality.
    Display right text for the language choose in configuration
    """

    def __init__(self, **kwargs):
        """
        Initialization fo the class
        :param kwargs:
        :return:
        """
        super(LabelWeather, self).__init__(**kwargs)
        Clock.schedule_once(self.update_text)

    def update_text(self, dt):
        """
        updating the text
        :param dt:
        :return:
        """
        if locale.getdefaultlocale()[0][0:2] == 'fr':
            self.text = "Météo"
        else:
            self.text = "Weather"


class ButtonWeather(Button):
    """
    Kivy Button class overwritten for additional functionality.
    Display right text for the language choose in configuration
    """

    def __init__(self, **kwargs):
        """
        Initialization fo the class
        :param kwargs:
        :return:
        """
        super(ButtonWeather, self).__init__(**kwargs)
        Clock.schedule_once(self.update_weather)
        Clock.schedule_interval(self.update_weather, 300)

    def update_weather(self, dt):
        """
        updating the text
        :param dt:
        :return:
        """
        print("mise a jour")
        # get settings
        appSettings = asettings.Settings()

        # get weather info
        weather = weatherinfo.WeatherInfo(appSettings.apikey, appSettings.location, appSettings.degree)
        weather.update()
        weather.current_weather()
        weather.daily_weather()
        if appSettings.degree == 'celsius':
            temp1 = weather.nowData['TempC']
        else:
            temp1 = weather.nowData['TempF']
        humi1 = weather.nowData['Humidity']
        speed1 = weather.nowData['Wind']
        deg1 = weather.nowData['Direction']

        if appSettings.lang == "fr_CA":
            self.text = "Température actuel : {0}°C       Humidité : {1}%       Vitesse du vent : {2}       Direction du vent : {3}".format(
                temp1, humi1, speed1, deg1)

        else:
            self.text = "Actual temperature : {0}°C          Humidity : {1}% Wind speed : {2}          Wind Direction : {3}".format(
                temp1, humi1, speed1, deg1)


class ButtonAlarms(Button):
    """
    Kivy Button class overwritten for additional functionality.
    Display right text for the language choose in configuration
    """

    def __init__(self, **kwargs):
        """
        Initialization fo the class
        :param kwargs:
        :return:
        """
        super(ButtonAlarms, self).__init__(**kwargs)
        Clock.schedule_once(self.update_text)

    def update_text(self, dt):
        """
        updating the text
        :param dt:
        :return:
        """
        if locale.getdefaultlocale()[0][0:2] == 'fr':
            self.text = "Alarme(s)"
        else:
            self.text = "Alarm(s)"


class ButtonQuit(Button):
    """
    Kivy Button class overwritten for additional functionality.
    Display right text for the language choose in configuration
    """

    def __init__(self, **kwargs):
        """
        Initialization fo the class
        :param kwargs:
        :return:
        """
        super(ButtonQuit, self).__init__(**kwargs)
        Clock.schedule_once(self.update_text)

    def update_text(self, dt):
        """
        updating the text
        :param dt:
        :return:
        """
        if locale.getdefaultlocale()[0][0:2] == 'fr':
            self.text = "Quitter"
        else:
            self.text = "Quit"


class ButtonConfiguration(Button):
    """
    Kivy Button class overwritten for additional functionality.
    Display right text for the language choose in configuration
    """

    def __init__(self, **kwargs):
        """
        Initialization fo the class
        :param kwargs:
        :return:
        """
        super(ButtonConfiguration, self).__init__(**kwargs)
        Clock.schedule_once(self.update_text)

    def update_text(self, dt):
        """
        updating the text
        :param dt:
        :return:
        """
        if locale.getdefaultlocale()[0][0:2] == 'fr':
            self.text = "Paramètres"
        else:
            self.text = "Settings"


class ButtonAutomation(Button):
    """
    Kivy Button class overwritten for additional functionality.
    Display right text for the language choose in configuration
    """

    def __init__(self, **kwargs):
        """
        Initialization fo the class
        :param kwargs:
        :return:
        """
        super(ButtonAutomation, self).__init__(**kwargs)
        Clock.schedule_once(self.update_text)

    def update_text(self, dt):
        """
        updating the text
        :param dt:
        :return:
        """
        if locale.getdefaultlocale()[0][0:2] == 'fr':
            self.text = "Domotique"
        else:
            self.text = "Automation"

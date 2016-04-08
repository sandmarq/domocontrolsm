"""

"""
import json

import pyowm


class WeatherInfo:
    """
    This class will be used to get information need from openweathermap and prepare to be used by the rest of the
    application.
    """

    def __init__(self, apikeytxt, citynametxt, degreeformat):
        """

        :param apikeytxt:
        :param citynametxt:
        :param degreeformat:
        :return:
        """
        self.apiKey = apikeytxt
        self.cityName = citynametxt
        self.degree = degreeformat
        self.owm = ''
        self.observation = ''
        self.w = ''
        self.now = ''
        self.daily_fc = ''
        self.obsDaily = ''
        self.tomorrow = ''
        self.nowData = {}
        self.dailyData = {}
        self.connection = False
        self.init()

    def init(self):
        """

        :return:
        """
        try:
            self.owm = pyowm.OWM(self.apiKey)
            self.observation = self.owm.weather_at_place(self.cityName)
            self.now = self.observation.get_weather()
            self.obsDaily = self.owm.daily_forecast(self.cityName, limit=4)
            self.daily_fc = self.obsDaily.get_forecast()
            self.connection = True
        except:
            self.connection = False

    def update(self):  # , dt):
        """

        :return:
        """
        if self.connection:
            self.now = self.observation.get_weather()
            self.daily_fc = self.obsDaily.get_forecast()

    def current_weather(self):
        """

        :return:
        """
        if self.connection:
            jsonnow = json.loads(self.json_now())
            # print("Now:")
            self.nowData.clear()
            # print(self.nowData)
            self.nowData['TempC'] = self.kelvin_to_celsius(jsonnow['temperature']['temp'])  # "TempC"
            self.nowData['TempF'] = self.kelvin_to_fahrenheit(jsonnow['temperature']['temp'])  # "TempF"
            self.nowData['Humidity'] = jsonnow['humidity']  # "Humidity"
            self.nowData['Humidex'] = jsonnow['humidex']  # "Humidity"
            self.nowData['Heat'] = jsonnow['heat_index']  # "Humidity"

            if not jsonnow['wind']:
                self.nowData['Wind'] = jsonnow['wind']['speed']  # "Wind"
            else:
                self.nowData['Wind'] = "N/A"

            if not jsonnow['wind']:
                self.nowData['Direction'] = self.wind_direction(int(jsonnow['wind']['deg']))  # "Direction"
            else:
                self.nowData['Direction'] = "N/A"  # "Direction"

            self.nowData['Status'] = jsonnow['status']  # "Humidity"
            self.nowData['Detail'] = jsonnow['detailed_status']  # "Humidity"
            self.nowData['Code'] = jsonnow['weather_code']  # "Humidity"
            self.nowData['Icon'] = jsonnow['weather_icon_name']  # "Humidity"
            self.nowData['Rain'] = jsonnow['rain']  # "Humidity"
            self.nowData['Snow'] = jsonnow['snow']  # "Humidity"
            self.nowData['Clouds'] = jsonnow['clouds']  # "Clouds"
            # print(self.nowData)
        else:
            # print("Now:")
            self.nowData.clear()
            # print("N/A")
            self.nowData['TempC'] = "N/A"
            self.nowData['TempF'] = "N/A"
            self.nowData['Humidity'] = "N/A"
            self.nowData['Humidex'] = "N/A"
            self.nowData['Heat'] = "N/A"
            self.nowData['Wind'] = "N/A"
            self.nowData['Direction'] = "N/A"
            self.nowData['Status'] = "N/A"
            self.nowData['Detail'] = "N/A"
            self.nowData['Code'] = "N/A"
            self.nowData['Icon'] = "N/A"
            self.nowData['Rain'] = "N/A"
            self.nowData['Snow'] = "N/A"
            self.nowData['Clouds'] = "N/A"
            # print("N/A")

    def daily_weather(self):
        """

        :return:
        """
        if self.connection:
            print("Daily:")
            jsondaily = json.loads(self.json_daily())
            self.dailyData.clear()
            for x in range(4):
                # self.dailyData[str(x)] = jsondaily['weathers'][x]['temperature']['min']
                print(jsondaily['weathers'][x])

                print("TempC Min   :", self.kelvin_to_celsius(jsondaily['weathers'][x]['temperature']['min']))
                print("TempC Max   :", self.kelvin_to_celsius(jsondaily['weathers'][x]['temperature']['max']))
                print("TempC Morn  :", self.kelvin_to_celsius(jsondaily['weathers'][x]['temperature']['morn']))
                print("TempC Day   :", self.kelvin_to_celsius(jsondaily['weathers'][x]['temperature']['day']))
                print("TempC Eve   :", self.kelvin_to_celsius(jsondaily['weathers'][x]['temperature']['eve']))
                print("TempC Night :", self.kelvin_to_celsius(jsondaily['weathers'][x]['temperature']['night']))
                print("TempF Min   :", self.kelvin_to_fahrenheit(jsondaily['weathers'][x]['temperature']['min']))
                print("TempF Max   :", self.kelvin_to_fahrenheit(jsondaily['weathers'][x]['temperature']['max']))
                print("TempF Morn  :", self.kelvin_to_fahrenheit(jsondaily['weathers'][x]['temperature']['morn']))
                print("TempF Day   :", self.kelvin_to_fahrenheit(jsondaily['weathers'][x]['temperature']['day']))
                print("TempF Eve   :", self.kelvin_to_fahrenheit(jsondaily['weathers'][x]['temperature']['eve']))
                print("TempF Night :", self.kelvin_to_fahrenheit(jsondaily['weathers'][x]['temperature']['night']))
                print("Humidity    :", jsondaily['weathers'][x]['humidity'])
                print("Hudidex     :", jsondaily['weathers'][x]['humidex'])
                print("Heat Index  :", jsondaily['weathers'][x]['heat_index'])
                print("D Status    :", jsondaily['weathers'][x]['detailed_status'])
                print("W Code      :", jsondaily['weathers'][x]['weather_code'])
                print("W Icon      :", jsondaily['weathers'][x]['weather_icon_name'])
                print("Rain        :", jsondaily['weathers'][x]['rain'])
                print("Snow        :", jsondaily['weathers'][x]['snow'])
                print("Clouds      :", jsondaily['weathers'][x]['clouds'])

        else:
            print("Daily")
            print("N/A")

    def json_now(self):
        """

        :return:
        """
        return self.now.to_JSON()

    def json_daily(self):
        """

        :return:
        """
        return self.daily_fc.to_JSON()

    @staticmethod
    def kelvin_to_celsius(k_temp):
        return round(k_temp - 273.15, 1)

    @staticmethod
    def kelvin_to_fahrenheit(k_temp):
        return round(((k_temp - 273.15) * 1.8) + 32, 1)

    @staticmethod
    def wind_direction(degree):
        """
        Wind direction in degres
        Cardinal Dir Degree Direction
        1 	       N  348.75 -  11.25
        2 	     NNE   11.25 -  33.75
        3 	      NE   33.75 -  56.25
        4 	     ENE   56.25 -  78.75
        5 	       E   78.75 - 101.25
        6 	     ESE  101.25 - 123.75
        7 	      SE  123.75 - 146.25
        8 	     SSE  146.25 - 168.75
        9 	       S  168.75 - 191.25
        10	     SSW  191.25 - 213.75
        11	      SW  213.75 - 236.25
        12	     WSW  236.25 - 258.75
        13	       W  258.75 - 281.25
        14	     WNW  281.25 - 303.75
        15	      NW  303.75 - 326.25
        16	     NNW  326.25 - 348.75
        :param degree:
        :return:
        """
        if (degree > 348.75) or (degree <= 11.25):
            # 1
            return "N"
        elif (degree > 11.25) and (degree <= 33.75):
            # 2
            return "NNE"
        elif (degree > 33.75) and (degree <= 56.25):
            # 3
            return "NE"
        elif (degree > 56.25) and (degree <= 78.75):
            # 4
            return "ENE"
        elif (degree > 78.75) and (degree <= 101.25):
            # 5
            return "E"
        elif (degree > 101.25) and (degree <= 123.75):
            # 6
            return "ESE"
        elif (degree > 123.75) and (degree <= 146.25):
            # 7
            return "SE"
        elif (degree > 146.25) and (degree <= 168.75):
            # 8
            return "SSE"
        elif (degree > 168.75) and (degree <= 191.25):
            # 9
            return "S"
        elif (degree > 191.25) and (degree <= 213.75):
            # 10
            return "SSW"
        elif (degree > 213.75) and (degree <= 236.25):
            # 11
            return "SW"
        elif (degree > 236.25) and (degree <= 258.75):
            # 12
            return "WSW"
        elif (degree > 258.75) and (degree <= 281.25):
            # 13
            return "W"
        elif (degree > 281.25) and (degree <= 303.75):
            # 14
            return "WNW"
        elif (degree > 303.75) and (degree <= 326.25):
            # 15
            return "NW"
        elif (degree > 326.25) and (degree <= 348.75):
            # 16
            return "NNW"
        else:
            return "ERROR"

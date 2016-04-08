"""

"""
import json

# Const
SETFILE = "/etc/domocontrolsm/settings.json"
READ = 'r'
WRITE = 'w'


class Settings(object):
    """
    This class read and write settings to file and keep them in variables
    """

    def __init__(self):
        """
        Variables used in the class
        :return: class object
        """
        self.jsondata = ''
        self._lang = ''
        self._degree = ''
        self._apiKey = ''
        self._cityName = ''
        self._country = ''
        self._location = ''
        self.read()

    @property
    def lang(self):
        """
        get the lng from file
        :return:
        """
        self.read()
        return self._lang

    @property
    def apikey(self):
        """
        get the apikey from file
        :return:
        """
        self.read()
        return self._apiKey

    @property
    def cityname(self):
        """
        get cityname from file
        :return:
        """
        self.read()
        return self._cityName

    @property
    def country(self):
        """
        get country from file
        :return:
        """
        self.read()
        return self._country

    @property
    def degree(self):
        """
        get degree format from file
        :return:
        """
        self.read()
        return self._degree

    @property
    def location(self):
        """
        get country from file
        :return:
        """
        self.read()
        return self.cityname + ',' + self.country

    @lang.setter
    def lang(self, value):
        """
        set the lang to the new value and write it to file
        :param value:
        :return:
        """
        self._lang = value
        self.jsondata['Settings']['Application']['lang'] = value
        self.write()

    @apikey.setter
    def apikey(self, value):
        """
        set the apiKey to the new value and write it to file
        :param value:
        :return:
        """
        self._apiKey = value
        self.jsondata['Settings']['Weather']['apiKey'] = value
        self.write()

    @cityname.setter
    def cityname(self, value):
        """
        set the cityname to the new value and write it to file
        :param value:
        :return:
        """
        self._cityName = value
        self.jsondata['Settings']['Weather']['cityName'] = value
        self.write()

    @country.setter
    def country(self, value):
        """
        set the country to the new value and write it to file
        :param value:
        :return:
        """
        self._country = value
        self.jsondata['Settings']['Weather']['country'] = value
        self.write()

    @degree.setter
    def degree(self, value):
        """
        set the country to the new value and write it to file
        :param value:
        :return:
        """
        self._degree = value
        self.jsondata['Settings']['Application']['degree'] = value
        self.write()

    def read(self):
        """
        Read json setting file to put configurations in variables
        :return:
        """
        with open(SETFILE, READ) as jsonFile:
            self.jsondata = json.load(jsonFile)
            self._lang = self.jsondata['Settings']['Application']['lang']
            self._degree = self.jsondata['Settings']['Application']['degree']
            self._apiKey = self.jsondata['Settings']['Weather']['apiKey']
            self._cityName = self.jsondata['Settings']['Weather']['cityName']
            self._country = self.jsondata['Settings']['Weather']['country']
        jsonFile.close()

    def write(self):
        """
        Write setting to file.
        :return:
        """
        with open(SETFILE, WRITE) as jsonFile:
            jsonFile.write(json.dumps(self.jsondata, indent=2))
        jsonFile.close()

from countryinfo import CountryInfo


class CountryInf:

    """
        Class CountryInf main purpose is to connect and get data from CountryInfo API.
        Also it has special methods that will be used to save information to the file in user friendly way

    """
    def __init__(self, country_name):
        self.__country_name = country_name
        self.__country = CountryInfo(self.country_name)
        self.__capital = self.__country.capital()
        self.__currencies = self.__country.currencies()
        self.__languages = self.__country.languages()
        self.__population = self.__country.population()
        self.__area = self.__country.area()
        self.__timezones = self.__country.timezones()
        self.__region = self.__country.region()
        self.__subregion = self.__country.subregion()
        self.__provinces = self.__country.provinces()
        self.__borders = self.__country.borders()
        self.__alt_spellings = self.__country.alt_spellings()
        self.__native_name = self.__country.native_name()
        self.__calling_codes = self.__country.calling_codes()
        self.__wiki = self.__country.wiki()

    @property
    def country_name(self):
        return self.__country_name

    @property
    def capital(self):
        return self.__capital

    @property
    def currencies(self):
        return self.__currencies

    @property
    def languages(self):
        return self.__languages

    @property
    def population(self):
        return self.__population

    @property
    def area(self):
        return self.__area

    @property
    def timezones(self):
        return self.__timezones

    @property
    def region(self):
        return self.__region

    @property
    def subregion(self):
        return self.__subregion

    @property
    def provinces(self):
        return self.__provinces

    @property
    def borders(self):
        return self.__borders

    @property
    def alt_spellings(self):
        return self.__alt_spellings

    @property
    def native_name(self):
        return self.__native_name

    @property
    def calling_codes(self):
        return self.__calling_codes

    @property
    def wiki(self):
        return self.__wiki

    def get_all_the_info_for_country(self):
        all_info = {
            'name': self.country_name,
            'capital': self.capital,
            'region': self.region,
            'subregion': self.subregion,
            'provinces': self.provinces,
            'borders': self.borders,
            'currencies': self.currencies,
            'languages': self.languages,
            'population': self.population,
            'area': self.area,
            'timezones': self.timezones,
            'alt_spellings': self.alt_spellings,
            'native_name': self.native_name,
            'calling_codes': self.calling_codes,
            'wiki': self.wiki,
        }
        return all_info.items()

    def get_basic_info_for_country(self):
        basic_info = 'Information:\n' + 'Country: ' + self.country_name + '\nCapital city: ' + self.capital \
                    + '\nRegion: ' + self.region + '\nPopulation: ' + str(self.population) + '\nWikipedia: ' + self.wiki
        return basic_info

    def get_calling_codes_for_country(self):
        calling_codes = '\nCalling codes: ' + str(', '.join(self.calling_codes))
        return calling_codes

    def get_area_for_country(self):
        area = '\nArea: ' + str(self.area)
        return area

    def get_timezones_for_country(self):
        timezones = '\nTime zones: ' + str(', '.join(self.timezones))
        return timezones

    def get_languages_for_country(self):
        languages = '\nLanguages: ' + str(', '.join(self.languages))
        return languages

    def get_currencies_for_country(self):
        currencies = '\nCurrencies: ' + str(', '.join(self.currencies))
        return currencies

    def get_native_name_for_country(self):
        native_name = '\nCurrencies: ' + self.native_name
        return native_name




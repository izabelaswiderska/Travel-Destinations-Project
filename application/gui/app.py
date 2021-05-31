import tkinter as tk
from builtins import str
from tkinter import *
import application.logic.country_info as country_information
import application.logic.const as const
import application.logic.error_helper as error_helper


class App:
    """
    Class contains windows components
    """

    def __init__(self, root):
        self.__root = root
        self.__root.title(const.TITLE)
        self.__root.minsize(700, 720)
        self.__root.geometry('800x600')
        self.__root.config(background=const.BACKGROUND_COLOUR)
        self.__icon = tk.PhotoImage(file=const.GLOBE_IMG)
        self.__root.iconphoto(False, self.__icon)

        # values
        self.__country_name = tk.StringVar()
        self.__checked_native_name = tk.IntVar()
        self.__checked_currencies = tk.IntVar()
        self.__checked_languages = tk.IntVar()
        self.__checked_area = tk.IntVar()
        self.__checked_timezones = tk.IntVar()
        self.__checked_calling_codes = tk.IntVar()

        # frames for components
        self.__app_name_frame = tk.Frame(self.__root, bg=const.BACKGROUND_COLOUR)
        self.__app_name_frame.pack()
        self.__app_image_frame = tk.Frame(self.__root, bg=const.BACKGROUND_COLOUR)
        self.__app_image_frame.pack()
        self.__entry_frame = tk.Frame(self.__root, bg=const.BACKGROUND_COLOUR)
        self.__entry_frame.pack()
        self.__extra_options_title_frame = tk.Frame(self.__root, bg=const.BACKGROUND_COLOUR)
        self.__extra_options_title_frame.pack()
        self.__extra_options_frame = tk.Frame(self.__root, bg=const.BACKGROUND_COLOUR)
        self.__extra_options_frame.pack()
        self.__search_frame = tk.Frame(self.__root, bg=const.BACKGROUND_COLOUR)
        self.__search_frame.pack()

        # components in their frames
        self.__init_app_title_label()
        self.__init_app_image()
        self.__init_entry_field()
        self.__init_search_button()
        self.__init_extra_options_label()
        self.__init_extra_options_check_bar()

    def __init_app_title_label(self):
        self.title = tk.Label(self.__app_name_frame, text=const.TITLE, font=(const.FONT, 30, 'bold'),
                              bg=const.BACKGROUND_COLOUR,
                              fg=const.FONT_COLOUR)
        self.title.pack(pady=(20, 10))

    def __init_app_image(self):
        self.photo = tk.PhotoImage(file=const.DESTINATION_SIGN_IMG)
        self.label = tk.Label(self.__app_image_frame, image=self.photo, bg=const.BACKGROUND_COLOUR)
        self.label.pack(pady=(20, 20))

    def __init_entry_field(self):
        self.entry_field = tk.Entry(self.__entry_frame, textvariable=self.__country_name, font=(const.FONT, 18),
                                    width=28, bd=1, bg=const.BACKGROUND_COLOUR, fg=const.FONT_COLOUR)
        self.entry_field.grid(row=0, column=0, pady=(20, 20))

    def __init_extra_options_label(self):
        self.options_label = tk.Label(self.__extra_options_title_frame, text='Extra info',
                                      font=(const.FONT, 18, 'bold'),
                                      bg=const.BACKGROUND_COLOUR,
                                      fg=const.FONT_COLOUR)
        self.options_label.grid(pady=(20, 10))

    def __init_extra_options_check_bar(self):
        self.checked_native_name_btt = Checkbutton(self.__extra_options_frame, text='Native name',
                                                   variable=self.__checked_native_name, onvalue=1, offvalue=0,
                                                   font=(const.FONT, 14), bg=const.BACKGROUND_COLOUR,
                                                   fg=const.FONT_COLOUR)
        self.checked_native_name_btt.grid(row=0, column=0, padx=20, sticky='W')

        self.checked_currencies_btt = Checkbutton(self.__extra_options_frame, text='Currencies',
                                                  variable=self.__checked_currencies, onvalue=1, offvalue=0,
                                                  font=(const.FONT, 14), bg=const.BACKGROUND_COLOUR,
                                                  fg=const.FONT_COLOUR)
        self.checked_currencies_btt.grid(row=0, column=1, padx=20, sticky='W')

        self.checked_languages_btt = Checkbutton(self.__extra_options_frame, text='Languages',
                                                 variable=self.__checked_languages, onvalue=1, offvalue=0,
                                                 font=(const.FONT, 14), bg=const.BACKGROUND_COLOUR,
                                                 fg=const.FONT_COLOUR)
        self.checked_languages_btt.grid(row=0, column=2, padx=20, sticky='W')

        self.checked_timezones_btt = Checkbutton(self.__extra_options_frame, text='Time zones',
                                                 variable=self.__checked_timezones, onvalue=1, offvalue=0,
                                                 font=(const.FONT, 14), bg=const.BACKGROUND_COLOUR,
                                                 fg=const.FONT_COLOUR)
        self.checked_timezones_btt.grid(row=1, column=0, padx=20, sticky='W')

        self.checked_calling_codes_btt = Checkbutton(self.__extra_options_frame, text='Calling codes',
                                                     variable=self.__checked_calling_codes, onvalue=1, offvalue=0,
                                                     font=(const.FONT, 14), bg=const.BACKGROUND_COLOUR,
                                                     fg=const.FONT_COLOUR)
        self.checked_calling_codes_btt.grid(row=1, column=1, padx=20, sticky='W')

        self.checked_area_btt = Checkbutton(self.__extra_options_frame, text='Area (km\u00b2)',
                                            variable=self.__checked_area,
                                            onvalue=1, offvalue=0, font=(const.FONT, 14,),
                                            bg=const.BACKGROUND_COLOUR, fg=const.FONT_COLOUR)
        self.checked_area_btt.grid(row=1, column=2, padx=20, sticky='W')

    def __init_search_button(self):
        self.search_button = tk.Button(self.__entry_frame, text='Search', bg=const.BACKGROUND_COLOUR,
                                       font=(const.FONT, 18, 'bold'),
                                       bd=1,
                                       fg=const.FONT_COLOUR, activeforeground='snow', activebackground='AntiqueWhite4',
                                       command=lambda: self.create_new_window())
        self.search_button.grid(row=0, column=1, padx=(20, 10))

    def __get_entered_country_name(self):
        name = self.__country_name.get()
        return name

    def __clear_entry(self):
        self.entry_field.delete(0, END)

    def __deselect_check_buttons(self):
        self.checked_currencies_btt.deselect()
        self.checked_native_name_btt.deselect()
        self.checked_area_btt.deselect()
        self.checked_calling_codes_btt.deselect()
        self.checked_languages_btt.deselect()
        self.checked_timezones_btt.deselect()

    def save_country_info_to_file(self, country):
        name_of_file = country.capitalize()
        file = open(const.DEFAULT_COUNTRY_INFO_FILES_PATH + name_of_file + const.TXT_FILE_FORMAT, 'w')
        file.write(str(country_information.CountryInf(name_of_file).get_basic_info_for_country()))

        try:
            if self.__checked_calling_codes.get() == 1:
                file.write(str(country_information.CountryInf(name_of_file).get_calling_codes_for_country()))

            if self.__checked_area.get() == 1:
                file.write(str(country_information.CountryInf(name_of_file).get_area_for_country()))

            if self.__checked_timezones.get() == 1:
                file.write(str(country_information.CountryInf(name_of_file).get_timezones_for_country()))

            if self.__checked_languages.get() == 1:
                file.write(str(country_information.CountryInf(name_of_file).get_languages_for_country()))

            if self.__checked_currencies.get() == 1:
                file.write(str(country_information.CountryInf(name_of_file).get_timezones_for_country()))

            if self.__checked_native_name.get() == 1:
                file.write(str(country_information.CountryInf(name_of_file).get_native_name_for_country()))
        except ValueError:
            error_helper.incorrect_text_format_messagebox()

    def create_new_window(self):
        entered_name = self.__get_entered_country_name()
        entered_input_flag = False
        if entered_name == '':
            error_helper.empty_input_messagebox()
        else:
            entered_input_flag = True

        if entered_input_flag:
            try:
                country = country_information.CountryInf(entered_name)
                new_window = tk.Toplevel(self.__root)
                new_window.title(entered_name.capitalize() + ' info')
                new_window.geometry('600x600')
                new_window.minsize(500, 500)
                new_window.config(bg=const.BACKGROUND_COLOUR)
                icon = tk.PhotoImage(file=const.GLOBE_IMG)
                new_window.iconphoto(False, icon)

                country_name_frame = tk.Frame(new_window, bg=const.BACKGROUND_COLOUR)
                country_name_frame.pack()
                basic_info_frame = tk.Frame(new_window, bg=const.BACKGROUND_COLOUR)
                basic_info_frame.pack(side=TOP, anchor=NW, padx=(50, 30))
                extra_info_frame = tk.Frame(new_window, bg=const.BACKGROUND_COLOUR)
                extra_info_frame.pack(side=TOP, anchor=NW, padx=(50, 30))
                save_info_frame = tk.Frame(new_window, bg=const.BACKGROUND_COLOUR)
                save_info_frame.pack(side=TOP, anchor=NW, padx=(50, 30))

                # top label with country name
                label = tk.Label(country_name_frame, text=country.country_name.capitalize(), font=(const.FONT, 30,
                                                                                                   'bold'),
                                 bg=const.BACKGROUND_COLOUR, fg=const.FONT_COLOUR)
                label.grid(row=0, column=0, pady=10)

                # basic info labels
                info_label = tk.Label(basic_info_frame, text='Information', font=(const.FONT, 16, 'bold'),
                                      bg=const.BACKGROUND_COLOUR)
                info_label.grid(row=0, column=0, sticky='W')

                capital_city_label = tk.Label(basic_info_frame, text='Capital city: ' + country.capital,
                                              font=(const.FONT, 14), bg=const.BACKGROUND_COLOUR)
                capital_city_label.grid(row=1, column=0, sticky='W')

                continent_label = tk.Label(basic_info_frame, text='Continent: ' + country.region, font=(const.FONT, 14),
                                           bg=const.BACKGROUND_COLOUR)
                continent_label.grid(row=2, column=0, sticky='W')

                region_label = tk.Label(basic_info_frame, text='Region: ' + country.subregion, font=(const.FONT, 14),
                                        bg=const.BACKGROUND_COLOUR)
                region_label.grid(row=3, column=0, sticky='W')

                population_label = tk.Label(basic_info_frame, text='Population: ' + str(country.population),
                                            font=(const.FONT, 14),
                                            bg=const.BACKGROUND_COLOUR)
                population_label.grid(row=4, column=0, sticky='W')

                wikipedia_label = tk.Label(basic_info_frame, text='Wikipedia: ' + country.wiki, font=(const.FONT, 14),
                                           bg=const.BACKGROUND_COLOUR)
                wikipedia_label.grid(row=5, column=0, sticky='W')

                # extra info labels
                if self.__checked_calling_codes.get() == 1:
                    calling_codes_label = tk.Label(extra_info_frame,
                                                   text='Calling codes: ' + str(', '.join(country.calling_codes)),
                                                   font=(const.FONT, 14), bg=const.BACKGROUND_COLOUR)
                    calling_codes_label.pack(anchor=W)

                if self.__checked_area.get() == 1:
                    area_label = tk.Label(extra_info_frame, text='Area: ' + str(country.area) + ' km\u00b2',
                                          font=(const.FONT, 14), bg=const.BACKGROUND_COLOUR)
                    area_label.pack(anchor=W)

                if self.__checked_timezones.get() == 1:
                    timezones_label = tk.Label(extra_info_frame, text='Time zones: ' + str(', '.join(country.timezones)),
                                               font=(const.FONT, 14), bg=const.BACKGROUND_COLOUR)
                    timezones_label.pack(anchor=W)

                if self.__checked_languages.get() == 1:
                    languages_label = tk.Label(extra_info_frame, text='Languages: ' + str(', '.join(country.languages)),
                                               font=(const.FONT, 14), bg=const.BACKGROUND_COLOUR)
                    languages_label.pack(anchor=W)

                if self.__checked_currencies.get() == 1:
                    currencies_label = tk.Label(extra_info_frame, text='Currencies: ' + str(', '.join(country.currencies)),
                                                font=(const.FONT, 14), bg=const.BACKGROUND_COLOUR)
                    currencies_label.pack(anchor=W)

                if self.__checked_native_name.get() == 1:
                    native_name_label = tk.Label(extra_info_frame, text='Native name: ' + country.native_name,
                                                 font=(const.FONT, 14), bg=const.BACKGROUND_COLOUR)
                    native_name_label.pack(anchor=W)

                save_info_to_file_btt = tk.Button(save_info_frame, text='Save info to file', bg=const.BACKGROUND_COLOUR,
                                                  font=(const.FONT, 18, 'bold'), fg=const.FONT_COLOUR,
                                                  activeforeground='snow', activebackground='AntiqueWhite4',
                                                  command=lambda: self.save_country_info_to_file(country.country_name))
                save_info_to_file_btt.pack(pady=(50, 50))

                self.__clear_entry()
                self.__deselect_check_buttons()
            except KeyError:
                error_helper.input_error_messagebox()




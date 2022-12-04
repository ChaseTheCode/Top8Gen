import ttkbootstrap as ttk
from PIL import Image, ImageFont, ImageDraw
from ttkwidgets.autocomplete import AutocompleteEntry
from datetime import date
from tkinter.ttk import *
from os.path import exists
import params

class Event(ttk.Frame):
    def __init__(self, event_name="", event_number="", event_day="", event_entrant_count="", event_link=""):
        self.event_name = ttk.StringVar()
        self.event_number = ttk.StringVar()
        self.event_day = ttk.Variable(value=date)
        self.event_entrant_count = ttk.StringVar()
        self.event_link = ttk.StringVar(value="start.gg/")

class Game(ttk.Frame):
    def __init__(self, game_name=""):
        self.game_name = ttk.StringVar()

class Entrant(ttk.Frame):
    def __init__(self, team="", name_tag="", main_character="", main_character_color="", alternate1_character="", alternate1_character_color="", alternate2_character="", alternate2_character_color=""):
            self.team = ttk.StringVar()
            self.name_tag = ttk.StringVar()
            self.main_character = ttk.StringVar()
            self.main_character_color = ttk.StringVar()
            self.alternate1_character = ttk.StringVar()
            self.alternate1_character_color = ttk.StringVar()
            self.alternate2_character = ttk.StringVar()
            self.alternate2_character_color = ttk.StringVar()

    def __str__(self):
        return f"{self.team.get()} {self.name_tag.get()} {self.main_character.get()}_{self.main_character_color.get()} + {self.alternate1_character.get()}_{self.alternate1_character_color.get()} ++ {self.alternate2_character.get()}_{self.alternate2_character_color.get()}"


class MainApp(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.event = Event(event_name="", event_number="", event_day="", event_entrant_count="", event_link="")
        self.game = Game(game_name="")
        self.first_place = Entrant(team="", name_tag="", main_character="", main_character_color="", alternate1_character="", alternate1_character_color="", alternate2_character="", alternate2_character_color="")
        self.second_place = Entrant(team="", name_tag="", main_character="", main_character_color="", alternate1_character="", alternate1_character_color="", alternate2_character="", alternate2_character_color="")
        self.third_place = Entrant(team="", name_tag="", main_character="", main_character_color="", alternate1_character="", alternate1_character_color="", alternate2_character="", alternate2_character_color="")
        self.fourth_place = Entrant(team="", name_tag="", main_character="", main_character_color="", alternate1_character="", alternate1_character_color="", alternate2_character="", alternate2_character_color="")
        self.fifth_place = Entrant(team="", name_tag="", main_character="", main_character_color="", alternate1_character="", alternate1_character_color="", alternate2_character="", alternate2_character_color="")
        self.sixth_place = Entrant(team="", name_tag="", main_character="", main_character_color="", alternate1_character="", alternate1_character_color="", alternate2_character="", alternate2_character_color="")
        self.seventh_place = Entrant(team="", name_tag="", main_character="", main_character_color="", alternate1_character="", alternate1_character_color="", alternate2_character="", alternate2_character_color="")
        self.eighth_place = Entrant(team="", name_tag="", main_character="", main_character_color="", alternate1_character="", alternate1_character_color="", alternate2_character="", alternate2_character_color="")
        self.blurb_1 = ttk.StringVar(value="don't forget to register for DFW's Bizzare Adventure,")
        self.blurb_2 = ttk.StringVar(value="powered by the Liberty Rec Center in Plano, TX! Sign up today!")
        self.blurb_3 = ttk.StringVar(value="DFWba will feature Singles, 3v3 Squad Strike, and Doubles!")


        # oh boy time for characters

        with open('characters.csv', 'r') as file2:
            character_base = file2.readlines()

            characters, em_list = [], []
            for i in character_base:
                    characters.append(i.split(",")[0])
                    em_list.append(i.split(",")[1])

        event_list = ["USW", "MNM", "SSO", "NB"]

        game_list = ["SSBU", "SSBM", "GGST", "KOFXV", "DBFZ", "DNF", "MBTL", "XRD", ]

        color_list = ["00", "01", "02", "03", "04", "05", "06", "07"]

        # GUI BUILDER 9000

        # EVENT STUFF GOES HERE

        event_name_label = ttk.Label(eventbox, text="Event")

        event_name_entry = ttk.Combobox(eventbox, textvariable=self.event.event_name, width=15)
        event_name_entry['values'] = event_list
        event_number_entry = ttk.Entry(eventbox, textvariable=self.event.event_number, width=4)

        event_day_label = ttk.Label(eventbox, text="Date")
        event_day_entry = ttk.DateEntry(eventbox, dateformat="%B %d, %Y", width=20) # Entry for Event Day
        event_day_entry.entry.configure(textvariable=self.event.event_day) # configures textvariable for Event Day

        event_entrants_label = ttk.Label(eventbox, text="Entrants")
        event_entrants_entry = ttk.Entry(eventbox, textvariable=self.event.event_entrant_count, width=4)

        event_link_label = ttk.Label(eventbox, text="Event Link")
        event_link_entry = ttk.Entry(eventbox, textvariable=self.event.event_link, width=25)

        event_game_label = ttk.Label(eventbox, text="Game")
        event_game_entry = ttk.Combobox(eventbox, textvariable=self.game.game_name, width=6)
        event_game_entry['values'] = game_list

        make_it_button = ttk.Button(eventbox, text="MAKE IT", command=self.create_banner)

        event_name_label.grid(row=0, column=0, padx=2, pady=2)
        event_name_entry.grid(row=0, column=1, padx=2, pady=2)
        event_number_entry.grid(row=0, column=2, padx=2, pady=2)

        event_day_label.grid(row=0, column=3, padx=2, pady=2)
        event_day_entry.grid(row=0, column=4, padx=2, pady=2)

        event_entrants_label.grid(row=0, column=5, padx=2, pady=2)
        event_entrants_entry.grid(row=0, column=6, padx=2, pady=2)

        event_link_label.grid(row=0, column=7, padx=2, pady=2)
        event_link_entry.grid(row=0, column=8, padx=2, pady=2)

        event_game_label.grid(row=0, column=9, padx=2, pady=2)
        event_game_entry.grid(row=0, column=10, padx=2, pady=2)

        make_it_button.grid(row=0, column=11, padx=2, pady=2)
        # PLAYERS, THEIR CHARACTERS, AND WHERE TO CATCH HANDS

        # ALRIGHT, FIRST PLACE!

        firstplace_labelframe = ttk.LabelFrame(entrybox, text="1st Place", bootstyle="WARNING")
        firstplace_labelframe.grid(row=0, column=0, padx=2, pady=2)

        firstplace_team_label = ttk.Label(firstplace_labelframe, text="Team")
        firstplace_name_label = ttk.Label(firstplace_labelframe, text="Name")
        firstplace_main_char_label = ttk.Label(firstplace_labelframe, text="Main")
        firstplace_alt1_char_label = ttk.Label(firstplace_labelframe, text="Alt 1")
        firstplace_alt2_char_label = ttk.Label(firstplace_labelframe, text="Alt 2")

        firstplace_team_entry = ttk.Entry(firstplace_labelframe, textvariable=self.first_place.team)
        firstplace_name_entry = ttk.Entry(firstplace_labelframe, textvariable=self.first_place.name_tag)
        # Main Character
        firstplace_main_char_entry = AutocompleteEntry(firstplace_labelframe,  textvariable=self.first_place.main_character, completevalues=characters)
        firstplace_main_char_color_entry = ttk.Combobox(firstplace_labelframe, width=3, textvariable=self.first_place.main_character_color)
        firstplace_main_char_color_entry['values'] = color_list
        firstplace_main_char_color_entry.set("00")
        # Alternate 1
        firstplace_alt1_char_entry = AutocompleteEntry(firstplace_labelframe, textvariable=self.first_place.alternate1_character, completevalues=characters)
        firstplace_alt1_char_color_entry = ttk.Combobox(firstplace_labelframe, width=3, textvariable=self.first_place.alternate1_character_color)
        firstplace_alt1_char_color_entry['values'] = color_list
        firstplace_alt1_char_color_entry.set("00")
        # Alternate 2
        firstplace_alt2_char_entry = AutocompleteEntry(firstplace_labelframe, textvariable=self.first_place.alternate2_character, completevalues=characters)
        firstplace_alt2_char_color_entry = ttk.Combobox(firstplace_labelframe, width=3, textvariable=self.first_place.alternate2_character_color)
        firstplace_alt2_char_color_entry['values'] = color_list
        firstplace_alt2_char_color_entry.set("00")

        firstplace_team_label.grid(row=0, column=0, padx=2, pady=2)
        firstplace_team_entry.grid(row=0, column=1, padx=2, pady=2)

        firstplace_name_label.grid(row=1, column=0, padx=2, pady=2)
        firstplace_name_entry.grid(row=1, column=1, padx=2, pady=2)

        firstplace_main_char_label.grid(row=2, column=0, padx=2, pady=2)
        firstplace_main_char_entry.grid(row=2, column=1, padx=2, pady=2)
        firstplace_main_char_color_entry.grid(row=2, column=2, padx=2, pady=2)

        firstplace_alt1_char_label.grid(row=3, column=0, padx=2, pady=2)
        firstplace_alt1_char_entry.grid(row=3, column=1, padx=2, pady=2)
        firstplace_alt1_char_color_entry.grid(row=3, column=2, padx=2, pady=2)

        firstplace_alt2_char_label.grid(row=4, column=0, padx=2, pady=2)
        firstplace_alt2_char_entry.grid(row=4, column=1, padx=2, pady=2)
        firstplace_alt2_char_color_entry.grid(row=4, column=2, padx=2, pady=2)

        # YEAH, SECOND PLACE!

        secondplace_labelframe = ttk.LabelFrame(entrybox, text="2nd Place", bootstyle="SECONDARY")
        secondplace_labelframe.grid(row=0, column=1, padx=2, pady=2)

        secondplace_team_label = ttk.Label(secondplace_labelframe, text="Team")
        secondplace_name_label = ttk.Label(secondplace_labelframe, text="Name")
        secondplace_main_char_label = ttk.Label(secondplace_labelframe, text="Main")
        secondplace_alt1_char_label = ttk.Label(secondplace_labelframe, text="Alt 1")
        secondplace_alt2_char_label = ttk.Label(secondplace_labelframe, text="Alt 2")

        secondplace_team_entry = ttk.Entry(secondplace_labelframe, textvariable=self.second_place.team)
        secondplace_name_entry = ttk.Entry(secondplace_labelframe, textvariable=self.second_place.name_tag)
        # Main Character
        secondplace_main_char_entry = AutocompleteEntry(secondplace_labelframe,  textvariable=self.second_place.main_character, completevalues=characters)
        secondplace_main_char_color_entry = ttk.Combobox(secondplace_labelframe, width=3, textvariable=self.second_place.main_character_color)
        secondplace_main_char_color_entry['values'] = color_list
        secondplace_main_char_color_entry.set("00")
        # Alternate 1
        secondplace_alt1_char_entry = AutocompleteEntry(secondplace_labelframe, textvariable=self.second_place.alternate1_character, completevalues=characters)
        secondplace_alt1_char_color_entry = ttk.Combobox(secondplace_labelframe, width=3, textvariable=self.second_place.alternate1_character_color)
        secondplace_alt1_char_color_entry['values'] = color_list
        secondplace_alt1_char_color_entry.set("00")
        # Alternate 2
        secondplace_alt2_char_entry = AutocompleteEntry(secondplace_labelframe, textvariable=self.second_place.alternate2_character, completevalues=characters)
        secondplace_alt2_char_color_entry = ttk.Combobox(secondplace_labelframe, width=3, textvariable=self.second_place.alternate2_character_color)
        secondplace_alt2_char_color_entry['values'] = color_list
        secondplace_alt2_char_color_entry.set("00")

        secondplace_team_label.grid(row=0, column=0, padx=2, pady=2)
        secondplace_team_entry.grid(row=0, column=1, padx=2, pady=2)

        secondplace_name_label.grid(row=1, column=0, padx=2, pady=2)
        secondplace_name_entry.grid(row=1, column=1, padx=2, pady=2)

        secondplace_main_char_label.grid(row=2, column=0, padx=2, pady=2)
        secondplace_main_char_entry.grid(row=2, column=1, padx=2, pady=2)
        secondplace_main_char_color_entry.grid(row=2, column=2, padx=2, pady=2)

        secondplace_alt1_char_label.grid(row=3, column=0, padx=2, pady=2)
        secondplace_alt1_char_entry.grid(row=3, column=1, padx=2, pady=2)
        secondplace_alt1_char_color_entry.grid(row=3, column=2, padx=2, pady=2)

        secondplace_alt2_char_label.grid(row=4, column=0, padx=2, pady=2)
        secondplace_alt2_char_entry.grid(row=4, column=1, padx=2, pady=2)
        secondplace_alt2_char_color_entry.grid(row=4, column=2, padx=2, pady=2)
    


        # OKAY, THIRD PLACE!

        thirdplace_labelframe = ttk.LabelFrame(entrybox, text="3rd Place", bootstyle="DANGER")
        thirdplace_labelframe.grid(row=0, column=2, padx=2, pady=2)

        thirdplace_team_label = ttk.Label(thirdplace_labelframe, text="Team")
        thirdplace_name_label = ttk.Label(thirdplace_labelframe, text="Name")
        thirdplace_main_char_label = ttk.Label(thirdplace_labelframe, text="Main")
        thirdplace_alt1_char_label = ttk.Label(thirdplace_labelframe, text="Alt 1")
        thirdplace_alt2_char_label = ttk.Label(thirdplace_labelframe, text="Alt 2")

        thirdplace_team_entry = ttk.Entry(thirdplace_labelframe, textvariable=self.third_place.team)
        thirdplace_name_entry = ttk.Entry(thirdplace_labelframe, textvariable=self.third_place.name_tag)
        # Main Character
        thirdplace_main_char_entry = AutocompleteEntry(thirdplace_labelframe,  textvariable=self.third_place.main_character, completevalues=characters)
        thirdplace_main_char_color_entry = ttk.Combobox(thirdplace_labelframe, width=3, textvariable=self.third_place.main_character_color)
        thirdplace_main_char_color_entry['values'] = color_list
        thirdplace_main_char_color_entry.set("00")
        # Alternate 1
        thirdplace_alt1_char_entry = AutocompleteEntry(thirdplace_labelframe, textvariable=self.third_place.alternate1_character, completevalues=characters)
        thirdplace_alt1_char_color_entry = ttk.Combobox(thirdplace_labelframe, width=3, textvariable=self.third_place.alternate1_character_color)
        thirdplace_alt1_char_color_entry['values'] = color_list
        thirdplace_alt1_char_color_entry.set("00")
        # Alternate 2
        thirdplace_alt2_char_entry = AutocompleteEntry(thirdplace_labelframe, textvariable=self.third_place.alternate2_character, completevalues=characters)
        thirdplace_alt2_char_color_entry = ttk.Combobox(thirdplace_labelframe, width=3, textvariable=self.third_place.alternate2_character_color)
        thirdplace_alt2_char_color_entry['values'] = color_list
        thirdplace_alt2_char_color_entry.set("00")

        thirdplace_team_label.grid(row=0, column=0, padx=2, pady=2)
        thirdplace_team_entry.grid(row=0, column=1, padx=2, pady=2)

        thirdplace_name_label.grid(row=1, column=0, padx=2, pady=2)
        thirdplace_name_entry.grid(row=1, column=1, padx=2, pady=2)

        thirdplace_main_char_label.grid(row=2, column=0, padx=2, pady=2)
        thirdplace_main_char_entry.grid(row=2, column=1, padx=2, pady=2)
        thirdplace_main_char_color_entry.grid(row=2, column=2, padx=2, pady=2)

        thirdplace_alt1_char_label.grid(row=3, column=0, padx=2, pady=2)
        thirdplace_alt1_char_entry.grid(row=3, column=1, padx=2, pady=2)
        thirdplace_alt1_char_color_entry.grid(row=3, column=2, padx=2, pady=2)

        thirdplace_alt2_char_label.grid(row=4, column=0, padx=2, pady=2)
        thirdplace_alt2_char_entry.grid(row=4, column=1, padx=2, pady=2)
        thirdplace_alt2_char_color_entry.grid(row=4, column=2, padx=2, pady=2)

        # OKAY, FOURTH PLACE...

        fourthplace_labelframe = ttk.LabelFrame(entrybox, text="4th Place", bootstyle="LIGHT")
        fourthplace_labelframe.grid(row=0, column=3, padx=2, pady=2)

        fourthplace_team_label = ttk.Label(fourthplace_labelframe, text="Team")
        fourthplace_name_label = ttk.Label(fourthplace_labelframe, text="Name")
        fourthplace_main_char_label = ttk.Label(fourthplace_labelframe, text="Main")
        fourthplace_alt1_char_label = ttk.Label(fourthplace_labelframe, text="Alt 1")
        fourthplace_alt2_char_label = ttk.Label(fourthplace_labelframe, text="Alt 2")

        fourthplace_team_entry = ttk.Entry(fourthplace_labelframe, textvariable=self.fourth_place.team)
        fourthplace_name_entry = ttk.Entry(fourthplace_labelframe, textvariable=self.fourth_place.name_tag)
        # Main Character
        fourthplace_main_char_entry = AutocompleteEntry(fourthplace_labelframe,  textvariable=self.fourth_place.main_character, completevalues=characters)
        fourthplace_main_char_color_entry = ttk.Combobox(fourthplace_labelframe, width=3, textvariable=self.fourth_place.main_character_color)
        fourthplace_main_char_color_entry['values'] = color_list
        fourthplace_main_char_color_entry.set("00")
        # Alternate 1
        fourthplace_alt1_char_entry = AutocompleteEntry(fourthplace_labelframe, textvariable=self.fourth_place.alternate1_character, completevalues=characters)
        fourthplace_alt1_char_color_entry = ttk.Combobox(fourthplace_labelframe, width=3, textvariable=self.fourth_place.alternate1_character_color)
        fourthplace_alt1_char_color_entry['values'] = color_list
        fourthplace_alt1_char_color_entry.set("00")
        # Alternate 2
        fourthplace_alt2_char_entry = AutocompleteEntry(fourthplace_labelframe, textvariable=self.fourth_place.alternate2_character, completevalues=characters)
        fourthplace_alt2_char_color_entry = ttk.Combobox(fourthplace_labelframe, width=3, textvariable=self.fourth_place.alternate2_character_color)
        fourthplace_alt2_char_color_entry['values'] = color_list
        fourthplace_alt2_char_color_entry.set("00")

        fourthplace_team_label.grid(row=0, column=0, padx=2, pady=2)
        fourthplace_team_entry.grid(row=0, column=1, padx=2, pady=2)

        fourthplace_name_label.grid(row=1, column=0, padx=2, pady=2)
        fourthplace_name_entry.grid(row=1, column=1, padx=2, pady=2)

        fourthplace_main_char_label.grid(row=2, column=0, padx=2, pady=2)
        fourthplace_main_char_entry.grid(row=2, column=1, padx=2, pady=2)
        fourthplace_main_char_color_entry.grid(row=2, column=2, padx=2, pady=2)

        fourthplace_alt1_char_label.grid(row=3, column=0, padx=2, pady=2)
        fourthplace_alt1_char_entry.grid(row=3, column=1, padx=2, pady=2)
        fourthplace_alt1_char_color_entry.grid(row=3, column=2, padx=2, pady=2)

        fourthplace_alt2_char_label.grid(row=4, column=0, padx=2, pady=2)
        fourthplace_alt2_char_entry.grid(row=4, column=1, padx=2, pady=2)
        fourthplace_alt2_char_color_entry.grid(row=4, column=2, padx=2, pady=2)


        # HMM, FIFTH PLACE...

        fifthplace_labelframe = ttk.LabelFrame(entrybox, text="5th Place [1]", bootstyle="LIGHT")
        fifthplace_labelframe.grid(row=1, column=0, padx=2, pady=2)

        fifthplace_team_label = ttk.Label(fifthplace_labelframe, text="Team")
        fifthplace_name_label = ttk.Label(fifthplace_labelframe, text="Name")
        fifthplace_main_char_label = ttk.Label(fifthplace_labelframe, text="Main")
        fifthplace_alt1_char_label = ttk.Label(fifthplace_labelframe, text="Alt 1")
        fifthplace_alt2_char_label = ttk.Label(fifthplace_labelframe, text="Alt 2")

        fifthplace_team_entry = ttk.Entry(fifthplace_labelframe, textvariable=self.fifth_place.team)
        fifthplace_name_entry = ttk.Entry(fifthplace_labelframe, textvariable=self.fifth_place.name_tag)
        # Main Character
        fifthplace_main_char_entry = AutocompleteEntry(fifthplace_labelframe,  textvariable=self.fifth_place.main_character, completevalues=characters)
        fifthplace_main_char_color_entry = ttk.Combobox(fifthplace_labelframe, width=3, textvariable=self.fifth_place.main_character_color)
        fifthplace_main_char_color_entry['values'] = color_list
        fifthplace_main_char_color_entry.set("00")
        # Alternate 1
        fifthplace_alt1_char_entry = AutocompleteEntry(fifthplace_labelframe, textvariable=self.fifth_place.alternate1_character, completevalues=characters)
        fifthplace_alt1_char_color_entry = ttk.Combobox(fifthplace_labelframe, width=3, textvariable=self.fifth_place.alternate1_character_color)
        fifthplace_alt1_char_color_entry['values'] = color_list
        fifthplace_alt1_char_color_entry.set("00")
        # Alternate 2
        fifthplace_alt2_char_entry = AutocompleteEntry(fifthplace_labelframe, textvariable=self.fifth_place.alternate2_character, completevalues=characters)
        fifthplace_alt2_char_color_entry = ttk.Combobox(fifthplace_labelframe, width=3, textvariable=self.fifth_place.alternate2_character_color)
        fifthplace_alt2_char_color_entry['values'] = color_list
        fifthplace_alt2_char_color_entry.set("00")

        fifthplace_team_label.grid(row=0, column=0, padx=2, pady=2)
        fifthplace_team_entry.grid(row=0, column=1, padx=2, pady=2)

        fifthplace_name_label.grid(row=1, column=0, padx=2, pady=2)
        fifthplace_name_entry.grid(row=1, column=1, padx=2, pady=2)

        fifthplace_main_char_label.grid(row=2, column=0, padx=2, pady=2)
        fifthplace_main_char_entry.grid(row=2, column=1, padx=2, pady=2)
        fifthplace_main_char_color_entry.grid(row=2, column=2, padx=2, pady=2)

        fifthplace_alt1_char_label.grid(row=3, column=0, padx=2, pady=2)
        fifthplace_alt1_char_entry.grid(row=3, column=1, padx=2, pady=2)
        fifthplace_alt1_char_color_entry.grid(row=3, column=2, padx=2, pady=2)

        fifthplace_alt2_char_label.grid(row=4, column=0, padx=2, pady=2)
        fifthplace_alt2_char_entry.grid(row=4, column=1, padx=2, pady=2)
        fifthplace_alt2_char_color_entry.grid(row=4, column=2, padx=2, pady=2)

        # HMM, SIXTH PLACE...

        sixthplace_labelframe = ttk.LabelFrame(entrybox, text="5th Place [2]", bootstyle="LIGHT")
        sixthplace_labelframe.grid(row=1, column=1, padx=2, pady=2)

        sixthplace_team_label = ttk.Label(sixthplace_labelframe, text="Team")
        sixthplace_name_label = ttk.Label(sixthplace_labelframe, text="Name")
        sixthplace_main_char_label = ttk.Label(sixthplace_labelframe, text="Main")
        sixthplace_alt1_char_label = ttk.Label(sixthplace_labelframe, text="Alt 1")
        sixthplace_alt2_char_label = ttk.Label(sixthplace_labelframe, text="Alt 2")

        sixthplace_team_entry = ttk.Entry(sixthplace_labelframe, textvariable=self.sixth_place.team)
        sixthplace_name_entry = ttk.Entry(sixthplace_labelframe, textvariable=self.sixth_place.name_tag)
        # Main Character
        sixthplace_main_char_entry = AutocompleteEntry(sixthplace_labelframe,  textvariable=self.sixth_place.main_character, completevalues=characters)
        sixthplace_main_char_color_entry = ttk.Combobox(sixthplace_labelframe, width=3, textvariable=self.sixth_place.main_character_color)
        sixthplace_main_char_color_entry['values'] = color_list
        sixthplace_main_char_color_entry.set("00")
        # Alternate 1
        sixthplace_alt1_char_entry = AutocompleteEntry(sixthplace_labelframe, textvariable=self.sixth_place.alternate1_character, completevalues=characters)
        sixthplace_alt1_char_color_entry = ttk.Combobox(sixthplace_labelframe, width=3, textvariable=self.sixth_place.alternate1_character_color)
        sixthplace_alt1_char_color_entry['values'] = color_list
        sixthplace_alt1_char_color_entry.set("00")
        # Alternate 2
        sixthplace_alt2_char_entry = AutocompleteEntry(sixthplace_labelframe, textvariable=self.sixth_place.alternate2_character, completevalues=characters)
        sixthplace_alt2_char_color_entry = ttk.Combobox(sixthplace_labelframe, width=3, textvariable=self.sixth_place.alternate2_character_color)
        sixthplace_alt2_char_color_entry['values'] = color_list
        sixthplace_alt2_char_color_entry.set("00")

        sixthplace_team_label.grid(row=0, column=0, padx=2, pady=2)
        sixthplace_team_entry.grid(row=0, column=1, padx=2, pady=2)

        sixthplace_name_label.grid(row=1, column=0, padx=2, pady=2)
        sixthplace_name_entry.grid(row=1, column=1, padx=2, pady=2)

        sixthplace_main_char_label.grid(row=2, column=0, padx=2, pady=2)
        sixthplace_main_char_entry.grid(row=2, column=1, padx=2, pady=2)
        sixthplace_main_char_color_entry.grid(row=2, column=2, padx=2, pady=2)

        sixthplace_alt1_char_label.grid(row=3, column=0, padx=2, pady=2)
        sixthplace_alt1_char_entry.grid(row=3, column=1, padx=2, pady=2)
        sixthplace_alt1_char_color_entry.grid(row=3, column=2, padx=2, pady=2)

        sixthplace_alt2_char_label.grid(row=4, column=0, padx=2, pady=2)
        sixthplace_alt2_char_entry.grid(row=4, column=1, padx=2, pady=2)
        sixthplace_alt2_char_color_entry.grid(row=4, column=2, padx=2, pady=2)

        # OH, SEVENTH PLACE...

        seventhplace_labelframe = ttk.LabelFrame(entrybox, text="7th Place [1]", bootstyle="LIGHT")
        seventhplace_labelframe.grid(row=1, column=2, padx=2, pady=2)

        seventhplace_team_label = ttk.Label(seventhplace_labelframe, text="Team")
        seventhplace_name_label = ttk.Label(seventhplace_labelframe, text="Name")
        seventhplace_main_char_label = ttk.Label(seventhplace_labelframe, text="Main")
        seventhplace_alt1_char_label = ttk.Label(seventhplace_labelframe, text="Alt 1")
        seventhplace_alt2_char_label = ttk.Label(seventhplace_labelframe, text="Alt 2")

        seventhplace_team_entry = ttk.Entry(seventhplace_labelframe, textvariable=self.seventh_place.team)
        seventhplace_name_entry = ttk.Entry(seventhplace_labelframe, textvariable=self.seventh_place.name_tag)
        # Main Character
        seventhplace_main_char_entry = AutocompleteEntry(seventhplace_labelframe,  textvariable=self.seventh_place.main_character, completevalues=characters)
        seventhplace_main_char_color_entry = ttk.Combobox(seventhplace_labelframe, width=3, textvariable=self.seventh_place.main_character_color)
        seventhplace_main_char_color_entry['values'] = color_list
        seventhplace_main_char_color_entry.set("00")
        # Alternate 1
        seventhplace_alt1_char_entry = AutocompleteEntry(seventhplace_labelframe, textvariable=self.seventh_place.alternate1_character, completevalues=characters)
        seventhplace_alt1_char_color_entry = ttk.Combobox(seventhplace_labelframe, width=3, textvariable=self.seventh_place.alternate1_character_color)
        seventhplace_alt1_char_color_entry['values'] = color_list
        seventhplace_alt1_char_color_entry.set("00")
        # Alternate 2
        seventhplace_alt2_char_entry = AutocompleteEntry(seventhplace_labelframe, textvariable=self.seventh_place.alternate2_character, completevalues=characters)
        seventhplace_alt2_char_color_entry = ttk.Combobox(seventhplace_labelframe, width=3, textvariable=self.seventh_place.alternate2_character_color)
        seventhplace_alt2_char_color_entry['values'] = color_list
        seventhplace_alt2_char_color_entry.set("00")

        seventhplace_team_label.grid(row=0, column=0, padx=2, pady=2)
        seventhplace_team_entry.grid(row=0, column=1, padx=2, pady=2)

        seventhplace_name_label.grid(row=1, column=0, padx=2, pady=2)
        seventhplace_name_entry.grid(row=1, column=1, padx=2, pady=2)

        seventhplace_main_char_label.grid(row=2, column=0, padx=2, pady=2)
        seventhplace_main_char_entry.grid(row=2, column=1, padx=2, pady=2)
        seventhplace_main_char_color_entry.grid(row=2, column=2, padx=2, pady=2)

        seventhplace_alt1_char_label.grid(row=3, column=0, padx=2, pady=2)
        seventhplace_alt1_char_entry.grid(row=3, column=1, padx=2, pady=2)
        seventhplace_alt1_char_color_entry.grid(row=3, column=2, padx=2, pady=2)

        seventhplace_alt2_char_label.grid(row=4, column=0, padx=2, pady=2)
        seventhplace_alt2_char_entry.grid(row=4, column=1, padx=2, pady=2)
        seventhplace_alt2_char_color_entry.grid(row=4, column=2, padx=2, pady=2)

        # OH, EIGHTH PLACE...

        eighthplace_labelframe = ttk.LabelFrame(entrybox, text="7th Place [2]", bootstyle="LIGHT")
        eighthplace_labelframe.grid(row=1, column=3, padx=2, pady=2)

        eighthplace_team_label = ttk.Label(eighthplace_labelframe, text="Team")
        eighthplace_name_label = ttk.Label(eighthplace_labelframe, text="Name")
        eighthplace_main_char_label = ttk.Label(eighthplace_labelframe, text="Main")
        eighthplace_alt1_char_label = ttk.Label(eighthplace_labelframe, text="Alt 1")
        eighthplace_alt2_char_label = ttk.Label(eighthplace_labelframe, text="Alt 2")

        eighthplace_team_entry = ttk.Entry(eighthplace_labelframe, textvariable=self.eighth_place.team)
        eighthplace_name_entry = ttk.Entry(eighthplace_labelframe, textvariable=self.eighth_place.name_tag)
        # Main Character
        eighthplace_main_char_entry = AutocompleteEntry(eighthplace_labelframe,  textvariable=self.eighth_place.main_character, completevalues=characters)
        eighthplace_main_char_color_entry = ttk.Combobox(eighthplace_labelframe, width=3, textvariable=self.eighth_place.main_character_color)
        eighthplace_main_char_color_entry['values'] = color_list
        eighthplace_main_char_color_entry.set("00")
        # Alternate 1
        eighthplace_alt1_char_entry = AutocompleteEntry(eighthplace_labelframe, textvariable=self.eighth_place.alternate1_character, completevalues=characters)
        eighthplace_alt1_char_color_entry = ttk.Combobox(eighthplace_labelframe, width=3, textvariable=self.eighth_place.alternate1_character_color)
        eighthplace_alt1_char_color_entry['values'] = color_list
        eighthplace_alt1_char_color_entry.set("00")
        # Alternate 2
        eighthplace_alt2_char_entry = AutocompleteEntry(eighthplace_labelframe, textvariable=self.eighth_place.alternate2_character, completevalues=characters)
        eighthplace_alt2_char_color_entry = ttk.Combobox(eighthplace_labelframe, width=3, textvariable=self.eighth_place.alternate2_character_color)
        eighthplace_alt2_char_color_entry['values'] = color_list
        eighthplace_alt2_char_color_entry.set("00")

        eighthplace_team_label.grid(row=0, column=0, padx=2, pady=2)
        eighthplace_team_entry.grid(row=0, column=1, padx=2, pady=2)

        eighthplace_name_label.grid(row=1, column=0, padx=2, pady=2)
        eighthplace_name_entry.grid(row=1, column=1, padx=2, pady=2)

        eighthplace_main_char_label.grid(row=2, column=0, padx=2, pady=2)
        eighthplace_main_char_entry.grid(row=2, column=1, padx=2, pady=2)
        eighthplace_main_char_color_entry.grid(row=2, column=2, padx=2, pady=2)

        eighthplace_alt1_char_label.grid(row=3, column=0, padx=2, pady=2)
        eighthplace_alt1_char_entry.grid(row=3, column=1, padx=2, pady=2)
        eighthplace_alt1_char_color_entry.grid(row=3, column=2, padx=2, pady=2)

        eighthplace_alt2_char_label.grid(row=4, column=0, padx=2, pady=2)
        eighthplace_alt2_char_entry.grid(row=4, column=1, padx=2, pady=2)
        eighthplace_alt2_char_color_entry.grid(row=4, column=2, padx=2, pady=2)

        # Blurb Time

        blurb_label = ttk.Label(blurbbox, text="Blurb")
        blurb_line_1 = ttk.Entry(blurbbox, textvariable=self.blurb_1, width=80)
        blurb_line_2 = ttk.Entry(blurbbox, textvariable=self.blurb_2, width=80)
        blurb_line_3 = ttk.Entry(blurbbox, textvariable=self.blurb_3, width=80)

        def update(event):
            label_b1.config(text=str(len(blurb_line_1.get())))
            label_b2.config(text=str(len(blurb_line_2.get())))
            label_b3.config(text=str(len(blurb_line_3.get())))


        label_b1 = ttk.Label(blurbbox)
        label_b2 = ttk.Label(blurbbox)
        label_b3 = ttk.Label(blurbbox)

        blurb_label.grid(row=0, column=0, padx=2, pady=2)
        blurb_line_1.grid(row=1, column=0, padx=2, pady=2)
        blurb_line_2.grid(row=2, column=0, padx=2, pady=2)
        blurb_line_3.grid(row=3, column=0, padx=2, pady=2)

        label_b1.grid(row=1, column=1, padx=2, pady=2)
        label_b2.grid(row=2, column=1, padx=2, pady=2)
        label_b3.grid(row=3, column=1, padx=2, pady=2)


        blurb_line_1.bind('<KeyPress>', update)
        blurb_line_1.bind('<KeyRelease>', update)

        blurb_line_2.bind('<KeyPress>', update)
        blurb_line_2.bind('<KeyRelease>', update)
        
        blurb_line_3.bind('<KeyPress>', update)
        blurb_line_3.bind('<KeyRelease>', update)
        


    def print_raw(self):
        print(self.first_place)
        print(self.second_place)
        print(self.third_place)
        print(self.fourth_place)
        print(self.fifth_place)
        print(self.sixth_place)
        print(self.seventh_place)
        print(self.eighth_place)
    
    def create_banner(self):

        # bg size 1920 x 1080
        bg = Image.open('resources/events/%s/background.png' % (self.event.event_name.get()))
        fg = Image.open('resources/events/%s/numbers.png' % (self.event.event_name.get()))
        cboxes = Image.open('resources/events/%s/playerboxes.png' % (self.event.event_name.get()))
        nameplates = Image.open('resources/events/%s/nameplates.png' % (self.event.event_name.get()))
        sponsor_big = Image.open('resources/events/%s/sponsor_big.png' % (self.event.event_name.get()))
        sponsor_med = Image.open('resources/events/%s/sponsor_med.png' % (self.event.event_name.get()))
        sponsor_sml = Image.open('resources/events/%s/sponsor_sml.png' % (self.event.event_name.get()))
        
        if self.event.event_name.get() == "NB":
            secondary_big = Image.open('resources/events/NB/secondary_large.png')
            secondary_med = Image.open('resources/events/NB/secondary_med.png')
            secondary_sml = Image.open('resources/events/NB/secondary_small.png')


        nboxW, nboxH = 600, 100

        bboxW, bboxH = 1300, 250

        spnsW, spnsH = 100, 50

        fnt = ImageFont.truetype('resources/events/%s/font.ttf' % (self.event.event_name.get()) , 1)

        def create_namebox(namebox, fawnt, name, vOffset=0, color=(255, 255, 255, 255) ):
            draw = ImageDraw.Draw(namebox)
            nameW, nameH = draw.textsize(name, fawnt)
            position = ((nboxW-nameW)/2,vOffset)
            draw.text(position, name, color, font=fawnt)

            return namebox

        def create_blurb_box(blurb_box, fawnt, name, vOffset=0, color=(255, 255, 255, 255) ):
            draw = ImageDraw.Draw(blurb_box)
            blurbW, blurbH = draw.textsize(name, fawnt)
            position = (0,vOffset)
            draw.text(position, name, color, font=fawnt, anchor="lt")

            return blurb_box

        def create_sponsorbox(sponsorbox, fawnt, name, vOffset=0, color=(255, 255, 255, 255) ):
            draw = ImageDraw.Draw(sponsorbox)
            spnsW, spnsH = draw.textsize(name, fawnt)
            position = ((spnsW-spnsW)/2,vOffset)
            draw.text(position, name, color, font=fawnt)

            return sponsorbox

        # 1st  w 600 x h 647

        # port size w 654 x h 706
        # icon size 64 x 64

        first_portrait = Image.open('resources/characters/%s/portraits/%s_%s.png' % (self.game.game_name.get(), self.first_place.main_character.get(), self.first_place.main_character_color.get()))

        first_portrait = first_portrait.resize((params.tier1_info[self.event.event_name.get()][0], params.tier1_info[self.event.event_name.get()][1]), Image.Resampling.LANCZOS)

        # open if
        if self.first_place.alternate1_character.get():
            if self.event.event_name.get() == "NB":
                first_portrait.paste(secondary_big, (params.tier1_info[self.event.event_name.get()][6], params.tier1_info[self.event.event_name.get()][7]))
            first_secondary_1 = Image.open('resources/characters/%s/icons/%s_%s.png' % (self.game.game_name.get(), self.first_place.alternate1_character.get(), self.first_place.alternate1_character_color.get()))
            first_secondary_1 = first_secondary_1.resize((params.tier1_info[self.event.event_name.get()][2],params.tier1_info[self.event.event_name.get()][3]), Image.Resampling.LANCZOS)
            first_portrait.paste(first_secondary_1, (params.tier1_info[self.event.event_name.get()][6], params.tier1_info[self.event.event_name.get()][7]), first_secondary_1)
        # close if

        # open if
        if self.first_place.alternate2_character.get():
            if self.event.event_name.get() == "NB":
                first_portrait.paste(secondary_big, (params.tier1_info[self.event.event_name.get()][8], params.tier1_info[self.event.event_name.get()][9]))
            first_secondary_2 = Image.open('resources/characters/%s/icons/%s_%s.png' % (self.game.game_name.get(), self.first_place.alternate2_character.get(), self.first_place.alternate2_character_color.get()))
            first_secondary_2 = first_secondary_2.resize((params.tier1_info[self.event.event_name.get()][2],params.tier1_info[self.event.event_name.get()][3]), Image.Resampling.LANCZOS)
            first_portrait.paste(first_secondary_2, (params.tier1_info[self.event.event_name.get()][8], params.tier1_info[self.event.event_name.get()][9]), first_secondary_2)
        # close if


        # open if sponsor
        if self.first_place.team.get():
            fnt = ImageFont.truetype('resources/events/%s/font.ttf' % (self.event.event_name.get()), params.tier1_info[self.event.event_name.get()][16])
            first_portrait.paste(sponsor_big, (params.tier1_info[self.event.event_name.get()][10], params.tier1_info[self.event.event_name.get()][11]))
        # open if sponsor text
            sponsor1_text = Image.new('RGBA', (spnsW, spnsH))
            sponsor1_text = create_sponsorbox(sponsor1_text, fnt, self.first_place.team.get())
            first_portrait.paste(sponsor1_text, (params.tier1_info[self.event.event_name.get()][12], params.tier1_info[self.event.event_name.get()][13]), sponsor1_text)
        # close sponsor text

        # open if sponsor image
            if exists('resources/sponsors/%s.png' % (self.first_place.team.get())):
                sponsor1_image = Image.open('resources/sponsors/%s.png' % (self.first_place.team.get()))
                sponsor1_image.getbbox()
                sponsor1_image = sponsor1_image.crop(sponsor1_image.getbbox())
                sponsor1_image.thumbnail((params.tier1_info[self.event.event_name.get()][4], params.tier1_info[self.event.event_name.get()][5]), Image.Resampling.LANCZOS)
                first_portrait.paste(sponsor1_image, (params.tier1_info[self.event.event_name.get()][14], params.tier1_info[self.event.event_name.get()][15]), sponsor1_image)
        # close if sponsor image

        # close if sponsor

        fnt = ImageFont.truetype('resources/events/%s/font.ttf' % (self.event.event_name.get()), params.tier1_info[self.event.event_name.get()][17])

        namebox1 = Image.new('RGBA', (nboxW, nboxH))
        namebox1 = create_namebox(namebox1, fnt, self.first_place.name_tag.get().upper())

        # 2nd-4th 322 x 348

        # second

        second_portrait = Image.open('resources/characters/%s/portraits/%s_%s.png' % (self.game.game_name.get(), self.second_place.main_character.get(), self.second_place.main_character_color.get()))

        second_portrait = second_portrait.resize((params.tier2_info[self.event.event_name.get()][0], params.tier2_info[self.event.event_name.get()][1]), Image.Resampling.LANCZOS)

        # open if secondary 1
        if self.second_place.alternate1_character.get():
            if self.event.event_name.get() == "NB":
                second_portrait.paste(secondary_med, (params.tier2_info[self.event.event_name.get()][6], params.tier2_info[self.event.event_name.get()][7]))
            second_secondary_1 = Image.open('resources/characters/%s/icons/%s_%s.png' % (self.game.game_name.get(), self.second_place.alternate1_character.get(), self.second_place.alternate1_character_color.get()))
            second_secondary_1 = second_secondary_1.resize((params.tier2_info[self.event.event_name.get()][2],params.tier2_info[self.event.event_name.get()][3]), Image.Resampling.LANCZOS)
            second_portrait.paste(second_secondary_1, (params.tier2_info[self.event.event_name.get()][6], params.tier2_info[self.event.event_name.get()][7]), second_secondary_1)
        # close if secondary 1

        # open if secondary 2
        if self.second_place.alternate2_character.get():
            if self.event.event_name.get() == "NB":
                second_portrait.paste(secondary_med, (params.tier2_info[self.event.event_name.get()][8], params.tier2_info[self.event.event_name.get()][9]))
            second_secondary_2 = Image.open('resources/characters/%s/icons/%s_%s.png' % (self.game.game_name.get(), self.second_place.alternate2_character.get(), self.second_place.alternate2_character_color.get()))
            second_secondary_2 = second_secondary_2.resize((params.tier2_info[self.event.event_name.get()][2],params.tier2_info[self.event.event_name.get()][3]), Image.Resampling.LANCZOS)
            second_portrait.paste(second_secondary_2, (params.tier2_info[self.event.event_name.get()][8], params.tier2_info[self.event.event_name.get()][9]), second_secondary_2)
        # close if secondary 2

        # open if sponsor
        if self.second_place.team.get():
            fnt = ImageFont.truetype('resources/events/%s/font.ttf' % (self.event.event_name.get()), params.tier2_info[self.event.event_name.get()][16])
            second_portrait.paste(sponsor_med, (params.tier2_info[self.event.event_name.get()][10], params.tier2_info[self.event.event_name.get()][11]))

            # open sponsor text
            sponsor2_text = Image.new('RGBA', (spnsW, spnsH))
            sponsor2_text = create_sponsorbox(sponsor2_text, fnt, self.second_place.team.get())
            second_portrait.paste(sponsor2_text, (params.tier2_info[self.event.event_name.get()][12], params.tier2_info[self.event.event_name.get()][13]), sponsor2_text)
            # close sponsor text

            # open sponsor image
            if exists('resources/sponsors/%s.png' % (self.second_place.team.get())):
                sponsor2_image = Image.open('resources/sponsors/%s.png' % (self.second_place.team.get()))
                sponsor2_image.getbbox()
                sponsor2_image = sponsor2_image.crop(sponsor2_image.getbbox())
                sponsor2_image.thumbnail((params.tier2_info[self.event.event_name.get()][4], params.tier2_info[self.event.event_name.get()][5]), Image.Resampling.LANCZOS)
                second_portrait.paste(sponsor2_image, (params.tier2_info[self.event.event_name.get()][14], params.tier2_info[self.event.event_name.get()][15]), sponsor2_image)
        # close sponsor image

        # close if sponsor


        fnt = ImageFont.truetype('resources/events/%s/font.ttf' % (self.event.event_name.get()), params.tier2_info[self.event.event_name.get()][17])
        namebox2 = Image.new('RGBA', (nboxW, nboxH))
        namebox2 = create_namebox(namebox2, fnt, self.second_place.name_tag.get().upper())

        # third

        third_portrait = Image.open('resources/characters/%s/portraits/%s_%s.png' % (self.game.game_name.get(), self.third_place.main_character.get(), self.third_place.main_character_color.get()))

        third_portrait = third_portrait.resize((params.tier2_info[self.event.event_name.get()][0], params.tier2_info[self.event.event_name.get()][1]), Image.Resampling.LANCZOS)

        if self.third_place.alternate1_character.get():
            if self.event.event_name.get() == "NB":
                third_portrait.paste(secondary_med, (params.tier2_info[self.event.event_name.get()][6], params.tier2_info[self.event.event_name.get()][7]))
            third_secondary_1 = Image.open('resources/characters/%s/icons/%s_%s.png' % (self.game.game_name.get(), self.third_place.alternate1_character.get(), self.third_place.alternate1_character_color.get()))
            third_secondary_1 = third_secondary_1.resize((params.tier2_info[self.event.event_name.get()][2],params.tier2_info[self.event.event_name.get()][3]), Image.Resampling.LANCZOS)
            third_portrait.paste(third_secondary_1, (params.tier2_info[self.event.event_name.get()][6], params.tier2_info[self.event.event_name.get()][7]), third_secondary_1)

        if self.third_place.alternate2_character.get():
            if self.event.event_name.get() == "NB":
                third_portrait.paste(secondary_med, (params.tier2_info[self.event.event_name.get()][8], params.tier2_info[self.event.event_name.get()][9]))
            third_secondary_2 = Image.open('resources/characters/%s/icons/%s_%s.png' % (self.game.game_name.get(), self.third_place.alternate2_character.get(), self.third_place.alternate2_character_color.get()))
            third_secondary_2 = third_secondary_2.resize((params.tier2_info[self.event.event_name.get()][2],params.tier2_info[self.event.event_name.get()][3]), Image.Resampling.LANCZOS)
            third_portrait.paste(third_secondary_2, (params.tier2_info[self.event.event_name.get()][8], params.tier2_info[self.event.event_name.get()][9]), third_secondary_2)

        # open if sponsor
        if self.third_place.team.get():
            fnt = ImageFont.truetype('resources/events/%s/font.ttf' % (self.event.event_name.get()), params.tier2_info[self.event.event_name.get()][16])
            third_portrait.paste(sponsor_med, (params.tier2_info[self.event.event_name.get()][10], params.tier2_info[self.event.event_name.get()][11]))

            # open sponsor text
            sponsor3_text = Image.new('RGBA', (spnsW, spnsH))
            sponsor3_text = create_sponsorbox(sponsor3_text, fnt, self.third_place.team.get())
            third_portrait.paste(sponsor3_text, (params.tier2_info[self.event.event_name.get()][12], params.tier2_info[self.event.event_name.get()][13]), sponsor3_text)
            # close sponsor text

            # open sponsor image
            if exists('resources/sponsors/%s.png' % (self.third_place.team.get())):
                sponsor3_image = Image.open('resources/sponsors/%s.png' % (self.third_place.team.get()))
                sponsor3_image.getbbox()
                sponsor3_image = sponsor3_image.crop(sponsor3_image.getbbox())
                sponsor3_image.thumbnail((params.tier2_info[self.event.event_name.get()][4], params.tier2_info[self.event.event_name.get()][5]), Image.Resampling.LANCZOS)
                third_portrait.paste(sponsor3_image, (params.tier2_info[self.event.event_name.get()][14], params.tier2_info[self.event.event_name.get()][15]), sponsor3_image)
        # close sponsor image

        # close if sponsor

        fnt = ImageFont.truetype('resources/events/%s/font.ttf' % (self.event.event_name.get()), params.tier2_info[self.event.event_name.get()][17])
        namebox3 = Image.new('RGBA', (nboxW, nboxH))
        namebox3 = create_namebox(namebox3, fnt, self.third_place.name_tag.get().upper())

        # fourth

        fourth_portrait = Image.open('resources/characters/%s/portraits/%s_%s.png' % (self.game.game_name.get(), self.fourth_place.main_character.get(), self.fourth_place.main_character_color.get()))

        fourth_portrait = fourth_portrait.resize((params.tier2_info[self.event.event_name.get()][0], params.tier2_info[self.event.event_name.get()][1]), Image.Resampling.LANCZOS)

        if self.fourth_place.alternate1_character.get():
            if self.event.event_name.get() == "NB":
                fourth_portrait.paste(secondary_med, (params.tier2_info[self.event.event_name.get()][6], params.tier2_info[self.event.event_name.get()][7]))
            fourth_secondary_1 = Image.open('resources/characters/%s/icons/%s_%s.png' % (self.game.game_name.get(), self.fourth_place.alternate1_character.get(), self.fourth_place.alternate1_character_color.get()))
            fourth_secondary_1 = fourth_secondary_1.resize((params.tier2_info[self.event.event_name.get()][2],params.tier2_info[self.event.event_name.get()][3]), Image.Resampling.LANCZOS)
            fourth_portrait.paste(fourth_secondary_1, (params.tier2_info[self.event.event_name.get()][6], params.tier2_info[self.event.event_name.get()][7]), fourth_secondary_1)

        if self.fourth_place.alternate2_character.get():
            if self.event.event_name.get() == "NB":
                fourth_portrait.paste(secondary_med, (params.tier2_info[self.event.event_name.get()][8], params.tier2_info[self.event.event_name.get()][9]))
            fourth_secondary_2 = Image.open('resources/characters/%s/icons/%s_%s.png' % (self.game.game_name.get(), self.fourth_place.alternate2_character.get(), self.fourth_place.alternate2_character_color.get()))
            fourth_secondary_2 = fourth_secondary_2.resize((params.tier2_info[self.event.event_name.get()][2],params.tier2_info[self.event.event_name.get()][3]), Image.Resampling.LANCZOS)
            fourth_portrait.paste(fourth_secondary_2, (params.tier2_info[self.event.event_name.get()][8], params.tier2_info[self.event.event_name.get()][9]), fourth_secondary_2)

        # open if sponsor
        if self.fourth_place.team.get():
            fnt = ImageFont.truetype('resources/events/%s/font.ttf' % (self.event.event_name.get()), params.tier2_info[self.event.event_name.get()][16])
            fourth_portrait.paste(sponsor_med, (params.tier2_info[self.event.event_name.get()][10], params.tier2_info[self.event.event_name.get()][11]))

            # open sponsor text
            sponsor4_text = Image.new('RGBA', (spnsW, spnsH))
            sponsor4_text = create_sponsorbox(sponsor4_text, fnt, self.fourth_place.team.get())
            fourth_portrait.paste(sponsor4_text, (params.tier2_info[self.event.event_name.get()][12], params.tier2_info[self.event.event_name.get()][13]), sponsor4_text)
            # close sponsor text

            # open sponsor image
            if exists('resources/sponsors/%s.png' % (self.fourth_place.team.get())):
                sponsor4_image = Image.open('resources/sponsors/%s.png' % (self.fourth_place.team.get()))
                sponsor4_image.getbbox()
                sponsor4_image = sponsor4_image.crop(sponsor4_image.getbbox())
                sponsor4_image.thumbnail((params.tier2_info[self.event.event_name.get()][4], params.tier2_info[self.event.event_name.get()][5]), Image.Resampling.LANCZOS)
                fourth_portrait.paste(sponsor4_image, (params.tier2_info[self.event.event_name.get()][14], params.tier2_info[self.event.event_name.get()][15]), sponsor4_image)
        # close sponsor image

        # close if sponsor

        fnt = ImageFont.truetype('resources/events/%s/font.ttf' % (self.event.event_name.get()), params.tier2_info[self.event.event_name.get()][17])
        namebox4 = Image.new('RGBA', (nboxW, nboxH))
        namebox4 = create_namebox(namebox4, fnt, self.fourth_place.name_tag.get().upper())

        # fifth

        # 238 x 257
        if self.fifth_place.main_character.get():

            fifth_portrait = Image.open('resources/characters/%s/portraits/%s_%s.png' % (self.game.game_name.get(), self.fifth_place.main_character.get(), self.fifth_place.main_character_color.get()))

            fifth_portrait = fifth_portrait.resize((params.tier3_info[self.event.event_name.get()][0], params.tier3_info[self.event.event_name.get()][1]), Image.Resampling.LANCZOS)

            if self.fifth_place.alternate1_character.get():
                if self.event.event_name.get() == "NB":
                    fifth_portrait.paste(secondary_sml, (params.tier3_info[self.event.event_name.get()][6], params.tier3_info[self.event.event_name.get()][7]))
                fifth_secondary_1 = Image.open('resources/characters/%s/icons/%s_%s.png' % (self.game.game_name.get(), self.fifth_place.alternate1_character.get(), self.fifth_place.alternate1_character_color.get()))
                fifth_secondary_1 = fifth_secondary_1.resize((params.tier3_info[self.event.event_name.get()][2], params.tier3_info[self.event.event_name.get()][3]), Image.Resampling.LANCZOS)
                fifth_portrait.paste(fifth_secondary_1, (params.tier3_info[self.event.event_name.get()][6], params.tier3_info[self.event.event_name.get()][7]), fifth_secondary_1)

            if self.fifth_place.alternate2_character.get():
                if self.event.event_name.get() == "NB":
                    fifth_portrait.paste(secondary_sml, (params.tier3_info[self.event.event_name.get()][8], params.tier3_info[self.event.event_name.get()][9]))
                fifth_secondary_2 = Image.open('resources/characters/%s/icons/%s_%s.png' % (self.game.game_name.get(), self.fifth_place.alternate2_character.get(), self.fifth_place.alternate2_character_color.get()))
                fifth_secondary_2 = fifth_secondary_2.resize((params.tier3_info[self.event.event_name.get()][2], params.tier3_info[self.event.event_name.get()][3]), Image.Resampling.LANCZOS)
                fifth_portrait.paste(fifth_secondary_2, (params.tier3_info[self.event.event_name.get()][8], params.tier3_info[self.event.event_name.get()][9]), fifth_secondary_2)

            # open if sponsor
            if self.fifth_place.team.get():
                fnt = ImageFont.truetype('resources/events/%s/font.ttf' % (self.event.event_name.get()), params.tier3_info[self.event.event_name.get()][16])
                fifth_portrait.paste(sponsor_sml, (params.tier3_info[self.event.event_name.get()][10], params.tier3_info[self.event.event_name.get()][11]))

                # open sponsor text
                sponsor5_text = Image.new('RGBA', (spnsW, spnsH))
                sponsor5_text = create_sponsorbox(sponsor5_text, fnt, self.fifth_place.team.get())
                fifth_portrait.paste(sponsor5_text, (params.tier3_info[self.event.event_name.get()][12], params.tier3_info[self.event.event_name.get()][13]), sponsor5_text)
                # close sponsor text

                # open sponsor image
                if exists('resources/sponsors/%s.png' % (self.fifth_place.team.get())):
                    sponsor5_image = Image.open('resources/sponsors/%s.png' % (self.fifth_place.team.get()))
                    sponsor5_image.getbbox()
                    sponsor5_image = sponsor5_image.crop(sponsor5_image.getbbox())
                    sponsor5_image.thumbnail((params.tier3_info[self.event.event_name.get()][4], params.tier3_info[self.event.event_name.get()][5]), Image.Resampling.LANCZOS)
                    fifth_portrait.paste(sponsor5_image, (params.tier3_info[self.event.event_name.get()][14], params.tier3_info[self.event.event_name.get()][15]), sponsor5_image)
            # close sponsor image

            # close if sponsor

            fnt = ImageFont.truetype('resources/events/%s/font.ttf' % (self.event.event_name.get()), params.tier3_info[self.event.event_name.get()][17])
            namebox5 = Image.new('RGBA', (nboxW, nboxH))
            namebox5 = create_namebox(namebox5, fnt, self.fifth_place.name_tag.get().upper())



        # sixth

        if self.sixth_place.main_character.get():

            sixth_portrait = Image.open('resources/characters/%s/portraits/%s_%s.png' % (self.game.game_name.get(), self.sixth_place.main_character.get(), self.sixth_place.main_character_color.get()))

            sixth_portrait = sixth_portrait.resize((params.tier3_info[self.event.event_name.get()][0], params.tier3_info[self.event.event_name.get()][1]), Image.Resampling.LANCZOS)

            if self.sixth_place.alternate1_character.get():
                if self.event.event_name.get() == "NB":
                    sixth_portrait.paste(secondary_sml, (params.tier3_info[self.event.event_name.get()][6], params.tier3_info[self.event.event_name.get()][7]))
                sixth_secondary_1 = Image.open('resources/characters/%s/icons/%s_%s.png' % (self.game.game_name.get(), self.sixth_place.alternate1_character.get(), self.sixth_place.alternate1_character_color.get()))
                sixth_secondary_1 = sixth_secondary_1.resize((params.tier3_info[self.event.event_name.get()][2], params.tier3_info[self.event.event_name.get()][3]), Image.Resampling.LANCZOS)
                sixth_portrait.paste(sixth_secondary_1, (params.tier3_info[self.event.event_name.get()][6], params.tier3_info[self.event.event_name.get()][7]), sixth_secondary_1)

            if self.sixth_place.alternate2_character.get():
                if self.event.event_name.get() == "NB":
                    sixth_portrait.paste(secondary_sml, (params.tier3_info[self.event.event_name.get()][8], params.tier3_info[self.event.event_name.get()][9]))
                sixth_secondary_2 = Image.open('resources/characters/%s/icons/%s_%s.png' % (self.game.game_name.get(), self.sixth_place.alternate2_character.get(), self.sixth_place.alternate2_character_color.get()))
                sixth_secondary_2 = sixth_secondary_2.resize((params.tier3_info[self.event.event_name.get()][2], params.tier3_info[self.event.event_name.get()][3]), Image.Resampling.LANCZOS)
                sixth_portrait.paste(sixth_secondary_2, (params.tier3_info[self.event.event_name.get()][8], params.tier3_info[self.event.event_name.get()][9]), sixth_secondary_2)

            # open if sponsor
            if self.sixth_place.team.get():
                fnt = ImageFont.truetype('resources/events/%s/font.ttf' % (self.event.event_name.get()), params.tier3_info[self.event.event_name.get()][16])
                sixth_portrait.paste(sponsor_sml, (params.tier3_info[self.event.event_name.get()][10], params.tier3_info[self.event.event_name.get()][11]))

                # open sponsor text
                sponsor6_text = Image.new('RGBA', (spnsW, spnsH))
                sponsor6_text = create_sponsorbox(sponsor6_text, fnt, self.sixth_place.team.get())
                sixth_portrait.paste(sponsor6_text, (params.tier3_info[self.event.event_name.get()][12], params.tier3_info[self.event.event_name.get()][13]), sponsor6_text)
                # close sponsor text

                # open sponsor image
                if exists('resources/sponsors/%s.png' % (self.sixth_place.team.get())):
                    sponsor6_image = Image.open('resources/sponsors/%s.png' % (self.sixth_place.team.get()))
                    sponsor6_image.getbbox()
                    sponsor6_image = sponsor6_image.crop(sponsor6_image.getbbox())
                    sponsor6_image.thumbnail((params.tier3_info[self.event.event_name.get()][4], params.tier3_info[self.event.event_name.get()][5]), Image.Resampling.LANCZOS)
                    sixth_portrait.paste(sponsor6_image, (params.tier3_info[self.event.event_name.get()][14], params.tier3_info[self.event.event_name.get()][15]), sponsor6_image)
            # close sponsor image

            # close if sponsor

            fnt = ImageFont.truetype('resources/events/%s/font.ttf' % (self.event.event_name.get()), params.tier3_info[self.event.event_name.get()][17])
            namebox6 = Image.new('RGBA', (nboxW, nboxH))
            namebox6 = create_namebox(namebox6, fnt, self.sixth_place.name_tag.get().upper())

        # seventh

        if self.seventh_place.main_character.get():

            seventh_portrait = Image.open('resources/characters/%s/portraits/%s_%s.png' % (self.game.game_name.get(), self.seventh_place.main_character.get(), self.seventh_place.main_character_color.get()))

            seventh_portrait = seventh_portrait.resize((params.tier3_info[self.event.event_name.get()][0], params.tier3_info[self.event.event_name.get()][1]), Image.Resampling.LANCZOS)

            if self.seventh_place.alternate1_character.get():
                if self.event.event_name.get() == "NB":
                    seventh_portrait.paste(secondary_sml, (params.tier3_info[self.event.event_name.get()][6], params.tier3_info[self.event.event_name.get()][7]))
                seventh_secondary_1 = Image.open('resources/characters/%s/icons/%s_%s.png' % (self.game.game_name.get(), self.seventh_place.alternate1_character.get(), self.seventh_place.alternate1_character_color.get()))
                seventh_secondary_1 = seventh_secondary_1.resize((params.tier3_info[self.event.event_name.get()][2], params.tier3_info[self.event.event_name.get()][3]), Image.Resampling.LANCZOS)
                seventh_portrait.paste(seventh_secondary_1, (params.tier3_info[self.event.event_name.get()][6], params.tier3_info[self.event.event_name.get()][7]), seventh_secondary_1)

            if self.seventh_place.alternate2_character.get():
                if self.event.event_name.get() == "NB":
                    seventh_portrait.paste(secondary_sml, (params.tier3_info[self.event.event_name.get()][8], params.tier3_info[self.event.event_name.get()][9]))
                seventh_secondary_2 = Image.open('resources/characters/%s/icons/%s_%s.png' % (self.game.game_name.get(), self.seventh_place.alternate2_character.get(), self.seventh_place.alternate2_character_color.get()))
                seventh_secondary_2 = seventh_secondary_2.resize((params.tier3_info[self.event.event_name.get()][2], params.tier3_info[self.event.event_name.get()][3]), Image.Resampling.LANCZOS)
                seventh_portrait.paste(seventh_secondary_2, (params.tier3_info[self.event.event_name.get()][8], params.tier3_info[self.event.event_name.get()][9]), seventh_secondary_2)

            # open if sponsor
            if self.seventh_place.team.get():
                fnt = ImageFont.truetype('resources/events/%s/font.ttf' % (self.event.event_name.get()), params.tier3_info[self.event.event_name.get()][16])
                seventh_portrait.paste(sponsor_sml, (params.tier3_info[self.event.event_name.get()][10], params.tier3_info[self.event.event_name.get()][11]))

                # open sponsor text
                sponsor7_text = Image.new('RGBA', (spnsW, spnsH))
                sponsor7_text = create_sponsorbox(sponsor7_text, fnt, self.seventh_place.team.get())
                seventh_portrait.paste(sponsor7_text, (params.tier3_info[self.event.event_name.get()][12], params.tier3_info[self.event.event_name.get()][13]), sponsor7_text)
                # close sponsor text

                # open sponsor image
                if exists('resources/sponsors/%s.png' % (self.seventh_place.team.get())):
                    sponsor7_image = Image.open('resources/sponsors/%s.png' % (self.seventh_place.team.get()))
                    sponsor7_image.getbbox()
                    sponsor7_image = sponsor7_image.crop(sponsor7_image.getbbox())
                    sponsor7_image.thumbnail((params.tier3_info[self.event.event_name.get()][4], params.tier3_info[self.event.event_name.get()][5]), Image.Resampling.LANCZOS)
                    seventh_portrait.paste(sponsor7_image, (params.tier3_info[self.event.event_name.get()][14], params.tier3_info[self.event.event_name.get()][15]), sponsor7_image)
            # close sponsor image

            # close if sponsor

            fnt = ImageFont.truetype('resources/events/%s/font.ttf' % (self.event.event_name.get()), params.tier3_info[self.event.event_name.get()][17])
            namebox7 = Image.new('RGBA', (nboxW, nboxH))
            namebox7 = create_namebox(namebox7, fnt, self.seventh_place.name_tag.get().upper())

        # eighth

        if self.eighth_place.main_character.get():

            eighth_portrait = Image.open('resources/characters/%s/portraits/%s_%s.png' % (self.game.game_name.get(), self.eighth_place.main_character.get(), self.eighth_place.main_character_color.get()))

            eighth_portrait = eighth_portrait.resize((params.tier3_info[self.event.event_name.get()][0], params.tier3_info[self.event.event_name.get()][1]), Image.Resampling.LANCZOS)

            if self.eighth_place.alternate1_character.get():
                if self.event.event_name.get() == "NB":
                    eighth_portrait.paste(secondary_sml, (params.tier3_info[self.event.event_name.get()][6], params.tier3_info[self.event.event_name.get()][7]))
                eighth_secondary_1 = Image.open('resources/characters/%s/icons/%s_%s.png' % (self.game.game_name.get(), self.eighth_place.alternate1_character.get(), self.eighth_place.alternate1_character_color.get()))
                eighth_secondary_1 = eighth_secondary_1.resize((params.tier3_info[self.event.event_name.get()][2], params.tier3_info[self.event.event_name.get()][3]), Image.Resampling.LANCZOS)
                eighth_portrait.paste(eighth_secondary_1, (params.tier3_info[self.event.event_name.get()][6], params.tier3_info[self.event.event_name.get()][7]), eighth_secondary_1)

            if self.eighth_place.alternate2_character.get():
                if self.event.event_name.get() == "NB":
                    eighth_portrait.paste(secondary_sml, (params.tier3_info[self.event.event_name.get()][8], params.tier3_info[self.event.event_name.get()][9]))
                eighth_secondary_2 = Image.open('resources/characters/%s/icons/%s_%s.png' % (self.game.game_name.get(), self.eighth_place.alternate2_character.get(), self.eighth_place.alternate2_character_color.get()))
                eighth_secondary_2 = eighth_secondary_2.resize((params.tier3_info[self.event.event_name.get()][2], params.tier3_info[self.event.event_name.get()][3]), Image.Resampling.LANCZOS)
                eighth_portrait.paste(eighth_secondary_2, (params.tier3_info[self.event.event_name.get()][8], params.tier3_info[self.event.event_name.get()][9]), eighth_secondary_2)

            # open if sponsor
            if self.eighth_place.team.get():
                fnt = ImageFont.truetype('resources/events/%s/font.ttf' % (self.event.event_name.get()), params.tier3_info[self.event.event_name.get()][16])
                eighth_portrait.paste(sponsor_sml, (params.tier3_info[self.event.event_name.get()][10], params.tier3_info[self.event.event_name.get()][11]))

                # open sponsor text
                sponsor8_text = Image.new('RGBA', (spnsW, spnsH))
                sponsor8_text = create_sponsorbox(sponsor8_text, fnt, self.eighth_place.team.get())
                eighth_portrait.paste(sponsor8_text, (params.tier3_info[self.event.event_name.get()][12], params.tier3_info[self.event.event_name.get()][13]), sponsor8_text)
                # close sponsor text

                # open sponsor image
                if exists('resources/sponsors/%s.png' % (self.eighth_place.team.get())):
                    sponsor8_image = Image.open('resources/sponsors/%s.png' % (self.eighth_place.team.get()))
                    sponsor8_image.getbbox()
                    sponsor8_image = sponsor8_image.crop(sponsor8_image.getbbox())
                    sponsor8_image.thumbnail((params.tier3_info[self.event.event_name.get()][4], params.tier3_info[self.event.event_name.get()][5]), Image.Resampling.LANCZOS)
                    eighth_portrait.paste(sponsor8_image, (params.tier3_info[self.event.event_name.get()][14], params.tier3_info[self.event.event_name.get()][15]), sponsor8_image)
            # close sponsor image

            # close if sponsor

            fnt = ImageFont.truetype('resources/events/%s/font.ttf' % (self.event.event_name.get()), params.tier3_info[self.event.event_name.get()][17])
            namebox8 = Image.new('RGBA', (nboxW, nboxH))
            namebox8 = create_namebox(namebox8, fnt, self.eighth_place.name_tag.get().upper())

        # top bar information

        fnt = ImageFont.truetype('resources/events/%s/font.ttf' % (self.event.event_name.get()), params.etc_info[self.event.event_name.get()][0])

        namebox_date = Image.new('RGBA', (nboxW, nboxH))
        namebox_date = create_namebox(namebox_date, fnt, self.event.event_day.get().upper())

        fnt = ImageFont.truetype('resources/events/%s/font.ttf' % (self.event.event_name.get()), params.etc_info[self.event.event_name.get()][1])

        namebox_slug = Image.new('RGBA', (nboxW, nboxH))
        namebox_slug = create_namebox(namebox_slug, fnt, self.event.event_link.get().upper())

        fnt = ImageFont.truetype('resources/events/%s/font.ttf' % (self.event.event_name.get()), params.etc_info[self.event.event_name.get()][2])

        namebox_entrants = Image.new('RGBA', (nboxW, nboxH))
        if self.event.event_name.get() == "NB":
            namebox_entrants = create_namebox(namebox_entrants, fnt, f"{self.event.event_entrant_count.get().upper()}")
        else:
            namebox_entrants = create_namebox(namebox_entrants, fnt, f"{self.event.event_entrant_count.get().upper()} ENTRANTS")

        # blurb time

        fnt = ImageFont.truetype('resources/events/%s/font.ttf' % (self.event.event_name.get()), params.etc_info[self.event.event_name.get()][3])

        blurb_box_1 = Image.new('RGBA', (bboxW, bboxH))
        blurb_box_1 = create_blurb_box(blurb_box_1, fnt, self.blurb_1.get().upper())

        blurb_box_2 = Image.new('RGBA', (bboxW, bboxH))
        blurb_box_2 = create_blurb_box(blurb_box_2, fnt, self.blurb_2.get().upper())

        blurb_box_3 = Image.new('RGBA', (bboxW, bboxH))
        blurb_box_3 = create_blurb_box(blurb_box_3, fnt, self.blurb_3.get().upper())

    # pasties!

        bg.paste(cboxes, (0,0), cboxes)

        bg.paste(first_portrait, (params.coords_portraits[self.event.event_name.get()][0], params.coords_portraits[self.event.event_name.get()][1]), first_portrait)
        bg.paste(second_portrait, (params.coords_portraits[self.event.event_name.get()][2], params.coords_portraits[self.event.event_name.get()][5]), second_portrait)
        bg.paste(third_portrait, (params.coords_portraits[self.event.event_name.get()][3], params.coords_portraits[self.event.event_name.get()][5]), third_portrait)
        bg.paste(fourth_portrait, (params.coords_portraits[self.event.event_name.get()][4], params.coords_portraits[self.event.event_name.get()][5]), fourth_portrait)
        if self.fifth_place.main_character.get():
            bg.paste(fifth_portrait, (params.coords_portraits[self.event.event_name.get()][6], params.coords_portraits[self.event.event_name.get()][10]), fifth_portrait)
        if self.sixth_place.main_character.get():
            bg.paste(sixth_portrait, (params.coords_portraits[self.event.event_name.get()][7], params.coords_portraits[self.event.event_name.get()][10]), sixth_portrait)
        if self.seventh_place.main_character.get():
            bg.paste(seventh_portrait, (params.coords_portraits[self.event.event_name.get()][8], params.coords_portraits[self.event.event_name.get()][10]), seventh_portrait)
        if self.eighth_place.main_character.get():
            bg.paste(eighth_portrait, (params.coords_portraits[self.event.event_name.get()][9], params.coords_portraits[self.event.event_name.get()][10]), eighth_portrait)

        bg.paste(nameplates, (0,0), nameplates)

        bg.paste(namebox1, (params.coords_nameboxes[self.event.event_name.get()][0], params.coords_nameboxes[self.event.event_name.get()][1]), namebox1)
        bg.paste(namebox2, (params.coords_nameboxes[self.event.event_name.get()][2], params.coords_nameboxes[self.event.event_name.get()][5]), namebox2)
        bg.paste(namebox3, (params.coords_nameboxes[self.event.event_name.get()][3], params.coords_nameboxes[self.event.event_name.get()][5]), namebox3)
        bg.paste(namebox4, (params.coords_nameboxes[self.event.event_name.get()][4], params.coords_nameboxes[self.event.event_name.get()][5]), namebox4)
        if self.fifth_place.main_character.get():
            bg.paste(namebox5, (params.coords_nameboxes[self.event.event_name.get()][6], params.coords_nameboxes[self.event.event_name.get()][10]), namebox5)
        if self.sixth_place.main_character.get():            
            bg.paste(namebox6, (params.coords_nameboxes[self.event.event_name.get()][7], params.coords_nameboxes[self.event.event_name.get()][10]), namebox6)
        if self.seventh_place.main_character.get():
            bg.paste(namebox7, (params.coords_nameboxes[self.event.event_name.get()][8], params.coords_nameboxes[self.event.event_name.get()][10]), namebox7)
        if self.eighth_place.main_character.get():
            bg.paste(namebox8, (params.coords_nameboxes[self.event.event_name.get()][9], params.coords_nameboxes[self.event.event_name.get()][10]), namebox8)

        bg.paste(namebox_date, (params.coords_misc[self.event.event_name.get()][0], params.coords_misc[self.event.event_name.get()][1]), namebox_date)
        bg.paste(namebox_slug, (params.coords_misc[self.event.event_name.get()][2], params.coords_misc[self.event.event_name.get()][3]), namebox_slug)
        bg.paste(namebox_entrants, (params.coords_misc[self.event.event_name.get()][4], params.coords_misc[self.event.event_name.get()][5]), namebox_entrants)

        bg.paste(blurb_box_1, (params.coords_misc[self.event.event_name.get()][6], params.coords_misc[self.event.event_name.get()][7]), blurb_box_1)
        bg.paste(blurb_box_2, (params.coords_misc[self.event.event_name.get()][6], params.coords_misc[self.event.event_name.get()][8]), blurb_box_2)
        bg.paste(blurb_box_3, (params.coords_misc[self.event.event_name.get()][6], params.coords_misc[self.event.event_name.get()][9]), blurb_box_3)

        bg.paste(fg, (0,0), fg)
        bg.save(f'output/{self.event.event_name.get()}{self.event.event_number.get()}-{self.game.game_name.get()}-{self.event.event_entrant_count.get()}_Entrants.png')
        print("OUTPUT COMPLETE! DOUBLE CHECK COLORS BEFORE YOU GO!")


if __name__ == "__main__":
    root = ttk.Window(themename="darkly")
    eventbox = ttk.Frame(root, padding=10)
    eventbox.grid(row=0)
    entrybox = ttk.Frame(root, padding=10)
    entrybox.grid(row=1)
    blurbbox = ttk.Frame(root,padding=(0, 0, 0, 10))
    blurbbox.grid(row=2)
    root.title("BannerMaster")
    MainApp(root).grid()
    root.mainloop()
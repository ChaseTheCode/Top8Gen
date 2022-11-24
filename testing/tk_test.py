from cgitb import text
import ttkbootstrap as ttk
import math
from PIL import Image, ImageFont, ImageDraw
from ttkwidgets.autocomplete import AutocompleteEntry
import os
from datetime import date
from tkinter.ttk import *
from os.path import exists




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
            self.n = 1
            self.team = ttk.StringVar()
            self.name_tag = ttk.StringVar()
            self.main_character = ttk.StringVar()
            self.main_character_color = ttk.StringVar()
            self.alternate1_character = ttk.StringVar()
            self.alternate1_character_color = ttk.StringVar()
            self.alternate2_character = ttk.StringVar()
            self.alternate2_character_color = ttk.StringVar()

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == 8:
            raise StopIteration
        else:
            self.n += 1
            return self.n - 1

class MainApp(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.event = Event(event_name="", event_number="", event_day="", event_entrant_count="", event_link="")
        self.game = Game(game_name="")
        self.blurb_1 = ttk.StringVar(value="don't forget to register for DFW's Bizzare Adventure,")
        self.blurb_2 = ttk.StringVar(value="powered by the Liberty Rec Center in Plano, TX! Sign up today!")
        self.blurb_3 = ttk.StringVar(value="DFWba will feature Singles, 3v3 Squad Strike, and Doubles!")

        # oh boy time for characters

        with open('resources/csv/characters.csv', 'r') as file2:
            character_base = file2.readlines()

            characters, em_list = [], []
            for i in character_base:
                    characters.append(i.split(",")[0])
                    em_list.append(i.split(",")[1])

        event_list = ["USW", "MNM", "SSO", "NB"]

        game_list = ["SSBU", "SSBM", "GGST", "KOFXV", "DBFZ", "DNF", "MBTL", ]

        color_list = ["00", "01", "02", "03", "04", "05", "06", "07"]

        # Set Lists for Indexing

        self.team_list = []
        self.name_list = []

        self.main_char_list = []
        self.main_char_color_list = []

        self.alt1_char_list = []
        self.alt1_char_color_list = []

        self.alt2_char_list = []
        self.alt2_char_color_list = []        


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

        # PLAYERS, THEIR CHARACTERS, AND WHERE TO CATCH HANDS

        # ALRIGHT, FIRST PLACE!

        for i in range(4):


            
            labelframe = ttk.LabelFrame(entrybox, text="%s Place" % (i+1), bootstyle="WARNING")
            labelframe.grid(row=0, column=i+1, padx=2, pady=2)

            team_label = ttk.Label(labelframe, text="Team")
            name_label = ttk.Label(labelframe, text="Name")
            main_char_label = ttk.Label(labelframe, text="Main")
            alt1_char_label = ttk.Label(labelframe, text="Alt 1")
            alt2_char_label = ttk.Label(labelframe, text="Alt 2")

            team_entry = ttk.Entry(labelframe)
            self.team_list.append(team_entry)
            name_entry = ttk.Entry(labelframe)
            self.name_list.append(name_entry)
            # Main Character
            main_char_entry = AutocompleteEntry(labelframe, completevalues=characters)
            self.main_char_list.append(main_char_entry)

            main_char_color_entry = ttk.Combobox(labelframe, width=3)
            self.main_char_color_list.append(main_char_color_entry)
            main_char_color_entry['values'] = color_list
            main_char_color_entry.set("00")
            # Alternate 1
            alt1_char_entry = AutocompleteEntry(labelframe, completevalues=characters)
            self.alt1_char_list.append(alt1_char_entry)

            alt1_char_color_entry = ttk.Combobox(labelframe, width=3)
            self.alt1_char_color_list.append(alt1_char_color_entry)
            alt1_char_color_entry['values'] = color_list
            alt1_char_color_entry.set("00")
            # Alternate 2
            alt2_char_entry = AutocompleteEntry(labelframe, completevalues=characters)
            self.alt2_char_list.append(alt2_char_entry)

            alt2_char_color_entry = ttk.Combobox(labelframe, width=3)
            self.alt2_char_color_list.append(alt2_char_color_entry)
            alt2_char_color_entry['values'] = color_list
            alt2_char_color_entry.set("00")

            team_label.grid(row=0, column=0, padx=2, pady=2)
            team_entry.grid(row=0, column=1, padx=2, pady=2)

            name_label.grid(row=1, column=0, padx=2, pady=2)
            name_entry.grid(row=1, column=1, padx=2, pady=2)

            main_char_label.grid(row=2, column=0, padx=2, pady=2)
            main_char_entry.grid(row=2, column=1, padx=2, pady=2)
            main_char_color_entry.grid(row=2, column=2, padx=2, pady=2)

            alt1_char_label.grid(row=3, column=0, padx=2, pady=2)
            alt1_char_entry.grid(row=3, column=1, padx=2, pady=2)
            alt1_char_color_entry.grid(row=3, column=2, padx=2, pady=2)

            alt2_char_label.grid(row=4, column=0, padx=2, pady=2)
            alt2_char_entry.grid(row=4, column=1, padx=2, pady=2)
            alt2_char_color_entry.grid(row=4, column=2, padx=2, pady=2)

        def print_list():
            for i in self.team_list:
                print(i[1].get())
            print(self.name_list)
            print(self.main_char_list)

        make_it_button = ttk.Button(eventbox, text="MAKE IT", command=print_list)
        make_it_button.grid(row=0, column=11, padx=2, pady=2)



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
'''

I refuse to learn my lesson

i'm going to make this in three parts, so I don't royally fuck myself over to infinity and beyond

1 - 1st place info & coordinates
2 - 2nd-4th place info & coordinates
3 - 5th-8th place info & coordinates
4 - event info & coordinates
5 - pasting portraits
7 - pasting tag nameboxes
8 - pasting event & blurb boxes

'''

tier1_info = {
    "USW": [
        # resizing
        600, # 0 : portrait resize x
        647, # 1 : portrait resize y
        64, # 2 : icon resize x
        64, # 3 : icon resize y
        90, # 4 : sponsor image resize x
        25, # 5 : sponsor image resize y

        # pasting
        528, # 6 : secondary 1 paste x
        8, # 7 : secondary 1 paste y
        456, # 8 : secondary 2 paste x
        8, # 9 : secondary 2 paste y
        445, # 10 : sponsor box paste x
        530, # 11 : sponsor box paste y
        510, # 12 : sponsor text paste x
        533, # 13 : sponsor text paste y
        465, # 14 : sponsor image paste x
        535, # 15 : sponsor image paste y

        # font size
        25, # 16 : sponsor text font size
        55, # 17 : name tag font size
    ],
    "NB": [
        # resizing
        678, # 0 : portrait resize x
        678, # 1 : portrait resize y
        112, # 2 : icon resize x
        112, # 3 : icon resize y
        90, # 4 : sponsor image resize x
        25, # 5 : sponsor image resize y

        # pasting
        554, # 6 : secondary 1 paste x
        101, # 7 : secondary 1 paste y
        554, # 8 : secondary 2 paste x
        216, # 9 : secondary 2 paste y
        445, # 10 : sponsor box paste x
        530, # 11 : sponsor box paste y
        510, # 12 : sponsor text paste x
        533, # 13 : sponsor text paste y
        465, # 14 : sponsor image paste x
        535, # 15 : sponsor image paste y

        # font size
        25, # 16 : sponsor text font size
        55, # 17 : name tag font size
    ],

}

tier2_info = {
    "USW": [
        # resizing
        320, # 0 : portrait resize x
        347, # 1 : portrait resize y
        48, # 2 : icon resize x
        48, # 3 : icon resize y
        80, # 4 : sponsor image resize x
        22, # 5 : sponsor image resize y

        # pasting
        267, # 6 : secondary 1 paste x
        8, # 7 : secondary 1 paste y
        211, # 8 : secondary 2 paste x
        8, # 9 : secondary 2 paste y
        197, # 10 : sponsor box paste x
        276, # 11 : sponsor box paste y
        250, # 12 : sponsor text paste x
        277, # 13 : sponsor text paste y
        215, # 14 : sponsor image paste x
        280, # 15 : sponsor image paste y

        # font size
        20, # 16 : sponsor text font size
        30, # 17 : name tag font size
    ],
    "NB": [
        # resizing
        346, # 0 : portrait resize x
        346, # 1 : portrait resize y
        86, # 2 : icon resize x
        86, # 3 : icon resize y
        80, # 4 : sponsor image resize x
        22, # 5 : sponsor image resize y

        # pasting
        253, # 6 : secondary 1 paste x
        77, # 7 : secondary 1 paste y
        253, # 8 : secondary 2 paste x
        166, # 9 : secondary 2 paste y
        197, # 10 : sponsor box paste x
        276, # 11 : sponsor box paste y
        250, # 12 : sponsor text paste x
        277, # 13 : sponsor text paste y
        215, # 14 : sponsor image paste x
        280, # 15 : sponsor image paste y

        # font size
        20, # 16 : sponsor text font size
        30, # 17 : name tag font size
    ],
}

tier3_info = {
    "USW": [
        # resizing
        238, # 0 : portrait resize x
        257, # 1 : portrait resize y
        32, # 2 : icon resize x
        32, # 3 : icon resize y
        80, # 4 : sponsor image resize x
        15, # 5 : sponsor image resize y

        # pasting
        202, # 6 : secondary 1 paste x
        4, # 7 : secondary 1 paste y
        166, # 8 : secondary 2 paste x
        4, # 9 : secondary 2 paste y
        144, # 10 : sponsor box paste x
        204, # 11 : sponsor box paste y
        188, # 12 : sponsor text paste x
        207, # 13 : sponsor text paste y
        155, # 14 : sponsor image paste x
        206, # 15 : sponsor image paste y

        # font size
        13, # 16 : sponsor text font size
        21, # 17 : name tag font size
    ],
    "NB": [
        # resizing
        259, # 0 : portrait resize x
        259, # 1 : portrait resize y
        61, # 2 : icon resize x
        61, # 3 : icon resize y
        80, # 4 : sponsor image resize x
        15, # 5 : sponsor image resize y

        # pasting
        192, # 6 : secondary 1 paste x
        53, # 7 : secondary 1 paste y
        192, # 8 : secondary 2 paste x
        117, # 9 : secondary 2 paste y
        144, # 10 : sponsor box paste x
        204, # 11 : sponsor box paste y
        188, # 12 : sponsor text paste x
        207, # 13 : sponsor text paste y
        155, # 14 : sponsor image paste x
        206, # 15 : sponsor image paste y

        # font size
        13, # 16 : sponsor text font size
        22, # 17 : name tag font size
    ],
}

etc_info = {
    # for the moment, this is just for adjusting any font sizes for date, short slug, entrants, blurb, etc.
    "USW": [
        33, # 0 : date font size
        33, # 1 : short slub font size
        43, # 2 : entrants font size
        35, # 3 : blurb font size
    ],
    "NB": [
        33, # 0 : date font size
        33, # 1 : short slub font size
        43, # 2 : entrants font size
        35, # 3 : blurb font size
    ],
}

coords_portraits = {
    # note: first has it's own x & y, second-fourth will have the same y, and fifth-eighth will have it's own y. X will come first, and then Y will after
    "USW": [
        156, # 0 : first place x
        206, # 1 : first place y
        772, # 2 : second place x
        1108, # 3 : third place x
        1443, # 4 : fourth place x
        206, # 5 : second-fourth place y
        770, # 6 : fifth place x
        1022, # 7 : sixth place x
        1274, # 8 : seventh place x
        1526, # 9 : eighth place x
        596, # 10 : fifth-eighth place y
    ],
    "NB": [
        62, # 0 : first place x
        107, # 1 : first place y
        776, # 2 : second place x
        1149, # 3 : third place x
        1521, # 4 : fourth place x
        107, # 5 : second-fourth place y
        776, # 6 : fifth place x
        1053, # 7 : sixth place x
        1330, # 8 : seventh place x
        1605, # 9 : eighth place x
        524, # 10 : fifth-eighth place y
    ],
}

coords_nameboxes = {
    # same as the portraits, first has it's own x & y, second-fourth will have the same y, and fifth-eighth will have it's own y. X will come first, and then Y will after
    "USW": [
        156, # 0 : first place x
        783, # 1 : first place y
        631, # 2 : second place x
        967, # 3 : third place x
        1302, # 4 : fourth place x
        516, # 5 : second-fourth place y
        588, # 6 : fifth place x
        840, # 7 : sixth place x
        1092, # 8 : seventh place x
        1344, # 9 : eighth place x
        825, # 10 : eighth place y
    ],
    "NB": [
        100, # 0 : first place x
        723, # 1 : first place y
        649, # 2 : second place x
        1023, # 3 : third place x
        1395, # 4 : fourth place x
        420, # 5 : second-fourth place y
        606, # 6 : fifth place x
        883, # 7 : sixth place x
        1160, # 8 : seventh place x
        1436, # 9 : eighth place x
        761, # 10 : fifth-eighth place y
    ],
}

coords_misc = {
    # the grab bag! this has every other coordinate that is on the page, for now...
    "USW": [
        252, # 0 : date x
        61, # 1 : date y
        1080, # 2 : short slug x
        61, # 3 : short slug y
        660, # 4 : entrants x
        50, # 5 : entrants y
        40, # 6 : blurb x
        949, # 7 : blurb line 1 y
        983, # 8 : blurb line 2 y
        1017, # 9 : blurb line 3 y
    ],
    "NB": [
        1392, # 0 : date x
        930, # 1 : date y
        1380, # 2 : short slug x
        986, # 3 : short slug y
        -108, # 4 : entrants x
        937, # 5 : entrants y
        2000, # 6 : blurb x
        949, # 7 : blurb line 1 y
        983, # 8 : blurb line 2 y
        1017, # 9 : blurb line 3 y
    ],
}
# Typing test games!!!!!!!!!!!!!!!!!!!!
# idea 12.12
# code design 12.18
# finish coding part 12.21
from cmu_graphics import *
import time
import sys

from cmu_graphics.shape_logic import cmu_graphics

# background part
app.background = "lightblue"


# start part
app.start_line = Group(
    Rect(60, 55, 280, 50, fill="white", border="yellow", borderWidth=7),
    Label("Welcome to typing test!!!!!!!!!", 200, 80, italic=True, size=20),
)

app.start_bottom = Group(
    Rect(160, 255, 80, 50, fill="white", border="navy", borderWidth=7),
    Label("Start", 200, 280, italic=True, size=20),
)
app.is_start = False

# game mode part

app.is_mode = False
app.mode_line = Group(
    Rect(60, 55, 280, 50, fill="white", border="yellow", borderWidth=7),
    Label("Choose a mode to play", 200, 80, italic=True, size=20),
)
app.mode_line.val = "choose a mode to play"

app.mode_1 = Group(
    Rect(60, 200, 80, 50, fill="lightgreen", border="navy", borderWidth=7),
    Label("1 min", 100, 225, italic=True, size=20),
)
app.mode_1.val = "1 min"
app.mode_2 = Group(
    Rect(160, 200, 80, 50, fill="yellow", border="navy", borderWidth=7),
    Label("2 min", 200, 225, italic=True, size=20),
)
app.mode_2.val = "2 min"
app.mode_3 = Group(
    Rect(260, 200, 80, 50, fill="red", border="navy", borderWidth=7),
    Label("3 min", 300, 225, italic=True, size=20),
)
app.mode_3.val = "3 min"

app.mode_list = [app.mode_line, app.mode_1, app.mode_2, app.mode_3]

# game test part

app.is_test = False
app.test_timer = [
    Rect(160, 55, 100, 50, fill="white", border="yellow", borderWidth=7),
    Label("", 200, 80, italic=True, size=20),
]
app.word = Label("", 200, 200, size=20, fill="grey")
app.word_index = 0
app.dis_type = Label("", 200, 200, size=20, fill="navy")
for each in app.test_timer:
    each.visible = False
app.word_list = [
    "An",
    "ever-growing",
    "number",
    "of",
    "complex",
    "and",
    "rigid",
    "rules",
    "plus",
    "hard-to-cope-with",
    "regulations",
    "are",
    "now",
    "being",
    "legislated",
    "from",
    "state",
    "to",
    "state.",
    "Key",
    "federal",
    "regulations",
    "were",
    "formulated",
    "by",
    "the",
    "FDA,",
    "FTC,",
    "and",
    "the",
    "CPSC.",
    "Each",
    "of",
    "these",
    "federal",
    "agencies",
    "serves",
    "a",
    "specific",
    "mission.",
    "One",
    "example:",
    "Laws",
    "sponsored",
    "by",
    "the",
    "Office",
    "of",
    "the",
    "Fair",
    "Debt",
    "Collection",
    "Practices",
    "prevent",
    "an",
    "agency",
    "from",
    "purposefully",
    "harassing",
    "clients",
    "in",
    "serious",
    "debt.",
    "The",
    "Fair",
    "Packaging",
    "and",
    "Labeling",
    "Act",
    "makes",
    "certain",
    "that",
    "protection",
    "from",
    "misleading",
    "packaging",
    "of",
    "goods",
    "is",
    "guaranteed",
    "to",
    "each",
    "buyer",
    "of",
    "goods",
    "carried",
    "in",
    "small",
    "shops",
    "as",
    "well",
    "as",
    "in",
    "large",
    "supermarkets.",
    "Products",
    "on",
    "the",
    "market",
    "must",
    "reveal",
    "the",
    "names",
    "of",
    "all",
    "ingredients",
    "on",
    "the",
    "label.",
    "Language",
    "must",
    "be",
    "in",
    "clear",
    "and",
    "precise",
    "terms",
    "that",
    "can",
    "be",
    "understood",
    "by",
    "everyone.",
    "This",
    "practice",
    "is",
    "very",
    "crucial",
    "for",
    "the",
    "lives",
    "of",
    "many",
    "people.",
    "It",
    "is",
    "prudent",
    "that",
    "we",
    "recall",
    "that",
    "the",
    "FDA",
    "specifically",
    "requires",
    "that",
    "all",
    "goods",
    "are",
    "pure,",
    "safe,",
    "and",
    "wholesome.",
    "The",
    "FDA",
    "states",
    "that",
    "all",
    "goods",
    "be",
    "produced",
    "under",
    "highly",
    "sanitary",
    "conditions.",
    "Drugs",
    "must",
    "be",
    "completely",
    "safe",
    "and",
    "must",
    "also",
    "be",
    "effective",
    "for",
    "their",
    "stated",
    "purpose.",
    "This",
    "policy",
    "applies",
    "to",
    "cosmetics",
    "that",
    "must",
    "be",
    "both",
    "safe",
    "and",
    "pure.",
    "Individuals",
    "are",
    "often",
    "totally",
    "unappreciative",
    "of",
    "the",
    "FDA's",
    "great",
    "dedication.",
]


# initialize the project
def Init():
    app.is_start = True
    app.start_line.visible = True
    app.start_bottom.visible = True
    app.mode_line.visible = False
    app.mode_2.visible = False
    app.mode_1.visible = False
    app.mode_3.visible = False
    pass


# first step: choose the mode part


def mode_select():
    app.is_start = False
    app.is_mode = True
    app.start_line.visible = False
    app.start_bottom.visible = False
    app.mode_line.visible = True
    # app.mode_2.visible=True
    # app.mode_1.visible=True
    # app.mode_3.visible=True
    for each in app.mode_list:
        each.visible = True


# second step: start timer (and go test)
def run_test(tm):
    print(app.mode_list)
    for each in app.mode_list:
        each.visible = False
    cnt = time.time()
    app.tm = cnt
    if tm == "1 min":
        cnt += 60
    elif tm == "2 min":
        cnt += 120
    else:
        cnt += 180
    print(cnt - time.time())
    for each in app.test_timer:
        each.visible = True
    app.cnt = cnt
    app.is_test = True
    app.is_mode = False


def display_word():
    app.word.value = app.word_list[app.word_index].lower()
    app.word_index += 1
    pass


def onMousePress(x, y):
    # init step
    if app.is_start:
        if app.start_bottom.hits(x, y) and app.start_bottom.visible:
            mode_select()
    # first step
    if app.is_mode:
        for each in app.mode_list:
            if each.hits(x, y) and each.val != app.mode_line.val:
                run_test(each.val)


app.speed = Label("wpm", 350, 20, size=20)


def onStep():
    # timer part
    if app.is_test and time.time() <= app.cnt:
        app.test_timer[1].value = f"{int(app.cnt-time.time())}s"
        app.test_timer[1].visible = True
    else:
        app.is_test = False
    if app.is_test:
        if app.dis_type.value == app.word.value:
            display_word()
            app.now_ch = 0
            app.dis_type.value = ""
        app.speed.value = f"{int(app.word_index/int(time.time()-app.tm+1)*60+1)}wpm"


app.now_ch = 0


def onKeyPress(key):
    print(key)
    if app.is_test:
        if app.word.value[app.now_ch] == key:
            app.now_ch += 1
            app.dis_type.value = app.dis_type.value + key
            app.dis_type.left = app.word.left

    pass


Init()
cmu_graphics.run()


import os
import threading
import time
import typing
import flet as ft
import lmstudio
import string
from numpy.random import *

# lm studio setup
try:
    lmstudio.configure_default_client("memorylaptop.local:3333")
    model = lmstudio.llm()
    chat = lmstudio.Chat("You're a Story maker that is to make cute little stories")
except Exception:
    print("lmstudio not running")

# character output structure
class Gen_StoryCharacter_Structure(lmstudio.BaseModel):
    characters: typing.List[str]
    story: str

def main(page: ft.Page):
    #
    #
    # ========= FLET SETUP ==========
    #
    #

    page.title = "AI Stories..."
    page.bgcolor = ft.Colors.LIGHT_BLUE_200
    page.window.width = 400
    page.window.height = 545
    page.fonts = {
        "cool_font": "ShortBaby-Mg2w.ttf"
    }

    #
    #
    # ========= LM FUNCTIONS ==========
    #
    #

    # requests story and characters from the LM model
    def gen_story_and_characters(p):
        global model, chat
        nonlocal character_container, story_container, character_text, story_text
        os.system("clear")
        gen_story = model.respond("make story and characters", response_format=Gen_StoryCharacter_Structure)
        gen_story = gen_story.parsed
        print(" ".join(gen_story['characters']))
        print(gen_story['story'])
        # add to character holder
        character_text.value = " \n".join(gen_story['characters'])
        story_text.value = gen_story['story']
        page.update()
        # wait to do different story
        time.sleep(60)
        # clears model context and resets with original prompt
        chat.__dict__.clear()
        chat = lmstudio.Chat("You're a Story maker that is to make cute little stories")
        threading.Thread(target=gen_story_and_characters, args=(page,), daemon=True).start()
    #
    #
    # ========= END OF LM FUNCTIONS ==========
    #
    #

    #
    #
    # ========= UI OBJECTS ==========
    #
    #

    # holds character names
    character_text = ft.Text(
        f"\n" * 20,
        size=32,
        font_family="cool_font",
    )

    character_container = ft.Column([
        ft.Container(
            character_text,
            border_radius=7,
            gradient=ft.LinearGradient(
                colors=[ft.Colors.BLUE_400, ft.Colors.BLUE_600],
            ),
            width=page.window.width,
        )
    ],
        width=page.window.width,
        height=120,
        scroll=ft.ScrollMode.ALWAYS,
    )
    story_text = ft.Text(
        f"\n" * 20,
        size=16,
        font_family="cool_font"
    )

    # A column object to holds text
    story_container = ft.Column([
        ft.Container(
            story_text,
            border_radius=7,
            gradient=ft.LinearGradient(
                colors=[ft.Colors.BLUE_400, ft.Colors.BLUE_600],
            ),
            width=page.window.width,
        )
    ],
        width=page.window.width,
        height=200,
        scroll=ft.ScrollMode.ALWAYS,
    )

    #
    #
    # ========= END OF UI OBJECTS ==========
    #
    #

    # important threads
    # thread starts generation of characters and story
    threading.Thread(target=gen_story_and_characters, args=(page,), daemon=True).start()

    # add all flet objects to page
    page.add(
        # Character Label
        ft.Container(
            ft.Text(
                "👶 Characters 🧔‍♂️",
                size=30,
                text_align=ft.TextAlign.CENTER,
                font_family="cool_font"
            ),
            border_radius=10,
            width=page.window.width,
            gradient=ft.LinearGradient(
                colors=[ft.Colors.BLUE_400, ft.Colors.BLUE_600],
            )
        ),
        # display character column
        character_container,
        # story label
        ft.Container(
            ft.Text(
                "📖 Story 📚",
                size=30,
                text_align=ft.TextAlign.CENTER,
                font_family="cool_font"
            ),
            border_radius=10,
            width=page.window.width,
            gradient=ft.LinearGradient(
                colors=[ft.Colors.BLUE_400, ft.Colors.BLUE_600],
            )
        ),
        # display story text
        story_container,
        # credits objects
        ft.Column([
            ft.Container(
                ft.Text(
                    "🧑🏻‍💻 Made by A_Memory 🧑🏻‍💻",
                    size=20,
                    text_align=ft.TextAlign.CENTER,
                    font_family="cool_font"
                ),
                border_radius=10,
                width=page.window.width,
                gradient=ft.LinearGradient(
                    colors=[ft.Colors.BLUE_400, ft.Colors.BLUE_600],
                )
            ),
            # my contact info via clickable container
            ft.Container(
                ft.Text(
                    "🖥️ My Github 🖱️",
                    size=20,
                    text_align=ft.TextAlign.CENTER,
                    font_family="cool_font"
                ),
                border_radius=10,
                width=page.window.width,
                gradient=ft.LinearGradient(
                    colors=[ft.Colors.BLUE_400, ft.Colors.BLUE_600],
                ),
                on_click=lambda _: page.launch_url("https://github.com/A-Memory")
            )
        ])

    )
# start of program
app = ft.app(target=main,)
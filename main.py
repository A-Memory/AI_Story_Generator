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
    # connects to LM Server
    lmstudio.configure_default_client("CHANGE TO YOUR SERVER IP")
    model = lmstudio.llm()
    chat = lmstudio.Chat("You're a Story maker that is to make cute little stories with character names that are store within a list.\n")
except:
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
    #page.bgcolor = ft.Colors.LIGHT_BLUE_200
    page.window.width = 400
    page.window.height = 545
    page.fonts = {
        "cool_font": "ShortBaby-Mg2w.ttf"
    }

    #
    #
    # ========= AI FUNCTIONS ==========
    #
    #

    # requests story and characters from the LM image_model
    def gen_story_and_characters_text(p):
        global model, chat
        nonlocal character_container, story_container, character_text, story_text
        os.system("clear")
        gen_story = model.respond("make story and characters", response_format=Gen_StoryCharacter_Structure)
        gen_story = gen_story.parsed
        print(" ".join(gen_story['characters']))
        print(gen_story['story'])
        # add to character holder
        character_text.value = " \n".join(gen_story['characters']) + ('\n' * 5)
        story_text.value = gen_story['story'] + ('\n' * 5)
        page.update()
        # wait to do different story
        time.sleep(60 * 3) # 3 min wait until reset
        # clears image_model context and resets with original prompt
        chat.__dict__.clear()
        chat = lmstudio.Chat("You're a Story maker that is to make cute little stories")
        threading.Thread(target=gen_story_and_characters_text, args=(page,), daemon=True).start()

    #
    #
    # ========= END OF AI FUNCTIONS ==========
    #
    #

    #
    #
    # ========= UI OBJECTS ==========
    #
    #

    # holds character names
    character_text = ft.TextField(
        f"Waiting for Character Names. . .\n" + ('\n' * 5),
        text_style=ft.TextStyle(
            font_family="cool_font",
            size=20,
        ),
        border_width=1,
        focused_border_width=3,
        multiline=True,
        read_only=True,
    )

    character_container = ft.Column([
        ft.Container(
            character_text,
            border_radius=10,
            gradient=ft.LinearGradient(
                colors=[ft.Colors.BLUE_400, ft.Colors.BLUE_600],
            ),
            height=120,
        )
    ],
        height=120,
        scroll=ft.ScrollMode.ALWAYS,
    )
    story_text = ft.TextField(
        f"Waiting for Story . . .\n" + ('\n' * 5),
        width=400,
        text_style=ft.TextStyle(
            font_family="cool_font",
            size=20,
        ),
        border_width=1,
        focused_border_width=3,
        multiline=True,
        read_only=True,
    )

    # A column object to holds text
    story_container = ft.Column([
        ft.Container(
            story_text,
            border_radius=10,
            gradient=ft.LinearGradient(
                colors=[ft.Colors.BLUE_400, ft.Colors.BLUE_600],
            ),
            height=200,
            width=400,
        )
    ],
        width=400,
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
    # LM STUDIO NEEDS TO RUN OR THIS WILL FAIL
    threading.Thread(target=gen_story_and_characters_text, args=(page,), daemon=True).start()

    # add all flet objects to page
    page.add(
        ft.Stack([
            #
            #
            # Background Gradient
            #
            #
            ft.Row([
                ft.Container(
                    width=page.window.width + 100,
                    height=page.window.height + 100,
                    gradient=ft.LinearGradient(
                        colors=[ft.Colors.BLUE_100, ft.Colors.BLUE_600],
                    )
                )
            for _ in range(2)
            ],
                offset=(-0.1, -0.1),
                spacing=0,
            ),
            #
            #
            #   Main App Column Stack
            #
            #
            ft.Column([
                # Character Label
                ft.Container(
                    ft.Text(
                        "👶 Characters 🧔‍♂️",
                        size=30,
                        text_align=ft.TextAlign.CENTER,
                        font_family="cool_font"
                    ),
                    border_radius=10,
                    width=400,
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
                    width=400,
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
                        width=400,
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
                        width=400,
                        gradient=ft.LinearGradient(
                            colors=[ft.Colors.BLUE_400, ft.Colors.BLUE_600],
                        ),
                        on_click=lambda _: page.launch_url("https://github.com/A-Memory")
                    )
                ])
            ])
        ]),
    )
# start of program
app = ft.app(target=main,)
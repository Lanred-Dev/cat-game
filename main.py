"""
coin sprite: https://opengameart.org/content/spinning-gold-coin
character sprite: https://opengameart.org/content/cats-rework
"""

# python -m nuitka --standalone --onefile --windows-console-mode=disable --msvc=latest --include-data-dir="C:/Users/lando/Documents/Programming/cat-game/assets=assets" --include-data-dir="C:/Users/lando/Documents/Programming/extro/src/extro/assets/Fonts=extro/assets/Fonts" main.py


import extro

import scenes.Title

extro.Services.RenderService.set_fps(60)
extro.Window.set_title("cat game")
extro.Console.set_log_priority(extro.Console.LogPriority.DEBUG)

extro.Services.InputService.register_action(
    "move.left", extro.Services.InputService.Key.A
)
extro.Services.InputService.register_action(
    "move.right", extro.Services.InputService.Key.D
)
extro.Services.InputService.register_action(
    "move.up", extro.Services.InputService.Key.W
)
extro.Services.InputService.register_action(
    "move.down", extro.Services.InputService.Key.S
)

extro.start()

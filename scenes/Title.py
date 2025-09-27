import extro

import scenes.Game as game_scene

scene = extro.Instances.Scene(
    type=extro.Services.RenderService.RenderTargetType.INDEPENDENT
)


def play_game():
    scene.destroy()
    game_scene.start()


title = extro.Instances.ui.Image(
    image_file="assets/title.png",
    # This size maintains the aspect ratio of the original image (362x155)
    size=extro.Coord(0.15 * 2.335483871, 0.15, extro.CoordType.NORMALIZED),
    position=extro.Coord(0.5, 0.1, extro.CoordType.NORMALIZED),
    anchor=extro.Vector2(0.5, 0),
)
scene.add(title)

play_button = extro.Instances.ui.Button(
    position=extro.Coord(0.5, 0.5, extro.CoordType.NORMALIZED),
    anchor=extro.Vector2(0.5, 0.5),
    size=extro.Coord(0.3, 0.1, extro.CoordType.NORMALIZED),
    color=extro.Color(154, 184, 247),
)
scene.add(play_button)

play_button_text_label = extro.Instances.ui.Text(
    text="Play",
    font=extro.Instances.ui.Fonts.Arial,
    font_size=30,
    character_spacing=2,
    color=extro.Color(0, 0, 0),
    position=extro.Coord(0.5, 0.5, extro.CoordType.PARENT),
    anchor=extro.Vector2(0.5, 0.5),
)
play_button.add_child(play_button_text_label)
play_button.on_click.connect(play_game)

quit_button = extro.Instances.ui.Button(
    position=extro.Coord(0.5, 0.65, extro.CoordType.NORMALIZED),
    anchor=extro.Vector2(0.5, 0.5),
    size=extro.Coord(0.3, 0.1, extro.CoordType.NORMALIZED),
    color=extro.Color(255, 116, 108),
)
scene.add(quit_button)

quit_button_text_label = extro.Instances.ui.Text(
    text="Quit",
    font=extro.Instances.ui.Fonts.Arial,
    font_size=30,
    character_spacing=2,
    color=extro.Color(255, 255, 255),
    position=extro.Coord(0.5, 0.5, extro.CoordType.PARENT),
    anchor=extro.Vector2(0.5, 0.5),
)
quit_button.add_child(quit_button_text_label)
quit_button.on_click.connect(lambda: extro.quit())

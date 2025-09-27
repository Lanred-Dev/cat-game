import extro

coins: int = 0

ui = extro.Instances.Scene(
    is_visible=False, type=extro.Services.RenderService.RenderTargetType.INDEPENDENT
)
coins_label = extro.Instances.ui.Text(
    text=f"{coins} coins",
    font_size=25,
    position=extro.Coord(0.5, 0.05, extro.CoordType.NORMALIZED),
    anchor=extro.Vector2(0.5, 0.5),
)
ui.add(coins_label)

SPEED_UPGRADE_COST: int = 50

camera = extro.Instances.world.TargetCamera()
extro.Services.WorldService.set_camera(camera)

speed_upgrade_button = extro.Instances.ui.Button(
    position=extro.Coord(0.5, 0.95, extro.CoordType.NORMALIZED),
    anchor=extro.Vector2(0.5, 1),
    size=extro.Coord(0.5, 0.05, extro.CoordType.NORMALIZED),
    color=extro.Color(100, 100, 100),
)
ui.add(speed_upgrade_button)
speed_upgrade_text_label = extro.Instances.ui.Text(
    text=f"Speed +25 ({SPEED_UPGRADE_COST} coins)",
    font=extro.Instances.ui.Fonts.Arial,
    font_size=20,
    character_spacing=2,
    color=extro.Color(255, 255, 255),
    position=extro.Coord(0.5, 0.5, extro.CoordType.PARENT),
    anchor=extro.Vector2(0.5, 0.5),
)
speed_upgrade_button.add_child(speed_upgrade_text_label)
speed_upgrade_button.on_click.connect(lambda: upgrade_speed())


def upgrade_speed():
    global coins

    if coins >= SPEED_UPGRADE_COST:
        character.speed += 25
        coins -= SPEED_UPGRADE_COST
        coins_label.text = f"{coins} coins"
        update_speed_upgrade_button()


scene = extro.Instances.Scene(is_visible=False)

character = extro.Instances.world.PlayableCharacter(
    image_file="assets/character_sprite.png",
    frame_size=extro.Vector2(25, 25),
    speed=60,
    size=extro.Coord(2, 2, extro.CoordType.WORLD),
    position=extro.Coord(-22, -22, extro.CoordType.WORLD),
    states={
        "move.down": extro.Vector2(2, 3),
        "move.left": extro.Vector2(3, 3),
        "move.right": extro.Vector2(1, 3),
        "move.up": extro.Vector2(0, 3),
        "idle.down": extro.Vector2(4, 1),
    },
)
scene.add(character)
camera.bind_to(character)

coin_count: int = 0


def spawn_tree():
    (random_x, random_y) = extro.Services.ScreenService.random_world_coords(
        start=extro.Vector2(-20, -20), end=extro.Vector2(20, 20)
    )
    random_position = extro.Coord(
        random_x,
        random_y,
        extro.CoordType.WORLD,
    )

    tree = extro.Instances.world.Sprite(
        image_file="assets/tree.png",
        size=extro.Coord(5 * (36 / 31), 5, extro.CoordType.WORLD),
        position=random_position,
    )
    tree.add_collider()
    tree.add_physics_body(is_anchored=True)
    scene.add(tree)


def update_speed_upgrade_button():
    if coins >= SPEED_UPGRADE_COST:
        speed_upgrade_button.color = extro.Color(0, 200, 0)
        speed_upgrade_text_label.color = extro.Color(255, 255, 255)
    else:
        speed_upgrade_button.color = extro.Color(100, 100, 100)
        speed_upgrade_text_label.color = extro.Color(150, 150, 150)


def on_coin_collision(
    coin: extro.Instances.world.Sprite, other: extro.Instances.world.Sprite
):
    global coins, coin_count

    if other == character:
        coin.destroy()
        coins += 1
        coin_count -= 1
        coins_label.text = f"{coins} coins"
        update_speed_upgrade_button()


def spawn_coin():
    global coin_count
    if coin_count >= 400:
        return
    coin_count += 1
    (random_x, random_y) = extro.Services.ScreenService.random_world_coords(
        start=extro.Vector2(-20, -20), end=extro.Vector2(20, 20)
    )
    random_position = extro.Coord(
        random_x,
        random_y,
        extro.CoordType.WORLD,
    )

    coin = extro.Instances.world.AnimatedSprite(
        image_file="assets/coin_sprite.png",
        frame_size=extro.Vector2(32, 32),
        frame_duration=0.1,
        size=extro.Coord(1, 1, extro.CoordType.WORLD),
        position=random_position,
        frame_count=9,
    )
    coin.add_collider()
    coin.collider.on_collision.connect(lambda other: on_coin_collision(coin, other))
    scene.add(coin)


coin_timeout = extro.Utils.Timeout(0.005)


def handle_coin_timeout():
    spawn_coin()
    coin_timeout.start()


coin_timeout.on_finish.connect(handle_coin_timeout)


def start():
    for _ in range(5):
        spawn_tree()

    scene.is_visible = True
    ui.is_visible = True
    coin_timeout.start()

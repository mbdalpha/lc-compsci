"""
Sprite Collect Coins

Simple program to show basic sprite usage.

Artwork from https://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_collect_coins
"""

import random
import arcade
import arcade.gui as gui
import math

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = .25
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Collect Coins Example"

GAME_SCALE = 10

class Projectile:
    def __init__(self, x, y, angle, speed):
        self.x = x
        self.y = y

        self.i = math.cos(math.radians(angle)) * speed
        self.j = math.sin(math.radians(angle)) * speed

    def update(self, delta_time):
        self.x += self.i * delta_time * GAME_SCALE
        self.y += self.j * delta_time * GAME_SCALE
        self.j -= 9.8 * delta_time * GAME_SCALE

        self.i -= 5 * delta_time * GAME_SCALE


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.manager = gui.UIManager()
        self.manager.enable()
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        bg_tex = arcade.load_texture(":resources:gui_basic_assets/window/grey_panel.png")

        self.label1 = arcade.gui.UILabel(
            text="Angle",
            text_color=arcade.color.DARK_RED,
            width=150,
            height=40,
            font_size=24,
            font_name="Kenney Future"
        )

        self.input_field1 = gui.UIInputText(
            color=arcade.color.DARK_BLUE_GRAY,
            font_size=24,
            width=100,
            text='',
            bg_color=arcade.color.LIGHT_GRAY
        )

        self.label2 = arcade.gui.UILabel(
            text="Speed",
            text_color=arcade.color.DARK_RED,
            width=150,
            height=40,
            font_size=24,
            font_name="Kenney Future"
        )

        self.input_field2 = gui.UIInputText(
            color=arcade.color.DARK_BLUE_GRAY,
            font_size=24,
            width=100,
            text='',
            bg_color=arcade.color.LIGHT_GRAY
        )

        # Create a button
        throw_button = gui.UIFlatButton(
            color=arcade.color.DARK_BLUE_GRAY,
            text='Throw'
        )

        throw_button.on_click = self.on_click

        # Create a horizontal box layout to organize the widgets
        self.h_box = gui.UIBoxLayout(vertical = False)
        self.h_box.add(self.label1.with_space_around(bottom=0))
        self.h_box.add(self.input_field1)
        self.h_box.add(self.label2.with_space_around(bottom=0))
        self.h_box.add(self.input_field2)
        self.h_box.add(throw_button)

        # Add the layout to the UI manager
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="top",
                child=self.h_box
            )
        )

        self.player_list = None
        self.player1_sprite = None
        self.player2_sprite = None
        self.current_player = 0

        self.projectile_list = None
        self.projectile_sprite = None
        self.projectile = None

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        self.player_list = arcade.SpriteList()

        self.player1_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", SPRITE_SCALING_PLAYER)
        self.player1_sprite.center_x = 50
        self.player1_sprite.center_y = 50
        self.player_list.append(self.player1_sprite)

        self.player2_sprite = arcade.Sprite(":resources:images/animated_characters/male_person/malePerson_idle.png", SPRITE_SCALING_PLAYER)
        self.player2_sprite.center_x = SCREEN_WIDTH-50
        self.player2_sprite.center_y = 50
        self.player_list.append(self.player2_sprite)

        self.projectile_list = arcade.SpriteList()
        self.projectile_sprite = arcade.Sprite(":resources:images/space_shooter/meteorGrey_small2.png", 0.5)
        self.projectile_list.append(self.projectile_sprite)

    def on_draw(self):
        self.clear()
        self.player_list.draw()
        self.projectile_list.draw()
        self.manager.draw()

    def on_update(self, delta_time):
        if self.projectile is not None:
            self.projectile_sprite.center_x = self.projectile.x
            self.projectile_sprite.center_y = self.projectile.y
            self.projectile.update(delta_time)

    def on_click(self, event):
        self.current_player += 1
        if self.current_player % 2 == 1:
            self.projectile = Projectile(self.player1_sprite.center_x, self.player1_sprite.center_y,
                                         int(self.input_field1.text), int(self.input_field2.text))

        else:
            self.projectile = Projectile(self.player2_sprite.center_x, self.player2_sprite.center_y,
                                         180-int(self.input_field1.text), int(self.input_field2.text))



def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
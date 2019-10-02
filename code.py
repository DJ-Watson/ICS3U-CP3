#!/usr/bin/env python3

# Created by DJ Watson
# Created on September 2019
# This program draws a sprite image with background on the PyBadge


import ugame
import stage


bank_1 = stage.Bank.from_bmp16("space_aliens.bmp")
sprites = []


def main():
    # set background
    background = stage.Grid(bank_1, 10, 8)
    # creates sprite
    alien = stage.Sprite(bank_1, 9, 64, 56)
    sprites.append(alien)
    ship = stage.Sprite(bank_1, 9, 64, 56)
    sprites.insert(0, ship)

    game = stage.Stage(ugame.display, 60)
    game.layers = sprites + [background]
    game.rander_block()

    while True:
        game.render_sprites(sprites)
        game.tick()


if __name__ == "__main__":
    main()
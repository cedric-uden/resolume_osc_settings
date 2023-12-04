from __future__ import annotations

import typing as t
from enum import Enum


class Transition(Enum):
    ADD = "Add"
    ALPHA = "Alpha"
    B_and_W = "B&W"
    BURN = "Burn"
    CUBE = "Cube"
    CUT = "Cut"
    DARKEN = "Darken"
    DIFFERENCE = "Difference"
    DIFFERENCE_I = "Difference I"
    DISPLACE = "Displace"
    DISSOLVE = "Dissolve"
    DODGE = "Dodge"
    EXCLUSION = "Exclusion"
    HARD_LIGHT = "Hard Light"
    JITTERBUG = "JitterBug"
    LIGHTEN = "Lighten"
    LOREZ = "LoRez"
    LUMA_IS_ALPHA = "Luma Is Alpha"
    LUMA_KEY = "Luma Key"
    LUMA_KEY_I = "Luma Key I"
    META_MIX = "Meta Mix"
    MULTIPLY = "Multiply"
    MULTI_TASK = "Multi Task"
    NOISY = "Noisy"
    OVERLAY = "Overlay"
    PARTS = "Parts"
    PIP = "PiP"
    PUSH_DOWN = "Push Down"
    PUSH_LEFT = "Push Left"
    PUSH_RIGHT = "Push Right"
    PUSH_UP = "Push Up"
    RGB = "RGB"
    ROTATE_X = "Rotate X"
    ROTATE_Y = "Rotate Y"
    SCREEN = "Screen"
    SHIFT_RGB = "Shift RGB"
    SIDE_BY_SIDE = "Side by Side"
    SOFT_LIGHT = "Soft Light"
    STATIC = "Static"
    SUBTRACT = "Subtract"
    TILE = "Tile"
    TIME_SWITCHER = "TimeSwitcher"
    TO_BLACK = "to Black"
    TO_COLOR = "to Color"
    TO_WHITE = "to White"
    TWITCH = "Twitch"
    WIPE_ELLIPSE = "Wipe Ellipse"
    ZOOM_IN = "Zoom In"
    ZOOM_OUT = "Zoom Out"


class PlayDirection(Enum):
    REVERSE = 0
    PAUSE = 1
    PLAY = 2

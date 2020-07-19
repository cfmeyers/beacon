# -*- coding: utf-8 -*-
import random
import time
from typing import List, Dict, Any

from phue import Bridge as PBridge


class Bridge(PBridge):
    def __init__(self, my_address):
        super().__init__(my_address)

    def is_on(self, group_num: int):
        group = self.get_group(1)
        return group["action"]["on"]

    def toggle_group(self, group_num: int):
        group = self.get_group(group_num)
        self.set_group(group_num, "on", not self.is_on(1))

    def turn_off_group(self, group_num: int):
        group = self.get_group(group_num)
        self.set_group(group_num, "on", False)


"""Main module."""

LIGHT_BOOKSHELF = 1  # Small Couch Lamp
LIGHT_FLOORLAMP = 2  # Standing Shaded Lamp
LIGHT_SHELF_FURTHEST = 3  # Standing Couch Lamp with Shelves
LIGHT_SHELF_NEAREST = 4  # Sora's Desk Lamp

ALL_LIGHTS = [
    LIGHT_BOOKSHELF,
    LIGHT_FLOORLAMP,
    LIGHT_SHELF_NEAREST,
    LIGHT_SHELF_FURTHEST,
]


FULL_BRIGHTNESS = 254

FULL_HUE = 65_535

HALF_HUE = 32_767


BRIGHT_RED_SCHEME = {"hue": 60897, "sat": 254, "bri": 254}
SORCEROUS_GREEN_SCHEME = {"hue": 35636, "sat": 235, "bri": 254}
PALE_PURPLE_SCHEME = {"hue": 48701, "sat": 218, "bri": 254}
WARM_WHITE_PINK_SCHEME = {"hue": 56062, "sat": 100, "bri": 254}
BRIGHT_WHITE_SCHEME = {"hue": 7676, "sat": 199, "bri": 254}

FIREWORKS_SCHEMES = [
    BRIGHT_RED_SCHEME,
    SORCEROUS_GREEN_SCHEME,
    PALE_PURPLE_SCHEME,
    WARM_WHITE_PINK_SCHEME,
]

SCHEMES = {
    "bright-white": {
        LIGHT_BOOKSHELF: BRIGHT_WHITE_SCHEME,
        LIGHT_FLOORLAMP: BRIGHT_WHITE_SCHEME,
        LIGHT_SHELF_NEAREST: BRIGHT_WHITE_SCHEME,
        LIGHT_SHELF_FURTHEST: BRIGHT_WHITE_SCHEME,
    }
}


def toggle_lights(bridge_address: str):
    """If the lights are on, turn them off.  If off, turn them on.

    Args:
        bridge_address (str): bridge_address, e.g. "192.168.1.182"
    """
    b = Bridge(bridge_address)
    b.toggle_group(1)

    # b.set_light(LIGHT_BOOKSHELF, "bri", 254)
    # b.set_light(LIGHT_FLOORLAMP, "bri", 254)
    # b.set_light(LIGHT_SHELF_NEAREST, "bri", 254)
    # b.set_light(LIGHT_SHELF_FURTHEST, "bri", 254)

    # b.set_light(ALL_LIGHTS, "bri", 254)
    # b.set_light(ALL_LIGHTS, "hue", FULL_HUE)
    # b.set_light(ALL_LIGHTS, BRIGHT_RED_SCHEME)
    # b.set_light(ALL_LIGHTS, SORCEROUS_GREEN_SCHEME)
    # b.set_light(ALL_LIGHTS, PALE_PURPLE_SCHEME)
    # b.set_light(ALL_LIGHTS, WARM_WHITE_PINK_SCHEME)


#


def toggle_lights_n_times(bridge_address: str, n: int):
    if n % 2 != 0:
        n += 1
    b = Bridge(bridge_address)
    for _ in range(n):
        b.toggle_group(1)
        time.sleep(0.5)


def alternate_red_blue(bridge_address: str, n: int):
    if n % 2 != 0:
        n += 1
    b = Bridge(bridge_address)
    use_red = True
    for i in range(n):
        if b.is_on(1):
            if use_red:
                scheme = BRIGHT_RED_SCHEME
            else:
                scheme = SORCEROUS_GREEN_SCHEME
            b.set_light(ALL_LIGHTS, scheme)
            use_red = not use_red
        b.turn_off_group(1)


def run_fireworks(bridge_address: str, n: int):
    if n % 2 != 0:
        n += 1
    b = Bridge(bridge_address)
    for i in range(n):
        if b.is_on(1):
            schemes = random.sample(FIREWORKS_SCHEMES, len(FIREWORKS_SCHEMES))
            for light_index in range(len(b.lights)):
                scheme = schemes[light_index]
                scheme["transitiontime"] = random.randint(0, 100)
                b.set_light(light_index, scheme)
        b.toggle_group(1)
        time.sleep(1)
    b.turn_off_group(1)


def print_color_scheme(bridge_address: str) -> List[str]:
    b = Bridge(bridge_address)
    color_schemes = []
    for i, light in enumerate(b.lights):
        scheme = f"{light.name} ({i+1}): {{'hue': {light.hue}, 'sat': {light.saturation}, 'bri': {light.brightness}}}"
        color_schemes.append(scheme)
    return color_schemes


def flash_all_lights_color(b: Bridge, n: int, schema: Dict[str, Any]):
    b.set_light(ALL_LIGHTS, schema)
    for i in range(n):
        b.set_light(ALL_LIGHTS, schema)
        group = b.get_group(1)
        b.toggle_group(1)
        time.sleep(1)
    b.turn_off_group(1)


def run_set_timer(bridge_address: str):
    b = Bridge(bridge_address)
    for i in range(3):
        flash_all_lights_color(b, 6, BRIGHT_RED_SCHEME)  # start sequence
        time.sleep(25)  # lift
        print(f"Do set {i+1}")
        print(f"Do set {i+1}")
        print(f"Do set {i+1}")
        print(f"Do set {i+1}")
        print(f"Do set {i+1}")
        flash_all_lights_color(b, 6, SORCEROUS_GREEN_SCHEME)  # break sequence
        time.sleep(30)  # rest
    flash_all_lights_color(b, 6, PALE_PURPLE_SCHEME)  # complete sequence


# def set_to_color_scheme(bridge_address: str, scheme: str):
#     if scheme not in SCHEMES:
#         print(f"Unknown scheme: {scheme}")
#         return
#     b = Bridge(bridge_address)

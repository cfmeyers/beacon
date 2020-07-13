# -*- coding: utf-8 -*-
import random
import time
from typing import List

from phue import Bridge

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

FIREWORKS_SCHEMES = [
    BRIGHT_RED_SCHEME,
    SORCEROUS_GREEN_SCHEME,
    PALE_PURPLE_SCHEME,
    WARM_WHITE_PINK_SCHEME,
]


def toggle_lights(bridge_address: str):
    """If the lights are on, turn them off.  If off, turn them on.

    Args:
        bridge_address (str): bridge_address, e.g. "192.168.1.182"
    """
    b = Bridge(bridge_address)
    group = b.get_group(1)
    is_on = group["action"]["on"]
    b.set_group(1, "on", not is_on)

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
        group = b.get_group(1)
        is_on = group["action"]["on"]
        b.set_group(1, "on", not is_on)
        # b.set_group(1, "on", not is_on, transitiontime=1)
        time.sleep(0.5)


def alternate_red_blue(bridge_address: str, n: int):
    if n % 2 != 0:
        n += 1
    b = Bridge(bridge_address)
    use_red = True
    for i in range(n):
        group = b.get_group(1)
        is_on = group["action"]["on"]
        if is_on:
            if use_red:
                scheme = BRIGHT_RED_SCHEME
            else:
                scheme = SORCEROUS_GREEN_SCHEME
            b.set_light(ALL_LIGHTS, scheme)
            use_red = not use_red
        b.set_group(1, "on", not is_on)
        time.sleep(1)


def run_fireworks(bridge_address: str, n: int):
    if n % 2 != 0:
        n += 1
    b = Bridge(bridge_address)
    for i in range(n):
        group = b.get_group(1)
        is_on = group["action"]["on"]
        if is_on:
            schemes = random.sample(FIREWORKS_SCHEMES, len(FIREWORKS_SCHEMES))
            for light_index in range(len(b.lights)):
                scheme = schemes[light_index]
                scheme["transitiontime"] = random.randint(0, 100)
                b.set_light(light_index, scheme)
        b.set_group(1, "on", not is_on)
        time.sleep(1)
    group = b.get_group(1)
    b.set_group(1, "on", False)


def print_color_scheme(bridge_address: str) -> List[str]:
    b = Bridge(bridge_address)
    color_schemes = []
    for i, light in enumerate(b.lights):
        scheme = f"{light.name} ({i+1}): {{'hue': {light.hue}, 'sat': {light.saturation}, 'bri': {light.brightness}}}"
        color_schemes.append(scheme)
    return color_schemes

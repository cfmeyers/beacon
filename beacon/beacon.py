# -*- coding: utf-8 -*-
from phue import Bridge

"""Main module."""


def toggle_lights(bridge_address: str):
    """toggle_lights.

    Args:
        bridge_address (str): bridge_address, e.g. "192.168.1.182"
    """
    b = Bridge(bridge_address)
    group = b.get_group(1)
    is_on = group["action"]["on"]
    b.set_group(1, "on", not is_on)

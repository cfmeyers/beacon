# -*- coding: utf-8 -*-

"""Console script for beacon."""
import sys
import click
from phue import Bridge
from beacon.beacon import toggle_lights


@click.group()
def main(args=None):
    """Console script for beacon.py"""
    return 0


# TODO https://macintoshguy.wordpress.com/2013/08/26/hacking-the-philips-hue/
# get color profiles


@main.command()
def toggle():
    """
    hue.py toggle
    """
    toggle_lights("192.168.1.182")


if __name__ == "__main__":
    main()

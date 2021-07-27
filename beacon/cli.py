# -*- coding: utf-8 -*-

"""Console script for beacon."""
import sys

import click
from phue import Bridge

from beacon.beacon import (
    SCHEMES,
    get_current_color_scheme,
    run_fireworks,
    run_interval_with_time,
    run_set_timer,
    set_to_color_scheme,
    toggle_lights,
    toggle_lights_n_times,
)

# IP_ADDRESS = '192.168.1.182'
IP_ADDRESS = "192.168.1.151"


@click.group()
def main(args=None):
    """Console script for beacon.py"""
    return 0


# TODO Pomodoro timer


@main.command()
def toggle():
    toggle_lights(IP_ADDRESS)


@main.command()
def set_timer():
    run_set_timer(IP_ADDRESS)


@main.command()
@click.argument("d", type=int)
def run_interval(d: int):
    run_interval_with_time(IP_ADDRESS, d)


@main.command()
@click.argument("n", type=int)
def toggle_n(n: int):
    toggle_lights_n_times(IP_ADDRESS, n)


@main.command()
@click.argument("n", type=int)
def fireworks(n: int):
    run_fireworks(IP_ADDRESS, n)


@main.command()
def show_schemes():
    for scheme in SCHEMES:
        click.echo(scheme)


@main.command()
def get_color_scheme():
    color_schemes = get_current_color_scheme(IP_ADDRESS)
    for light_scheme in color_schemes:
        click.echo(light_scheme)


@main.command()
@click.argument("scheme", type=str)
def set_to_scheme(scheme: str):
    set_to_color_scheme(IP_ADDRESS, scheme)


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-

"""Console script for beacon."""
import sys
import click
from phue import Bridge
from beacon.beacon import (
    toggle_lights,
    toggle_lights_n_times,
    get_current_color_scheme,
    run_fireworks,
    run_set_timer,
    set_to_color_scheme,
    SCHEMES,
)


@click.group()
def main(args=None):
    """Console script for beacon.py"""
    return 0


# TODO Pomodoro timer


@main.command()
def toggle():
    toggle_lights("192.168.1.182")


@main.command()
def set_timer():
    run_set_timer("192.168.1.182")


@main.command()
@click.argument("n", type=int)
def toggle_n(n: int):
    toggle_lights_n_times("192.168.1.182", n)


@main.command()
@click.argument("n", type=int)
def fireworks(n: int):
    run_fireworks("192.168.1.182", n)


@main.command()
def show_schemes():
    for scheme in SCHEMES:
        click.echo(scheme)


@main.command()
def get_color_scheme():
    color_schemes = get_current_color_scheme("192.168.1.182")
    for light_scheme in color_schemes:
        click.echo(light_scheme)


@main.command()
@click.argument("scheme", type=str)
def set_to_scheme(scheme: str):
    set_to_color_scheme("192.168.1.182", scheme)


if __name__ == "__main__":
    main()

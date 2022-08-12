import numpy as np
from mandlebrot import mandelbrot


def test_mandelbrot_small():
    x = np.linspace(-2.25, 0.75, 10)
    y = np.linspace(-1.25, 1.25, 10)
    output = mandelbrot(x, y, 100, False)
    assert output.shape == (10, 10)


def test_mandelbrot_zero_outside_active_area():
    # The Mandelbrot set should be zero outside the "active" area
    x = np.linspace(1.5, 2.0, 10)
    y = np.linspace(1.5, 2.0, 10)
    output = mandelbrot(x, y, 100, False)
    assert np.all(output == 0.0)


def test_1():
    x = np.linspace(-1.5, -2.0, 10)
    y = np.linspace(-1.25, 1.25, 10)
    output = mandelbrot(x, y, 100, False)
    assert np.all(output == 0.0)

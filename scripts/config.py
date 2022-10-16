import numpy as np

serial_port = '/dev/ttyUSB0'
serial_timeout = 1

count = 0

# 数値データが1増えると何度増えるか
data_rad_diff = 0.24

foot = {
    'front': {
        'left': {
            'standard': [500, 500, 200],
            'reverse': [True, True, False],
        },
        'right': {
            'standard': [500, 500, 200],
            'reverse': [True, True, False],
        },
    },
    'middle': {
        'left': {
            'standard': [500, 500, 200],
            'reverse': [True, True, False],
        },
        'right': {
            'standard': [500, 500, 200],
            'reverse': [True, True, False],
        },
    },
    'end': {
        'left': {
            'standard': [500, 500, 200],
            'reverse': [True, True, False],
        },
        'right': {
            'standard': [500, 500, 200],
            'reverse': [True, True, False],
        },
    },
}

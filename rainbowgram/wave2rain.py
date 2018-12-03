from functools import partial
from operator import add

import librosa
import numpy as np
from scipy.interpolate import interp1d
from toolz.functoolz import curry as currinize
from toolz import pipe, curry
from .melnize import linear2mel

add = currinize(add)

@curry
def execf(condition, f, arg):
    return f(arg) if condition is True else arg

@curry
def wave2rain(wave, *, sr, n_fft=1024, stride=256, fft_configs={}, power=1, log=False, range=False, mel=False):
    """
    convert waveform into rainbowgram
    Default STFT is 3/4 overlap 1024-bin STFT
    Args:
        wave (numpy.ndarray 1 x T): time-domain waveform
    Returns:
        numpy.ndarray n_fft/2+1 x frame: rainbowgram
    """
    # time => time-frequency
    C = librosa.stft(wave, n_fft=n_fft, hop_length=stride)

    mag = pipe(C,
        np.abs,
        lambda mag: mag ** power,
        execf(log,   add(1)), # strength offset
        execf(log,   np.log),
        execf(range, lambda mag: interp1d([0, mag.max()], [0, 1])(mag)),
        execf(mel,   linear2mel(freq_min=0, freq_max=sr/2))
    )

    arg = pipe(C,
        partial(np.angle, deg=False), # (-pi, pi]
        np.unwrap,
        lambda arg: np.concatenate([arg[:,0:1], np.diff(arg, n=1)], axis=1), # [-pi, pi]
        execf(range, interp1d([-1*np.pi-0.00001, np.pi+0.00001], [0, 1])),
        execf(mel,   linear2mel(freq_min=0, freq_max=sr/2))
    )

    return np.array([mag, arg])

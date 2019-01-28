import matplotlib.pyplot as plt
import librosa

from rainbowgram.wave_rain import wave2rain, rain2wave
from rainbowgram.rain2graph import rain2graph


# load wav
wave, sr = librosa.core.load("./demo/origin.wav", sr=16000)
rain = wave2rain(wave, sr=sr, stride=256, log_mag=True, clip=0.1)

_ = rain2graph(rain)
plt.show()

reconstructed_wave = rain2wave(rain, sr=sr, stride=256, log_mag=True, clip=0.1)
# librosa.output.write_wav("./demo/rain2wave.wav", reconstructed_wave, sr, norm=True)
librosa.output.write_wav("./demo/rain2wave.wav", reconstructed_wave, sr)
import matplotlib.pyplot as plt
import librosa
from rainbowgram.wave2rain import wave2rain
from rainbowgram.rain2graph import rain2graph
# load wav
# wave, sr = librosa.core.load("./data/test.wav", sr=16000)
wave, sr = librosa.core.load("./data/bach_interpolated.mp3")

print(f"sr is {sr}")
# wave2rain
rainbowgram = wave2rain(wave, sr=sr, log=True, range=True, mel=False)

# rain2graph & show
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
rain2graph(rainbowgram, ax)
plt.show()

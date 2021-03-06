# rainbowgram - represent Magnitude and phase at the same time
**rainbowgram** is time-frequency domain wave representation.  
This library provides many utilities related to rainbowgram (conversion, visualization and so on).  

# Demo
![Rainbowgram](demo/rain.png)

# API lists
* wave2rain
  + convert waveform into rainbowgram
* rain2wave
  + convert rainbowgram into waveform
* rain2graph
  + convert rainbowgram into graph (like spectrogram)

# How to use
## Install
As a library, please install via pip (or pipenv) like below.  
```bash
pipenv install git+https://github.com/tarepan/rainbowgram#egg=rainbowgram
```

As a stand alone project or simplest PoC, please clone this project like below.  
```bash
git clone https://github.com/tarepan/rainbowgram.git
```

## Use
Please read demo.py and docstring.  
Basically, you simpley needs **wave as numpy** + **sampling rate**.  
Other arguments are optional configurations.  

# consideration
## rainbowgram variation
This library defines **rainbowgram** as **magnitude + instantaneous_frequency**, not power, not CQT.  
For usability, scaling on time and/or frequency is desirable.  
This library provides these choice as option, but the standard is above one.  

* magnitude scaling
  + power
  + log
  + range
* IF scaling
  + range (-pi/pi or 0/1)
* frequency scaling
  + mel
    - (filter bank, not yet supported)
    - linear interpolation

## visualization
graph generation, presentation and storing should be separated.  

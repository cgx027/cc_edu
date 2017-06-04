import sounddevice as sd
duration = 3
fs = 48000
myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
sd.wait()
sd.play(myrecording.data, fs)
print(myrecording.data)

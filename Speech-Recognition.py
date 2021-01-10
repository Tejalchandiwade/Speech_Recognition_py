import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import speech_recognition as sr


class Recorder:

    def __init__(self,fs,time_duration,storage_address):
        self.fs=fs=44100 #Sample Rate
        self.time_duration=time_duration #Recording time
        self.storage_address=storage_address

    def myRecording(self):
        myrecording = sd.rec(int( self.time_duration* self.fs), samplerate=self.fs, channels=2)
        print("Recording has started will last for ",self.time_duration)
        sd.wait()  # Wait until recording is finished
        wv.write(self.storage_address, myrecording, self.fs, sampwidth=2)  # Save as WAV file

    def Speech_Recognition(self):
        r = sr.Recognizer()
        file = sr.AudioFile(self.storage_address)
        with file as source:
            audio = r.record(source)
        decoded_Recording = r.recognize_google(audio, language='en-GB')
        return print(decoded_Recording)



if __name__=='__main__':
    storage_address='C:\\Users\\tejal\\Desktop\\VOIce\\output2.wav'
    p1=Recorder(44100,10,storage_address)
    p1.myRecording()
    p1.Speech_Recognition()

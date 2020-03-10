#!/usr/bin/env python3
import pyaudio
import wave

def main():
    #recording configurations
    chunk = 2048
    Format = pyaudio.paInt16
    channels = 8
    rate = 96000
    record_seconds = 5
    wave_output_file = "testRecPython.wav"

    #create and configure the microphone
    mic = pyaudio.PyAudio()
    stream = mic.open(format = Format, channels = channels, rate = rate, 
        input=True, frames_per_buffer=chunk)
        
    print("recording...")

    #read and store microphone data per frame read
    frames = []
    for i in range(0, int(rate/chunk*record_seconds)):
        data = stream.read(chunk)
        frames.append(data)
    print("done recording ...")

    # kill the mic and recording
    stream.stop_stream()
    stream.close()
    mic.terminate()

    # combine & store all microphone data to output.wav file
    outputFile = wave.open(wave_output_filename, 'wb')
    outputFile.setnchannels(channels)
    outputFile.setsampwidth(mic.get_sample_size(Format))
    outputFile.setframerate(rate)
    outputFile.writeframes(b''.join(frames))
    outputFile.close()

if __name__ == "__main__":
    main()
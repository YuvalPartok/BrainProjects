import os
import mne


def plot_raw(file):
    raw = mne.io.read_raw(file, preload=True)
    raw.pick(['Pz', 'Cz', 'Fz', 'C3', 'C4'])
    raw.plot(duration=4)


def step1(file):
    raw = mne.io.read_raw(file, preload=True)
    raw.pick(['Pz', 'Cz', 'Fz', 'C3', 'C4'])
    bandpass_filter(raw)
    rereference(raw)
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('Pick bad channels')
    raw.plot(duration=4)
    return raw


def bandpass_filter(raw):
    raw.filter(l_freq=1, h_freq=40)
    raw.resample(sfreq=250)
    freqs = (60, 120, 180, 240)
    raw.notch_filter(freqs=freqs, picks='eeg', method='spectrum_fit', filter_length='4s')

def rereference(raw):
    raw.set_eeg_reference(ref_channels=['Cz'])
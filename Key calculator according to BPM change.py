import math

def calculate_new_key(original_bpm, new_bpm, original_key):
    # calculate the speed ratio
    speed_ratio = new_bpm / original_bpm

    # calculate the change in pitch in semitones
    semitone_change = 12 * math.log2(speed_ratio)

    # calculate the change in pitch in cents
    cents_change = semitone_change * 100

    # calculate the new key in terms of semitones
    new_key_semitones = (original_key + round(semitone_change)) % 12

    # convert the new key from semitones to note names
    notes = ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B']
    new_key = notes[new_key_semitones]

    # calculate the deviation in cents
    deviation_cents = cents_change - round(semitone_change) * 100

    return new_key, deviation_cents


# test with original key E major at 88 BPM sped up to 110 BPM
original_bpm = 90
new_bpm = 110
original_key = 2  # E is the 5th note in the chromatic scale, Python indexes start at 0
new_key, deviation_cents = calculate_new_key(original_bpm, new_bpm, original_key)
print(f"New key: {new_key}, Deviation: {deviation_cents:.2f} cents")
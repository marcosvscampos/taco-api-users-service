import random
import string

def generate_key() -> str:
    segments = []
    segment_length = 5

    for _ in range(5):
        segment_letters = random.choices(string.ascii_uppercase + string.digits, k=segment_length)
        segment = ''.join(segment_letters)
        segments.append(segment)

    serial_key:str = '-'.join(segments)
    return serial_key
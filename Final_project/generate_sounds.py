from pydub.generators import Sine
from pydub import AudioSegment
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, "PixelWeatherPro", "sounds")
os.makedirs(output_dir, exist_ok=True)

def generate_tone(filename, freq, duration=1000):
    tone = Sine(freq).to_audio_segment(duration=duration)
    tone = tone.set_frame_rate(44100).set_sample_width(2).set_channels(1)
    full_path = os.path.join(output_dir, filename)
    tone.export(full_path, format="wav")
    print(f"✅ Archivo generado: {full_path}")

# generate_tone("click.wav", freq=880)
# generate_tone("sunny.wav", freq=1200)
# generate_tone("rainy.wav", freq=300)
# generate_tone("stormy.wav", freq=100)
# generate_tone("snowy.wav", freq=600)
# generate_tone("cloudy.wav", freq=700)

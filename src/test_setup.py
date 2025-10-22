import cv2
import torch
import moviepy.editor as mp
from better_profanity import profanity
import whisper

print("OpenCV version:", cv2.__version__)
print("Torch version:", torch.__version__)
print("MoviePy imported successfully")
print("Better Profanity imported successfully")

# Test Whisper
model = whisper.load_model("tiny")
print("Whisper tiny model loaded successfully")

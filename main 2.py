import time
from gtts import gTTS
import tempfile
import os
import pygame
from detector import Detector

# Initialize Detector
detect_obj = Detector()
detect_obj.start()

prev_currency = None

# Initialize pygame mixer
pygame.mixer.init()

print("[INFO] Starting currency detection with TTS (gTTS + pygame Sound)... Press Ctrl+C to exit.")

try:
    while True:
        detect_obj.detect()  # updates detect_obj.detectedCurrency and detect_obj.maxMatching

        detected_currency = detect_obj.detectedCurrency
        matching_points = detect_obj.maxMatching

        if detected_currency is not None:
            print(f"[INFO] Detected Currency : {detected_currency}")
            print(f"[INFO] Matching Points : {matching_points}")

            if detected_currency != prev_currency:
                #text = f"{detected_currency} रुपये का नोट मिला"
                text = f"यह {detected_currency} रुपये का नोट है"
                tts = gTTS(text=text, lang="hi")

                # Create temp file
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                    tts.write_to_fp(fp)
                    temp_path = fp.name

                # Load into Sound (reads fully into memory)
                sound = pygame.mixer.Sound(temp_path)
                sound.play()

                # Wait until playback finishes
                while pygame.mixer.get_busy():
                    time.sleep(0.1)

                # Safe to delete now
                os.remove(temp_path)

                prev_currency = detected_currency

        time.sleep(0.1)

except KeyboardInterrupt:
    print("\n[INFO] Stopping detector...")
    detect_obj.stop()
    pygame.mixer.quit()

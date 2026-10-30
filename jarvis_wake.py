
import speech_recognition as sr
import sounddevice as sd
import subprocess
import os
import sys

PROJECT = r"C:\Users\adim\Desktop\Mark-LIII-main"
MAIN_FILE = os.path.join(PROJECT, "main.py")
SAMPLE_RATE = 16000
LISTEN_SECONDS = 4


def main():
    if not os.path.isfile(MAIN_FILE):
        print("ERROR: main.py nahi mili!")
        input("Enter dabao...")
        return

    recognizer = sr.Recognizer()

    print("JARVIS LISTENING...")
    print('Bolo "Hey Jarvis" to start main.py')
    print("Wake word milte hi listener band ho jayega.")

    try:
        while True:
            print("\nListening...")

            recording = sd.rec(
                int(LISTEN_SECONDS * SAMPLE_RATE),
                samplerate=SAMPLE_RATE,
                channels=1,
                dtype="int16"
            )
            sd.wait()

            audio = sr.AudioData(
                recording.tobytes(),
                SAMPLE_RATE,
                2
            )

            try:
                text = recognizer.recognize_google(
                    audio,
                    language="en-IN"
                ).lower().strip()

                print("Heard:", text)

                if "hey jarvis" in text:
                    print("Wake word detected! Starting main.py...")

                    # Listener ko dobara sunne se rokne ke liye
                    # pehle main.py launch karo, phir exit ho jao.
                    subprocess.Popen(
                        [sys.executable, MAIN_FILE],
                        cwd=PROJECT,
                        creationflags=subprocess.CREATE_NEW_CONSOLE
                    )

                    print("Jarvis started. Listener is now closing.")
                    return

            except sr.UnknownValueError:
                pass

            except sr.RequestError as error:
                print("Speech recognition/internet error:", error)
                print("Listener band kiya ja raha hai.")
                return

    except KeyboardInterrupt:
        print("\nListener stopped.")

    except Exception as error:
        print("Error:", error)
        input("Enter dabao...")


if __name__ == "__main__":
    main()

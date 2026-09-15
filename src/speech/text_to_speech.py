from __future__ import annotations


def speak(text: str) -> None:
    """Offline MVP TTS. Replace with a consented Kenyan/Sheng voice provider later."""
    try:
        import pyttsx3
    except ImportError as exc:
        raise RuntimeError("Install requirements.txt before using TTS") from exc

    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

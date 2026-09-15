from __future__ import annotations

from pathlib import Path


def transcribe(audio_path: str | Path, model_size: str = "small") -> dict:
    """Transcribe audio with faster-whisper.

    Model weights are downloaded by faster-whisper at runtime and are not stored in Git.
    """
    try:
        from faster_whisper import WhisperModel
    except ImportError as exc:
        raise RuntimeError("Install requirements.txt before using speech-to-text") from exc

    model = WhisperModel(model_size, compute_type="int8")
    segments, info = model.transcribe(str(audio_path), vad_filter=True)
    text = " ".join(segment.text.strip() for segment in segments).strip()
    return {"text": text, "language": info.language, "language_probability": info.language_probability}

from pathlib import Path
from typing import Union
from openai import OpenAI
from audiotextkonverter.core.services.audio_to_text import AudioToTextService

class OpenAIAudioToTextService(AudioToTextService):
    """
    An implementation of AudioToTextService that uses the OpenAI API.
    """

    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def transcribe(self, audio_path: Union[str, Path]) -> str:
        """
        Transcribes the audio file at the given path to text using OpenAI.

        Args:
            audio_path: The path to the audio file.

        Returns:
            The transcribed text.
        """
        with open(audio_path, "rb") as audio_file:
            transcript = self.client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
        return transcript.text

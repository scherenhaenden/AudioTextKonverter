from pathlib import Path
from typing import Union
from openai import OpenAI
from magnetar_aion.core.services.text_to_audio import TextToAudioService

class OpenAITextToAudioService(TextToAudioService):
    """
    An implementation of TextToAudioService that uses the OpenAI API.
    """

    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def synthesize(self, text: str, output_path: Union[str, Path]) -> None:
        """
        Synthesizes the given text to an audio file using OpenAI.

        Args:
            text: The text to synthesize.
            output_path: The path to save the audio file.
        """
        response = self.client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=text,
        )
        response.stream_to_file(output_path)

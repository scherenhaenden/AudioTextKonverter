from abc import ABC, abstractmethod
from pathlib import Path
from typing import Union

class AudioToTextService(ABC):
    """
    An abstract base class for audio-to-text services.
    """

    @abstractmethod
    def transcribe(self, audio_path: Union[str, Path]) -> str:
        """
        Transcribes the audio file at the given path to text.

        Args:
            audio_path: The path to the audio file.

        Returns:
            The transcribed text.
        """
        pass

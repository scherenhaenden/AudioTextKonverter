from abc import ABC, abstractmethod
from pathlib import Path
from typing import Union

class TextToAudioService(ABC):
    """
    An abstract base class for text-to-audio services.
    """

    @abstractmethod
    def synthesize(self, text: str, output_path: Union[str, Path]) -> None:
        """
        Synthesizes the given text to an audio file.

        Args:
            text: The text to synthesize.
            output_path: The path to save the audio file.
        """
        pass

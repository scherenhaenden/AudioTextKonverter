import pytest
from pathlib import Path
from unittest.mock import MagicMock
from magnetar_aion.core.services.providers.openai_text_to_audio import OpenAITextToAudioService

@pytest.fixture
def mock_openai_client_for_tts():
    """Fixture to mock the OpenAI client for text-to-speech."""
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.stream_to_file.return_value = None
    mock_client.audio.speech.create.return_value = mock_response
    return mock_client

def test_openai_text_to_audio_service_synthesize(mocker, mock_openai_client_for_tts):
    """
    Tests that the OpenAITextToAudioService correctly calls the OpenAI API.
    """
    # Arrange
    mocker.patch('magnetar_aion.core.services.providers.openai_text_to_audio.OpenAI', return_value=mock_openai_client_for_tts)
    service = OpenAITextToAudioService(api_key="fake_api_key")

    dummy_output_path = Path("test_audio.mp3")

    # Act
    service.synthesize("Hello, world!", dummy_output_path)

    # Assert
    mock_openai_client_for_tts.audio.speech.create.assert_called_once_with(
        model="tts-1",
        voice="alloy",
        input="Hello, world!",
    )
    mock_openai_client_for_tts.audio.speech.create.return_value.stream_to_file.assert_called_once_with(dummy_output_path)

    # Cleanup
    if dummy_output_path.exists():
        dummy_output_path.unlink()

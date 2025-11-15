import pytest
from pathlib import Path
from unittest.mock import MagicMock
from magnetar_aion.core.services.providers.openai_audio_to_text import OpenAIAudioToTextService

@pytest.fixture
def mock_openai_client():
    """Fixture to mock the OpenAI client."""
    mock_client = MagicMock()
    mock_transcript = MagicMock()
    mock_transcript.text = "This is a test transcription."
    mock_client.audio.transcriptions.create.return_value = mock_transcript
    return mock_client

def test_openai_audio_to_text_service_transcribe(mocker, mock_openai_client):
    """
    Tests that the OpenAIAudioToTextService correctly calls the OpenAI API.
    """
    # Arrange
    mocker.patch('magnetar_aion.core.services.providers.openai_audio_to_text.OpenAI', return_value=mock_openai_client)
    service = OpenAIAudioToTextService(api_key="fake_api_key")

    # Create a dummy audio file
    dummy_audio_path = Path("test_audio.mp3")
    with open(dummy_audio_path, "wb") as f:
        f.write(b"dummy audio content")

    # Act
    result = service.transcribe(dummy_audio_path)

    # Assert
    assert result == "This is a test transcription."
    mock_openai_client.audio.transcriptions.create.assert_called_once()

    # Cleanup
    dummy_audio_path.unlink()

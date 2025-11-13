# System Architecture: MagnetarAion

This document provides a high-level overview of the system architecture for MagnetarAion.

## Core Principles

- **Modularity**: The system is designed with a clear separation of concerns between the frontend, backend, and desktop components.
- **Scalability**: The backend is built with a stateless architecture, allowing it to be easily scaled horizontally.
- **Flexibility**: The application is designed to be platform-agnostic, with support for web, desktop, and console environments.

## Architecture Components

### 1. Backend (Python/FastAPI)

- **Framework**: FastAPI is used for building the RESTful API, providing high performance and automatic documentation.
- **Database**: A PostgreSQL database is used for data persistence, with SQLAlchemy as the ORM and Alembic for migrations.
- **Authentication**: JWT (JSON Web Tokens) are used for securing the API endpoints.
- **Audio Processing**: A dedicated service layer handles audio processing, including format conversion and quality adjustments.
- **AI/ML Integration**: A swappable service layer integrates with both local and cloud-based AI/ML models for speech-to-text and text-to-speech.

### 2. Frontend (Angular)

- **Framework**: Angular is used for building the single-page application (SPA).
- **Component Architecture**: The application is built using standalone components, promoting reusability and modularity.
- **State Management**: A lightweight state management solution will be used to manage application state.
- **API Communication**: A centralized `ApiService` handles all communication with the backend.

### 3. Desktop Application (Tauri)

- **Framework**: Tauri is used to wrap the Angular frontend into a cross-platform desktop application.
- **Native Integration**: Tauri allows for integration with native desktop features, such as file system access and notifications.
- **Security**: The desktop application benefits from Tauri's security features, such as a sandboxed webview.

### 4. Console/CLI (Python)

- **Interface**: A command-line interface (CLI) is provided for users who prefer to interact with the application from the terminal.
- **Functionality**: The CLI exposes the core functionality of the application, such as audio transcription and synthesis.

## Data Flow

1. **User Interaction**: The user interacts with the application through one of the interfaces (web, desktop, or CLI).
2. **API Request**: The client sends a request to the backend API.
3. **Authentication**: The API authenticates the user's request using a JWT.
4. **Processing**: The backend processes the request, which may involve audio conversion, AI/ML model inference, or database operations.
5. **API Response**: The backend sends a response back to the client.
6. **User Feedback**: The client displays the response to the user.

## Technology Stack

- **Backend**: Python, FastAPI, PostgreSQL, SQLAlchemy, Alembic, Poetry
- **Frontend**: TypeScript, Angular, SCSS
- **Desktop**: Tauri
- **Deployment**: Docker, Nginx

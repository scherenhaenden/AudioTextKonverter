# System Architecture: MagnetarAion

This document provides a high-level overview of the system architecture for MagnetarAion.

## Core Principles

- **Modularity**: The system is designed with a clear separation of concerns between the frontend, backend, and desktop components.
- **Scalability**: The backend is built with a stateless architecture, allowing it to be easily scaled horizontally.
- **Flexibility**: The application is designed to be platform-agnostic, with support for web, desktop, and console environments.

## Project Structure

This repository contains the following components:

-   `core`: The core logic of the application, shared between the `api` and `cli` packages. This includes database models, schemas, and business logic.
-   `api`: The backend API, built with FastAPI. This package is responsible for exposing the core logic through a RESTful API.
-   `cli`: A command-line interface for the application. This package provides a way to interact with the core logic from the terminal.
-   `web`: The frontend application, built with Angular. This application is a single-page application that communicates with the `api` package.

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

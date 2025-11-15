# Project Rules and Conventions: MagnetarAion

This document outlines the coding standards, conventions, and architectural rules for the MagnetarAion project. Adherence to these rules is mandatory to ensure code quality, consistency, and maintainability.

## Frontend (Angular)

### TypeScript

#### Classes
- **Documentation**: Every class must have a detailed JSDoc comment explaining its purpose, responsibilities, and how it interacts with other parts of the application.
- **Access Modifiers**: All class members (properties and methods) must have an explicit access modifier (`public`, `private`, or `protected`).
- **Readonly**: Use the `readonly` modifier for properties that should not be changed after initialization.

#### Methods
- **Return Types**: All methods must have an explicit return type.
- **Documentation**: All public methods must have a JSDoc comment explaining what the method does, its parameters (`@param`), and what it returns (`@returns`).

#### Variables
- **Access Modifiers**: All class properties must have an explicit access modifier (`public`, `private`, or `protected`).

### Component Structure
- **Standalone Components**: All new components should be created with `standalone: true`.
- **Imports**: Necessary modules like `CommonModule` must be included in the component's `imports` array.

### Services
- **API Communication**: Services must use the centralized `ApiService` for all backend HTTP requests. Direct use of `HttpClient` is forbidden, with the sole exception of a future `ConfigService`.
- **Endpoint Constants**: Each service should define a `const` for its specific API endpoint path.

### Styling (SCSS)
- **BEM Convention**: CSS classes must follow the Block, Element, Modifier (BEM) naming convention.
- **7-1 Pattern**: The SCSS is structured using the 7-1 architectural pattern.

## Backend (Python)

### General
- **Type Hinting**: All function and method signatures must include type hints for arguments and return values.
- **Docstrings**: Every module, class, and function must have a comprehensive docstring explaining its purpose.

### FastAPI
- **Database Sessions**: API endpoints must use the centralized `get_db` dependency function to manage database sessions.
- **CORS**: CORS will be configured to allow requests strictly from the Angular frontend's domain.

### Database (SQLAlchemy)
- **Password Hashing**: Passwords must be securely hashed using `passlib` with `bcrypt` before being stored. This logic will be encapsulated in `core/src/core/security.py`.
- **Enums**: Use Python `Enums` for model fields with a predefined set of choices (e.g., status, priority) to ensure data consistency.
- **Migrations**: Database migrations are managed with Alembic.
    - Before creating a new migration, ensure the database is upgraded to the latest version (`python -m alembic -c alembic.ini upgrade head`).
    - Generate migrations using `python -m alembic -c alembic.ini revision --autogenerate -m "<description>"`.
    - Manually review all generated migration scripts to ensure they only contain intended changes.

## Dependency Management

To streamline development, the project will incorporate helpers for managing dependencies.

- **Backend (Python)**: A utility script will be provided that wraps the application launcher. This script will check for required dependencies listed in `pyproject.toml` and automatically install any missing packages using `poetry`. This ensures that the development environment is always in sync.
- **Frontend (Angular)**: All dependencies must be explicitly added to `package.json`. While we won't auto-install based on code imports, pre-commit hooks will be used to ensure that `package.json` and the `node_modules` directory are synchronized, preventing inconsistencies.

## General Project Rules

### Testing
- **Mandatory Tests**: All new code and functionality must be accompanied by corresponding tests.
- **TDD Preference**: A Test-Driven Development (TDD) approach is highly preferred.

### Security
- **No Hardcoded Secrets**: Secrets must not be committed to the repository. They should be managed via environment variables. A `.env.template` file must be maintained to document required variables.

### Version Control
- **Gitflow**: We use Gitflow for branching. All feature development should happen in `feature/` branches.
- **Commit Messages**: Commit messages must follow the Conventional Commits specification.

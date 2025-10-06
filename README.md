# RAG-Langchain

## Development Setup

### Code Formatting with Black

This project uses [Black](https://black.readthedocs.io/) for code formatting to ensure consistent code style.

#### Automatic Formatting with Pre-commit Hooks

To automatically format your code before each commit, set up pre-commit hooks:

1. Install pre-commit:
   ```bash
   pip install pre-commit
   ```

2. Install the git hook scripts:
   ```bash
   pre-commit install
   ```

Now, Black will automatically format your Python files before each commit.

#### Manual Formatting

To manually format all Python files in the project:
```bash
black .
```

To check if files need formatting without modifying them:
```bash
black --check .
```

#### CI/CD

The repository has GitHub Actions workflows that:
- Check code formatting on pull requests
- Ensure all code committed to main/development branches is properly formatted
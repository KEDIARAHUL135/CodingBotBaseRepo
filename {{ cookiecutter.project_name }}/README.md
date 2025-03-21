# {{ cookiecutter.project_name }}

{{ cookiecutter.repo_description }}

## Overview

This repository is designed as a minimal base template for code generation projects that require integration with language models (LLMs) and basic database interactions. It includes:

- Utility functions for LLM communication
- Basic database connectivity utilities
- Centralized logging setup
- Environment setup using `venv` and dependency management via Poetry

## Environment Setup

### Using `venv`

Create and activate a virtual environment:

```bash
python -m venv venv
# Activate the virtual environment:
# On Unix/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```
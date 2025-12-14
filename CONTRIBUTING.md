# Contributing to DataRasta

Thank you for your interest in contributing to DataRasta! This document provides guidelines and instructions for contributing.

## Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/syedhaseebahmad/datarasta.git
   cd datarasta
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -e ".[dev]"
   ```

## Code Style

- Follow PEP 8 style guidelines
- Use type hints where applicable
- Write docstrings for all functions and classes
- Run `black` for code formatting:
  ```bash
  black datarasta tests
  ```

## Testing

- Write tests for new features
- Ensure all tests pass:
  ```bash
  pytest
  ```
- Aim for test coverage above 80%

## Adding New Metrics

When adding a new metric:

1. Add the function to the appropriate module in `datarasta/metrics/`
2. Export it in the module's `__init__.py` if needed
3. Add it to `datarasta/__init__.py` exports
4. Update `DataQualityMetrics.compute_metric()` in `core.py`
5. Add documentation in README.md
6. Write tests in `tests/`

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Write/update tests
5. Ensure all tests pass
6. Update documentation if needed
7. Commit your changes (`git commit -m 'Add some amazing feature'`)
8. Push to the branch (`git push origin feature/amazing-feature`)
9. Open a Pull Request

## Reporting Issues

Please use the GitHub issue tracker to report bugs or suggest features. Include:
- Description of the issue
- Steps to reproduce
- Expected vs. actual behavior
- Python version and package versions

## License

By contributing, you agree that your contributions will be licensed under the MIT License.


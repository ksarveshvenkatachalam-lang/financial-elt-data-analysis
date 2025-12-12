# Contributing to Financial ELT Data Analysis

First off, thank you for considering contributing to this project! It's people like you that make this project better for everyone.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Process](#development-process)
- [Style Guidelines](#style-guidelines)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)

## 📜 Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## 🤝 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples** to demonstrate the steps
- **Describe the behavior you observed** and what you expected
- **Include screenshots** if relevant
- **Include your environment details** (OS, Python version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

- **Use a clear and descriptive title**
- **Provide a detailed description** of the suggested enhancement
- **Explain why this enhancement would be useful**
- **List some examples** of how it would be used

### Your First Code Contribution

Unsure where to begin? You can start by looking through these issues:

- **good first issue** - Issues which should only require a few lines of code
- **help wanted** - Issues which need attention from contributors

## 🔧 Development Process

### Setting Up Your Development Environment

1. **Fork the repository** to your GitHub account

2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/financial-elt-data-analysis.git
   cd financial-elt-data-analysis
   ```

3. **Add the upstream repository**:
   ```bash
   git remote add upstream https://github.com/ksarveshvenkatachalam-lang/financial-elt-data-analysis.git
   ```

4. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

5. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # If available
   ```

### Making Changes

1. **Create a new branch** for your feature or fix:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

2. **Make your changes** following our style guidelines

3. **Test your changes** thoroughly

4. **Commit your changes** using conventional commits (see below)

### Branch Naming Convention

- `feature/` - New features (e.g., `feature/add-visualization`)
- `fix/` - Bug fixes (e.g., `fix/data-loading-error`)
- `docs/` - Documentation changes (e.g., `docs/update-readme`)
- `refactor/` - Code refactoring (e.g., `refactor/optimize-pipeline`)
- `test/` - Adding tests (e.g., `test/add-unit-tests`)

## 📝 Style Guidelines

### Python Style Guide

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code:

- **Indentation**: 4 spaces (no tabs)
- **Line length**: Maximum 88 characters (Black formatter standard)
- **Naming conventions**:
  - `snake_case` for functions and variables
  - `PascalCase` for class names
  - `UPPER_CASE` for constants

### Code Formatting

We recommend using these tools:

```bash
# Format code with Black
black .

# Sort imports with isort
isort .

# Lint with flake8
flake8 .

# Type checking with mypy (optional)
mypy .
```

### Documentation

- All functions and classes should have docstrings
- Use Google-style docstrings:
  ```python
  def function_name(param1, param2):
      """Brief description of function.
      
      Args:
          param1 (type): Description of param1.
          param2 (type): Description of param2.
          
      Returns:
          type: Description of return value.
          
      Raises:
          ExceptionType: Description of when this exception is raised.
      """
      pass
  ```

## 💬 Commit Messages

We use [Conventional Commits](https://www.conventionalcommits.org/) for commit messages:

### Format
```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, missing semi-colons, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Examples
```bash
git commit -m "feat(transform): add moving average calculation"
git commit -m "fix(extract): handle missing Kaggle credentials"
git commit -m "docs(readme): update installation instructions"
git commit -m "refactor(load): optimize database loading performance"
```

## 🔀 Pull Request Process

### Before Submitting

1. **Update your fork** with the latest changes:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Run tests** to ensure everything works:
   ```bash
   pytest tests/
   ```

3. **Update documentation** if needed

4. **Ensure your code follows** the style guidelines

### Submitting the Pull Request

1. **Push your branch** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Open a Pull Request** on GitHub:
   - Use a clear and descriptive title
   - Reference any related issues (e.g., "Fixes #123")
   - Describe your changes in detail
   - Include screenshots if relevant

3. **PR Template** (use this format):
   ```markdown
   ## Description
   Brief description of changes
   
   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Documentation update
   - [ ] Refactoring
   
   ## Testing
   - [ ] Tests pass locally
   - [ ] Added new tests for changes
   
   ## Checklist
   - [ ] Code follows style guidelines
   - [ ] Self-reviewed code
   - [ ] Commented complex code
   - [ ] Updated documentation
   - [ ] No breaking changes
   
   ## Related Issues
   Closes #(issue number)
   ```

### Review Process

1. **Maintainers will review** your PR within 3-5 business days
2. **Address feedback** promptly and professionally
3. **Make requested changes** in new commits (don't force push)
4. **Once approved**, your PR will be merged

## 🧪 Testing Guidelines

### Writing Tests

```python
import pytest
from extract.kaggle_extractor import KaggleExtractor

def test_kaggle_extractor_initialization():
    """Test KaggleExtractor can be initialized."""
    extractor = KaggleExtractor()
    assert extractor is not None
    assert extractor.dataset_name == "nazaninmottaghi2022/financial-data"
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test file
pytest tests/test_extractor.py

# Run specific test
pytest tests/test_extractor.py::test_kaggle_extractor_initialization
```

## 📚 Additional Resources

- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)

## 🎯 Project Goals

When contributing, keep these project goals in mind:

- **Modularity**: Keep components independent and reusable
- **Simplicity**: Prefer simple, readable code over complex solutions
- **Documentation**: All code should be well-documented
- **Testing**: Maintain high test coverage
- **Performance**: Optimize for efficiency without sacrificing readability
- **Best Practices**: Follow industry-standard data engineering practices

## ❓ Questions?

Don't hesitate to ask questions! You can:

- Open an issue with the `question` label
- Start a discussion in GitHub Discussions
- Contact the maintainers directly

## 🙏 Thank You!

Your contributions make this project better for everyone. Thank you for taking the time to contribute!

---

**Happy Coding! 🚀**

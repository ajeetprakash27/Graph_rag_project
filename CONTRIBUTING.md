# Contributing to GraphRAG

Thank you for your interest in contributing to GraphRAG! We appreciate your help in making this project better.

## Code of Conduct

Please be respectful and constructive in all interactions.

## How to Contribute

### 1. Reporting Bugs
- Check existing issues to avoid duplicates
- Provide a clear description of the bug
- Include steps to reproduce
- Add Python version, OS, and dependency versions
- Include error messages and stack traces

**Bug Report Template:**
```
## Description
Brief description of the bug

## Steps to Reproduce
1. First step
2. Second step
3. ...

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Environment
- Python: 3.x
- OS: Windows/Mac/Linux
- Key Dependencies: FastAPI x.x.x, etc.

## Additional Context
Any other relevant information
```

### 2. Suggesting Features
- Describe the feature clearly
- Explain the use case
- Provide examples if applicable
- Discuss potential implementation

**Feature Request Template:**
```
## Description
Brief description of the feature

## Motivation
Why is this feature needed?

## Proposed Solution
How should this work?

## Examples
Code examples or mock-ups

## Alternatives Considered
Other approaches you considered
```

### 3. Submitting Pull Requests

#### Before Starting
1. Fork the repository
2. Create a new branch for your feature: `git checkout -b feature/my-feature`
3. Set up development environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

#### During Development
1. Write clean, readable code
2. Add docstrings to functions
3. Include type hints where possible
4. Write tests for new features
5. Follow PEP 8 style guidelines

#### Before Submitting
1. Format code: `black app/`
2. Run linter: `flake8 app/`
3. Run tests: `pytest`
4. Update documentation if needed
5. Check for any sensitive information (API keys, etc.)

#### Commit Guidelines
```bash
# Good commit messages
git commit -m "Add feature: X capability"
git commit -m "Fix bug: Y issue"
git commit -m "Refactor: Z component for clarity"

# Avoid
git commit -m "fixed stuff"
git commit -m "wip"
```

#### PR Description Template
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Related Issues
Closes #issue_number

## Changes
- Change 1
- Change 2
- Change 3

## Testing
How was this tested?

## Checklist
- [ ] Code follows style guidelines
- [ ] New dependencies documented
- [ ] Tests pass locally
- [ ] Documentation updated
- [ ] No breaking changes
```

## Development Workflow

### Setting Up Development Environment
```bash
# Clone your fork
git clone https://github.com/your-username/graphrag-project.git
cd graphrag-project

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install with dev dependencies
pip install -r requirements.txt
pip install black flake8 pytest pytest-cov
```

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app

# Run specific test
pytest tests/test_main.py
```

### Code Quality
```bash
# Format code
black app/

# Check style
flake8 app/

# Check for common issues
pylint app/
```

## Project Structure

```
graphrag-project/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI endpoints
│   ├── config.py         # Configuration
│   ├── rag_pipeline.py   # RAG logic
│   ├── vector_store.py   # Vector DB
│   └── graph_utils.py    # Graph operations
├── tests/                # Unit tests
├── docs/                 # Documentation
└── examples/             # Example scripts
```

## Coding Standards

### Style Guide
- Follow PEP 8
- Max line length: 100 characters
- Use type hints for function parameters and returns
- Add docstrings to all public functions

### Example
```python
def retrieve_context(query: str, max_results: int = 3) -> list[str]:
    """
    Retrieve relevant context for a given query.
    
    Args:
        query: The search query string
        max_results: Maximum number of results to return
        
    Returns:
        List of relevant document contexts
        
    Raises:
        ValueError: If query is empty
    """
    if not query:
        raise ValueError("Query cannot be empty")
    
    # Implementation here
    return []
```

## Documentation

- Update README.md for user-facing changes
- Add docstrings for new functions
- Include type hints
- Add inline comments for complex logic
- Update API documentation for endpoint changes

## Performance Considerations

- Consider scalability when adding features
- Optimize database queries
- Cache results when appropriate
- Profile code for bottlenecks

## Security

- Never commit API keys or secrets
- Use environment variables for sensitive data
- Validate user inputs
- Sanitize data before storage
- Follow OWASP guidelines

## Release Process

1. Update version number
2. Update CHANGELOG.md
3. Create release notes
4. Tag release: `git tag v1.0.0`
5. Push tag: `git push origin v1.0.0`

## Getting Help

- Check existing issues and discussions
- Read the documentation
- Ask questions in discussions
- Contact maintainers if needed

## Recognition

Contributors will be recognized in:
- CONTRIBUTORS.md file
- Release notes
- GitHub contributors page

Thank you for contributing! 🎉

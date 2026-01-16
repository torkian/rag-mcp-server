# Contributing to RAG MCP Server

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- A clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Your environment (OS, Python version, Claude Desktop version)

### Suggesting Features

Feature requests are welcome! Please open an issue describing:
- The feature you'd like to see
- Why it would be useful
- How it might work

### Submitting Pull Requests

1. **Fork the repository**
2. **Create a branch** for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Test your changes** thoroughly
5. **Commit with clear messages**:
   ```bash
   git commit -m "Add: description of your feature"
   ```
6. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Open a pull request** with a clear description

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/torkian/rag-mcp-server.git
   cd rag-mcp-server
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   # or
   venv\Scripts\activate  # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Make your changes and test

## Code Style

- Follow [PEP 8](https://pep8.org/) for Python code
- Use clear, descriptive variable and function names
- Add comments for complex logic
- Keep functions focused and concise

## Testing

Before submitting a PR:
1. Test the server starts without errors
2. Test in Claude Desktop
3. Verify your changes work on your platform

## Questions?

Feel free to open an issue for any questions or clarifications!

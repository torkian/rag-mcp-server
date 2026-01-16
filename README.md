# RAG MCP Server

A simple **Model Context Protocol (MCP)** server that provides RAG (Retrieval-Augmented Generation) capabilities to Claude Desktop. This allows Claude to search through your custom knowledge base!

## 🤔 What is MCP?

**Model Context Protocol (MCP)** is an open standard created by Anthropic that allows AI assistants like Claude to securely connect to external data sources and tools. Think of it as a way to give Claude superpowers by connecting it to your own data and APIs.

## 🎯 What Does This Server Do?

This MCP server exposes a `search_rag` tool that Claude Desktop can use to search through a knowledge base. In this example, it returns test data, but you can easily customize it to:
- Query your own vector database
- Search through your documents
- Connect to your RAG API
- Access any custom data source

## 🚀 Quick Start

> **New to this?** Check out [QUICKSTART.md](QUICKSTART.md) for a simplified step-by-step guide!

### Prerequisites

- **Python 3.10 or higher** ([Download Python](https://www.python.org/downloads/))
- **Claude Desktop** ([Download here](https://claude.ai/download))
- Basic familiarity with command line

### Step 1: Clone or Download This Repository

```bash
git clone https://github.com/yourusername/rag-mcp-server.git
cd rag-mcp-server
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Test the Server

Make sure the server runs correctly:

```bash
python server.py
```

You should see the server start. Press `Ctrl+C` to stop it.

### Step 4: Configure Claude Desktop

Find your Claude Desktop configuration file:

- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

Open the file and add this configuration (replace `/path/to/` with your actual path):

```json
{
  "mcpServers": {
    "rag-server": {
      "command": "python3",
      "args": ["/absolute/path/to/rag-mcp-server/server.py"]
    }
  }
}
```

**Important**: Use the absolute path to `server.py`!

#### Finding Your Python Path

If `python3` doesn't work, find your Python path:

```bash
# macOS/Linux
which python3

# Windows (Command Prompt)
where python
```

Use the full path in your config, for example:

```json
{
  "mcpServers": {
    "rag-server": {
      "command": "/usr/local/bin/python3",
      "args": ["/Users/yourname/rag-mcp-server/server.py"]
    }
  }
}
```

### Step 5: Restart Claude Desktop

1. **Completely quit** Claude Desktop (don't just close the window)
   - **macOS**: Press `Cmd+Q` or go to Claude → Quit
   - **Windows**: Right-click the system tray icon and select Quit
2. **Reopen** Claude Desktop
3. Look for the **🔌 icon** at the bottom of the chat window - this means your MCP server is connected!

### Step 6: Test It!

In Claude Desktop, try asking:

```
Use the search_rag tool to find information about Python
```

You should see Claude call your tool and return the test message!

## 📝 How to Customize

### Option 1: Add Your Own Hardcoded Data

Edit `server.py` and modify the `KNOWLEDGE_BASE` list (lines 11-39):

```python
KNOWLEDGE_BASE = [
    {
        "id": 1,
        "title": "Your Document Title",
        "content": "Your document content here..."
    },
    # Add more documents...
]
```

Then update the `search_knowledge_base()` function (line 45) to implement real search logic.

### Option 2: Connect to Your API

Modify the `search_knowledge_base()` function to call your existing RAG API:

```python
import httpx

def search_knowledge_base(query: str) -> list:
    # Call your API
    response = httpx.get(f"https://your-api.com/search?q={query}")
    return response.json()
```

### Option 3: Connect to a Vector Database

Install a vector database client and query it:

```python
# Example with Pinecone
import pinecone

def search_knowledge_base(query: str) -> list:
    # Query your vector database
    results = index.query(query, top_k=5)
    return results
```

## 🛠️ Project Structure

```
rag-mcp-server/
├── server.py                           # Main MCP server implementation
├── requirements.txt                    # Python dependencies
├── README.md                           # Full documentation (you are here!)
├── QUICKSTART.md                       # Simplified quick start guide
├── CONTRIBUTING.md                     # Contribution guidelines
├── LICENSE                             # MIT License
├── claude_desktop_config.example.json  # Example config (copy and modify)
└── .gitignore                          # Git ignore patterns
```

## 🔧 Troubleshooting

### The 🔌 icon doesn't appear

1. **Check the config file path** - make sure you edited the correct file
2. **Verify absolute paths** - use full paths, not relative paths like `./server.py`
3. **Check Python path** - run `which python3` (macOS/Linux) or `where python` (Windows)
4. **View logs** - Claude Desktop logs errors to:
   - **macOS**: `~/Library/Logs/Claude/mcp*.log`
   - **Windows**: `%APPDATA%\Claude\Logs\mcp*.log`

### Server shows as connected but tool doesn't work

1. **Restart Claude Desktop** completely after any code changes
2. **Test the server manually**:
   ```bash
   python server.py
   ```
   It should start without errors

### Permission errors

Make the server executable:

```bash
chmod +x server.py
```

### Import errors

Make sure dependencies are installed:

```bash
pip install -r requirements.txt
```

If using virtual environments, activate it first:

```bash
# Create virtual environment
python -m venv venv

# Activate it
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

Then update your Claude Desktop config to use the virtual environment's Python:

```json
{
  "mcpServers": {
    "rag-server": {
      "command": "/absolute/path/to/venv/bin/python",
      "args": ["/absolute/path/to/server.py"]
    }
  }
}
```

## 📚 Learn More

- [MCP Documentation](https://modelcontextprotocol.io/)
- [MCP Specification](https://spec.modelcontextprotocol.io/)
- [Claude Desktop Documentation](https://claude.ai/docs)
- [Example MCP Servers](https://github.com/anthropics/anthropic-quickstarts/tree/main/mcp)

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Open issues for bugs or feature requests
- Submit pull requests
- Share your customizations

## 📄 License

MIT License - feel free to use this in your own projects!

## 💡 Example Use Cases

- **Personal knowledge base**: Search your notes, documents, or research
- **Company documentation**: Give Claude access to internal wikis or docs
- **Database queries**: Connect to SQL/NoSQL databases
- **API integration**: Bridge Claude with your existing APIs
- **Custom tools**: Add any functionality you need!

## 🎓 How It Works

1. **Server starts**: The Python server runs and waits for messages via stdin/stdout
2. **Claude connects**: Claude Desktop reads the config and connects to your server
3. **Tool registration**: The server tells Claude about the `search_rag` tool
4. **User asks**: When you ask Claude to search, it calls the tool
5. **Server responds**: Your server processes the request and returns results
6. **Claude uses results**: Claude incorporates the results into its response

---

**Built with ❤️ using the Model Context Protocol**

Questions? Open an issue or check the [MCP documentation](https://modelcontextprotocol.io/)!

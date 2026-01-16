# Quick Start Guide

Get your RAG MCP server running in 5 minutes!

## Step 1: Install Python

Make sure you have Python 3.10 or higher:

```bash
python3 --version
```

Don't have Python? [Download it here](https://www.python.org/downloads/)

## Step 2: Download This Project

```bash
git clone https://github.com/torkian/rag-mcp-server.git
cd rag-mcp-server
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 4: Find Your Paths

Get your Python path:
```bash
which python3  # macOS/Linux
where python   # Windows
```

Get your project path:
```bash
pwd  # Should show full path to rag-mcp-server
```

## Step 5: Configure Claude Desktop

Open your Claude Desktop config:

- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

Add this (replace with YOUR paths):

```json
{
  "mcpServers": {
    "rag-server": {
      "command": "/YOUR/PYTHON/PATH",
      "args": ["/YOUR/PROJECT/PATH/server.py"]
    }
  }
}
```

## Step 6: Restart Claude Desktop

1. Quit Claude Desktop completely (Cmd+Q on Mac)
2. Reopen it
3. Look for the 🔌 icon

## Step 7: Test It!

In Claude Desktop:
```
Use the search_rag tool to search for anything
```

## ✅ Success!

You should see a test message from your MCP server!

## ❌ Not Working?

See the [Troubleshooting section](README.md#-troubleshooting) in the main README.

## Next Steps

- Customize `server.py` with your own data
- Connect to your RAG API
- Add more tools
- Check out the full [README](README.md)

Need help? [Open an issue](https://github.com/torkian/rag-mcp-server/issues)

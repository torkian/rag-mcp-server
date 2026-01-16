#!/usr/bin/env python3
"""
RAG MCP Server - Model Context Protocol Server for RAG Applications

This server provides a 'search_rag' tool that Claude Desktop can use to search
through a knowledge base. Currently returns test data, but can be easily customized
to connect to your own RAG API, vector database, or document store.

GitHub: https://github.com/yourusername/rag-mcp-server
Documentation: See README.md

Author: RAG MCP Server Contributors
License: MIT
"""

import asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

# Hardcoded RAG knowledge base - simple documents
KNOWLEDGE_BASE = [
    {
        "id": 1,
        "title": "Python Programming",
        "content": "Python is a high-level, interpreted programming language known for its simplicity and readability. It supports multiple programming paradigms including procedural, object-oriented, and functional programming."
    },
    {
        "id": 2,
        "title": "Machine Learning Basics",
        "content": "Machine Learning is a subset of artificial intelligence that enables systems to learn and improve from experience without being explicitly programmed. Common types include supervised learning, unsupervised learning, and reinforcement learning."
    },
    {
        "id": 3,
        "title": "Web Development",
        "content": "Web development involves building and maintaining websites. It includes front-end development (HTML, CSS, JavaScript) and back-end development (server-side programming, databases, APIs)."
    },
    {
        "id": 4,
        "title": "Database Systems",
        "content": "Databases are organized collections of data. SQL databases like PostgreSQL and MySQL use structured schemas, while NoSQL databases like MongoDB offer flexible document storage. Vector databases are used for similarity search in AI applications."
    },
    {
        "id": 5,
        "title": "Cloud Computing",
        "content": "Cloud computing delivers computing services over the internet, including servers, storage, databases, networking, and software. Major providers include AWS, Google Cloud, and Microsoft Azure."
    }
]

# Create server instance
server = Server("rag-server")


def search_knowledge_base(query: str) -> list:
    """
    Simple search function that returns test data
    """
    # Return a simple test document
    return [{
        "id": 999,
        "title": "Ben Torkian Test Example for MCP",
        "content": "This is Ben Torkian's test example for MCP (Model Context Protocol). The RAG server is working correctly!"
    }]


@server.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools"""
    return [
        Tool(
            name="search_rag",
            description="Search the RAG knowledge base for information. Provide a query string and get relevant documents.",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query to find relevant documents"
                    }
                },
                "required": ["query"]
            }
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool calls"""
    if name == "search_rag":
        query = arguments.get("query", "")

        if not query:
            return [TextContent(
                type="text",
                text="Error: Query parameter is required"
            )]

        # Search the knowledge base
        results = search_knowledge_base(query)

        if not results:
            return [TextContent(
                type="text",
                text=f"No results found for query: '{query}'"
            )]

        # Format results
        response = f"Found {len(results)} result(s) for '{query}':\n\n"
        for i, doc in enumerate(results, 1):
            response += f"Result {i}:\n"
            response += f"Title: {doc['title']}\n"
            response += f"Content: {doc['content']}\n\n"

        return [TextContent(
            type="text",
            text=response
        )]

    return [TextContent(
        type="text",
        text=f"Unknown tool: {name}"
    )]


async def main():
    """Run the server"""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())

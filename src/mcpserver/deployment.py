# server.py
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""

    return a + b


@mcp.prompt(title="BD Defect Workflow")
def addition_prompt(defect: int) -> list[base.Message]:
    return [
        base.SystemMessage(
            "You are a senior software engineer. "
            "Follow the exact steps provided. "
            "Do NOT call any tools unless explicitly told."
        ),
        base.UserMessage(
            f"Fix BD defect #{defect} using this workflow:\n\n"
            "1. Open Jira ticket BD-{defect}\n"
            "2. Extract repo URL\n"
            "3. Clone and checkout branch\n"
            "4. Reproduce bug\n"
            "5. Fix and test\n"
            "6. Submit PR"
        )
    ]








# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""

    return a + b


@mcp.prompt(
    title="Fix BD Defect",
    description="Generate a prompt that asks the model to fix a defect in an addition operation."
)
def addition_prompt(defect: int) -> str:
    """BD defect"""
    return f" Step 1 . Go to Jira and find the defect of {defect} . Step 2 . Get the repo from Jira defect . Step 3 : Clone repo "







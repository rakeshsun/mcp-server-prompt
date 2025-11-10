# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""

    return a + b


@self.prompt(
        title="Addition Defect Fix",
        description="Generate a prompt to fix a defect in addition logic."
    )
    def addition_prompt(self, defect: int) -> str:
        """BD defect"""
        return f"Fix the defect of {defect} in the addition prompt."





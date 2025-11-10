# server.py
from mcp.server.fastmcp import FastMCP


# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""

    return a + b


@mcp.tool()
def run_bd_workflow(defect: int) -> str:
    """Invoke BD Defect Workflow prompt."""
    messages = addition_prompt(defect)  # Call your prompt function
    # Simulate LLM response or return formatted text
    return f"Workflow for defect {defect}: [Simulated output from prompt messages]"


def addition_prompt(defect: str) -> str:
    """BD defect workflow"""
    return """
            Step 1 : Execute this workflow for BD defect #{defect}:\n\n"
            Step 2: Go to Jira and find defect {defect}. Retrieve ticket details (summary, assignee, status).\n"
            Step 3: Get the repo URL from the Jira defect description.\n"
            Step 4: Clone the repo and checkout the relevant branch.\n"
        
       """














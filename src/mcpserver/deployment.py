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


@mcp.prompt(
    title="BD Defect Workflow",
    description="Step-by-step guide to investigate and fix a BD defect from Jira."
)
def addition_prompt(defect: int) -> list[base.Message]:
    """BD defect workflow"""
    return [
        base.SystemMessage(
            "You are a senior DevOps engineer. Follow the workflow steps exactly. "
            "Do not call tools or make assumptions—respond with the output of each step."
        ),
        base.UserMessage(
            f"Execute this workflow for BD defect #{defect}:\n\n"
            f"Step 1: Go to Jira and find defect {defect}. Retrieve ticket details (summary, assignee, status).\n"
            f"Step 2: Get the repo URL from the Jira defect description.\n"
            f"Step 3: Clone the repo and checkout the relevant branch.\n"
            f"Step 4: Reproduce the defect and propose a fix.\n\n"
            f"Start with Step 1 and report progress."
        )
    ]








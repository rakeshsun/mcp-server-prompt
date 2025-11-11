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
    title="BD Defect Workflow",
    description="Step-by-step guide to fix a BD defect from Jira."
)
def bd_defect_workflow(defect: int) -> list[dict]:
    return [
        {
            "role": "system",
            "content": {"type": "text", "text": "You are a senior DevOps engineer. Execute the workflow step-by-step. Simulate actions. Do NOT call tools."}
        },
        {
            "role": "user",
            "content": {"type": "text", "text": f"""
Execute BD Defect Workflow for defect BD-{defect}:

1. Open Jira ticket BD-{defect}
2. Extract repo URL
3. Clone repo and checkout branch
4. Reproduce bug
5. Propose fix
6. Submit PR

Report each step.
"""}
        }
    ]

# Tool: Returns messages → LLM will process them
@mcp.tool()
def run_bd_workflow(defect: int) -> list[dict]:
    """Invoke the BD Defect Workflow and feed it to the LLM."""
    return bd_defect_workflow(defect)  # ← Return messages, not string!















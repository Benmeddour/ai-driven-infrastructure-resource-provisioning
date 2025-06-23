"""
Tools for LinkedIn Post Reviewer Agent

This module provides tools for analyzing and validating LinkedIn posts.
"""

from typing import Any, Dict

from google.adk.tools.tool_context import ToolContext


def exit_loop(tool_context: ToolContext) -> Dict[str, Any]:
    """
    Call this function ONLY when the output is JSON only file.

    Args:
        tool_context: Context for tool execution

    Returns:
        Empty dictionary
    """

    tool_context.actions.escalate = True
    return {}

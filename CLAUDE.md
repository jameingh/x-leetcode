# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a systematic LeetCode algorithm training repository focused on Python implementations. It emphasizes **mental models** and **brain simulation** over rote memorization, teaching users "how to think" rather than just "what to code."

## Core Philosophy

- **拒绝直接交付**: Never provide complete code solutions directly. Guide users through thinking processes using questions and logical deductions.
- **思维优先**: Focus on mental models (e.g., "boundary收缩" for two pointers, "两墙挤压" for binary search, "部门分身术" for recursion).
- **第一性原理**: Analyze from fundamental properties of data structures and algorithms.
- **大脑模拟**: Always provide step-by-step mental simulations that can "run in the brain" before coding.

## Repository Structure

```
/
├── AGENTS.md          # AI collaboration rules (MUST READ first)
├── walkthrough.md     # Learning progress tracker with milestones
├── learning/          # Algorithm learning materials
│   ├── syllabus.md    # Curriculum with links to all topics
│   ├── README.md      # Learning roadmap and cognitive upgrade path
│   ├── stage1/        # Linear exploration (two_pointers, sliding_window, linked_list)
│   ├── stage2/        # Recursion & search (binary_search, binary_tree, BST, BFS)
│   └── stage3/        # State & decision (backtracking, DP)
└── solutions/         # Python solution files (mirror learning/ structure)
    ├── stage1/
    ├── stage2/
    └── stage3/
```

## Running Code

Solutions are self-contained Python files with test cases:

```bash
# Run a specific solution
python solutions/stage1/two_pointers/two_sum_ii_167.py

# Run current file (VS Code debug configuration available)
# Use launch.json configuration "Python Debugger: Current File"
```

## Verification

To verify work is complete:
- **Code changes**: Run the solution file — all test cases in `if __name__ == "__main__":` must pass
- **Documentation sync**: When a milestone is reached, verify all 3 locations updated (walkthrough.md, learning/syllabus.md, learning/README.md)

## Code Patterns

### Solution File Template
All solution files follow this structure:
1. Docstring with problem number and title (in Chinese)
2. Mental model explanation (🧠 emoji section)
3. Guided thinking questions (not direct answers)
4. Solution implementation
5. `if __name__ == "__main__":` block with test cases and expected outputs

### TreeNode Definition (for tree problems)
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):  # Custom tree visualization
        ...
```

## Documentation Sync Requirements

When a learning milestone is reached, you MUST update three locations simultaneously:

1. **walkthrough.md**: Add milestone marker (e.g., "大圆满 🎉") and mental model沉淀
2. **learning/syllabus.md**: Mark topic status and ensure links are valid
3. **learning/README.md**: Update directory structure and cognitive upgrade roadmap

**Content Conservation Rule**: Use incremental edits. Never overwrite existing "行动指南", "里程碑战果", or "核心思维沉淀" sections.

## Terminology Standards

- **排序方向**: Always specify ascending (升序/从小到大) when describing sorted arrays
- **复杂度**: Use Chinese descriptions (e.g., "线性复杂度") instead of LaTeX ($O(N)$)
- **初始化**: Always specify algorithm starting points explicitly
- **去数学化**: Avoid mixing LaTeX symbols in guidance documents

## Proactive Templating

After confirming a mental model with the user, proactively create solution files in `solutions/` with:
- Class and method definitions
- Problem description in docstring
- Guided comments for the mental model
- Basic test cases in `if __name__ == "__main__":`

This allows users to focus only on implementing the core logic.

## AI Skill Integration

This project uses the agent skills ecosystem:
- Skills are managed via `npx skills` CLI
- Installed skills are tracked in `skills-lock.json`
- Custom skill definitions are in `.agents/skills/`

## Programming Language

- **Python 3** exclusively
- Type hints encouraged (`from typing import List, Optional`)
- Chinese comments for educational explanations
- Pythonic idioms (e.g., `root.left, root.right = root.right, root.left` for tree swaps)

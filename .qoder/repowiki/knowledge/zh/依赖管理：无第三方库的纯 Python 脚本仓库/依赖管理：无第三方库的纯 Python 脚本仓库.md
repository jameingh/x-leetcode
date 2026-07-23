---
kind: dependency_management
name: 依赖管理：无第三方库的纯 Python 脚本仓库
category: dependency_management
scope:
    - '**'
source_files:
    - skills-lock.json
---

本仓库是一个以 Python 3 编写的 LeetCode 算法训练项目，所有题解均为自包含的独立脚本文件（`solutions/stage*/**/*.py`），仅使用 Python 标准库（如 `typing`、`collections` 等），未引入任何第三方包。因此仓库中不存在传统意义上的依赖声明与版本锁定机制：没有 `requirements.txt`、`pyproject.toml`、`setup.py`、`go.mod`、`package.json`、`Cargo.toml` 或任何 lockfile。代码通过 `python <file>` 直接运行，每个文件自带 `if __name__ == "__main__":` 测试块用于验证。

唯一涉及“依赖”的文件是 `skills-lock.json`，它由 `npx skills` CLI 生成，用于锁定从 GitHub 拉取的 AI agent skills（如 `vercel-labs/skills/find-skills`）的版本哈希，属于多端 AI 助手技能生态的依赖锁定，而非编程语言层面的第三方库管理。该锁文件位于仓库根目录，随 Git 提交，确保不同环境安装的技能来源与计算哈希一致。

总结：本项目在语言运行时层面不管理第三方依赖；仅在 AI 技能层通过 `skills-lock.json` 对远程 skill 源做版本锁定。
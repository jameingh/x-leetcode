---
kind: configuration_system
name: AI 助手 Skills 与本地配置（无应用级运行时配置系统）
category: configuration_system
scope:
    - '**'
source_files:
    - .claude/settings.local.json
    - .gemini/skills/continuous-learning/config.json
    - .gemini/skills/continuous-learning/evaluate-session.sh
    - skills-lock.json
---

本仓库是一个以 Python 题解和 Markdown 笔记为主的算法训练集合，**不存在统一的运行时配置系统**（没有 `config/` 目录、没有 `.env`、没有 YAML/TOML 配置文件、也没有任何代码中调用 `os.environ` / `dotenv` / `pydantic-settings` 等加载逻辑）。所有“配置”仅围绕三个 AI 编程助手的本地 Skills 机制展开：

1. **Claude Code 权限白名单** — `.claude/settings.local.json`：通过 JSON 声明允许执行的 Bash 命令、WebSearch 以及可读取的本地路径，用于限制 Claude Agent 在本仓库中的能力范围。
2. **Gemini CLI 持续学习技能配置** — `.gemini/skills/continuous-learning/config.json`：定义会话长度阈值、提取策略、自动审批开关、已学技能落盘路径以及要检测/忽略的模式列表；`evaluate-session.sh` 在会话结束时用 `jq` 解析该文件并触发持续学习钩子。
3. **Skills 锁定清单** — `skills-lock.json`：记录从 GitHub 拉取的第三方 skills 源及其计算哈希，保证多端复现一致性。

这些配置均为**开发期/工具期**静态 JSON，不涉及应用运行时的环境变量注入、多环境覆盖或密钥管理。若未来引入后端服务或可执行脚本，建议新增 `config/` 目录并使用统一格式（如 TOML + pydantic-settings），将上述分散的 JSON 迁移至同一体系。
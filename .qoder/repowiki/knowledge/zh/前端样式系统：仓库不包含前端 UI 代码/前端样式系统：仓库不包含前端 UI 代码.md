---
kind: frontend_style
name: 前端样式系统：仓库不包含前端 UI 代码
category: frontend_style
scope:
    - '**'
---

本仓库是一个 LeetCode 算法训练与学习笔记集合，核心内容全部由 Python 题解（solutions/）和 Markdown 学习文档（learning/）组成，并辅以多 Agent 平台的 skills 配置。经全仓检索，未发现任何 CSS、SCSS、Tailwind 配置文件、HTML 模板或前端组件库引用；`style` 关键字仅出现在 Mermaid 流程图内联样式中（如 `fill:#f9f,stroke:#333`），属于图表渲染语法而非前端样式体系。因此，该仓库不存在前端样式层面的架构、设计令牌或视觉一致性规范，`frontend_style` 类别不适用于本项目。
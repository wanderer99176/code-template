# 架构决策记录 (Architecture Decision Records)

本目录包含了项目的所有重要架构决策记录 (ADR)。

## 什么是 ADR？

架构决策记录 (Architecture Decision Record, ADR) 是一种记录软件架构决策的轻量级文档方法。每个 ADR 记录了：

- **上下文**: 为什么需要做出这个决策？
- **决策**: 我们决定做什么？
- **备选方案**: 我们考虑过哪些其他选项？
- **后果**: 这个决策会带来什么影响？

## 为什么使用 ADR？

1. **知识传承**: 记录决策的理由，帮助新成员理解系统
2. **决策透明**: 让所有人了解架构选择的原因
3. **避免重复讨论**: 记录已经做出的决策和理由
4. **历史追溯**: 了解架构演进的过程

## ADR 列表

| 编号 | 标题 | 状态 | 日期 |
|------|------|------|------|
| [001](001-monorepo-architecture.md) | Monorepo 架构决策 | 已接受 | 2025-10-10 |

## ADR 状态

- **草案** (Draft): 正在讨论中
- **建议** (Proposed): 已提出，等待批准
- **已接受** (Accepted): 已批准并实施
- **已废弃** (Deprecated): 不再推荐使用
- **已替代** (Superseded): 被新的 ADR 替代

## 如何创建新的 ADR

1. 复制 ADR 模板
2. 填写所有部分
3. 提交 PR 并请求审查
4. 批准后合并

### ADR 模板

```markdown
# ADR XXX: [标题]

**状态**: [草案/建议/已接受/已废弃/已替代]  
**日期**: YYYY-MM-DD  
**决策者**: [姓名]

## 上下文

描述问题和背景。

## 决策

我们决定...

## 备选方案

我们考虑过：

### 方案 A
### 方案 B

## 理由

我们选择当前方案的理由...

## 后果

### 正面影响
### 负面影响

## 参考资料

- [链接1]
- [链接2]
```

## 相关资源

- [ADR GitHub 组织](https://adr.github.io/)
- [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
- [ADR Tools](https://github.com/npryce/adr-tools)


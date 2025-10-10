# 贡献指南

感谢您考虑为 {{ cookiecutter.project_name }} 做贡献！

## 开发流程

1. **Fork 本仓库**

2. **克隆您的 Fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/{{ cookiecutter.project_slug }}.git
   cd {{ cookiecutter.project_slug }}
   ```

3. **创建功能分支**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **安装依赖**
   ```bash
   pnpm install
   ```

5. **设置 pre-commit**
   ```bash
   pre-commit install
   ```

6. **进行更改**
   - 编写清晰、简洁的代码
   - 添加或更新测试
   - 添加或更新文档
   - 确保所有测试通过

7. **运行测试和检查**
   ```bash
   # 运行所有测试
   pnpm test
   
   # 运行代码检查
   pnpm lint
   
   # 运行类型检查
   pnpm typecheck
   ```

8. **提交更改**
   ```bash
   git add .
   git commit -m "feat: 添加新功能"
   ```
   
   提交信息格式请遵循 [Conventional Commits](https://www.conventionalcommits.org/)：
   - `feat:` 新功能
   - `fix:` 修复 bug
   - `docs:` 文档更新
   - `style:` 代码格式（不影响代码运行的变动）
   - `refactor:` 重构（既不是新增功能，也不是修复bug）
   - `perf:` 性能优化
   - `test:` 增加测试
   - `chore:` 构建过程或辅助工具的变动

9. **推送到您的 Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

10. **创建 Pull Request**
    - 在 GitHub 上创建 PR
    - 填写 PR 模板
    - 等待代码审查

## 代码规范

### Python 代码
- 使用 `ruff` 进行代码检查和格式化
- 遵循 PEP 8 规范
- 添加类型注解
- 编写 docstring（使用 Google 风格）

```python
def calculate_total(items: list[Item], discount: float = 0.0) -> Decimal:
    """计算订单总价。

    Args:
        items: 订单项列表
        discount: 折扣率，范围 0.0-1.0

    Returns:
        计算后的总价

    Raises:
        ValueError: 如果折扣率不在有效范围内
    """
    if not 0.0 <= discount <= 1.0:
        raise ValueError("折扣率必须在 0.0 到 1.0 之间")
    
    subtotal = sum(item.price * item.quantity for item in items)
    return subtotal * (1 - discount)
```

### TypeScript/JavaScript 代码
- 使用 ESLint 和 Prettier 进行代码检查和格式化
- 优先使用 TypeScript
- 使用 Composition API（Vue 3）
- 编写 JSDoc 注释

```typescript
/**
 * 计算订单总价
 * @param items - 订单项列表
 * @param discount - 折扣率（0-1）
 * @returns 计算后的总价
 */
export function calculateTotal(items: Item[], discount = 0): number {
  if (discount < 0 || discount > 1) {
    throw new Error('折扣率必须在 0 到 1 之间')
  }
  
  const subtotal = items.reduce((sum, item) => sum + item.price * item.quantity, 0)
  return subtotal * (1 - discount)
}
```

## 测试要求

### Python 测试
使用 pytest 编写测试：

```python
import pytest
from decimal import Decimal
from myapp.models import Item
from myapp.services import calculate_total


def test_calculate_total_without_discount():
    """测试无折扣的总价计算"""
    items = [
        Item(name="商品A", price=Decimal("10.00"), quantity=2),
        Item(name="商品B", price=Decimal("5.00"), quantity=3),
    ]
    total = calculate_total(items)
    assert total == Decimal("35.00")


def test_calculate_total_with_discount():
    """测试带折扣的总价计算"""
    items = [Item(name="商品A", price=Decimal("100.00"), quantity=1)]
    total = calculate_total(items, discount=0.2)
    assert total == Decimal("80.00")


def test_calculate_total_invalid_discount():
    """测试无效的折扣率"""
    items = [Item(name="商品A", price=Decimal("10.00"), quantity=1)]
    with pytest.raises(ValueError):
        calculate_total(items, discount=1.5)
```

### TypeScript 测试
使用 Vitest 编写单元测试：

```typescript
import { describe, it, expect } from 'vitest'
import { calculateTotal } from './orders'

describe('calculateTotal', () => {
  it('计算无折扣的总价', () => {
    const items = [
      { name: '商品A', price: 10, quantity: 2 },
      { name: '商品B', price: 5, quantity: 3 },
    ]
    expect(calculateTotal(items)).toBe(35)
  })

  it('计算带折扣的总价', () => {
    const items = [{ name: '商品A', price: 100, quantity: 1 }]
    expect(calculateTotal(items, 0.2)).toBe(80)
  })

  it('抛出无效折扣率错误', () => {
    const items = [{ name: '商品A', price: 10, quantity: 1 }]
    expect(() => calculateTotal(items, 1.5)).toThrow()
  })
})
```

## 文档

- 更新相关的 README
- 为新功能添加使用示例
- 更新 API 文档
- 如果有重大架构决策，添加 ADR (Architecture Decision Record)

## Pull Request 指南

### PR 标题
使用清晰、描述性的标题：
- ✅ `feat(backend): 添加用户认证功能`
- ✅ `fix(frontend): 修复登录页面样式问题`
- ❌ `update code`
- ❌ `bug fix`

### PR 描述
包含以下内容：

```markdown
## 描述
简要描述此 PR 的目的和实现方法

## 类型
- [ ] 新功能
- [ ] Bug 修复
- [ ] 文档更新
- [ ] 性能优化
- [ ] 重构
- [ ] 其他

## 变更内容
- 添加了 XXX 功能
- 修复了 YYY 问题
- 优化了 ZZZ 性能

## 测试
- [ ] 单元测试
- [ ] 集成测试
- [ ] E2E 测试
- [ ] 手动测试

## 截图（如适用）

## 相关 Issue
Closes #123
```

### 代码审查
- 所有 PR 需要至少一个审查者批准
- 解决所有审查意见
- 确保 CI 检查全部通过

## 报告 Bug

使用 GitHub Issues 报告 bug，包含：

1. **bug 描述**：清晰简洁的描述
2. **重现步骤**：详细的重现步骤
3. **期望行为**：期望发生什么
4. **实际行为**：实际发生了什么
5. **环境信息**：
   - OS 版本
   - Python/Node.js 版本
   - 浏览器版本（如适用）
6. **截图**：如果适用
7. **额外信息**：日志、错误信息等

## 功能请求

使用 GitHub Issues 提交功能请求，包含：

1. **功能描述**：清晰描述想要的功能
2. **使用场景**：为什么需要这个功能
3. **建议实现**：如果有想法，描述如何实现
4. **替代方案**：考虑过的其他方案

## 社区准则

- 尊重所有贡献者
- 使用友好、包容的语言
- 接受建设性的批评
- 专注于对社区最有利的事情

## 问题？

如有任何问题，请：
- 查看[文档](docs/)
- 搜索现有的 Issues
- 在 Discussions 中提问
- 发送邮件至 {{ cookiecutter.author_email }}

再次感谢您的贡献！🎉


# 模板重命名指南

本文档说明如何将模板从旧命名方式迁移到新的语义化命名。

## 📋 命名变更对照表

| 旧名称 | 新名称 | 说明 |
|:---|:---|:---|
| `wanderer99176-py-template-01-mvp` | `py-starter-minimal` | 极简版 - 快速原型 |
| `wanderer99176-py-template-02-small` | `py-starter-cli` | CLI版 - 命令行工具 |
| `wanderer99176-py-template-03-medium` | `py-starter-api` | API版 - Web服务 |
| `wanderer99176-py-template-05-enterprise` | `py-starter-enterprise` | 企业版 - 大型项目 |
| `wanderer99176-py-template-06-project01` | `py-starter-monorepo-ai` | Monorepo版 - 全栈AI |

## 🚀 执行重命名

### 方法 1: 使用自动化脚本（推荐）

#### 在 Git Bash / Linux / macOS:

```bash
# 进入模板目录
cd "d:/code template"

# 运行 Bash 脚本
bash rename-templates.sh
```

#### 在 Windows PowerShell:

```powershell
# 进入模板目录
cd "d:\code template"

# 运行 PowerShell 脚本
.\rename-templates.ps1
```

### 方法 2: 手动重命名

如果您喜欢手动操作，可以使用以下命令：

#### Git Bash:

```bash
cd "d:/code template"

# 重命名所有模板
mv wanderer99176-py-template-01-mvp py-starter-minimal
mv wanderer99176-py-template-02-small py-starter-cli
mv wanderer99176-py-template-03-medium py-starter-api
mv wanderer99176-py-template-05-enterprise py-starter-enterprise
mv wanderer99176-py-template-06-project01 py-starter-monorepo-ai

# 验证结果
ls -la
```

#### Windows PowerShell:

```powershell
cd "d:\code template"

# 重命名所有模板
Rename-Item -Path "wanderer99176-py-template-01-mvp" -NewName "py-starter-minimal"
Rename-Item -Path "wanderer99176-py-template-02-small" -NewName "py-starter-cli"
Rename-Item -Path "wanderer99176-py-template-03-medium" -NewName "py-starter-api"
Rename-Item -Path "wanderer99176-py-template-05-enterprise" -NewName "py-starter-enterprise"
Rename-Item -Path "wanderer99176-py-template-06-project01" -NewName "py-starter-monorepo-ai"

# 验证结果
Get-ChildItem
```

#### Windows CMD:

```cmd
cd "d:\code template"

# 重命名所有模板
ren "wanderer99176-py-template-01-mvp" "py-starter-minimal"
ren "wanderer99176-py-template-02-small" "py-starter-cli"
ren "wanderer99176-py-template-03-medium" "py-starter-api"
ren "wanderer99176-py-template-05-enterprise" "py-starter-enterprise"
ren "wanderer99176-py-template-06-project01" "py-starter-monorepo-ai"

# 验证结果
dir
```

## ✅ 验证重命名

重命名完成后，您应该看到以下目录结构：

```
d:\code template\
├── py-starter-minimal/
├── py-starter-cli/
├── py-starter-api/
├── py-starter-enterprise/
├── py-starter-monorepo-ai/
├── README.md (已更新)
├── rename-templates.sh
├── rename-templates.ps1
└── RENAMING-GUIDE.md (本文件)
```

## 📝 更新 Git 仓库

重命名完成后，提交更改到 Git：

```bash
# 添加所有更改
git add .

# 提交更改
git commit -m "refactor: rename templates to semantic names

- wanderer99176-py-template-01-mvp → py-starter-minimal
- wanderer99176-py-template-02-small → py-starter-cli
- wanderer99176-py-template-03-medium → py-starter-api
- wanderer99176-py-template-05-enterprise → py-starter-enterprise
- wanderer99176-py-template-06-project01 → py-starter-monorepo-ai

Updated README.md with new naming convention."

# 推送到远程仓库
git push
```

## 🔄 更新使用命令

重命名后，使用新的命令创建项目：

### 旧命令（不再使用）:
```bash
❌ cookiecutter gh:wanderer99176/code-template --directory wanderer99176-py-template-01-mvp
```

### 新命令（推荐使用）:
```bash
✅ cookiecutter gh:wanderer99176/code-template --directory py-starter-minimal
```

## 📚 已更新的文档

以下文档已经更新为新命名：

- ✅ `README.md` - 根目录说明文件
- ✅ 所有模板的使用示例
- ✅ 命令行示例
- ✅ 功能对比表格

## ⚠️ 注意事项

1. **向后兼容性**: 如果您已经有使用旧名称创建的项目，它们不受影响，仍然可以正常工作。

2. **文档同步**: 确保您的所有文档、Wiki、博客文章等都更新为新的命名。

3. **分支和标签**: 如果您在 Git 中有包含旧名称的分支或标签，建议保持不变，避免混淆历史记录。

4. **本地缓存**: Cookiecutter 可能缓存了旧名称，清理方法：
   ```bash
   # 清理 cookiecutter 缓存
   rm -rf ~/.cookiecutters/code-template  # Linux/macOS
   # 或
   Remove-Item -Recurse -Force "$env:USERPROFILE\.cookiecutters\code-template"  # Windows
   ```

## 🎯 命名原则

新命名遵循以下原则：

1. **简洁明了**: `py-starter-minimal` 比 `wanderer99176-py-template-01-mvp` 更直观
2. **语义化**: 名称直接表达用途（minimal, cli, api, enterprise, monorepo-ai）
3. **一致性**: 统一使用 `py-starter-*` 前缀
4. **可扩展性**: 便于未来添加新的启动器

## ❓ 常见问题

**Q: 为什么要重命名？**  
A: 旧名称包含版本号（01, 02, 03, 05, 06）容易混淆，新名称更加语义化和易记。

**Q: 旧项目会受影响吗？**  
A: 不会。已创建的项目完全独立，不受模板重命名影响。

**Q: GitHub 上的链接会失效吗？**  
A: 如果您使用了 `--directory` 参数，需要更新为新名称。建议在 README 中提供迁移指南。

**Q: 我可以自定义命名吗？**  
A: 当然可以！这是您的仓库，可以根据需求自由命名。

## 📞 需要帮助？

如果遇到问题，请：
1. 查看本文档
2. 检查 Git 状态: `git status`
3. 提交 Issue 或联系维护者

---

**祝重命名顺利！🎉**


# 模板重命名脚本 (PowerShell)
# 将旧的命名方式改为新的语义化命名

Write-Host "========================================" -ForegroundColor Blue
Write-Host "  Python Starter Templates 重命名工具" -ForegroundColor Blue
Write-Host "========================================" -ForegroundColor Blue
Write-Host ""

# 定义重命名映射
$renameMap = @{
    "wanderer99176-py-template-01-mvp" = "py-starter-minimal"
    "wanderer99176-py-template-02-small" = "py-starter-cli"
    "wanderer99176-py-template-03-medium" = "py-starter-api"
    "wanderer99176-py-template-05-enterprise" = "py-starter-enterprise"
    "wanderer99176-py-template-06-project01" = "py-starter-monorepo-ai"
}

# 获取当前目录
$currentDir = Get-Location
Write-Host "当前目录: $currentDir" -ForegroundColor Yellow
Write-Host ""
Write-Host "即将执行以下重命名操作:" -ForegroundColor Yellow
Write-Host ""

# 显示重命名计划
foreach ($oldName in $renameMap.Keys) {
    $newName = $renameMap[$oldName]
    if (Test-Path $oldName) {
        Write-Host "  ✓ $oldName → $newName" -ForegroundColor Green
    } else {
        Write-Host "  ⚠ $oldName (不存在，跳过)" -ForegroundColor Yellow
    }
}

Write-Host ""
$confirmation = Read-Host "是否继续？[y/N]"

if ($confirmation -ne 'y' -and $confirmation -ne 'Y') {
    Write-Host "操作已取消" -ForegroundColor Yellow
    exit
}

Write-Host ""
Write-Host "开始重命名..." -ForegroundColor Blue
Write-Host ""

# 执行重命名
$successCount = 0
$skipCount = 0

foreach ($oldName in $renameMap.Keys) {
    $newName = $renameMap[$oldName]
    
    if (Test-Path $oldName) {
        Write-Host "重命名: $oldName → $newName" -ForegroundColor Blue
        Rename-Item -Path $oldName -NewName $newName
        $successCount++
        Write-Host "✓ 完成" -ForegroundColor Green
    } else {
        Write-Host "⚠ 跳过: $oldName (目录不存在)" -ForegroundColor Yellow
        $skipCount++
    }
    Write-Host ""
}

Write-Host "========================================" -ForegroundColor Blue
Write-Host "✓ 重命名完成！" -ForegroundColor Green
Write-Host ""
Write-Host "  成功: $successCount 个" -ForegroundColor Green
Write-Host "  跳过: $skipCount 个" -ForegroundColor Yellow
Write-Host ""
Write-Host "下一步:" -ForegroundColor Blue
Write-Host "  1. 检查重命名结果: " -NoNewline; Write-Host "ls" -ForegroundColor Yellow
Write-Host "  2. 更新 Git 仓库: " -NoNewline; Write-Host "git add . && git commit -m 'refactor: rename templates to semantic names'" -ForegroundColor Yellow
Write-Host "  3. 推送到远程: " -NoNewline; Write-Host "git push" -ForegroundColor Yellow
Write-Host ""
Write-Host "========================================" -ForegroundColor Blue


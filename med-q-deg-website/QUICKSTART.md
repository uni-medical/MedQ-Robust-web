# 🚀 快速启动指南

MedQ-Deg 医学图像退化基准测试网站

## 📦 1. 安装依赖（首次使用）

```bash
cd med-q-deg-website
npm install
```

## 🔥 2. 启动开发服务器

```bash
npm run dev
```

访问 http://localhost:4321 查看网站

## 📝 3. 替换数据（重要！）

### 快速替换清单

#### ✅ 步骤 1：更新配置
编辑 `src/data/config.ts`：
```javascript
export const SITE_CONFIG = {
  // 更新这些链接
  links: {
    paper: 'https://arxiv.org/abs/YOUR_PAPER',
    github: 'https://github.com/YOUR_USERNAME/YOUR_REPO',
    dataset: 'https://YOUR_DATASET_LINK',
  },
  // 更新作者和机构
  authors: ['Your Name', 'Co-author Name'],
  affiliation: 'Your Institution',
};
```

#### ✅ 步骤 2：准备图片
将论文中的示例图片放入：
```
public/images/degradations/
```

命名建议：`{type}_{severity}_{number}.jpg`

#### ✅ 步骤 3：创建数据文件

创建 4 个 JSON 文件在 `public/data/` 目录：

**a) degradation-examples.json**
```json
[
  {
    "id": "example-001",
    "type": "gaussian_blur",
    "category": "blur",
    "severity": "mild",
    "imagePath": "/images/degradations/your_image.jpg",
    "modality": "MRI"
  }
]
```

**b) performance.json**
```json
[
  {
    "method": "DPL (Ours)",
    "accuracy": 87.3,
    "f1Score": 85.6,
    "auroc": 92.1
  }
]
```

**c) confusion-matrix.json**
```json
[
  [89, 3, 2, 4, 1, 1],
  [2, 92, 1, 2, 2, 1],
  ...
]
```

**d) tsne.json**
```json
[
  {
    "x": 145.32,
    "y": -78.91,
    "category": "Blur",
    "type": "gaussian_blur"
  }
]
```

📖 详细格式说明：查看 `DATA_REPLACEMENT_GUIDE.md`

## 🏗️ 4. 构建和预览

```bash
# 构建生产版本
npm run build

# 预览构建结果
npm run preview
```

## 🚀 5. 部署到 GitHub Pages

### 步骤 1：创建 GitHub 仓库
在 GitHub 上创建新仓库

### 步骤 2：更新部署配置
编辑 `astro.config.mjs`：
```javascript
export default defineConfig({
  site: 'https://YOUR_USERNAME.github.io',
  base: '/YOUR_REPO_NAME/',
  // ...
});
```

### 步骤 3：推送代码
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### 步骤 4：启用 GitHub Pages
1. 进入仓库 → Settings → Pages
2. Source 选择：**GitHub Actions**
3. 等待部署完成（约 2-3 分钟）

✅ 完成！访问 `https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/`

## 📊 Python 数据转换示例

### 从论文数据生成 JSON

```python
import json
import numpy as np

# 示例：生成 performance.json
performance_data = [
    {"method": "DPL (Ours)", "accuracy": 87.3, "f1Score": 85.6, "auroc": 92.1},
    {"method": "CLIP", "accuracy": 74.9, "f1Score": 74.8, "auroc": 76.9},
]

with open('public/data/performance.json', 'w') as f:
    json.dump(performance_data, f, indent=2)

# 示例：从混淆矩阵生成 JSON
confusion_matrix = np.array([
    [89, 3, 2, 4, 1, 1],
    [2, 92, 1, 2, 2, 1],
    # ... 6x6 矩阵
])

with open('public/data/confusion-matrix.json', 'w') as f:
    json.dump(confusion_matrix.tolist(), f, indent=2)
```

## 🔍 常见问题

### Q: 图片不显示？
**A:** 确保图片在 `public/` 目录下，路径以 `/` 开头

### Q: 数据没有更新？
**A:** 清除浏览器缓存，或重启开发服务器

### Q: 部署失败？
**A:** 检查 GitHub Actions 日志，确认 `astro.config.mjs` 配置正确

### Q: 如何修改颜色？
**A:** 编辑 `tailwind.config.mjs` 中的 `colors` 配置

## 📁 重要文件位置

```
配置文件：   src/data/config.ts
数据文件：   public/data/*.json
图片目录：   public/images/
样式文件：   src/styles/global.css
部署配置：   .github/workflows/deploy.yml
```

## ⚡ 常用命令速查

| 命令 | 说明 |
|------|------|
| `npm run dev` | 启动开发服务器 |
| `npm run build` | 构建生产版本 |
| `npm run preview` | 预览构建结果 |

## 🎯 完成检查清单

- [ ] 安装依赖
- [ ] 启动开发服务器
- [ ] 更新 config.ts 配置
- [ ] 准备示例图片
- [ ] 创建 4 个 JSON 数据文件
- [ ] 本地测试所有页面
- [ ] 更新 astro.config.mjs
- [ ] 推送到 GitHub
- [ ] 启用 GitHub Pages
- [ ] 验证部署成功

## 📚 更多文档

- **完整项目说明**：`README.md`
- **数据替换详解**：`DATA_REPLACEMENT_GUIDE.md`
- **项目总结**：`PROJECT_SUMMARY.md`

---

**准备好了吗？** 现在就开始替换数据，让你的研究成果在线展示！🚀

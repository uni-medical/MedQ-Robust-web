# 📌 下一步操作指南

恭喜！MedQ-Deg 网站框架已经完成。以下是接下来需要完成的步骤。

---

## 🎯 立即可做的事情

### 1️⃣ 快速测试 (5 分钟)

```bash
# 进入项目目录
cd /Users/junzhin/coding_files/playgrounds/med_roubst

# 安装依赖 (首次运行)
npm install

# 启动开发服务器
npm run dev
```

然后访问 http://localhost:4321 查看网站效果。

你会看到:
- ✅ 完整的 4 个页面
- ✅ 示例数据和占位符
- ✅ 所有可视化组件
- ✅ 交互式功能

---

## 📊 数据替换流程 (1-2 天)

### 准备工作

#### 步骤 1: 安装 Python 依赖

```bash
pip install pandas scikit-learn numpy Pillow
```

#### 步骤 2: 从论文提取数据

你需要准备以下数据:

1. **退化示例数据**
   - 图片文件
   - 对应的标签 (类型, 严重程度, 模态)

2. **性能对比数据**
   - 方法名称
   - 准确率, F1分数, AUROC

3. **混淆矩阵**
   - 真实标签
   - 预测标签

4. **t-SNE 数据**
   - 特征向量
   - 类别标签

#### 步骤 3: 生成 JSON 文件

**方法 A: 使用提供的脚本**

```python
from scripts.generate_data import *

# 1. 从 CSV 生成示例
generate_degradation_examples('your_data.csv')

# 2. 生成性能数据
metrics = {
    "DPL (Ours)": {"accuracy": 87.3, "f1Score": 85.6, "auroc": 92.1},
    "CLIP": {"accuracy": 74.9, "f1Score": 74.8, "auroc": 76.9},
}
generate_performance_data(metrics)

# 3. 生成混淆矩阵
generate_confusion_matrix(y_true, y_pred)

# 4. 生成 t-SNE
generate_tsne_visualization(features, labels, types)
```

**方法 B: 手动创建 JSON**

参考 `DATA_REPLACEMENT_GUIDE.md` 中的格式说明。

#### 步骤 4: 处理图片

```bash
# 批量压缩图片
python scripts/process_images.py compress \
    /path/to/original/images/ \
    public/images/degradations/ \
    --max-size 800 \
    --quality 85

# 批量重命名
python scripts/process_images.py rename \
    public/images/degradations/ \
    --prefix gaussian_blur_mild_ \
    --start 1
```

---

## 🔧 配置更新 (30 分钟)

### 更新 `src/data/config.ts`

```typescript
export const SITE_CONFIG = {
  // 更新链接
  links: {
    paper: 'https://arxiv.org/abs/YOUR_PAPER',  // 你的论文链接
    github: 'https://github.com/YOUR_REPO',      // 你的 GitHub 仓库
    dataset: 'https://YOUR_DATASET_LINK',        // 数据集链接
  },

  // 更新作者
  authors: ['你的名字', '合作者名字'],
  affiliation: '你的机构',

  // 更新统计数据 (如有变化)
  stats: {
    categories: 6,
    types: 28,
    datasets: 4,
    modalities: ['MRI', 'CT', 'X-Ray', 'Ultrasound'],
  },
};
```

### 更新 `astro.config.mjs` (部署前)

```javascript
export default defineConfig({
  site: 'https://YOUR_USERNAME.github.io',
  base: '/YOUR_REPO_NAME/',  // 注意前后的斜杠
  // ...
});
```

---

## 🧪 本地测试 (1 小时)

### 测试清单

```bash
# 1. 开发模式测试
npm run dev
```

访问并测试:
- [ ] 首页 (/)
- [ ] 基准测试 (/benchmark)
- [ ] 示例展示 (/examples)
- [ ] 结果可视化 (/results)

检查:
- [ ] 所有数据正确显示
- [ ] 图片正常加载
- [ ] 交互功能正常
- [ ] 移动端显示正常

```bash
# 2. 生产模式测试
npm run build
npm run preview
```

再次检查所有功能。

---

## 🚀 部署到 GitHub Pages (30 分钟)

### 步骤 1: 创建 GitHub 仓库

1. 访问 https://github.com/new
2. 仓库名称: `medq-deg-benchmark`
3. 设为 Public
4. 创建仓库

### 步骤 2: 推送代码

```bash
# 初始化 Git (如果还没有)
git init
git add .
git commit -m "Initial commit: MedQ-Deg benchmark website"
git branch -M main

# 添加远程仓库
git remote add origin https://github.com/YOUR_USERNAME/medq-deg-benchmark.git

# 推送
git push -u origin main
```

### 步骤 3: 启用 GitHub Pages

1. 进入仓库 Settings
2. 找到 Pages 选项
3. Source 选择 "GitHub Actions"
4. 等待 2-3 分钟

### 步骤 4: 验证部署

访问: `https://YOUR_USERNAME.github.io/medq-deg-benchmark/`

---

## 📈 后续优化 (可选)

### 短期优化

1. **添加 Google Analytics**
   - 跟踪网站访问
   - 了解用户行为

2. **SEO 优化**
   - 添加 sitemap
   - 优化 meta 标签
   - 提交到搜索引擎

3. **性能优化**
   - 图片懒加载
   - 代码分割
   - CDN 加速

### 长期增强

1. **功能增强**
   - 添加搜索功能
   - 支持中英文切换
   - 添加在线 Demo

2. **内容更新**
   - 定期更新数据
   - 添加博客/新闻
   - 收集用户反馈

---

## 🆘 遇到问题?

### 常见问题

**Q: npm install 很慢?**
```bash
# 使用国内镜像
npm config set registry https://registry.npmmirror.com
npm install
```

**Q: 图片不显示?**
- 检查图片路径是否以 `/` 开头
- 确保图片在 `public/` 目录下

**Q: 部署后 404?**
- 检查 `astro.config.mjs` 中的 `base` 配置
- 确保 GitHub Pages 已启用

**Q: 数据不更新?**
- 清除浏览器缓存
- 重启开发服务器

### 查看文档

- `README.md` - 项目说明
- `QUICKSTART.md` - 快速启动
- `DATA_REPLACEMENT_GUIDE.md` - 数据替换详解
- `DEPLOYMENT.md` - 部署详解
- `COMMANDS.md` - 命令参考
- `CHECKLIST.md` - 完整检查清单

---

## 📅 推荐时间线

### 第 1 天
- [x] 框架已完成 ✅
- [ ] 安装依赖并测试
- [ ] 了解项目结构

### 第 2-3 天
- [ ] 从论文提取数据
- [ ] 生成 JSON 文件
- [ ] 处理图片

### 第 4 天
- [ ] 替换占位符数据
- [ ] 更新配置
- [ ] 本地全面测试

### 第 5 天
- [ ] 创建 GitHub 仓库
- [ ] 部署到 GitHub Pages
- [ ] 验证和优化

### 第 6-7 天 (可选)
- [ ] SEO 优化
- [ ] 性能优化
- [ ] 收集反馈

---

## ✅ 准备好了吗?

现在你可以:

1. **立即测试:** `npm install && npm run dev`
2. **阅读文档:** 查看 `QUICKSTART.md`
3. **准备数据:** 按照 `DATA_REPLACEMENT_GUIDE.md` 操作
4. **开始部署:** 参考 `DEPLOYMENT.md`

---

## 💡 重要提示

### 核心设计理念

这个项目的设计遵循以下原则:

1. **数据驱动** - 修改数据文件即可更新内容
2. **配置优先** - 通过 `config.ts` 控制所有可配置项
3. **工具辅助** - Python 脚本自动化数据处理
4. **文档完善** - 每个步骤都有详细说明

### 你不需要:
- ❌ 修改组件代码
- ❌ 理解 React/Astro 细节
- ❌ 手动处理图片
- ❌ 担心部署配置

### 你只需要:
- ✅ 准备论文数据
- ✅ 运行提供的脚本
- ✅ 更新配置文件
- ✅ 推送到 GitHub

---

## 🎉 开始吧!

```bash
# 第一步: 测试框架
npm install
npm run dev

# 访问 http://localhost:4321
# 看到网站运行，就成功了！
```

**祝你成功！** 如有问题，参考文档或重新运行 Ralph Loop。🚀

---

**项目路径:** `/Users/junzhin/coding_files/playgrounds/med_roubst`
**创建时间:** 2026年1月31日
**状态:** ✅ 框架完成，待数据替换

# ⚡ 快速命令参考

MedQ-Deg 网站开发和部署的所有常用命令。

---

## 🚀 开发命令

### 启动开发服务器
```bash
cd med-q-deg-website
npm run dev
```
访问: http://localhost:4321

### 构建生产版本
```bash
npm run build
```

### 预览生产版本
```bash
npm run preview
```

---

## 📊 数据处理

### 生成占位符数据
```bash
python scripts/generate_data.py --placeholder
```

### 从 CSV 生成示例数据
```python
from scripts.generate_data import generate_degradation_examples
generate_degradation_examples('your_data.csv')
```

### 生成性能数据
```python
from scripts.generate_data import generate_performance_data

metrics = {
    "DPL (Ours)": {"accuracy": 87.3, "f1Score": 85.6, "auroc": 92.1},
    "CLIP": {"accuracy": 74.9, "f1Score": 74.8, "auroc": 76.9},
}
generate_performance_data(metrics)
```

### 生成混淆矩阵
```python
from scripts.generate_data import generate_confusion_matrix
generate_confusion_matrix(y_true, y_pred)
```

### 生成 t-SNE 数据
```python
from scripts.generate_data import generate_tsne_visualization
generate_tsne_visualization(features, labels, types)
```

---

## 🖼️ 图片处理

### 批量压缩图片
```bash
python scripts/process_images.py compress \
    原始图片目录/ \
    public/images/degradations/ \
    --max-size 800 \
    --quality 85
```

### 批量重命名 (预览)
```bash
python scripts/process_images.py rename \
    public/images/degradations/ \
    --prefix gaussian_blur_mild_ \
    --dry-run
```

### 批量重命名 (执行)
```bash
python scripts/process_images.py rename \
    public/images/degradations/ \
    --prefix gaussian_blur_mild_ \
    --start 1
```

### 创建测试图片
```bash
python scripts/process_images.py placeholder \
    --output-dir public/images/degradations \
    --count 20
```

---

## 🔧 Git 操作

### 初始化仓库
```bash
git init
git add .
git commit -m "Initial commit: MedQ-Deg website"
git branch -M main
```

### 添加远程仓库
```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
```

### 推送代码
```bash
git push -u origin main
```

### 更新代码
```bash
git add .
git commit -m "Update data and content"
git push
```

---

## 🚀 部署

### 本地测试部署
```bash
# 构建
npm run build

# 预览
npm run preview
```

### 推送到 GitHub
```bash
git add .
git commit -m "Ready for deployment"
git push
```

GitHub Actions 会自动部署到 GitHub Pages

---

## 🛠️ 依赖管理

### 安装 Node.js 依赖
```bash
npm install
```

### 安装 Python 依赖
```bash
pip install pandas scikit-learn numpy Pillow
```

### 更新依赖
```bash
npm update
```

---

## 📁 文件操作

### 查看项目结构
```bash
tree -L 3 -I 'node_modules|dist'
```

### 检查文件大小
```bash
du -sh public/images/degradations/*
```

### 查找大文件
```bash
find public/images -size +500k
```

---

## 🐛 调试

### 检查构建错误
```bash
npm run build 2>&1 | tee build.log
```

### 检查端口占用
```bash
lsof -ti:4321
```

### 杀死占用端口的进程
```bash
kill -9 $(lsof -ti:4321)
```

### 清除缓存
```bash
rm -rf node_modules/.vite
rm -rf dist
npm run build
```

---

## 📊 数据验证

### 验证 JSON 格式
```bash
# macOS/Linux
python -m json.tool public/data/degradation-examples.json

# 或使用 jq
jq . public/data/performance.json
```

### 检查图片
```bash
# 列出所有图片
ls -lh public/images/degradations/

# 检查图片尺寸
file public/images/degradations/*.jpg
```

---

## 🔍 搜索和查找

### 在代码中搜索
```bash
grep -r "SITE_CONFIG" src/
```

### 查找特定文件
```bash
find . -name "*.astro" -type f
```

### 查找大于指定大小的文件
```bash
find public/images -size +1M
```

---

## 🎨 样式调试

### 查看 Tailwind 配置
```bash
cat tailwind.config.mjs
```

### 重新生成 Tailwind CSS
```bash
npx tailwindcss -i ./src/styles/global.css -o ./dist/output.css --watch
```

---

## 📈 性能分析

### 分析构建大小
```bash
npm run build
du -sh dist/
```

### 查看依赖大小
```bash
npx vite-bundle-visualizer
```

---

## 🔒 安全检查

### 检查依赖漏洞
```bash
npm audit
```

### 修复依赖漏洞
```bash
npm audit fix
```

---

## 📝 常用文件路径

```bash
# 配置文件
src/data/config.ts                  # 核心配置
astro.config.mjs                    # Astro 配置
tailwind.config.mjs                 # Tailwind 配置

# 数据文件
public/data/degradation-examples.json
public/data/performance.json
public/data/confusion-matrix.json
public/data/tsne.json

# 页面文件
src/pages/index.astro               # 首页
src/pages/benchmark.astro           # 基准测试
src/pages/examples.astro            # 示例
src/pages/results.astro             # 结果

# 组件
src/components/visualization/       # 可视化组件
src/components/common/              # 通用组件

# 文档
README.md                           # 项目说明
QUICKSTART.md                       # 快速启动
DATA_REPLACEMENT_GUIDE.md           # 数据替换
DEPLOYMENT.md                       # 部署指南
```

---

## 🎯 一键完成常见任务

### 完整的数据准备流程
```bash
# 1. 生成测试数据
python scripts/generate_data.py --placeholder

# 2. 创建测试图片
python scripts/process_images.py placeholder --count 20

# 3. 启动开发服务器
npm run dev
```

### 完整的部署流程
```bash
# 1. 构建并测试
npm run build
npm run preview

# 2. 提交并推送
git add .
git commit -m "Deploy to production"
git push

# 3. 等待 GitHub Actions 完成
# 访问 https://github.com/YOUR_USERNAME/YOUR_REPO/actions
```

### 批量处理图片
```bash
# 1. 压缩
python scripts/process_images.py compress \
    原始图片/ public/images/degradations/ \
    --max-size 800 --quality 85

# 2. 重命名
python scripts/process_images.py rename \
    public/images/degradations/ \
    --prefix example_ --start 1
```

---

## 💡 提示

### 开发模式热重载
开发服务器会自动重载，无需手动刷新

### 构建前检查
```bash
# 检查 TypeScript 错误
npx tsc --noEmit

# 检查格式
npx prettier --check "src/**/*.{astro,tsx,ts}"
```

### 快速清理
```bash
rm -rf node_modules dist .astro
npm install
```

---

## 📚 帮助命令

### npm 脚本列表
```bash
npm run
```

### Python 脚本帮助
```bash
python scripts/generate_data.py --help
python scripts/process_images.py --help
```

---

**提示:** 将此文件加入书签以快速查找常用命令！

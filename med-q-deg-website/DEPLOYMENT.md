# 🚀 部署到 GitHub Pages 详细指南

完整的部署流程和故障排除指南。

## 📋 前提条件

- [x] GitHub 账号
- [x] 已完成本地测试
- [x] 数据和图片已准备好

---

## 🎯 部署步骤

### 步骤 1: 创建 GitHub 仓库

1. 访问 https://github.com/new
2. 仓库名称: `medq-deg-benchmark` (或你喜欢的名字)
3. 选择 **Public** (GitHub Pages 要求)
4. 不要初始化 README (我们已经有了)
5. 点击 **Create repository**

### 步骤 2: 更新 Astro 配置

编辑 `astro.config.mjs`:

```javascript
export default defineConfig({
  site: 'https://YOUR_USERNAME.github.io',
  base: '/YOUR_REPO_NAME/',  // 如果是 user.github.io 仓库则留空
  integrations: [
    react(),
    tailwind(),
  ],
});
```

**重要提示:**
- 替换 `YOUR_USERNAME` 为你的 GitHub 用户名
- 替换 `YOUR_REPO_NAME` 为你的仓库名
- 如果仓库名是 `username.github.io` 格式，`base` 应该设为 `'/'`

### 步骤 3: 初始化 Git 并推送

```bash
cd med-q-deg-website

# 初始化 Git
git init

# 添加所有文件
git add .

# 创建初始提交
git commit -m "Initial commit: MedQ-Deg benchmark website"

# 设置主分支名
git branch -M main

# 添加远程仓库
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git

# 推送到 GitHub
git push -u origin main
```

### 步骤 4: 启用 GitHub Pages

1. 进入你的 GitHub 仓库
2. 点击 **Settings** (设置)
3. 在左侧菜单找到 **Pages**
4. 在 **Source** 下拉菜单选择: **GitHub Actions**
5. 保存更改

### 步骤 5: 等待部署完成

1. 进入 **Actions** 标签
2. 你会看到一个正在运行的工作流 "Deploy to GitHub Pages"
3. 等待约 2-3 分钟
4. ✅ 看到绿色勾号表示部署成功

### 步骤 6: 访问你的网站

访问: `https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/`

---

## 🔄 更新网站内容

### 更新数据或代码后重新部署

```bash
# 修改文件后
git add .
git commit -m "Update data and content"
git push

# GitHub Actions 会自动重新部署
```

---

## 🛠️ 自定义域名 (可选)

### 使用自定义域名

1. 购买域名 (如 `medqdeg.com`)
2. 在 GitHub Pages 设置中添加自定义域名
3. 配置 DNS 记录:

**A 记录:**
```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

**CNAME 记录:**
```
www -> YOUR_USERNAME.github.io
```

4. 更新 `astro.config.mjs`:

```javascript
export default defineConfig({
  site: 'https://medqdeg.com',  // 你的自定义域名
  base: '/',                     // 自定义域名时设为 /
  // ...
});
```

---

## 🐛 常见问题和解决方案

### Q1: 部署失败 - "Page build failed"

**原因:** 通常是配置错误或构建失败

**解决:**
```bash
# 本地测试构建
npm run build

# 检查错误信息
# 修复后重新推送
git add .
git commit -m "Fix build errors"
git push
```

### Q2: 网站显示 404

**原因:** `base` 配置不正确

**解决:**

检查 `astro.config.mjs`:
```javascript
// 如果 URL 是 user.github.io/repo-name/
base: '/repo-name/',

// 如果 URL 是 user.github.io/ 或自定义域名
base: '/',
```

### Q3: 样式/图片不显示

**原因:** 资源路径不正确

**解决:**

确保所有资源路径都是相对路径或使用 `import.meta.env.BASE_URL`:

```astro
<!-- 正确 -->
<img src="/images/logo.png" />

<!-- 如果需要动态 base -->
<img src={`${import.meta.env.BASE_URL}images/logo.png`} />
```

### Q4: Actions 权限错误

**解决:**

1. 进入仓库 Settings → Actions → General
2. 在 "Workflow permissions" 选择 "Read and write permissions"
3. 保存并重新运行工作流

### Q5: 数据没有更新

**原因:** 浏览器缓存

**解决:**
- 强制刷新: `Cmd + Shift + R` (Mac) 或 `Ctrl + Shift + R` (Windows)
- 或清除浏览器缓存

### Q6: 部署很慢

**原因:** 依赖安装慢

**优化 GitHub Actions:**

编辑 `.github/workflows/deploy.yml`，添加缓存:

```yaml
- name: Setup Node
  uses: actions/setup-node@v3
  with:
    node-version: 18
    cache: 'npm'  # 添加这一行

- name: Install dependencies
  run: npm ci  # 使用 ci 代替 install
```

---

## 📊 性能优化

### 图片优化

```bash
# 压缩所有图片
python scripts/process_images.py compress \
    public/images/degradations/ \
    public/images/degradations/ \
    --max-size 800 \
    --quality 85
```

### 启用 Astro 图片优化

编辑 `astro.config.mjs`:

```javascript
import { defineConfig } from 'astro/config';
import image from '@astrojs/image';

export default defineConfig({
  integrations: [
    react(),
    tailwind(),
    image(),  // 添加图片优化
  ],
});
```

---

## 🔒 安全性

### 环境变量

如果需要 API 密钥等敏感信息:

1. 在 GitHub 仓库中设置 Secrets:
   - Settings → Secrets and variables → Actions
   - 添加新的 secret

2. 在工作流中使用:

```yaml
env:
  API_KEY: ${{ secrets.API_KEY }}
```

3. 在代码中访问:

```javascript
const apiKey = import.meta.env.API_KEY;
```

---

## 📈 监控和分析

### 添加 Google Analytics

在 `src/layouts/Layout.astro` 中添加:

```astro
---
const GA_TRACKING_ID = 'G-XXXXXXXXXX';
---

<head>
  <!-- 其他头部内容 -->

  {GA_TRACKING_ID && (
    <script async src={`https://www.googletagmanager.com/gtag/js?id=${GA_TRACKING_ID}`}></script>
    <script is:inline define:vars={{GA_TRACKING_ID}}>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', GA_TRACKING_ID);
    </script>
  )}
</head>
```

---

## 🎯 部署检查清单

在部署前确保:

- [ ] 本地运行 `npm run build` 无错误
- [ ] 本地运行 `npm run preview` 查看生产版本
- [ ] 更新了 `astro.config.mjs` 中的 `site` 和 `base`
- [ ] 更新了 `src/data/config.ts` 中的链接
- [ ] 所有图片都在 `public/` 目录下
- [ ] 数据文件格式正确
- [ ] GitHub Actions 工作流文件存在
- [ ] 仓库是 public
- [ ] 推送了所有更改

---

## 📚 相关链接

- [Astro 部署文档](https://docs.astro.build/en/guides/deploy/github/)
- [GitHub Pages 文档](https://docs.github.com/en/pages)
- [GitHub Actions 文档](https://docs.github.com/en/actions)

---

## 💡 下一步

部署成功后，你可以:

1. **分享链接** - 在论文中、社交媒体上分享网站
2. **添加徽章** - 在 README 中添加部署状态徽章
3. **设置监控** - 使用 Google Analytics 跟踪访问
4. **持续更新** - 定期更新数据和内容
5. **收集反馈** - 添加反馈表单或 GitHub Discussions

祝部署成功！🎉

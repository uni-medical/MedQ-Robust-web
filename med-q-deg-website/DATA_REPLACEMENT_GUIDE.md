/**
 * Data Replacement Guide
 *
 * This file explains how to replace placeholder data with your actual benchmark data.
 */

# 数据替换指南

## 📋 概述

本网站设计为数据驱动，所有可视化内容都可以通过替换 JSON 文件轻松更新。

## 📁 数据文件位置

所有数据文件应放在 `public/data/` 目录下：

```
public/data/
├── degradation-examples.json  # 退化示例数据
├── performance.json           # 性能对比数据
├── confusion-matrix.json      # 混淆矩阵数据
└── tsne.json                  # t-SNE 可视化数据
```

## 📊 数据格式

### 1. degradation-examples.json

退化类型示例数据：

```json
[
  {
    "id": "example-001",
    "type": "gaussian_blur",
    "category": "blur",
    "severity": "mild",
    "imagePath": "/images/degradations/gaussian_blur_mild_001.jpg",
    "modality": "MRI",
    "description": "T2-weighted MRI with mild Gaussian blur"
  },
  {
    "id": "example-002",
    "type": "gaussian_noise",
    "category": "noise",
    "severity": "severe",
    "imagePath": "/images/degradations/gaussian_noise_severe_002.jpg",
    "modality": "CT",
    "description": "CT scan with severe Gaussian noise"
  }
]
```

**字段说明：**
- `id`: 唯一标识符
- `type`: 退化类型（与 config.ts 中的 DEGRADATION_TYPES 对应）
- `category`: 分类（blur, noise, artifact, contrast, compression, other）
- `severity`: 严重程度（mild, moderate, severe）
- `imagePath`: 图片路径（相对于 public 目录）
- `modality`: 医学成像模态（MRI, CT, X-Ray, Ultrasound）
- `description`: 可选描述

### 2. performance.json

方法性能对比数据：

```json
[
  {
    "method": "DPL (Ours)",
    "accuracy": 87.3,
    "f1Score": 85.6,
    "auroc": 92.1,
    "parameters": "86.2M"
  },
  {
    "method": "CLIP",
    "accuracy": 74.9,
    "f1Score": 74.8,
    "auroc": 76.9,
    "parameters": "151.3M"
  }
]
```

**字段说明：**
- `method`: 方法名称
- `accuracy`: 准确率（0-100）
- `f1Score`: F1 分数（0-100）
- `auroc`: AUROC 值（0-100）
- `parameters`: 参数量（可选）

### 3. confusion-matrix.json

混淆矩阵数据（6x6 矩阵）：

```json
[
  [89, 3, 2, 4, 1, 1],
  [2, 92, 1, 2, 2, 1],
  [3, 2, 85, 6, 2, 2],
  [4, 1, 5, 86, 3, 1],
  [2, 3, 1, 2, 88, 4],
  [5, 2, 4, 3, 4, 82]
]
```

**格式说明：**
- 6x6 数组，对应 6 个类别（Blur, Noise, Artifact, Contrast, Compress, Other）
- 行：实际类别
- 列：预测类别
- 值：百分比（0-100）

### 4. tsne.json

t-SNE 可视化数据：

```json
[
  {
    "x": 145.32,
    "y": -78.91,
    "category": "Blur",
    "type": "gaussian_blur",
    "modality": "MRI"
  },
  {
    "x": -89.45,
    "y": 123.67,
    "category": "Noise",
    "type": "gaussian_noise",
    "modality": "CT"
  }
]
```

**字段说明：**
- `x`, `y`: t-SNE 坐标
- `category`: 分类名称
- `type`: 退化类型
- `modality`: 医学成像模态（可选）

## 🖼️ 图片替换

### 示例图片

将退化示例图片放在 `public/images/degradations/` 目录：

```
public/images/degradations/
├── gaussian_blur_mild_001.jpg
├── gaussian_blur_moderate_002.jpg
├── gaussian_noise_severe_003.jpg
└── ...
```

**命名建议：**
- 格式：`{type}_{severity}_{number}.jpg`
- 示例：`motion_blur_moderate_012.jpg`

### 其他图片

```
public/images/
├── og.jpg              # Open Graph 图片（社交分享）
├── favicon.svg         # 网站图标
└── logo.png            # 网站 logo（可选）
```

## 🔄 快速替换流程

### 步骤 1：准备数据

1. 导出论文中的数据为 JSON 格式
2. 按照上述格式组织数据
3. 将图片复制到对应目录

### 步骤 2：创建 JSON 文件

```bash
cd med-q-deg-website/public/data
# 创建你的数据文件
nano degradation-examples.json
nano performance.json
nano confusion-matrix.json
nano tsne.json
```

### 步骤 3：验证数据

在本地运行网站检查数据是否正确加载：

```bash
npm run dev
```

访问 `http://localhost:4321` 查看效果。

### 步骤 4：部署

```bash
git add .
git commit -m "Update data and images"
git push
```

## 🛠️ Python 脚本示例

### 生成 degradation-examples.json

```python
import json
import os

# 假设你有一个包含图片路径和标签的 CSV 文件
import pandas as pd

df = pd.read_csv('degradation_labels.csv')

examples = []
for idx, row in df.iterrows():
    examples.append({
        'id': f'example-{idx:03d}',
        'type': row['degradation_type'],
        'category': row['category'],
        'severity': row['severity'],
        'imagePath': f"/images/degradations/{row['filename']}",
        'modality': row['modality'],
        'description': row.get('description', '')
    })

with open('public/data/degradation-examples.json', 'w') as f:
    json.dump(examples, f, indent=2)
```

### 生成 confusion-matrix.json

```python
import json
import numpy as np
from sklearn.metrics import confusion_matrix

# 假设你有真实标签和预测标签
y_true = [...]  # 你的真实标签
y_pred = [...]  # 你的预测标签

cm = confusion_matrix(y_true, y_pred, normalize='true')
cm_percent = (cm * 100).round(0).astype(int).tolist()

with open('public/data/confusion-matrix.json', 'w') as f:
    json.dump(cm_percent, f, indent=2)
```

### 生成 tsne.json

```python
import json
from sklearn.manifold import TSNE

# 假设你有特征矩阵和标签
features = [...]  # 你的特征矩阵 (N, D)
labels = [...]    # 你的标签 (N,)
types = [...]     # 退化类型 (N,)

# 计算 t-SNE
tsne = TSNE(n_components=2, random_state=42)
coords = tsne.fit_transform(features)

# 生成 JSON
tsne_data = []
for i, (x, y) in enumerate(coords):
    tsne_data.append({
        'x': float(x),
        'y': float(y),
        'category': labels[i],
        'type': types[i]
    })

with open('public/data/tsne.json', 'w') as f:
    json.dump(tsne_data, f, indent=2)
```

## ⚠️ 注意事项

1. **图片格式**：建议使用 JPG 或 PNG，大小控制在 500KB 以内
2. **数据验证**：确保所有引用的图片路径都存在
3. **JSON 格式**：使用在线 JSON 验证器检查格式正确性
4. **性能优化**：如果图片很多，考虑使用懒加载
5. **缓存清理**：更新数据后可能需要清除浏览器缓存

## 📝 常见问题

**Q: 图片不显示怎么办？**
A: 检查路径是否以 `/` 开头，确保图片在 `public/` 目录下

**Q: 数据更新后没有变化？**
A: 清除浏览器缓存，或在开发模式下强制刷新（Cmd+Shift+R）

**Q: 如何批量处理图片？**
A: 使用 Python 的 PIL 或 ImageMagick 进行批量压缩和重命名

## 🎯 完成检查清单

- [ ] 创建所有 JSON 数据文件
- [ ] 复制所有示例图片
- [ ] 更新 OG 图片和 favicon
- [ ] 本地测试所有页面
- [ ] 检查所有链接和图片
- [ ] 更新 config.ts 中的链接
- [ ] 提交并推送到 GitHub
- [ ] 验证部署成功

---

**需要帮助？** 查看 `src/utils/dataLoader.ts` 了解数据加载逻辑

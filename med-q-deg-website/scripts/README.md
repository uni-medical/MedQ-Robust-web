# 工具脚本

这个目录包含用于数据处理和网站维护的工具脚本。

## 脚本列表

### 1. `generate_data.py` - 数据生成脚本

用于从论文数据生成网站所需的 JSON 文件。

#### 快速开始

```bash
# 创建占位符数据用于测试
python scripts/generate_data.py --placeholder
```

#### Python API 使用

```python
from scripts.generate_data import (
    generate_degradation_examples,
    generate_performance_data,
    generate_confusion_matrix,
    generate_tsne_visualization
)

# 1. 从 CSV 生成退化示例数据
generate_degradation_examples('data/examples.csv')

# 2. 生成性能数据
metrics = {
    "DPL (Ours)": {"accuracy": 87.3, "f1Score": 85.6, "auroc": 92.1},
    "CLIP": {"accuracy": 74.9, "f1Score": 74.8, "auroc": 76.9},
}
generate_performance_data(metrics)

# 3. 生成混淆矩阵
from sklearn.metrics import confusion_matrix
generate_confusion_matrix(y_true, y_pred)

# 4. 生成 t-SNE 可视化
generate_tsne_visualization(features, labels, types)
```

#### 依赖安装

```bash
pip install pandas scikit-learn numpy
```

---

### 2. `process_images.py` - 图片批量处理脚本

用于批量压缩、重命名和创建占位符图片。

#### 使用方法

##### 压缩图片

```bash
# 压缩图片到最大 800px，质量 85%
python scripts/process_images.py compress input_folder/ public/images/degradations/ --max-size 800 --quality 85
```

##### 批量重命名

```bash
# 预览重命名
python scripts/process_images.py rename public/images/degradations/ --prefix gaussian_blur_mild_ --dry-run

# 实际重命名
python scripts/process_images.py rename public/images/degradations/ --prefix gaussian_blur_mild_ --start 1
```

##### 创建占位符图片

```bash
# 创建 10 张测试图片
python scripts/process_images.py placeholder --count 10
```

#### 依赖安装

```bash
pip install Pillow
```

---

## 完整工作流程

### 准备数据的步骤

#### 步骤 1: 安装 Python 依赖

```bash
pip install pandas scikit-learn numpy Pillow
```

#### 步骤 2: 处理图片

```bash
# 压缩原始图片
python scripts/process_images.py compress /path/to/original/images/ public/images/degradations/

# 批量重命名 (按退化类型和严重程度)
python scripts/process_images.py rename public/images/degradations/ --prefix gaussian_blur_mild_
```

#### 步骤 3: 生成数据文件

```python
# 创建一个 Python 脚本
from scripts.generate_data import *

# 从你的实验数据生成 JSON
generate_degradation_examples('your_data.csv')
generate_performance_data(your_metrics)
generate_confusion_matrix(y_true, y_pred)
generate_tsne_visualization(features, labels)
```

#### 步骤 4: 测试网站

```bash
cd med-q-deg-website
npm run dev
```

访问 http://localhost:4321 查看效果

---

## CSV 格式示例

### degradation_labels.csv

```csv
filename,degradation_type,category,severity,modality,description
img001.jpg,gaussian_blur,blur,mild,MRI,T2-weighted MRI with mild Gaussian blur
img002.jpg,gaussian_noise,noise,severe,CT,CT scan with severe Gaussian noise
img003.jpg,motion_artifact,artifact,moderate,X-Ray,Chest X-ray with motion artifact
```

---

## 故障排除

### Q: 模块找不到错误？

```bash
# 确保在项目根目录运行
cd /path/to/med-q-deg-website

# 或者设置 PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:."
```

### Q: PIL/Pillow 错误？

```bash
# macOS
pip install --upgrade Pillow

# Linux
sudo apt-get install python3-pil
pip install Pillow
```

### Q: scikit-learn 安装很慢？

```bash
# 使用清华镜像
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple scikit-learn
```

---

## 高级使用

### 自定义数据生成

你可以创建自己的数据生成脚本:

```python
import json
from pathlib import Path

# 你的自定义逻辑
def generate_custom_data():
    data = {
        # 你的数据结构
    }

    with open('public/data/custom.json', 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == '__main__':
    generate_custom_data()
```

### 批量操作多个文件夹

```bash
# 使用 shell 循环
for category in blur noise artifact contrast compression other; do
    for severity in mild moderate severe; do
        python scripts/process_images.py rename \
            raw_images/${category}/${severity}/ \
            --prefix ${category}_${severity}_
    done
done
```

---

## 相关文档

- 数据替换指南: [`../DATA_REPLACEMENT_GUIDE.md`](../DATA_REPLACEMENT_GUIDE.md)
- 快速启动: [`../QUICKSTART.md`](../QUICKSTART.md)
- 项目说明: [`../README.md`](../README.md)

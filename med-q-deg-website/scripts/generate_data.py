#!/usr/bin/env python3
"""
数据生成脚本

这个脚本帮助你从论文数据生成网站所需的 JSON 文件。
"""

import json
import os
from pathlib import Path
import argparse


def generate_degradation_examples(csv_path: str, output_dir: str = "public/data"):
    """
    从 CSV 文件生成 degradation-examples.json

    CSV 格式应该包含以下列:
    - filename: 图片文件名
    - degradation_type: 退化类型 (如 gaussian_blur)
    - category: 分类 (blur, noise, artifact, contrast, compression, other)
    - severity: 严重程度 (mild, moderate, severe)
    - modality: 医学成像模态 (MRI, CT, X-Ray, Ultrasound)
    - description: 可选描述
    """
    import pandas as pd

    df = pd.read_csv(csv_path)

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

    output_path = Path(output_dir) / 'degradation-examples.json'
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(examples, f, indent=2, ensure_ascii=False)

    print(f"✅ 生成 {len(examples)} 个示例到 {output_path}")


def generate_performance_data(metrics: dict, output_dir: str = "public/data"):
    """
    从字典生成 performance.json

    示例:
    metrics = {
        "DPL (Ours)": {"accuracy": 87.3, "f1Score": 85.6, "auroc": 92.1},
        "CLIP": {"accuracy": 74.9, "f1Score": 74.8, "auroc": 76.9},
    }
    """
    performance_data = []
    for method, scores in metrics.items():
        performance_data.append({
            "method": method,
            **scores
        })

    output_path = Path(output_dir) / 'performance.json'
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(performance_data, f, indent=2)

    print(f"✅ 生成 {len(performance_data)} 个方法性能到 {output_path}")


def generate_confusion_matrix(y_true, y_pred, output_dir: str = "public/data"):
    """
    从真实标签和预测标签生成混淆矩阵

    参数:
    - y_true: 真实标签数组
    - y_pred: 预测标签数组
    - output_dir: 输出目录
    """
    from sklearn.metrics import confusion_matrix
    import numpy as np

    # 计算混淆矩阵 (归一化为百分比)
    cm = confusion_matrix(y_true, y_pred, normalize='true')
    cm_percent = (cm * 100).round(0).astype(int).tolist()

    output_path = Path(output_dir) / 'confusion-matrix.json'
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(cm_percent, f, indent=2)

    print(f"✅ 生成混淆矩阵到 {output_path}")
    print(f"   矩阵大小: {len(cm_percent)}x{len(cm_percent[0])}")


def generate_tsne_visualization(features, labels, types=None, output_dir: str = "public/data"):
    """
    从特征矩阵生成 t-SNE 可视化数据

    参数:
    - features: 特征矩阵 (N, D)
    - labels: 类别标签 (N,)
    - types: 退化类型 (N,) 可选
    - output_dir: 输出目录
    """
    from sklearn.manifold import TSNE
    import numpy as np

    # 计算 t-SNE
    print("⏳ 计算 t-SNE (这可能需要几分钟)...")
    tsne = TSNE(n_components=2, random_state=42, perplexity=30, n_iter=1000)
    coords = tsne.fit_transform(features)

    # 生成 JSON
    tsne_data = []
    for i, (x, y) in enumerate(coords):
        data_point = {
            'x': float(x),
            'y': float(y),
            'category': str(labels[i])
        }
        if types is not None:
            data_point['type'] = str(types[i])

        tsne_data.append(data_point)

    output_path = Path(output_dir) / 'tsne.json'
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(tsne_data, f, indent=2)

    print(f"✅ 生成 {len(tsne_data)} 个 t-SNE 点到 {output_path}")


def create_placeholder_data(output_dir: str = "public/data"):
    """创建占位符数据用于测试"""

    # 示例数据
    examples = [
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

    performance = [
        {"method": "DPL (Ours)", "accuracy": 87.3, "f1Score": 85.6, "auroc": 92.1, "parameters": "86.2M"},
        {"method": "CLIP", "accuracy": 74.9, "f1Score": 74.8, "auroc": 76.9, "parameters": "151.3M"},
        {"method": "BiomedCLIP", "accuracy": 75.2, "f1Score": 75.1, "auroc": 77.3, "parameters": "151.3M"}
    ]

    confusion = [
        [89, 3, 2, 4, 1, 1],
        [2, 92, 1, 2, 2, 1],
        [3, 2, 85, 6, 2, 2],
        [4, 1, 5, 86, 3, 1],
        [2, 3, 1, 2, 88, 4],
        [5, 2, 4, 3, 4, 82]
    ]

    tsne = [
        {"x": 145.32, "y": -78.91, "category": "Blur", "type": "gaussian_blur"},
        {"x": -89.45, "y": 123.67, "category": "Noise", "type": "gaussian_noise"},
        {"x": 67.82, "y": 168.45, "category": "Artifact", "type": "motion_artifact"}
    ]

    # 创建输出目录
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # 写入文件
    files = {
        'degradation-examples.json': examples,
        'performance.json': performance,
        'confusion-matrix.json': confusion,
        'tsne.json': tsne
    }

    for filename, data in files.items():
        filepath = output_path / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"✅ 创建 {filepath}")


def main():
    parser = argparse.ArgumentParser(description='生成 MedQ-Deg 网站数据文件')
    parser.add_argument('--placeholder', action='store_true', help='创建占位符数据用于测试')
    parser.add_argument('--output-dir', default='public/data', help='输出目录')

    args = parser.parse_args()

    if args.placeholder:
        print("📝 创建占位符数据...")
        create_placeholder_data(args.output_dir)
        print("\n✅ 完成! 你可以运行 'npm run dev' 查看效果")
        print("📌 记得稍后用真实数据替换这些文件")
    else:
        print("使用示例:")
        print("  python scripts/generate_data.py --placeholder  # 创建占位符数据")
        print("\n或者在 Python 中导入函数:")
        print("  from scripts.generate_data import generate_confusion_matrix")
        print("  generate_confusion_matrix(y_true, y_pred)")


if __name__ == '__main__':
    main()

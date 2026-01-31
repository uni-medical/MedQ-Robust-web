#!/usr/bin/env python3
"""
图片批量处理脚本

用于批量压缩和重命名医学图像示例。
"""

from PIL import Image
import os
from pathlib import Path
import argparse


def process_images(
    input_dir: str,
    output_dir: str,
    max_size: int = 800,
    quality: int = 85,
    format: str = 'JPEG'
):
    """
    批量处理图片

    参数:
    - input_dir: 输入图片目录
    - output_dir: 输出图片目录
    - max_size: 图片最大尺寸 (像素)
    - quality: JPEG 质量 (1-100)
    - format: 输出格式 ('JPEG' 或 'PNG')
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # 支持的图片格式
    image_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff'}

    processed = 0
    for img_file in input_path.iterdir():
        if img_file.suffix.lower() not in image_extensions:
            continue

        try:
            # 打开图片
            with Image.open(img_file) as img:
                # 转换为 RGB (JPEG 不支持 RGBA)
                if img.mode in ('RGBA', 'LA', 'P'):
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    if img.mode == 'P':
                        img = img.convert('RGBA')
                    background.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
                    img = background
                elif img.mode != 'RGB':
                    img = img.convert('RGB')

                # 调整大小 (保持比例)
                if max(img.size) > max_size:
                    ratio = max_size / max(img.size)
                    new_size = tuple(int(dim * ratio) for dim in img.size)
                    img = img.resize(new_size, Image.Resampling.LANCZOS)

                # 保存
                output_file = output_path / f"{img_file.stem}.jpg"
                img.save(output_file, format, quality=quality, optimize=True)

                # 显示文件大小
                original_size = img_file.stat().st_size / 1024
                new_size = output_file.stat().st_size / 1024
                reduction = (1 - new_size / original_size) * 100

                print(f"✅ {img_file.name}")
                print(f"   {original_size:.1f}KB → {new_size:.1f}KB (减少 {reduction:.1f}%)")

                processed += 1

        except Exception as e:
            print(f"❌ 处理失败: {img_file.name} - {e}")

    print(f"\n📊 完成! 处理了 {processed} 张图片")


def rename_images(
    directory: str,
    prefix: str = "",
    start_number: int = 1,
    dry_run: bool = False
):
    """
    批量重命名图片

    参数:
    - directory: 图片目录
    - prefix: 文件名前缀 (如 "gaussian_blur_mild_")
    - start_number: 起始编号
    - dry_run: 仅预览，不实际重命名
    """
    dir_path = Path(directory)
    image_extensions = {'.jpg', '.jpeg', '.png'}

    files = sorted([f for f in dir_path.iterdir() if f.suffix.lower() in image_extensions])

    for i, img_file in enumerate(files, start=start_number):
        new_name = f"{prefix}{i:03d}{img_file.suffix}"
        new_path = dir_path / new_name

        if dry_run:
            print(f"预览: {img_file.name} → {new_name}")
        else:
            img_file.rename(new_path)
            print(f"✅ {img_file.name} → {new_name}")

    if dry_run:
        print(f"\n💡 这是预览模式。移除 --dry-run 参数来实际重命名")
    else:
        print(f"\n✅ 重命名了 {len(files)} 个文件")


def create_placeholder_images(output_dir: str = "public/images/degradations", count: int = 10):
    """
    创建占位符图片用于测试

    参数:
    - output_dir: 输出目录
    - count: 要创建的图片数量
    """
    from PIL import ImageDraw, ImageFont
    import random

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    categories = ['blur', 'noise', 'artifact', 'contrast', 'compression', 'other']
    severities = ['mild', 'moderate', 'severe']
    colors = ['#6366f1', '#8b5cf6', '#ec4899', '#f59e0b', '#10b981', '#64748b']

    for i in range(count):
        cat = random.choice(categories)
        sev = random.choice(severities)
        color = colors[categories.index(cat)]

        # 创建图片
        img = Image.new('RGB', (400, 300), color='#18181b')
        draw = ImageDraw.Draw(img)

        # 绘制文本
        try:
            font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 32)
            font_small = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 20)
        except:
            font = ImageFont.load_default()
            font_small = ImageFont.load_default()

        # 绘制类别
        text = f"{cat.upper()}"
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        draw.text(
            ((400 - text_width) / 2, (300 - text_height) / 2 - 20),
            text,
            fill=color,
            font=font
        )

        # 绘制严重程度
        severity_text = f"Severity: {sev}"
        bbox = draw.textbbox((0, 0), severity_text, font=font_small)
        text_width = bbox[2] - bbox[0]
        draw.text(
            ((400 - text_width) / 2, (300 - text_height) / 2 + 30),
            severity_text,
            fill='#a1a1aa',
            font=font_small
        )

        # 保存
        filename = f"{cat}_{sev}_{i+1:03d}.jpg"
        filepath = output_path / filename
        img.save(filepath, 'JPEG', quality=90)

        print(f"✅ 创建 {filename}")

    print(f"\n✅ 创建了 {count} 张占位符图片到 {output_path}")


def main():
    parser = argparse.ArgumentParser(description='批量处理医学图像')
    subparsers = parser.add_subparsers(dest='command', help='子命令')

    # 压缩命令
    compress_parser = subparsers.add_parser('compress', help='批量压缩图片')
    compress_parser.add_argument('input_dir', help='输入目录')
    compress_parser.add_argument('output_dir', help='输出目录')
    compress_parser.add_argument('--max-size', type=int, default=800, help='最大尺寸 (像素)')
    compress_parser.add_argument('--quality', type=int, default=85, help='JPEG 质量 (1-100)')

    # 重命名命令
    rename_parser = subparsers.add_parser('rename', help='批量重命名图片')
    rename_parser.add_argument('directory', help='图片目录')
    rename_parser.add_argument('--prefix', default='', help='文件名前缀')
    rename_parser.add_argument('--start', type=int, default=1, help='起始编号')
    rename_parser.add_argument('--dry-run', action='store_true', help='预览模式')

    # 占位符命令
    placeholder_parser = subparsers.add_parser('placeholder', help='创建占位符图片')
    placeholder_parser.add_argument('--output-dir', default='public/images/degradations', help='输出目录')
    placeholder_parser.add_argument('--count', type=int, default=10, help='图片数量')

    args = parser.parse_args()

    if args.command == 'compress':
        process_images(args.input_dir, args.output_dir, args.max_size, args.quality)
    elif args.command == 'rename':
        rename_images(args.directory, args.prefix, args.start, args.dry_run)
    elif args.command == 'placeholder':
        create_placeholder_images(args.output_dir, args.count)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()

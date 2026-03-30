#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
打包脚本 - 将程序打包为exe
"""

import os
import sys
import shutil
import subprocess

def main():
    print("=" * 50)
    print("无压力随笔记录工具 - 打包脚本")
    print("=" * 50)
    
    # 检查pyinstaller是否安装
    try:
        import PyInstaller
        print("✓ PyInstaller 已安装")
    except ImportError:
        print("✗ PyInstaller 未安装，正在安装...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
        print("✓ PyInstaller 安装完成")
    
    # 清理旧的构建文件
    print("\n清理旧的构建文件...")
    for folder in ['build', 'dist']:
        if os.path.exists(folder):
            shutil.rmtree(folder)
            print(f"  已删除 {folder}/")
    
    # 执行打包命令
    print("\n开始打包...")
    
    # 检测操作系统
    if sys.platform == 'win32':
        separator = ';'
    else:
        separator = ':'
    
    cmd = [
        'pyinstaller',
        '--onefile',
        '--windowed',
        f'--add-data=templates{separator}templates',
        '--name', '随笔记录',
        '--clean',
        'main.py'
    ]
    
    print(f"执行命令: {' '.join(cmd)}")
    result = subprocess.run(cmd)
    
    if result.returncode != 0:
        print("\n✗ 打包失败！")
        return
    
    # 复制templates文件夹到dist
    print("\n复制资源文件...")
    if os.path.exists('dist/templates'):
        shutil.rmtree('dist/templates')
    shutil.copytree('templates', 'dist/templates')
    print("  ✓ templates/ 已复制到 dist/")
    
    # 创建数据目录
    os.makedirs('dist/data', exist_ok=True)
    print("  ✓ data/ 已创建")
    
    print("\n" + "=" * 50)
    print("✓ 打包完成！")
    print("=" * 50)
    print("\n输出文件:")
    print(f"  dist/随笔记录.exe")
    print(f"  dist/templates/index.html")
    print("\n使用方法:")
    print("  双击 dist/随笔记录.exe 即可运行")
    print("=" * 50)

if __name__ == '__main__':
    main()

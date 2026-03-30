#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
无压力随笔记录工具
书本式左右翻页版
"""

import os
import sys
import sqlite3
import webbrowser
import threading
from flask import Flask, render_template, request, jsonify

# 获取程序运行目录（支持打包后的exe）
if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 数据目录和数据库
DATA_DIR = os.path.join(BASE_DIR, 'data')
DB_PATH = os.path.join(DATA_DIR, 'diary.db')
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

os.makedirs(DATA_DIR, exist_ok=True)

app = Flask(__name__, template_folder=TEMPLATE_DIR)

# ---------- 数据库操作 ----------
def init_db():
    """初始化数据库"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS diary (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT DEFAULT '',
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute('SELECT COUNT(*) FROM diary')
    if cursor.fetchone()[0] == 0:
        cursor.execute('INSERT INTO diary (content) VALUES (?)', ('',))
    conn.commit()
    conn.close()

def get_content():
    """获取日记内容"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT content FROM diary ORDER BY id DESC LIMIT 1')
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else ''

def save_content(content):
    """保存日记内容"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE diary 
        SET content = ?, updated_at = CURRENT_TIMESTAMP 
        WHERE id = (SELECT id FROM diary ORDER BY id DESC LIMIT 1)
    ''', (content,))
    conn.commit()
    conn.close()

# ---------- Flask 路由 ----------
@app.route('/')
def index():
    content = get_content()
    return render_template('index.html', content=content)

@app.route('/api/save', methods=['POST'])
def api_save():
    try:
        data = request.get_json()
        content = data.get('content', '')
        save_content(content)
        return jsonify({'success': True, 'message': '已保存'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

# ---------- 自动打开浏览器 ----------
def open_browser():
    webbrowser.open('http://127.0.0.1:5000')

# ---------- 主函数 ----------
def main():
    print("="*50)
    print("无压力随笔记录工具 - 书本左右翻页版")
    print("="*50)
    print("正在启动...")
    init_db()
    print("✓ 数据库初始化完成")
    threading.Thread(target=open_browser).start()
    print("✓ 即将自动打开浏览器...")
    print("-"*50)
    print("访问地址: http://127.0.0.1:5000")
    print("按 Ctrl+C 退出程序")
    print("="*50)
    app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False, threaded=True)

if __name__ == '__main__':
    main()
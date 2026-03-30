# 无压力随笔记录工具

一个极简的本地日记应用，打开就能写，没有负担。

## 功能特点

- ✅ 打开程序自动启动服务并打开浏览器
- ✅ 连续书写体验，所有内容按时间顺序显示
- ✅ 支持 Ctrl+S 保存，右下角显示"已保存"提示
- ✅ 30秒自动保存
- ✅ 刷新页面后保持光标位置
- ✅ 极简UI设计，专注写作

## 项目结构

```
diary_tool/
├── main.py              # 程序入口
├── requirements.txt     # 依赖列表
├── README.md           # 说明文档
├── templates/
│   └── index.html      # 前端页面
└── data/
    └── diary.db        # SQLite数据库（自动创建）
```

## 运行方式

### 方式一：直接运行（开发调试）

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 运行程序
python main.py
```

程序会自动打开浏览器访问 http://127.0.0.1:5000

### 方式二：打包为 EXE（推荐）

#### 步骤1：安装打包工具

```bash
pip install pyinstaller
```

#### 步骤2：打包程序

在项目目录下执行：

```bash
pyinstaller --onefile --windowed --add-data "templates;templates" --name "随笔记录" main.py
```

**参数说明：**
- `--onefile`：打包为单个exe文件
- `--windowed`：不显示命令行窗口
- `--add-data "templates;templates"`：包含templates文件夹（Windows用分号;分隔）
- `--name "随笔记录"`：生成的exe文件名

#### 步骤3：复制templates文件夹

打包完成后，将 `templates` 文件夹复制到 `dist` 目录下：

```
dist/
├── 随笔记录.exe
└── templates/
    └── index.html
```

#### 步骤4：运行

双击 `随笔记录.exe` 即可运行，程序会自动打开浏览器。

## 使用说明

| 快捷键 | 功能 |
|--------|------|
| Ctrl + S | 保存当前内容 |
| 任意输入 | 自动保存光标位置 |

## 数据存储

所有内容保存在程序目录下的 `data/diary.db` 文件中，可随时备份。

## 注意事项

1. 首次运行会自动创建数据库
2. 不要删除或修改 `data` 文件夹，否则数据会丢失
3. 打包后的exe需要与 `templates` 文件夹在同一目录

## 技术栈

- Python 3
- Flask
- SQLite
- HTML/CSS/JavaScript

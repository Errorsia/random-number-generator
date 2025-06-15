# Random Number Generator

## 项目简介
`Random Number Generator` 是一个基于 `Python` 和 `Tkinter` 的简单随机数发生器。用户可以输入范围，并指定需要排除的数字，程序会生成一个不在排除列表中的随机数。

## 功能特色
- **随机数生成**：输入两个整数作为范围，生成该范围内的随机数。
- **排除指定数值**：支持多个需排除的数值，输入时可用逗号或分号隔开。
- **界面友好**：基于 `Tkinter` 创建图形界面，简单直观。
- **Easter Egg**：内置隐藏彩蛋，增加趣味性。

## 使用方法
1. **运行程序**：确保 Python 环境已安装，运行 `random-number-generator.py`。
2. **输入范围**：
   - 在 **“请输入开始数字”** 和 **“请输入结束数字”** 两个输入框中填入两个整数。
3. **排除特定数值**：
   - 可在 **“排除的数字”** 输入框中输入需排除的整数，以逗号或分号隔开。(此项可留空)
4. **点击 `Start` 按钮**：
   - 生成的随机数将在界面中央显示。
5. **点击 `一键清除` 按钮**：
   - 清空所有输入框，重置程序状态。
6. **查看说明**：
   - 点击 `使用说明` 按钮，获取详细使用指南。

## 安装依赖
本项目基于 `Python 3.x` 运行，无需额外安装第三方库，仅使用标准库：
```bash
pip install tkinter
```

## 代码结构

```
random-number-generator/
│── random-number-generator.py  # 主程序文件
│── EnableSpecialInput.txt      # 特殊输入选项(可选)
│── README.md                   # 项目说明文档
```

## 贡献

欢迎提供建议或改进代码！如有问题，请联系作者。

© 2025 Errorsia & Ariskanyaa. All Rights Reserved
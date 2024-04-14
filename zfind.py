# -*- coding=utf-8 -*-
import json
import os
import shutil
import urllib.parse

# 读取json文件
with open('attachment.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 获取当前工作目录
current_dir = os.getcwd()

# 遍历每个对象
for obj in data['messages']:
    file_name = obj['file']
    text_url = obj['text']
    
    # 解析网址获取目标文件的相对路径
    parsed_url = urllib.parse.urlparse(text_url)
    relative_path = parsed_url.path.lstrip('/')
    
    # 构造目标文件的完整路径
    target_path = os.path.join(current_dir, 'mcbbsimg', 'attachment', relative_path)

    # 如果文件存在，移动并重命名文件
    if not os.path.exists(target_path):
        print(f'File {target_path} not found, attention {file_name}')

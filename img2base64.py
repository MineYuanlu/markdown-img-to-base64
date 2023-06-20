import base64
import json
import re
import markdown
import requests
from css_tool import get_html


def img_url_to_base64(in_file, out_file):
    """将图片链接转换为base64格式"""
    with open(in_file, 'r', encoding='utf-8') as f:
        content = f.read()

    def convert_image_to_base64(match):
        image_name = match.group(1)
        image_url = match.group(2)  # 获取匹配的图片链接
        extension = image_url[image_url.rfind('.') + 1:]
        print("正在替换", image_name, image_url, f"({extension})")
        response = requests.get(image_url, stream=True)
        image_data = response.content
        base64_data = base64.b64encode(image_data).decode('utf-8')
        return f"![{image_name}](data:image/{extension};base64,{base64_data})"

    # 正则表达式匹配Markdown图片链接
    pattern = r"!\[(.*?)\]\((.*?)\)"
    replaced_content = re.sub(pattern, convert_image_to_base64, content)

    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(replaced_content)


def img_to_tag(in_file, out_file, map_file):
    """将图片替换为临时标记"""
    image_id = 1
    image_map = {}

    with open(in_file, 'r', encoding='utf-8') as f:
        content = f.read()

    def special_tag(id): return f"/IMG_REPLACE_TAG_{id}/"

    def replace(match):
        nonlocal image_id
        tag = special_tag(image_id)
        image_map[tag] = (match.group(1), match.group(2))
        image_id += 1
        return tag

    pattern = r"!\[(.*?)\]\((.*?)\)"
    replaced_content = re.sub(pattern, replace, content)

    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(replaced_content)

    with open(map_file, 'w', encoding='utf-8') as f:
        json.dump(image_map, f, indent=4)


def tag_to_img(in_file, out_file, map_file):
    """将临时标记转换回图片"""
    with open(in_file, 'r', encoding='utf-8') as f:
        content = f.read()

    with open(map_file, 'r', encoding='utf-8') as f:
        image_map = json.load(f)

    for tag, values in image_map.items():
        image_name, image_url = values
        content = content.replace(tag, f"![{image_name}]({image_url})")

    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(content)


def md_to_html(in_file, out_file):
    """markdown转换为html"""
    with open(in_file, 'r', encoding='utf-8') as f:
        content = f.read()
    html = markdown.markdown(content)
    html = get_html(html)
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(html)

import os
from csscompressor import compress as compress_css_txt

raw_css_dir = "assets\\css\\raw"
dst_css = "assets\\css\\index.css"


def get_css(dir_path=raw_css_dir, out=dst_css, save=False):
    """合并+压缩css"""
    merged_css = ""
    for file_name in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file_name)

        # 检查文件是否为 .css 文件
        if os.path.isfile(file_path) and file_name.endswith(".css"):
            with open(file_path, 'r', encoding='utf-8') as f:
                css_content = f.read()
                merged_css += css_content
    css = compress_css_txt(merged_css)
    if save:
        with open(out, 'w', encoding='utf-8') as f:
            f.write(css)
    return css


def get_html(content):
    """获取html内容"""
    with open("assets\\index.html", 'r', encoding='utf-8') as f:
        html = f.read()
    style = get_css()
    return html.replace('/*!!!STYLE!!!*/', style).replace('<!--!!!CONTENT!!!-->', content)


if __name__ == "__main__":
    get_css(save=True)

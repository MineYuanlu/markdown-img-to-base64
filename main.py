import os
from img2base64 import img_url_to_base64, img_to_tag, tag_to_img, md_to_html
if __name__ == "__main__":
    dir1 = os.path.dirname(os.path.realpath(__file__))
    dir2 = os.getcwd()
    sfn = ("raw.md", "base64.md", "txt.md",
                     "img2tag_map.json", "dst.md", "final.html")
    folder_name = input(f'请输入文件夹名称(应放入"{dir2}\\content"中): ')

    md_dir = os.path.join(dir2, "content", folder_name)
    steps = input(f"\n以下操作均基于\"{md_dir}\"内的文件:\n选择操作:\n" +
                  f" 1. 替换url图片为base64({sfn[0]} -> {sfn[1]})\n" +
                  f" 2. 将图片转换为临时标签({sfn[1]} -> {sfn[2]}, {sfn[3]})\n" +
                  f" 3. 将临时标签转换为图片({sfn[2]}, {sfn[3]} -> {sfn[4]})\n" +
                  f" 4. 将md文档转换为html({sfn[4]} -> {sfn[5]})\n")

    sfn = [os.path.join(md_dir, fn) for fn in sfn]
    for step in steps:
        if step == '1':
            img_url_to_base64(sfn[0], sfn[1])
        elif step == '2':
            img_to_tag(sfn[1], sfn[2], sfn[3])
        elif step == '3':
            tag_to_img(sfn[2], sfn[4], sfn[3])
        elif step == '4':
            md_to_html(sfn[4], sfn[5])
        else:
            print("无效的选择", step)

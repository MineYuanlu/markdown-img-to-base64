# MARKDOWN IMG to base64
> 一个将markdown文档中链接本地化的工具


可用步骤:
1. 替换url图片为base64 (raw.md -> base64.md)
2. 将图片转换为临时标签 (base64.md -> txt.md, img2tag_map.json)
3. 将临时标签转换为图片 (txt.md, img2tag_map.json -> dst.md)
4. 将md文档转换为html  (dst.md -> final.html)

所有文件应在工作目录中的"content\name"文件夹中, name即为输入的文件夹名

## 使用方法
```bash
python3 main.py
```
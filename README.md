# MCBBS 图片备份

本仓库保存的是MCBBS论坛图片资源（时间跨度约为2020年末至2024年初）。资源文件全部来自TG@mcbbsimg频道。

# 使用方法

仓库开启了Pages服务以便于备份网页中引用等用途。

图片保存路径按照mcbbs原路径保存。若保存了mcbbs论坛原版页面，可通过批量替换应用本仓库图片资源。

我们将attachment、static和www三个子域的图片分别保存在同名文件夹中，替换时使用本仓库pages地址`https://luoyunlingyu-mcbbs.github.io/mcbbsimg/`来代替原域名，并在其后加上子域名称即可。其后路径保持不变。

如：

- `https://www.mcbbs.net/static/image/hrline/4.gif`
- `https://static.mcbbs.net/static/image/smiley/tong/doge.png`
- `https://attachment.mcbbs.net/forum/202101/16/084431yfgz01scc9soe7az.png`

可分别替换为：

- `https://luoyunlingyu-mcbbs.github.io/mcbbsimg/www/static/image/hrline/4.gif`
- `https://luoyunlingyu-mcbbs.github.io/mcbbsimg/static/static/image/smiley/tong/doge.png`
- `https://luoyunlingyu-mcbbs.github.io/mcbbsimg/attachment/forum/202101/16/084431yfgz01scc9soe7az.png`

> 提示：论坛网页中某些链接并非原图链接，而是显示缩略图，如`img_thumb.png`。
> 
> 对于某些图片的缩略图我们并未保存。同时也有部分图片只保留了缩略图。
> 
> 如果替换的链接存在无法找到资源的情况，请考虑替换链接为原图或缩略图链接后再试。

# 声明

本仓库中所有文件资源均来自于mcbbsimg频道，原图片均为“我的世界中文论坛”MCBBS所有。本仓库仅对图片作保存处理，对图片内容和保存的信息不负有任何形式的责任。图片内容解释权最终归MCBBS所有。
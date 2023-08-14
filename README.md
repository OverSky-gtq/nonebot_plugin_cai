<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-cai

_✨ 将Character.ai对接到QQ频道 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/owner/nonebot-plugin-example.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-example">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-example.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>

这是一个 nonebot2 插件项目的模板库, 你可以直接使用本模板创建你的 nonebot2 插件项目的仓库

模板库使用方法:
1. 点击仓库中的 "Use this template" 按钮, 输入仓库名与描述, 点击 "  Create repository from template" 创建仓库
2. 在创建好的新仓库中, 在 "Add file" 菜单中选择 "Create new file", 在新文件名处输入`LICENSE`, 此时在右侧会出现一个 "Choose a license template" 按钮, 点击此按钮选择开源协议模板, 然后在最下方提交新文件到主分支
3. 全局替换`owner`为仓库所有者ID; 全局替换`nonebot-plugin-example`为插件名; 全局替换`nonebot_plugin_example`为包名; 修改 python 徽标中的版本为你插件的运行所需版本
4. 修改 README 中的插件名和插件描述, 并在下方填充相应的内容

配置发布工作流:
1. 前往 https://pypi.org/manage/account/#api-tokens 并创建一个新的 API 令牌。创建成功后不要关闭页面，不然你将无法再次查看此令牌。
2. 在单独的浏览器选项卡或窗口中，[打开 Actions secrets and variables 页面](./settings/secrets/actions)。你也可以在 Settings - Secrets and variables - Actions 中找到此页面。
3. 点击 New repository secret 按钮，创建一个名为 `PYPI_API_TOKEN` 的新令牌，并从第一步复制粘贴令牌。

触发发布工作流:
推送任意 tag 即可触发。

创建 tag:

    git tag <tag_name>

推送本地所有 tag:

    git push origin --tags

## 📖 介绍

这里是插件的详细介绍部分

## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-cai

</details>



打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_cai"]

</details>

## ⚙️ 配置
在`__init__.py`中添加你的`char_token`，获取方式：`F12->Application->local_storage`

在config.json中添加你想要对接的AI的char和别名，获取方式:
beat.character.ai官网对话界面url最后面一串字母

暂无

## 🎉 使用
### 指令表
| 指令 | 默认参数 | 需要@ | 参数 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| ep | 无 | 否 | 对话内容 | 发送对话给AI |
| newchat | 当前AI | 否 | AI别名 | 开启一个新对话 |
| menu | 无 | 否 | 无 | 列出可对接AI |
| change | 无 | 否 | AI别名 | 切换对接AI |
| roll | 无 | 否 | 无 | 回滚一条对话 |
### 效果图
如果有效果图的话

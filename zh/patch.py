#!/usr/bin/env python3
"""zh-CN: 把 launcher_pages.rs 里的界面英文替换成中文（构建时自动运行）。"""
import pathlib

PAIRS = [
    ('Ready to play', '准备好了'),
    ('Play Minecraft', '启动游戏'),
    ('Browse Mods', '看模组'),
    ('Export diagnostics', '导出诊断'),
    ('Your Java worlds, on Android', '安卓上的 Java 世界'),
    ('Downloads official Minecraft', '下载官方 Minecraft'),
    ('assets directly from Mojang', '资源，直连 Mojang'),
    ('Live download speed, ETA and 6-step verification', '实时下载速度、ETA 与六步校验'),
    ('Play offline or sign in with your Microsoft account', '离线游玩，或用微软账号登录'),
    ('Native Rust client with hardware Vulkan & OpenGL ES rendering', 'Rust 原生客户端，硬件 Vulkan 与 OpenGL ES 渲染'),
    ('Resource Packs & Shaders with Modrinth previews', '资源包与光影，Modrinth 预览'),
    ('Customize MCPE & GoyControl HUD layouts in Settings', '自定义 MCPE 与 GoyControl 的 HUD 布局'),
    ('Download Minecraft', '下载 Minecraft'),
    ('Retry installation', '重试安装'),
    ('Launching', '启动中'),
    ('Tap for versions, Modrinth info & screenshots', '点此查看版本、Modrinth 信息与截图'),
    ('Searching... You can switch tabs while results load.', '搜索中…切换标签不影响结果加载'),
    ('Theme customization, profiles, DPI scale & preferences', '主题、配置、DPI 与偏好设置'),
    ('HUD touch layout, buttons, sensitivity and profiles', 'HUD 布局、按钮、灵敏度与配置'),
    ('Unstable features. We put the weird shit here.', '不稳定功能，奇怪的东西都放这'),
    ('Hold Z to zoom; configurable in Options > Mods', '按住 Z 缩放，可在 选项 > 模组 配置'),
    ('Item recipes and uses beside the inventory', '背包旁显示配方与用途'),
    ('Search installed mods, packs & shaders...', '搜索模组、资源包与光影…'),
    ('Search mods or paste .hmod HTTPS link...', '搜索模组或粘贴 .hmod 链接…'),
    ('A configurable map in the screen corner', '屏幕角落的配置小地图'),
    ('Logs, device info and troubleshooting', '日志、设备信息与故障排查'),
    ('Rendering, resolution and performance', '渲染、分辨率与性能'),
    ('No local add-ons installed yet', '还没有安装本地内容'),
    ('Microsoft and Xbox sign-in', '微软与 Xbox 登录'),
    ('Experimental Stuff', '实验性功能'),
    ('Launcher Settings', '启动器设置'),
    ('Video Settings', '视频设置'),
    ('Content Library', '内容库'),
    ('Search catalog...', '搜索目录…'),
    ('Import Pack', '导入包'),
    ('Import Mod', '导入模组'),
    ('File Manager', '文件管理器'),
    ('Previous Page', '上一页'),
    ('Next Page', '下一页'),
    ('Shader Packs', '光影包'),
    ('Installed Mods', '已安装模组'),
    ('Play', '开始'),
    ('Mods', '模组'),
    ('Resource Pack', '资源包'),
    ('Resource Packs', '资源包'),
    ('Shaders', '光影'),
    ('Skins', '皮肤'),
    ('Installed', '已安装'),
    ('Settings', '设置'),
    ('Controls', '操作控制'),
    ('Diagnostics', '诊断'),
    ('Account', '账号'),
    ('Install', '安装'),
    ('Search', '搜索'),
    ('Cancel', '取消'),
    ('Previous', '上一页'),
    ('Next', '下一页'),
    ('Library', '资料库'),
    ('Profile', '配置'),
    ('Official Horizon Mods', '官方 Horizon 模组'),
    ('In-Process Engine', '进程内引擎'),
    ('Active Profile Mods', '当前配置启用的模组'),
    ('Built-in Mods Ready', '内置模组就绪'),
    ('RELEASE HIGHLIGHTS', '版本亮点'),
    ('Horizon Mod Engine', 'Horizon 模组引擎'),
]

target = pathlib.Path("crates/horizon-client/src/android/launcher_pages.rs")
src = target.read_text(encoding="utf-8")
hits = 0
for en, zh in PAIRS:
    lit = '"' + en.replace('\\', '\\\\').replace('"', '\\"') + '"'
    n = src.count(lit)
    if n:
        src = src.replace(lit, '"' + zh + '"')
        hits += n
target.write_text(src, encoding="utf-8")
print(f"zh-CN: replaced {hits} literals in {target}")

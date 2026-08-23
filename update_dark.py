import re

# 1. Update 3D Profile YAML
with open('.github/workflows/3d-profile.yml', 'r') as f:
    yaml_content = f.read()

yaml_content = yaml_content.replace('"background": "#2E2910"', '"background": "#0d1117"')
yaml_content = yaml_content.replace('"text": "#EBE3A7"', '"text": "#c9d1d9"')
yaml_content = yaml_content.replace('"level0": "#2C5745"', '"level0": "#161b22"')
yaml_content = yaml_content.replace('"level1": "#4B6B40"', '"level1": "#30363d"')
yaml_content = yaml_content.replace('"level2": "#768630"', '"level2": "#484f58"')
yaml_content = yaml_content.replace('"level3": "#B0AA14"', '"level3": "#8b949e"')
yaml_content = yaml_content.replace('"level4": "#EB7D00"', '"level4": "#ffffff"')

with open('.github/workflows/3d-profile.yml', 'w') as f:
    f.write(yaml_content)


# 2. Update README.md
with open('README.md', 'r') as f:
    content = f.read()

# Replace Hero Banner source
content = content.replace('assets/hero_banner.jpg', 'assets/hero_banner.png')

# Update typing SVG colors
content = content.replace('color=EBE3A7', 'color=c9d1d9')

# Update Analytics Endpoints
stats_old_1 = 'src="https://github-readme-stats-fast.vercel.app/api?username=yamantaka-singh&show_icons=true&hide_border=true&bg_color=2E2910&title_color=EBE3A7&text_color=EBE3A7&icon_color=EB7D00"'
stats_new_1 = 'src="https://github-readme-stats-fast.vercel.app/api?username=yamantaka-singh&show_icons=true&hide_border=true&theme=github_dark"'
content = content.replace(stats_old_1, stats_new_1)

stats_old_2 = 'src="https://github-readme-stats-fast.vercel.app/api/top-langs/?username=yamantaka-singh&layout=compact&hide_border=true&bg_color=2E2910&title_color=EBE3A7&text_color=EBE3A7&card_width=450"'
stats_new_2 = 'src="https://github-readme-stats-fast.vercel.app/api/top-langs/?username=yamantaka-singh&layout=compact&hide_border=true&theme=github_dark&card_width=450"'
content = content.replace(stats_old_2, stats_new_2)

streak_old = 'src="https://streak-stats.demolab.com?user=yamantaka-singh&hide_border=true&background=2E2910&stroke=EB7D00&ring=EB7D00&fire=EB7D00&currStreakNum=EBE3A7&sideNums=EBE3A7&currStreakLabel=EBE3A7&sideLabels=EBE3A7&dates=EBE3A7"'
streak_new = 'src="https://streak-stats.demolab.com?user=yamantaka-singh&hide_border=true&theme=github-dark"'
content = content.replace(streak_old, streak_new)

# Update Shields.io badges to monochrome
content = re.sub(r'badge/([^-\?]+)-2C5745\?', r'badge/\1-1e1e1e?', content)
content = re.sub(r'badge/([^-\?]+)-2C5745"', r'badge/\1-1e1e1e"', content)
content = re.sub(r'logoColor=EB7D00', r'logoColor=ffffff', content)

with open('README.md', 'w') as f:
    f.write(content)

print("Updated README.md and 3d-profile.yml")

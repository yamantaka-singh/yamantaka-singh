import re

with open('README.md', 'r') as f:
    content = f.read()

# 1. Replace Hero Banner
content = re.sub(
    r'<div align="center">\s*<img src="https://capsule-render\.vercel\.app/api\?type=waving.*?</div>',
    '<div align="center">\n  <img src="assets/hero_banner.jpg" width="100%" alt="3D Hero Banner" />\n</div>',
    content,
    flags=re.DOTALL
)

# 2. Update typing SVG color
content = content.replace('color=3FB950', 'color=EBE3A7')

# 3. Add 3D graph after typing SVG
typing_svg = '</a>\n\n<br/>'
graph_html = '''</a>

<br/>

<div align="center">
  <h3>🏙️ 3D Contribution Landscape</h3>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/yamantaka-singh/yamantaka-singh/main/profile-3d-contrib/profile-night-view.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/yamantaka-singh/yamantaka-singh/main/profile-3d-contrib/profile-night-view.svg">
    <img alt="3D Github Contribution Graph" src="https://raw.githubusercontent.com/yamantaka-singh/yamantaka-singh/main/profile-3d-contrib/profile-night-view.svg">
  </picture>
</div>

<br/>'''
content = content.replace(typing_svg, graph_html)

# 4. Standardize all Shields.io badges in the Technical Arsenal
# Find all img.shields.io/badge/
# We want to replace the color (like -3776AB) with -2C5745
content = re.sub(r'badge/([^-\?]+)-[0-9A-Fa-f]{6}\?', r'badge/\1-2C5745?', content)
content = re.sub(r'badge/([^-\?]+)-[0-9A-Fa-f]{6}"', r'badge/\1-2C5745"', content)
# And set logoColor to EB7D00 if it exists
content = re.sub(r'logoColor=(?:white|black|[0-9A-Fa-f]{6})', r'logoColor=EB7D00', content)

# 5. Update Analytics Endpoints
# github-readme-stats
stats_old_1 = 'src="https://github-readme-stats-fast.vercel.app/api?username=yamantaka-singh&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0d1117"'
stats_new_1 = 'src="https://github-readme-stats-fast.vercel.app/api?username=yamantaka-singh&show_icons=true&hide_border=true&bg_color=2E2910&title_color=EBE3A7&text_color=EBE3A7&icon_color=EB7D00"'
content = content.replace(stats_old_1, stats_new_1)

stats_old_2 = 'src="https://github-readme-stats-fast.vercel.app/api/top-langs/?username=yamantaka-singh&layout=compact&theme=tokyonight&hide_border=true&bg_color=0d1117"'
stats_new_2 = 'src="https://github-readme-stats-fast.vercel.app/api/top-langs/?username=yamantaka-singh&layout=compact&hide_border=true&bg_color=2E2910&title_color=EBE3A7&text_color=EBE3A7&card_width=450"'
content = content.replace(stats_old_2, stats_new_2)

# streak-stats
streak_old = 'src="https://streak-stats.demolab.com?user=yamantaka-singh&theme=tokyonight&hide_border=true&background=0d1117"'
streak_new = 'src="https://streak-stats.demolab.com?user=yamantaka-singh&hide_border=true&background=2E2910&stroke=EB7D00&ring=EB7D00&fire=EB7D00&currStreakNum=EBE3A7&sideNums=EBE3A7&currStreakLabel=EBE3A7&sideLabels=EBE3A7&dates=EBE3A7"'
content = content.replace(streak_old, streak_new)

with open('README.md', 'w') as f:
    f.write(content)

print("Updated README.md")

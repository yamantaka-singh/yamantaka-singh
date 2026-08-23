import re

with open('README.md', 'r') as f:
    content = f.read()

# Fix the brown background on stats
content = re.sub(r'bg_color=2E2910', 'bg_color=0d1117', content)
content = re.sub(r'icon_color=EB7D00', 'icon_color=58a6ff', content)
content = re.sub(r'title_color=[a-zA-Z0-9]+', 'title_color=58a6ff', content)
content = re.sub(r'text_color=[a-zA-Z0-9]+', 'text_color=c9d1d9', content)

# Fix streak stats to be all blue and dark
streak_new = 'src="https://streak-stats.demolab.com?user=yamantaka-singh&hide_border=true&background=0d1117&stroke=58a6ff&ring=58a6ff&fire=58a6ff&currStreakNum=c9d1d9&sideNums=c9d1d9&currStreakLabel=c9d1d9&sideLabels=c9d1d9&dates=c9d1d9"'
content = re.sub(r'src="https://streak-stats.demolab.com[^"]+"', streak_new, content)

# Change badge logos to GitHub Blue
content = content.replace('logoColor=ffffff', 'logoColor=58a6ff')

# Change typing SVG color to GitHub Blue
content = content.replace('color=c9d1d9', 'color=58a6ff')

with open('README.md', 'w') as f:
    f.write(content)

# Update 3D Profile YAML for Blue Theme
with open('.github/workflows/3d-profile.yml', 'r') as f:
    yaml_content = f.read()

yaml_content = yaml_content.replace('"level0": "#161b22"', '"level0": "#161b22"')
yaml_content = yaml_content.replace('"level1": "#30363d"', '"level1": "#0a3069"')
yaml_content = yaml_content.replace('"level2": "#484f58"', '"level2": "#0969da"')
yaml_content = yaml_content.replace('"level3": "#8b949e"', '"level3": "#54aeff"')
yaml_content = yaml_content.replace('"level4": "#ffffff"', '"level4": "#b6e3ff"')

with open('.github/workflows/3d-profile.yml', 'w') as f:
    f.write(yaml_content)

print("Applied GitHub Blue theme!")

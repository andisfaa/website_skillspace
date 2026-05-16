import os

files = [
    'tentang-kami.html', 
    'search-results.html', 
    'search-results-jakarta.html', 
    'search-results-bandung.html', 
    'profil-freelancer.html', 
    'preview.html', 
    'post-skill.html', 
    'dashboard-pesanan.html', 
    'cara-kerja.html'
]

for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        new_content = content.replace('homepage.html', 'index.html')
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"Skipped {filename} (not found)")

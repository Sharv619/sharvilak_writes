import subprocess
import re
import os

def extract_instagram_links(xml_file):
    with open(xml_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex for instagram post links (shortcodes)
    # Examples: /p/B7QurmElxyI/ or /p/B7QurmElxyI
    shortcodes = re.findall(r'instagram\.com/p/([a-zA-Z0-9_-]+)', content)
    
    return sorted(list(set(shortcodes)))

def download_posts(shortcodes):
    if not os.path.exists('scraped_posts'):
        os.makedirs('scraped_posts')
    
    os.chdir('scraped_posts')
    
    for code in shortcodes:
        print(f"Downloading post: {code}")
        # Using - prefix for shortcodes in instaloader
        subprocess.run(['../venv/bin/instaloader', '--', f'-{code}'])
    
    os.chdir('..')

if __name__ == "__main__":
    shortcodes = extract_instagram_links('himanshoe.WordPress.2026-04-30.xml')
    print(f"Found {len(shortcodes)} post shortcodes.")
    download_posts(shortcodes)

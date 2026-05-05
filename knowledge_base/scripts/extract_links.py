import re
import xml.etree.ElementTree as ET

def extract_instagram_links(xml_file):
    with open(xml_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex for instagram post and profile links
    links = re.findall(r'https?://(?:www\.)?instagram\.com/[p|reels|stories|]/?[a-zA-Z0-9_-]+/?', content)
    profile_links = re.findall(r'https?://(?:www\.)?instagram\.com/[a-zA-Z0-9_.]+/?', content)
    
    # Filter out common false positives and clean up
    clean_links = set()
    for link in links + profile_links:
        link = link.split('?')[0] # Remove query params
        if link.endswith('/'):
            link = link[:-1]
        
        # Exclude base domain and generic paths
        if link not in ['https://www.instagram.com', 'https://instagram.com']:
             clean_links.add(link)
            
    return sorted(list(clean_links))

if __name__ == "__main__":
    links = extract_instagram_links('himanshoe.WordPress.2026-04-30.xml')
    for link in links:
        print(link)

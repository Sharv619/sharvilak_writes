import re
import json

def extract_wp_instagram_content(xml_file):
    with open(xml_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find paragraphs that contain instagram.com
    # This is a bit rough but will get the context
    items = re.findall(r'<item>.*?</item>', content, re.DOTALL)
    
    ig_data = []
    for item in items:
        if 'instagram.com' in item:
            title_match = re.search(r'<title>(.*?)</title>', item)
            title = title_match.group(1) if title_match else "Untitled"
            
            content_match = re.search(r'<content:encoded><!\[CDATA\[(.*?)]]>', item, re.DOTALL)
            body = content_match.group(1) if content_match else ""
            
            # Find specific links in this item
            links = re.findall(r'https?://(?:www\.)?instagram\.com/[^\s<"\'\]]+', item)
            
            ig_data.append({
                "title": title,
                "content": body,
                "links": list(set(links))
            })
            
    return ig_data

if __name__ == "__main__":
    data = extract_wp_instagram_content('himanshoe.WordPress.2026-04-30.xml')
    with open('instagram_kb/wordpress_ig_context.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print(f"Extracted {len(data)} items with Instagram context to instagram_kb/wordpress_ig_context.json")

import urllib.request
import re
import json
import xml.etree.ElementTree as ET
import html

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept-Language': 'es,es-419;q=0.9,en;q=0.8',
    'Sec-Fetch-Mode': 'navigate'
}

url = 'https://www.youtube.com/watch?v=ONwQDjk1TXg'
req = urllib.request.Request(url, headers=headers)

try:
    with urllib.request.urlopen(req) as resp:
        content = resp.read().decode('utf-8', errors='ignore')
        print(f"HTML length: {len(content)}")
        
        # Check for captionTracks
        match = re.search(r'"captionTracks":\s*(\[.*?\])', content)
        if match:
            print("captionTracks found!")
            tracks = json.loads(match.group(1))
            for t in tracks:
                print(f"Track: {t.get('name', {}).get('simpleText')} - {t.get('languageCode')} - {t.get('baseUrl')}")
            
            # Fetch the first track
            track_url = tracks[0]['baseUrl']
            treq = urllib.request.Request(track_url, headers=headers)
            with urllib.request.urlopen(treq) as tresp:
                xml_data = tresp.read().decode('utf-8')
                root = ET.fromstring(xml_data)
                lines = []
                for elem in root.findall('text'):
                    t_text = html.unescape(elem.text or '')
                    lines.append(t_text)
                
                full_transcript = " ".join(lines)
                with open("transcript_extracted.txt", "w", encoding="utf-8") as f:
                    f.write(full_transcript)
                print(f"Transcript written to transcript_extracted.txt (length {len(full_transcript)})")
        else:
            print("captionTracks NOT found directly in HTML.")
            # Search for title, description, and keywords
            title_match = re.search(r'<title>(.*?)</title>', content)
            if title_match:
                print("Title:", title_match.group(1))
            desc_match = re.search(r'"shortDescription":\s*"([^"]+)"', content)
            if desc_match:
                print("Description:", desc_match.group(1)[:500])
except Exception as e:
    print("Error:", e)

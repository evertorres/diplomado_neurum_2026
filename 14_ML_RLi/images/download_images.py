import os
import json
import urllib.request
import urllib.error

# Script path is relative to its folder
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(CURRENT_DIR, "slides_images.json")
OUTPUT_DIR = CURRENT_DIR

def main():
    if not os.path.exists(JSON_PATH):
        print(f"Error: {JSON_PATH} not found!")
        return

    with open(JSON_PATH, "r") as f:
        slides = json.load(f)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    downloaded_count = 0
    total_images_to_download = sum(len(slide["urls"]) for slide in slides)
    print(f"Found {total_images_to_download} image URLs to download.")

    for slide in slides:
        slide_num = slide["slideIndex"] + 1
        urls = slide["urls"]
        if not urls:
            continue
        
        slide_name = f"slide{slide_num:02d}"
        print(f"Processing {slide_name} ({len(urls)} images)...")

        for idx, url in enumerate(urls):
            if len(urls) == 1:
                filename_base = f"{slide_name}_img"
            else:
                filename_base = f"{slide_name}_img{idx+1:02d}"

            req = urllib.request.Request(url, headers=headers)
            try:
                with urllib.request.urlopen(req, timeout=15) as response:
                    content_type = response.headers.get("Content-Type", "")
                    ext = ".png"
                    if "image/jpeg" in content_type:
                        ext = ".jpg"
                    elif "image/webp" in content_type:
                        ext = ".webp"
                    elif "image/gif" in content_type:
                        ext = ".gif"
                    
                    filename = f"{filename_base}{ext}"
                    filepath = os.path.join(OUTPUT_DIR, filename)

                    data = response.read()
                    with open(filepath, "wb") as out_f:
                        out_f.write(data)
                    print(f"  Downloaded: {filename} ({len(data)} bytes) [Content-Type: {content_type}]")
                    downloaded_count += 1
            except urllib.error.URLError as e:
                print(f"  Error downloading {url}: {e}")
            except Exception as e:
                print(f"  Unexpected error downloading {url}: {e}")

    print(f"\nCompleted downloading {downloaded_count} of {total_images_to_download} images.")

if __name__ == "__main__":
    main()

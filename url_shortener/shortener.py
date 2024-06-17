import pyshorteners
import qrcode
from PIL import Image
from tinydb import TinyDB, Query
import os
import pyperclip
from datetime import datetime, timedelta

# Setup database
db = TinyDB('db.json')
urls_table = db.table('urls')

class URLShortener:
    def __init__(self):
        self.shortener = pyshorteners.Shortener()

    def shorten_url(self, long_url, custom_alias=None, custom_domain=None):
        if custom_alias:
            domain = custom_domain if custom_domain else "short.url"
            short_url = f"https://{domain}/{custom_alias}"
        else:
            short_url = self.shortener.tinyurl.short(long_url)
        
        url_data = {
            'long_url': long_url,
            'short_url': short_url,
            'created_at': datetime.now().isoformat(),
            'expires_at': (datetime.now() + timedelta(days=30)).isoformat()  
        }
        
        urls_table.insert(url_data)
        return short_url

    def expand_url(self, short_url):
        URL = Query()
        url_data = urls_table.search(URL.short_url == short_url)
        if url_data:
            return url_data[0]['long_url']
        return "URL tidak ditemukan."

    def generate_qr(self, short_url):
        img = qrcode.make(short_url)
        img.show()
        img.save(f"{short_url.split('/')[-1]}.png")

    def get_statistics(self, short_url):
        URL = Query()
        url_data = urls_table.search(URL.short_url == short_url)
        if url_data:
            return url_data[0]
        else:
            return "URL tidak ditemukan."

    def delete_url(self, short_url):
        URL = Query()
        urls_table.remove(URL.short_url == short_url)

    def update_expiry(self, short_url, new_expiry_days):
        URL = Query()
        urls_table.update({'expires_at': (datetime.now() + timedelta(days=new_expiry_days)).isoformat()}, URL.short_url == short_url)

    def copy_to_clipboard(self, text):
        pyperclip.copy(text)

    def list_urls(self):
        return urls_table.all()

shortener = URLShortener()

from datetime import datetime

def is_url_expired(url_data):
    expiry_date = datetime.fromisoformat(url_data['expires_at'])
    return datetime.now() > expiry_date

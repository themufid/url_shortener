from url_shortener.shortener import shortener
from url_shortener.utils import is_url_expired
import sys

def menu():
    print("1. Shorten URL")
    print("2. Expand URL")
    print("3. Generate QR Code")
    print("4. Get URL Statistics")
    print("5. Delete URL")
    print("6. Update URL Expiry")
    print("7. Copy URL to Clipboard")
    print("8. List all URLs")
    print("0. Exit")

def main():
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            long_url = input("Enter the long URL: ")
            custom_alias = input("Enter custom alias (or leave blank): ")
            custom_domain = input("Enter custom domain (or leave blank): ")
            short_url = shortener.shorten_url(long_url, custom_alias if custom_alias else None, custom_domain if custom_domain else None)
            print(f"Short URL: {short_url}")
        elif choice == '2':
            short_url = input("Enter the short URL: ")
            long_url = shortener.expand_url(short_url)
            print(f"Long URL: {long_url}")
        elif choice == '3':
            short_url = input("Enter the short URL: ")
            shortener.generate_qr(short_url)
        elif choice == '4':
            short_url = input("Enter the short URL: ")
            stats = shortener.get_statistics(short_url)
            print(stats)
        elif choice == '5':
            short_url = input("Enter the short URL: ")
            shortener.delete_url(short_url)
            print(f"URL {short_url} deleted.")
        elif choice == '6':
            short_url = input("Enter the short URL: ")
            days = int(input("Enter the new expiry time (days): "))
            shortener.update_expiry(short_url, days)
            print(f"Expiry time updated for {short_url}.")
        elif choice == '7':
            text = input("Enter text to copy to clipboard: ")
            shortener.copy_to_clipboard(text)
            print("Text copied to clipboard.")
        elif choice == '8':
            urls = shortener.list_urls()
            for url in urls:
                status = "Expired" if is_url_expired(url) else "Valid"
                print(f"{url['short_url']} ({status})")
        elif choice == '0':
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

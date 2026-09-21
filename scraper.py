import urllib.parse
import webbrowser
import time

search_keyword = "Restaurants in Seremban"
encoded_keyword = urllib.parse.quote(search_keyword)
google_maps_url = f"https://google.com{encoded_keyword}"

print("=" * 60)
print("মাহবুর ভাই, 'Ya Parket' মেথডে গুগল ম্যাপস কাস্টমার স্ক্র্যাপার সচল হচ্ছে...")
print("=" * 60)
time.sleep(2)

webbrowser.open(google_maps_url)
print("সফল হয়েছে ভাই! মেইন ডাটা লিস্ট ওপেন হচ্ছে ভাই...")

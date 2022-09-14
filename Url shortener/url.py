import pyshorteners
long_url =input("Enter the URL to shorten it: ")


type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)

print("The shortened URL is displayed as: " + short_url)
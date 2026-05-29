# import requests
# from bs4 import BeautifulSoup


# def scrape_website(url):
#     try:
#         headers = {
#             "User-Agent": "Mozilla/5.0"
#         }

#         response = requests.get(
#             url,
#             headers=headers,
#             timeout=10
#         )

#         soup = BeautifulSoup(response.text, "html.parser")

#         title = soup.title.string if soup.title else "No Title"

#         text = soup.get_text(
#             separator=" ",
#             strip=True
#         )

#         return {
#             "title": title,
#             "content": text[:5000]
#         }

#     except Exception as e:
#         return {
#             "error": str(e)
#         }

# import requests
# res_parse_list = []
# response = requests.get("https://coinmarketcap.com/")
# # print(response.text)
# response_text = response.text
# response_parse = response_text.split("<span>")
# for parse_elem_1 in response_parse:
#     if parse_elem_1.startswith("$"):
#         # print(parse_elem_1)
#         for parse_elem_2 in parse_elem_1.split("</span>"):
#             if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
#                 # print(parse_elem_2)
#                 res_parse_list.append(parse_elem_2)
# # #
# bitcoin_exchange_rate = res_parse_list[0]
# print(bitcoin_exchange_rate)
from bs4 import BeautifulSoup
import requests
response = requests.get("https://coinmarketcap.com/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text,features="html.parser")
    soup_list = soup.find_all("a", {"href":"/currencies/bitcoin/#markets"})
    res = soup_list[0].find("span")
    print(res.text)

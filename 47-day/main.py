import requests
# import lxml

URL="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
headers= {

}
response = requests.get(url=URL, headers=headers)

print(response.text)
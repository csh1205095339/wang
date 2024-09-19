import requests


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "BIDUPSID": "E6F5D19B222F2A20972C1601658CA1B3",
    "PSTM": "1720425030",
    "BAIDUID": "E6F5D19B222F2A20922CE72B248F1A2B:FG=1",
    "BD_UPN": "12314753",
    "H_WISE_SIDS_BFESS": "60448_60598_60622_60664_60678",
    "ZFY": "nzgR:BhfpYc:AnpnvWllt5d47sfF4RWqk:BYK0Bh9Pceys:C",
    "BAIDUID_BFESS": "E6F5D19B222F2A20922CE72B248F1A2B:FG=1",
    "COOKIE_SESSION": "363888_0_9_9_1_19_1_0_9_7_0_4_0_0_0_0_1723173437_0_1725008639%7C9%230_0_1725944546%7C1%7C1",
    "H_WISE_SIDS": "60448_60598_60678_60360_60732",
    "ab_sr": "1.0.1_YjNhY2Q2MGFhZGRlMDU5NzYwOTU5ZjgyYTQ5ZTNjZDkwYTEyNzhlMTI4ZjM4YWJlNmU2ZmM2ODcwZGQwODM5NDIyNTgyMTZjMWJhMmJkMjcyZmViNjA1MzZiYjYxNjNkODljZjM2NTNkNzg5ZWYxMTIyZjBmZWNiOTc2YTg4YjE4YWQxYjgyODgzNDBiYmM2NzE5Y2IwZDYyNjdkMDczYw==",
    "RT": "\"z=1&dm=baidu.com&si=381ae46f-d6df-40ce-959b-82cd644169d7&ss=m17h92uh&sl=y&tt=b28&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=1a2hf\"",
    "BDRCVFR[p9L08uoHmuf]": "mk3SLVN4HKm",
    "H_PS_PSSID": "60448_60598_60360_60732_60797_60785",
    "BD_HOME": "1",
    "BA_HECTOR": "20aha00ga005812401240h8g2h7q761jel0531u"
}
url = "https://www.baidu.com/"
params = {
    "tn": "54093922_26_hao_pg"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)
# -*-coding: Utf-8 -*-
# @File : 07_urllib_post请求百度翻译之详细翻译 .py
# author: fwx
# Time：2024/1/18

import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

# data 确保 key 和 value 中没有空格
data = {
    'from':'en',
    'to':'zh',
    'query':'spider',
    'simple_means_flag':'3',
    'sign':'63766.268839',
    'token':'b1bb5a7ed140466af85329205b985c2d',
    'domain':'common',
    'ts':'1705544498152'
}

# headers 中只需要传 Cookie 既可
headers = {
    #'Accept':'*/*',

    # *** 这行必须注释掉
    # 'Accept-Encoding':'gzip, deflate, br',

    # 'Accept-Language':'zh-CN,zh;q=0.9,und;q=0.8',
    # 'Acs-Token':'1705489690522_1705544498194_+yQOP6OTDZU+nKfUUzSmN2hVNvz8bDsySERxmKNHSD/nZK7sdnepAOixXiLKcwVf5IWzslA+eIPOc5K2AxttHtnfhFpol6RyOVlB1fARjiF9YZ4kF5ijSYstyftjm3guuVFwPX0B3LyOtyThwAGUsLEAEnj7A9poz2Svj0JCP9iVqFlGVQH6tCK1tS09eB7TZra5KGVOhD5VKAWiPxsTlg3UmCV/dEE9RlOJoHyvRYcU8jHNxVmSSAjuHRCfQWgIDrd4thupPLy5N5nBt8fheEjJjn260clZhoPPvaUG1TZ6I93CaX6E64XTblbB58dzeDp9xSL1ZwWvoAEkEt0uSohnzB+mSh6VTMxzykSyD2Uh3YmXDd2Md1HCvjVi9SyK4ytZNz9+FhJ70DW9VnNiO2eq8UmTara3r4xMNERYdULCBqXGotcy8tl1YChWXok4eeZS5GYRW+nv/4Gn/ywLu9ZTun2XajSo84MeQiunS8c=',
    # 'Connection':'keep-alive',
    # 'Content-Length':'134',
    # 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie':'BIDUPSID=CD0CEC2DDEDC292E36AB1BC1D4B58E56; PSTM=1670440529; BDUSS=czeTBHa1JZeTN3MmJZdmRRd2xHZUM4eUNNSUxoSG54eHlpekxvcFRJTC1HNHhrRVFBQUFBJCQAAAAAAAAAAAEAAAAV0JYKZnd4MDMwOQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP6OZGT-jmRkeD; BDUSS_BFESS=czeTBHa1JZeTN3MmJZdmRRd2xHZUM4eUNNSUxoSG54eHlpekxvcFRJTC1HNHhrRVFBQUFBJCQAAAAAAAAAAAEAAAAV0JYKZnd4MDMwOQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP6OZGT-jmRkeD; MCITY=-218%3A; BAIDUID=D6AFBBB5FFDF10227A343DD130C8B02D:FG=1; H_WISE_SIDS_BFESS=39938_39999_40024_40043; H_WISE_SIDS=39999_40024_40043; H_PS_PSSID=39999_40024_40043; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=D6AFBBB5FFDF10227A343DD130C8B02D:FG=1; BA_HECTOR=048g80aga02g8l2g21a480a1dbdo4k1iqf71f1s; ZFY=sVjCQWD:BDB0DhXfeSx:BHWXNvdb6CHCBvWmgr0L1Gmaw:C; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1705499500,1705543599; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=2; delPer=0; BDRCVFR[n9rYh9b3bT0]=mk3SLVN4HKm; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1705544488; ab_sr=1.0.1_MGRjMWU3OWFkYTJjOWI1MzNhODM2MzM5ZmQzODNmODllN2QwNGY4MTZjYTQ4NzUyMzljYzM2NzI2NGM4OTdhMzEyODZiNmEzYWI4ZmQ1YWM5M2M1NzBlOGExZjRlMWUwZDJiMWQwOGQ0MTEwMzA0ZDg1MjgyY2Y4MTZmNGRiMjRmMmYzNjZjOTkyNDMwZGFmMjM0YjJiZmM3YWQwMjA2OTRjNWU5YmUwMTUwMWUwNjZlMTAxZWM1NzI2ZjE5MWM4',
    # 'Host':'fanyi.baidu.com',
    # 'Origin':'https://fanyi.baidu.com/',
    # 'Referer':'https://fanyi.baidu.com/',
    # 'Sec-Ch-Ua':'"Not.A/Brand";v="8", "Chromium";v="114"',
    # 'Sec-Ch-Ua-Mobile':'?0',
    # 'Sec-Ch-Ua-Platform':'"Windows"',
    # 'Sec-Fetch-Dest':'empty',
    # 'Sec-Fetch-Mode':'cors',
    # 'Sec-Fetch-Site':'same-origin',
    # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36',
    # 'X-Requested-With':'XMLHttpRequest'
}

data = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url=url,data=data,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

obj = json.loads(content)

print(obj)

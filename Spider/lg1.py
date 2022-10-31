import json

import requests

url = 'https://jiaobenwang.com/wp-admin/admin-ajax.php'
url = 'https://jiaobenwang.com/wp-admin/admin-ajax.php'

head = {
    """
    POST /wp-admin/admin-ajax.php HTTP/3
Host: jiaobenwang.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: */*
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br

Cookie: wordpress_1c1f77de48fa74f1aa1ade161b8a0725=yysyzdnp%7C1667345200%7CnBc5NBYTcHXcTYw2Pa0GzObHWTPiiKt55Pz7ezYFmeb%7Cdacb9c106d759524dd10a83fd1a6922006b8d7a486593d958b897070b5bfaf6a; X_CACHE_KEY=9318a2057b722898ef1092b32b71d791; PHPSESSID=mirk4iuuuo5rqubg634usai2g2; Hm_lvt_d10552eaee0c3b28f92a28fb03a1bf88=1667172362; Hm_lpvt_d10552eaee0c3b28f92a28fb03a1bf88=1667172406; cao_notice_cookie=1; wordpress_logged_in_1c1f77de48fa74f1aa1ade161b8a0725=yysyzdnp%7C1667345200%7CnBc5NBYTcHXcTYw2Pa0GzObHWTPiiKt55Pz7ezYFmeb%7C7230af23d640bdb19bdde18283756307cf3065d2b657691d887670bb072844ce
    """

    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'X-Requested-With': 'XMLHttpRequest',
    # 'Content-Length': '19',
    'Origin': 'https://jiaobenwang.com',
    'Alt-Used': 'jiaobenwang.com',
    'Connection': 'keep-alive',
    'Referer': 'https://jiaobenwang.com/',
    # 'Cookie': 'X_CACHE_KEY=9318a2057b722898ef1092b32b71d791; Hm_lvt_d10552eaee0c3b28f92a28fb03a1bf88=1667172362,1667181189; cao_notice_cookie=1; PHPSESSID=8m8e5g1rodg0maq3lr6u50gjod; Hm_lpvt_d10552eaee0c3b28f92a28fb03a1bf88=1667181288; wordpress_test_cookie=WP%20Cookie%20check',
    # 'Cookie': 'wordpress_1c1f77de48fa74f1aa1ade161b8a0725=yysyzdnp%7C1667345200%7CnBc5NBYTcHXcTYw2Pa0GzObHWTPiiKt55Pz7ezYFmeb%7Cdacb9c106d759524dd10a83fd1a6922006b8d7a486593d958b897070b5bfaf6a; X_CACHE_KEY=9318a2057b722898ef1092b32b71d791; PHPSESSID=mirk4iuuuo5rqubg634usai2g2; Hm_lvt_d10552eaee0c3b28f92a28fb03a1bf88=1667172362; Hm_lpvt_d10552eaee0c3b28f92a28fb03a1bf88=1667172406; cao_notice_cookie=1; wordpress_logged_in_1c1f77de48fa74f1aa1ade161b8a0725=yysyzdnp%7C1667345200%7CnBc5NBYTcHXcTYw2Pa0GzObHWTPiiKt55Pz7ezYFmeb%7C7230af23d640bdb19bdde18283756307cf3065d2b657691d887670bb072844ce',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'TE': 'trailers',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'

}

data = {

    "action": "user_login",
    "username": "sch1532694569c@163.com",
    "password": "123456789c"

}

r = requests.post(url=url, headers=head, data=data)
# print(r.content)
res = json.loads(r.content)
print(res)

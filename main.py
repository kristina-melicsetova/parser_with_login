import requests
from bs4 import BeautifulSoup as BS

s = requests.Session()

# get CSRF
auth_html = s.get("https://smartprogress.do/")
auth_bs = BS(auth_html.content, "html.parser")
csrf = auth_bs.select("input[name=YII_CSRF_TOKEN]")[0]['value']


# do login
payload = {
    "YII_CSRF_TOKEN": csrf,
    "returnUrl": '/',
    "UserLoginForm[email]": "meliksetova02@bk.ru",
    "UserLoginForm[password]": "123987mar",
    "UserLoginForm[rememberMe]": 1

}
ans = s.post("https://smartprogress.do/user/login/", data=payload)
ans_bs = BS(ans.content, "html.parser")

print("Имя:{}\nУровень: {}\nОпыт: {}".format(
    ans_bs.select(".user-menu__name")[0].text.strip(),
    ans_bs.select(".user-menu__info-text--lvl")[0].text.strip(),
    ans_bs.select(".user-menu__info-text--exp")[0].text.strip(),
))

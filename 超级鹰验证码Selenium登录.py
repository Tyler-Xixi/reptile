import time

from selenium.webdriver import Chrome

from chaojiying import Chaojiying_Client

# 进入网站
web = Chrome()
url = 'http://www.chaojiying.com/user/login/'
web.get(url)

# 验证码识别提取
img = web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
chaojiying = Chaojiying_Client('tylerxixi', '1433233', '920741')
dic = chaojiying.PostPic(img, 1902)
Verification_Code = dic['pic_str']

# 用户，密码，验证码输入
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys('tylerxixi')
time.sleep(0.5)
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys('1433233')
time.sleep(0.5)
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(Verification_Code)
time.sleep(0.5)

# 进行登陆
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()

import time
from selenium.webdriver import Chrome
from chaojiying import Chaojiying_Client
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

# 嵌入游览器避开识别selenium自动化控制设置
option = Options()  # 将对象进行实例化
# 嵌入js反检测参数
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_argument("--disable-blink-features=AutomationControlled")

# 请求url
web = Chrome(options=option)
url = 'https://kyfw.12306.cn/otn/resources/login.html'
web.get(url)
time.sleep(2)

# 初始化超级鹰配置
chaojiying = Chaojiying_Client('tylerxixi', '1433233', '920741')
web.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a').click()
time.sleep(2)

# 处理图像验证码
img_elemnet_code = web.find_element_by_xpath('//*[@id="J-loginImg"]')
dic = chaojiying.PostPic(img_elemnet_code.screenshot_as_png, 9004)
value = dic['pic_str']

# 返回x1，y1，x2，y2...型坐标，将坐标进行拆分
img_code = value.split("|")
for code in img_code:
    x_y_code = code.split(",")
    x = int(x_y_code[0])
    y = int(x_y_code[1])
    ActionChains(web).move_to_element_with_offset(img_elemnet_code, x, y).click().perform()  # .perform将这个时间线进行上传

# 进行用户，密码，登陆
time.sleep(0.5)
# 用户
web.find_element_by_xpath('//*[@id="J-userName"]').send_keys("eqwewqeqe")
time.sleep(0.5)
# 密码
web.find_element_by_xpath('//*[@id="J-password"]').send_keys("1433233")
time.sleep(0.5)
# 登陆
web.find_element_by_xpath('//*[@id="J-login"]').click()
time.sleep(2)

# 进行滑块的拖拽工作

drgp = web.find_element_by_xpath('//*[@id="nc_1_n1z"]')
ActionChains(web).drag_and_drop_by_offset(drgp, 300, 0,).perform()
time.sleep(2)
web.find_element_by_xpath('//*[@id="J-slide-passcode"]/div/span/a').click()
time.sleep(2)

# 二次滑块验证
drgp_1 = web.find_element_by_xpath('//*[@id="nc_1_n1z"]')
ActionChains(web).drag_and_drop_by_offset(drgp_1, 300, 0,).perform()



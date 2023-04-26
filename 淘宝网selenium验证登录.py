import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains

t = time
web = Chrome()
url = 'https://login.taobao.com/member/login.jhtml?spm=a2e0b.20350158.1997563269.1.1c23468aOOuwDU&f=top&redirectURL=https%3A%2F%2Fuland.taobao.com%2Fsem%2Ftbsearch%3Frefpid%3Dmm_26632258_3504122_32538762%26keyword%3D%25E6%25B7%2598%25E5%25AE%259D%25E7%25BD%2591%2521%26clk1%3D0aa0bcf15bbb5fc52f3401ef434d9621%26upsId%3D0aa0bcf15bbb5fc52f3401ef434d9621&pid=mm_26632258_3504122_32538762&union_lens=recoveryid%3A201_11.15.136.35_13344196_1628410985491%3Bprepvid%3A201_11.15.136.35_13344196_1628410985491&clk1=0aa0bcf15bbb5fc52f3401ef434d9621'
web.get(url)
time.sleep(1)

# 用户，密码，登陆，操作
web.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys('2220597840@qq.com')
t.sleep(1)
web.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys('wosituxin200212.')
t.sleep(1)
web.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()
t.sleep(2)

# 滑块验证

drge = web.find_element_by_xpath('//*[@id="nc_2_n1z"]')
ActionChains(web).drag_and_drop_by_offset(drge, 300, 0).click().perform()
t.sleep(1)
web.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()

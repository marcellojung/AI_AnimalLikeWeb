from selenium import webdriver
from selenium.webdriver.common.by import By  # By.CSS_SELECTOR를 사용하기 위해 import google search 
from selenium.webdriver.chrome.options import Options
import time
import urllib.request
import requests

search = 'rabbitpicture'
fileName = f'{search}_image'
number = 120

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()

driver.get(f'https://www.google.com/search?q={search}&sca_esv=604fe53e2192f73a&rlz=1C5CHFA_enKR1004KR1004&udm=2&sxsrf=ADLYWIJepxRIhuV84ggVXFsFN3q7gRvCXA:1723705452502&source=lnt&tbs=sur:ol&sa=X&ved=2ahUKEwi-ksaZt_aHAxWEm68BHYPaJbAQpwV6BAgDECE&biw=1710&bih=908&dpr=2')
# firstImage = driver.find_element_by_css_selector('#islrg > div.islrc > div:nth-child(1) > a.wXeWr.islib.nfEiy.mM5pbd > div.bRMDJf.islir > img')

firstImage = driver.find_element(By.CSS_SELECTOR, '#rso > div > div > div.wH6SXe.u32vCb > div > div > div:nth-child(7) > div.czzyk.XOEbc > h3 > a > div > div > div > g-img > img')
firstImage.click()
for i in range(number):
    try:
    #1. 첫번째 이미지 클릭 
        time.sleep(1)   
        #2. 이미지 클릭 후 이미지 저장
        image = driver.find_element(By.CSS_SELECTOR, '#Sva75c > div.A8mJGd.NDuZHe > div.LrPjRb > div > div.BIB1wf.EIehLd.fHE6De.Emjfjd > c-wiz > div > div.v6bUne > div.p7sI2.PUxBg > a > img.sFlh5c.FyHeAf.iPVvYb')
        print(image.get_attribute('src'))
        #Sva75c > div.A8mJGd.NDuZHe > div.LrPjRb > div > div.BIB1wf.EIehLd.fHE6De.Emjfjd > c-wiz > div > div.v6bUne > div.p7sI2.PUxBg > a > img.sFlh5c.FyHeAf.iPVvYb
        imageSrc = image.get_attribute('src')
        # urllib.request.urlretrieve(imageSrc, f'cat_image_{i+1}.jpg')
        response = requests.get(imageSrc)
        with open(f'{fileName}_{i+1}.jpg', 'wb') as file:
            file.write(response.content)
        #3. next 버튼 클릭
    except:
        print(f'{i+1} failed!')
    else:
        print(f'{i+1} succeed!')
    finally:
        # time.sleep(100)
        # nextButton = driver.find_element(By.CSS_SELECTOR,'#Sva75c > div.A8mJGd.NDuZHe > div.LrPjRb > div > div.BIB1wf.EIehLd.fHE6De.Emjfjd > c-wiz > div > div.XQEEtd.VTMWGb > div > div.HJRshd > button:nth-child(2)')
        nextButton = driver.find_element(By.CSS_SELECTOR,'#Sva75c > div.A8mJGd.NDuZHe > div.LrPjRb > div > div.BIB1wf.EIehLd.fHE6De.Emjfjd > c-wiz > div > div.XQEEtd.VTMWGb > div > div.HJRshd > button:nth-child(2)')
        nextButton.click()
        #Sva75c > div.A8mJGd.NDuZHe > div.LrPjRb > div > div.BIB1wf.EIehLd.fHE6De.Emjfjd > c-wiz > div > div.XQEEtd.VTMWGb > div > div.HJRshd > button:nth-child(2)
        #Sva75c > div.A8mJGd.NDuZHe > div.LrPjRb > div > div.BIB1wf.EIehLd.fHE6De.Emjfjd > c-wiz > div > div.XQEEtd.VTMWGb > div > div.HJRshd > button:nth-child(2)
driver.quit()
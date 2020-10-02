
# coding: utf-8

# In[156]:


from selenium import webdriver
import pandas as pd
from selenium.common import exceptions
import csv
from selenium.webdriver.support.ui import WebDriverWait
import codecs
import pandas as pd


driver = webdriver.Firefox()  # Using firefox webdrive
driver.get(
       'http://f10.eastmoney.com/f10_v2/FinanceAnalysis.aspx?code=SZ000599#bfbbb-0')

driver.implicitly_wait(40)

q = driver.find_element_by_xpath('//span[@id="hq_1"]')
arr_title = []
for i in range(9):
    arr_title.append(q.text)
    

h = driver.find_element_by_xpath('//a[@id="lrb_a"]')
h.click()


d = driver.find_element_by_xpath('//ul[@id="lrb_ul"]/li[3]')
d.click()
driver.implicitly_wait(40)



arr_singleDate = []
singleDate =  driver.find_elements_by_xpath('//th[@class="tips-fieldname-Right"]/span')
length = len(singleDate)
for i in range(9) :
    print(singleDate[i].text)
    arr_singleDate.append(singleDate[i].text)
print(arr_singleDate)



driver.implicitly_wait(40)
arr_allcome = []
allcome = driver.find_elements_by_xpath('//table[@id="report_lrb"]/tbody/tr[2]/*/span')
length = len(allcome)
for i in range(1,6) :
    print(allcome[i].text)
    arr_allcome.append(allcome[i].text)
for i in range(4):
    arr_allcome.append("")
    

driver.implicitly_wait(40)
arr_profit = []
profit = driver.find_elements_by_xpath('//table[@id="report_lrb"]/tbody/tr[37]/*/span')
for i in range(1,6) :
    print(profit[i].text)
    arr_profit.append(profit[i].text)
for i in range(4):
    arr_profit.append("")



c = driver.find_element_by_xpath('//ul[@id="lrb_ul"]/li[4]')
c.click()
driver.implicitly_wait(60)
arr_allcome1 = []
allcome1 = driver.find_elements_by_xpath('//table[@id="report_lrb"]/tbody/tr[2]/*/span')
length = len(allcome1)
for i in range(1,6):
    print(allcome1[i].text)
    arr_allcome1.append(allcome1[i].text)
for i in range(4):
    arr_allcome1.append("")


arr_profit1 = []
profit1 = driver.find_elements_by_xpath('//table[@id="report_lrb"]/tbody/tr[37]/*/span')
length = len(profit1)
for i in range(1,6) :
    print(profit1[i].text)
    arr_profit1.append(profit1[i].text)
for i in range(4):
    arr_profit1.append("")
    

e = driver.find_element_by_xpath('//a[@id="bfbbb_a"]')
e.click()
driver.implicitly_wait(40)
arr_asserts = []
asserts = driver.find_elements_by_xpath('//table[@id="AssetStatementTable"]/tbody/tr[2]/*/span')
length = len(asserts)
for i in range(1,2):
    print(asserts[i].text)
    arr_asserts.append(asserts[i].text)
for i in range(8):
    arr_asserts.append("")
    

arr_capital = []
capital = driver.find_elements_by_xpath('//table[@id="AssetStatementTable"]/tbody/tr[4]/*/span')
length = len(capital)
for i in range(1,2):
    print(capital[i].text)
    arr_capital.append(capital[i].text)
for i in range(8):
    arr_capital.append("")
    

arr_receivables = []
receivables = driver.find_elements_by_xpath('//table[@id="AssetStatementTable"]/tbody/tr[5]/*/span')
for i in range(1,2):
    print(receivables[i].text)
    arr_receivables.append(receivables[i].text)
for i in range(8):
    arr_receivables.append("")
    

arr_inventary = []
inventary = driver.find_elements_by_xpath('//table[@id="AssetStatementTable"]/tbody/tr[6]/*/span')
for i in range(1,2):
    print(inventary[i].text)
    arr_inventary.append(inventary[i].text)
for i in range(8):
    arr_inventary.append("")
    

b = driver.find_element_by_xpath('//li[@data-type="0"]')
b.click()
driver.implicitly_wait(40)
arr_should = []
should = driver.find_elements_by_xpath('//tr[@data-index="27"]/*/span')
length = len(should)
for i in range(1,10) :
    print(should[i].text)
    arr_should.append(should[i].text)
    

day = driver.find_elements_by_xpath('//tr[@data-index="28"]/*/span')
length = len(day)
arr_day = []
for i in range(1,10) :
    print(day[i].text)
    arr_day.append(day[i].text)
    


dataframe = pd.DataFrame({'标题': arr_title,'日期':arr_singleDate, '总收入': arr_allcome, '净利润':arr_profit, '总收入':arr_allcome1,
                          '净利润':arr_profit1, '总资产':arr_asserts, '货币资金':arr_capital, '应收账款':arr_receivables, 
                          '存货':arr_inventary, '应收账款周转天数':arr_should, '存款周转天数':arr_day})
dataframe.to_csv("/Users/luoshanshan/Desktop/2.csv", index=False, sep=',', encoding='utf-8-sig')
    


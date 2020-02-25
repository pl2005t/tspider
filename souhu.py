from selenium import webdriver
driver=webdriver.PhantomJS(executable_path=r'D:\soft\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.get('http://news.sohu.com/scroll/')
print(driver.find_element_by_class_name('title').text)
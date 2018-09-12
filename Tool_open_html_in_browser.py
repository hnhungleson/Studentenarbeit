from selenium import webdriver
import time


driver = webdriver.Chrome("/home/hung/chromedriver")
driver.get("file:///home/hung/AnacondaProjects/Studentenarbeit/Munich_with_points_and_lines.html")
it = 0

for i in range(10):
    driver.refresh()
    time.sleep(5)
    it += 1

driver.quit()
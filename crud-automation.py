import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoqa.com/webtables")

def clickButton(id) -> None:
    driver.find_element(By.ID, id).click()


def fillForm(dataContext, request='insert') -> None:
    for i in range(0, len(dataContext)):
        key = list(dataContext.keys())[i]
        elem = driver.find_element(By.ID, key)
        if request == "update":
            elem.clear()
        elem.send_keys(dataContext[key])


def updateTitle(newTitle):
  driver.execute_script(f"document.title = '{newTitle}'")
  
insertData = {
    "firstName": "Samarth",
    "lastName": "Shah",
    "userEmail": "samarthshah992@gmail.com",
    "age": "22",
    "salary": "30000",
    "department": "Software Engineer",
}

insertData2 = {
    "firstName": "Yash",
    "lastName": "Panchal",
    "userEmail": "Yash123@gmail.com",
    "age": "22",
    "salary": "30000",
    "department": "Software Engineer",
}

updateData = {
    "firstName": "Dhwani",
    "lastName": "Mittal",
    "userEmail": "Dhwani@gmail.com",
    "age": "20",
    "salary": "30000",
    "department": "Software Engineer",
}

# Inserting 2 new entries:

updateTitle("Inserting data")
clickButton("addNewRecordButton")
fillForm(insertData)
clickButton("submit")

clickButton("addNewRecordButton")
fillForm(insertData2)
clickButton("submit")

# Deleting the entry 2 and 3:
updateTitle("Deleting data")

clickButton("delete-record-2")
clickButton("delete-record-3")

# Updating the entry 1:
updateTitle("Updating data")
clickButton("edit-record-1")
fillForm(updateData, "update")
clickButton("submit")

time.sleep(5)
driver.close()

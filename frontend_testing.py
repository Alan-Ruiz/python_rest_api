from selenium import webdriver
from selenium.webdriver.common.by import By

def test_frontend(user_id):
    driver = webdriver.Chrome()  # Ensure you have the correct WebDriver for your browser
    url = f'http://127.0.0.1:5001/users/get_user_data/{user_id}'
    driver.get(url)

    try:
        user_name_element = driver.find_element(By.ID, 'user_name')
        print(f"User name: {user_name_element.text}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

if __name__ == '__main__':
    test_frontend(1)  # Change the user_id as needed
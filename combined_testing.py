import requests
import db_connector as db
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_combined():
    user_id = 2
    user_name = "george"
    
    # Test POST
    response = requests.post(f'http://127.0.0.1:5000/users/{user_id}', json={"user_name": user_name})
    assert response.status_code == 200, "POST request failed"
    
    # Test GET
    response = requests.get(f'http://127.0.0.1:5000/users/{user_id}')
    assert response.status_code == 200, "GET request failed"
    assert response.json()['user_name'] == user_name, "GET request returned incorrect data"
    
    # Test DB
    db_user = db.get_user(user_id)
    assert db_user['user_name'] == user_name, "Database data does not match"
    
    # Test frontend
    driver = webdriver.Chrome()  # Ensure you have the correct WebDriver for your browser
    url = f'http://127.0.0.1:5001/users/get_user_data/{user_id}'
    driver.get(url)

    try:
        user_name_element = driver.find_element(By.ID, 'user_name')
        assert user_name_element.text == user_name, "Frontend data does not match"
    except Exception as e:
        print(f"Error: {e}")
        raise Exception("test failed")
    finally:
        driver.quit()

if __name__ == '__main__':
    test_combined()
import requests
import db_connector as db

def test_backend():
    user_id = 1
    user_name = "john"
    
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

if __name__ == '__main__':
    test_backend()
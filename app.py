#Hai from folder 2 

import requests
import json


def get_request(url, headers=None, params=None):
    """
    Make a GET request to the specified URL.
    
    Args:
        url: The API endpoint URL
        headers: Optional dictionary of headers
        params: Optional query parameters
    
    Returns:
        Response JSON or None if error
    """
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"GET request failed: {e}")
        return None


def post_request(url, data=None, json_data=None, headers=None):
    """
    Make a POST request to the specified URL.
    
    Args:
        url: The API endpoint URL
        data: Form data to send
        json_data: JSON data to send
        headers: Optional dictionary of headers
    
    Returns:
        Response JSON or None if error
    """
    try:
        response = requests.post(url, data=data, json=json_data, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"POST request failed: {e}")
        return None


def put_request(url, json_data=None, headers=None):
    """
    Make a PUT request to the specified URL.
    
    Args:
        url: The API endpoint URL
        json_data: JSON data to send
        headers: Optional dictionary of headers
    
    Returns:
        Response JSON or None if error
    """
    try:
        response = requests.put(url, json=json_data, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"PUT request failed: {e}")
        return None


def delete_request(url, headers=None):
    """
    Make a DELETE request to the specified URL.
    
    Args:
        url: The API endpoint URL
        headers: Optional dictionary of headers
    
    Returns:
        Response JSON or None if error
    """
    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"DELETE request failed: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Example: GET request to a public API
    print("=== GET Request Example ===")
    result = get_request("https://jsonplaceholder.typicode.com/posts/1")
    if result:
        print(json.dumps(result, indent=2))
    
    print("\n=== POST Request Example ===")
    # Example: POST request with JSON data
    new_post = {
        "title": "My New Post",
        "body": "This is the content of my post",
        "userId": 1
    }
    result = post_request(
        "https://jsonplaceholder.typicode.com/posts",
        json_data=new_post
    )
    if result:
        print(json.dumps(result, indent=2))
    
    print("\n=== PUT Request Example ===")
    # Example: PUT request to update data
    updated_post = {
        "id": 1,
        "title": "Updated Title",
        "body": "Updated content",
        "userId": 1
    }
    result = put_request(
        "https://jsonplaceholder.typicode.com/posts/1",
        json_data=updated_post
    )
    if result:
        print(json.dumps(result, indent=2))
    
    print("\n=== DELETE Request Example ===")
    # Example: DELETE request
    result = delete_request("https://jsonplaceholder.typicode.com/posts/1")
    print(f"Delete result: {result}")

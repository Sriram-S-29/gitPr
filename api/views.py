"""
Django REST API Views
Basic API endpoints demonstrating GET, POST, PUT, DELETE operations.
"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
import json
import os


# In-memory data store for demo purposes
ITEMS = {
    1: {"id": 1, "name": "Item One", "description": "First item"},
    2: {"id": 2, "name": "Item Two", "description": "Second item"},
    3: {"id": 3, "name": "Item Three", "description": "Third item"},
}


@api_view(['GET'])
def get_all_items(request):
    """
    GET /api/items/
    Retrieve all items.
    """
    return Response(list(ITEMS.values()), status=status.HTTP_200_OK)


@api_view(['GET'])
def get_item(request, item_id):
    """
    GET /api/items/<id>/
    Retrieve a single item by ID.
    """
    if item_id in ITEMS:
        return Response(ITEMS[item_id], status=status.HTTP_200_OK)
    return Response(
        {"error": "Item not found"}, 
        status=status.HTTP_404_NOT_FOUND
    )


@api_view(['POST'])
def create_item(request):
    """
    POST /api/items/
    Create a new item.
    Request body: {"name": "string", "description": "string"}
    """
    data = request.data
    if not data.get('name'):
        return Response(
            {"error": "Name is required"}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    new_id = max(ITEMS.keys()) + 1 if ITEMS else 1
    new_item = {
        "id": new_id,
        "name": data.get('name'),
        "description": data.get('description', '')
    }
    ITEMS[new_id] = new_item
    return Response(new_item, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def update_item(request, item_id):
    """
    PUT /api/items/<id>/
    Update an existing item.
    Request body: {"name": "string", "description": "string"}
    """
    if item_id not in ITEMS:
        return Response(
            {"error": "Item not found"}, 
            status=status.HTTP_404_NOT_FOUND
        )
    
    data = request.data
    ITEMS[item_id].update({
        "name": data.get('name', ITEMS[item_id]['name']),
        "description": data.get('description', ITEMS[item_id]['description'])
    })
    return Response(ITEMS[item_id], status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_item(request, item_id):
    """
    DELETE /api/items/<id>/
    Delete an item.
    """
    if item_id not in ITEMS:
        return Response(
            {"error": "Item not found"}, 
            status=status.HTTP_404_NOT_FOUND
        )
    
    deleted_item = ITEMS.pop(item_id)
    return Response(
        {"message": "Item deleted", "item": deleted_item}, 
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
def save_items(request):
    """
    POST /api/save/
    Save all items to a JSON file.
    """
    # Get the directory where the file should be saved
    save_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'items_data.json')
    
    try:
        with open(save_path, 'w') as f:
            json.dump(list(ITEMS.values()), f, indent=2)
        
        return Response({
            "message": "Items saved successfully",
            "file": save_path,
            "items_count": len(ITEMS)
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"error": f"Failed to save items: {str(e)}"}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def external_api_call(request):
    """
    GET /api/external/
    Example of calling an external API from Django.
    """
    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/posts/1"
        )
        response.raise_for_status()
        return Response(response.json(), status=status.HTTP_200_OK)
    except requests.exceptions.RequestException as e:
        return Response(
            {"error": str(e)}, 
            status=status.HTTP_502_BAD_GATEWAY
        )

import pytest
import search_books 
import unittest.mock as mock

@mock.patch("requests.get")
def test_fetch_books_by_title(mock_get):
    # Mock response from the API
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"items": [{"volumeInfo": {"title": "The Alchemist", "authors": ["Paulo Coelho"], "publishedDate": "2015-02-24"}}]}
    
    # Set the mock_get return value to the mock_response
    mock_get.return_value = mock_response
    
    # Call the function under test
    result = search_books.fetch_books_by_title('The Alchemist')
    
    # Assert the result
    assert result == {}

@mock.patch("requests.get")
def test_fetch_books_by_author(mock_get):
    
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"items": [{"volumeInfo": {"title": "12 Rules for Life", "authors": ["Jordan B. Peterson"], "publishedDate": "2018-01-23"}}]}

    mock_get.return_value = mock_response

    result = search_books.fetch_books_by_author('Jordan Peterson')

    assert result == {"items": [{"volumeInfo": {"title": "12 Rules for Life", "authors": ["Jordan B. Peterson"], "publishedDate": "2018-01-23"}}]}



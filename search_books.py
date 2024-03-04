import os, requests


#define the base url to call the Google books API
base_url = 'https://www.googleapis.com/books/v1/volumes'


def fetch_books_by_title(title_name):
    '''
    This fuctions will call the Google Books API and
    return json output based on books
    
    '''
    #setting up url parameters, setting maxResults so only 5 book are returned
    params = {
        'q':f'intitle:{title_name}',
        'maxResults':'5',
        'key': os.environ.get('GOOGLE_API_KEY')
    }

    #running a try except if their is an issue with API Request
    try:
        response = requests.get(base_url,params=params)
        return response.json()
    
    except requests.exceptions.RequestException as err:

        print(f"API Connection Failed with following error: {err}")
        return None

def fetch_books_by_author(author_name):

    '''
        This fuction will fetch the books data via the author name.

    '''
    params = {
        'q':f'inauthor:{author_name}',
        'maxResults':'40', #This is the max number of results that google books API will return, anything above will give an error.
        'key':os.environ.get('GOOGLE_API_KEY')
    }

    try:
        response = requests.get(base_url,params=params)
        return response.json()
    
    except requests.exceptions.RequestException as err:

        print(f"API Connection Failed with following error: {err}")
        return None
    
def fetch_books_by_author_year(author_name, year):

    '''
        This fuction returns will search book data for the given author in that given year. 
    
    '''
    #Calling the fetch_books_by_author to bring in json data for the author
    author_books = fetch_books_by_author(author_name)

    #intialzing an empty list so we can add the books into this list
    search_list = []
    
    #Checking if fetch_books_by_author returned none
    if author_books:
        #checking if fetch_books_by_author returs "totalItems": 0, this implies that the API call was
        #sucessfull but serach result did not return anything
        if not author_books.get('totalItems') == 0:
            for book in author_books.get('items'):
                #Chekcing if book has a publishedDate key
                if book['volumeInfo'].get('publishedDate'):
                    #get the year from the publishedDate via split
                    if book['volumeInfo'].get('publishedDate').split('-')[0] == year:
                        search_list.append(book)
        else:
            # Returning the following if JSON totalItems == 0 to feed to print_book_results  
            return {'totalItems': 0}
    else: 
        return None

    #Cheking if the list for books is empty which implies that there were no books for that author in given year.
    if len(search_list) != 0: 
        return {'items':search_list}
    else:
        return {'totalItems': 0}


def print_book_results(books_json_output):

    '''
    This fuction will parse the json output and 
    will print some of the data related to defined search
    
    '''
    #checking if API json file returs "totalItems": 0, this implies that the API call was
    #sucessfull but serach result did not return anything

    if not books_json_output.get('totalItems') == 0:
        for book in books_json_output['items']:

            print('---------------------------------------------')
            print(f"Title: {book['volumeInfo']['title']}")

            #Checking if the key I am looking for exists
            if book['volumeInfo'].get('authors') == None:
                print("No Author added for this book")
            else:
                print(f"Author: {book['volumeInfo']['authors'][0]}")
            
            if book['volumeInfo'].get('publishedDate') == None:
                print("No Published date provided for this book")
            else:
                print(f"Published Date: {book['volumeInfo']['publishedDate']}")

            if book['volumeInfo'].get('categories') == None:
                print("Book Genre not defined!")
            else:
                print(f"Genre: {book['volumeInfo'].get('categories')[0]}")

            if (book['volumeInfo'].get('pageCount') == None) or (book['volumeInfo'].get('pageCount') == 0):
                print("No number of pages defined for this book")
            else:
                print(f"Pages: {book['volumeInfo']['pageCount']}")    
            
            print()
    else:
        print("No Books found")
        print()



from search_books import fetch_books_by_title, fetch_books_by_author, fetch_books_by_author_year, print_book_results

'''
Setting up the console app for the user's to interact. 

'''

print("Welcome to Book Search app with Goolge API")


#While loop for continued app run
while True:

    #Setup Menu options
    print('#######################################################')
    print("Please select one of the following options: ")
    print("1 - Search Book by title")
    print("2 - Search Books by the Author Name")
    print("3 - Search Books by Author and their books in Year")
    print("0 - Exit the Application")
    print('#######################################################')
    print()

    option = input("Enter your option: ")

    if option == '1':
        title = input("Enter the title name: ")
        books_by_title =  fetch_books_by_title(title_name=title)

        #check if any functions from search_books has returned none
        if books_by_title:
            print_book_results(books_by_title)
        else:
            break

    elif option == '2':
        author = input("Enter the Author name: ")

        books_by_author = fetch_books_by_author(author)

        if books_by_author:
            print_book_results(books_by_author)
        else:
            break

    elif option == '3':
        author_name = input("Enter the Author name: ")
        year = input("Enter the Year: ")
        books_by_author_year = fetch_books_by_author_year(author_name=author_name,year=year)

        if books_by_author_year:
            print_book_results(books_by_author_year)
        else:
            break

    elif option == '0':
        break

    else:
        print("Invalid option selected")
        print()
    

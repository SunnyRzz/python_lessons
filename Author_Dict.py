books_dict = {"J K Rowling": ['Harry Potter and the Philosopher\'s Stone (1997)','Harry Potter and the Chamber of Secrets (1998)','Harry Potter and the Prisoner of Azkaban (1999)', 'Harry Potter and the Goblet of Fire (2000)', 'Harry Potter and the Order of the Phoenix (2003), Harry Potter and the Half-Blood Prince (2005)', 'Harry Potter and the Deathly Hallows (2007)'], "Phillip Pullman":["The Golden Compass","The Subtle Knife","The Amber spyglass"], "George RR Martin": ["A Game of Thrones", "A Clash of Kings"]}

author_name = input("Please input the Author name: ")
if author_name in books_dict:
    books_list = ", ".join(books_dict[author_name])
    print(f"Books by {author_name} include: {books_list}")
else:
    print(f"Author {author_name} cannot be found in the Dictionary")
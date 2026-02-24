import streamlit as st  # type: ignore

st.title("Mine mini libreary app")

if "books" not in st.session_state:
    st.session_state.books = []

st.header("add book")
title = st.text_input("Title")
author = st.text_input("Author")
price = st.number_input("Price", min_value=0.0)
if st.button("Add book"):
    book ={
        "title": title,
        "author": author,
        "price": price 
    }
    st.session_state.books.apend(book)
    st.success("Book is added")
if len(st.session_state.books) == 0:
    st.write("No added books")
else: 
    st.write("Title", book["title"])
    st.write("Author", book["author"])
    st.write("Price", book["price"])
    st.write("-------------------")

    st.header("Author search")
    search_author = st.text_input("Enter authors name")
    if st.button("Search author"):
        found = False 
    for book in st.session_state.books:
        if book["author"] == search_author:
            st.write(book)
            found = True
            if found == False:
                st.write("Not found from this author")

st.header("search by title ")
search_title = st.text_input("enter title")
if st.button("Search title"):
        found = False 
        for book in st.session_state.books:
            if book["title"] == search_title:
             st.write(book)
            found = True
            if found == False:
                st.write("Title not found")

if st.button("show the cheapest"):
    if len(st.session_state.books) == 0:
        st.write("No books")
    else:
        cheapest = st.session_state.books[0]

        for book in st.session_state.books:
            if book["price"] < cheapest["price"]:
                cheapest = book
                st.write("The cheapest book is ")
                st.write(cheapest)



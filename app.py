import streamlit as st

#setup 
st.title("Christmas lists wonder-app")

tab1, tab2 = st.tabs(["Write your own list", "View other people's lists"])

import streamlit as st

#function to save script to a text file
def save_items_to_file(items):
    with open("items_list.txt", "w") as file:
        for item in items:
            file.write(f"{item}\n")
    st.success("Your list has been updated!")

#5 empty boxes on the 'your list' tab
if 'num_boxes' not in st.session_state:
    st.session_state.num_boxes = 5 

if 'items' not in st.session_state:
    st.session_state.items = [] 

#tab for adding items to your own Christmas list 
with tab1:
    st.header("Your Christmas list")

    #user inputs their name     
    name = st.text_input("What is your name?")

    if name:
        st.write(f"Welcome, {name}!")
        
        st.write("Please enter items for your Christmas list:")

        #item box
        new_item = st.text_input('Enter an item for your list')

        if st.button('Add to my list'):
            if new_item:
                st.session_state.items.append(new_item)
                st.success("Added!")
            else:
                st.warning("Please enter something")

        st.write("Your current list:")
        st.write(st.session_state.items)

        #button to save the list to a file 
        if st.button("Save my list"):
            if st.session_state.items:
                with open ("items_list.txt", "w") as file:
                    for item in st.session_state.items:
                        file.write(f"{item}\n")
                st.success("Your list has been saved!")
            else:
                st.warning("Your list is empty. Please add items before saving")

with tab2:
    st.header("Other people's Christmas lists")

    #all names for buttons
    all_names = ["Lizzie", "Ruth", "Cathy", "Charles", "Katharine", "Geraldine", 
             "Josie", "Ellen"]

    #show buttons for the people who aren't the current user
    if name in all_names:
        buttons_to_show = [n for n in all_names if n != name]

        for button in buttons_to_show:
            if st.button(button):
                st.write(f"You are viewing {button}'s list")
        else:
            st.write("Have you misspelt your name?")




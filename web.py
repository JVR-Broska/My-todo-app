import streamlit as st
import functions
import random

test121 = ["b", "a"]
todos = functions.get_todos()

def add_todo():
    if st.session_state["new_todo"] != "":
        todo = st.session_state["new_todo"] + "\n"
        todos.append(todo)
        functions.write_todos(todos)


random_message = random.choice(["This app to to increase your productivity.",
                           "Enjoy our functions!", "What's up for today?", "Let's make some plans!"])

st.title("My Todos App")
st.subheader("This is my todo app")
st.write(random_message)

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()



st.session_state

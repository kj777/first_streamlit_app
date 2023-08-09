import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# ここに選択リストを置き、含めたい果物を選択できるようにしましょう。
fruits_selected = streamlit.multiselect("Pick some Fruits:", list(my_fruit_list.index), ['Avocado','Strawberries']) 
fruits_to_show = my_fruit_list.loc[fruit_selected]

# ページにテーブルを表示します。
streamlit.dataframe(fruits_to_show)

import streamlit 
import pandas
import requests
import snowflake.connector
#from urllib.error import URLError

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text(' Kale, Spinach & Rocket Smoothie')

streamlit.text('\N{chicken}  Hard-Boiled Free-Range Egg')

streamlit.header('\N{banana}  Build your Own Fruit Smoothie' )

#Fruit list 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show  = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

#streamlit.header("Fruityvice Fruit Advice!")


#try:
 #   fruit_choice = streamlit.text_input('What fruit would you like information about?')
 #   if not fruit_choice:
 #      streamlit.error("Please sekect a fruit to get information.")
 #  else:
#    fruitvice_response = request.get("https://fruityvice.com/api/fruit/" + fruit_choice)
 #    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  #   streamlit.dataframe(fruityvice_normalized)





#import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)


#my_cur.execute("insert into fruit_load_list values ('from streamlit')")

# takes the json version of the reponse and normalize it 

# output it the screen as a table


streamlit.dataframe(fruits_to_show)
#dont run anything past here while we troubleshoot


#New section to display fruitvice api response 
streamlit.header('Fruitvice Fruit Advice!')
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
streamlit.stop()
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)


add_my_fruit = streamlit.text_input('What fruit would you like to add?')
streamlit.write('The user entered ', add_my_fruit)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + add_my_fruit)
streamlit.write('Thanks for adding ', add_my_fruit)
my_cur.execute("insert into fruit_load_list values ('from streamlit')")


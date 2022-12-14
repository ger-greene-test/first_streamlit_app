import streamlit 
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text(' Kale, Spinach & Rocket Smoothie')

streamlit.text('\N{chicken}  Hard-Boiled Free-Range Egg')

streamlit.header('\N{banana}  Build your Own Fruit Smoothie' )

#Fruit list 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include -- this is the table in the middle 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show  = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)


#streamlit.header("Fruityvice Fruit Advice!")
#Lesson 9 python 

#fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
#streamlit.write('The user entered ', fruit_choice)

##New new
#New Section to display fruityvice api response
#streamlit.header('Fruityvice Fruit Advice!!')
#try:
  #  fruit_choice = streamlit.text_input('What fruit would you like information about?')
 #   if not fruit_choice:
   #    streamlit.error("Please select a fruit to get information.")
    #else:
     #fruitvice_response = request.get("https://fruityvice.com/api/fruit/" + fruit_choice)
     #fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
     #streamlit.dataframe(fruityvice_normalized)
        
        
#create the repeatable coe block (called a function)
def get_fruityvice_data(this_fruit_choice):
	fruitvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
	fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
	return fruityvice_normalized

#New section to display API RESPONSE 
streamlit.header('Fruityvice Fruit Advice!!')
try:
	fruit_choice = streamlit.text_input('What fruit would you like information about?')
	if not fruit_choice:
		streamlit.error("Please select a fruit to get information.")
	else:
		back_from_function = get_fruityvice_data(fruit_choice)
		streamlit.dataframe(back_from_function)    
		
except URLError as e:
    	streamlit.error()

#except URLError as e:
#streamlit.error()
#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)

# write your own comment -what does the next line do? 
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())  #kust writes the data to the screen
# write your own comment - what does this do?
#streamlit.dataframe(fruityvice_normalized)

#streamlit.stop()

#bolt in snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")  #runs query vs snowflake table
my_data_rows = my_cur.fetchall()   # fetches results from query
my_cnx.close()
streamlit.header("View Our Fruit List - Add Your Favorites!")
streamlit.dataframe(my_data_rows)  # displays on ui

#bottom of page what fruit to add

##new allow end user ti add a fruit to the list 
def insert_row_snowflake( new_fruit):
	with my_cnx.cursor() as my_cur:
		my_cur.execute("insert into fruit_load_list values ('"+ new_fruit +"')")
		return "Thanks for adding " + new_fruit
add_my_fruit = streamlit.text_input('What fruit would you like to add')
if streamlit.button('Add a Fruit to the List'):
	my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
	back_from_function = insert_row_snowflake(add_my_fruit)
	streamlit.text(back_from_function)
my_cnx.close()
streamlit.write('The user entered ', add_my_fruit)

#my_cur.execute("insert into fruit_load_list values ('from streamlit')")

#try:
 #   fruit_choice = streamlit.text_input('What fruit would you like information about?')
 #   if not fruit_choice:
 #      streamlit.error("Please sekect a fruit to get information.")
 #  else:
#    fruitvice_response = request.get("https://fruityvice.com/api/fruit/" + fruit_choice)
 #    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  #   streamlit.dataframe(fruityvice_normalized)





#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)


#my_cur.execute("insert into fruit_load_list values ('from streamlit')")

# takes the json version of the reponse and normalize it 

# output it the screen as a table



#dont run anything past here while we troubleshoot


#New section to display fruitvice api response 
#streamlit.header('Fruitvice Fruit Advice!')
#fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
#streamlit.write('The user entered ', fruit_choice)

#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("select * from fruit_load_list")
#my_data_rows = my_cur.fetchall()
#streamlit.header("The fruit load list contains:")
#streamlit.dataframe(my_data_rows)
#streamlit.stop()

#add_my_fruit = streamlit.text_input('What fruit would you like to add?')
#streamlit.write('The user entered ', add_my_fruit)

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + add_my_fruit)
#streamlit.write('Thanks for adding ', add_my_fruit)
#my_cur.execute("insert into fruit_load_list values ('from streamlit')")


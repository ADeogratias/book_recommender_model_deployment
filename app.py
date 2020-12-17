import streamlit as st
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model

# ratings_df = pd.read_csv("D:/School Related Documents and Apps/4th Year/Machine Learning/books-host/book_recommender_model_deployment/dataset/ratings.csv")
# books_df = pd.read_csv("D:/School Related Documents and Apps/4th Year/Machine Learning/books-host/book_recommender_model_deployment/dataset/books.csv")

st.title("Books Recommender System")
html_temp = """
	<div style="background-color:black;padding:10px">
	<h3 style="color:white;text-align:center;">Machine Learning</h3>
	</div>
	<div>
	<h3 style="color:black;text-align:center;">Done By </h3>
	<p style="color:black;text-align:center;">Deogratias Amani</p>
	<p style="color:black;text-align:center;">Keras is here yeeeaaahhh</p>
	
	"""
st.markdown(html_temp,unsafe_allow_html=True)

# st.dataframe(ratings_df)

# b_id =list(ratings_df.book_id.unique())
# b_id.remove(10000)
# book_arr = np.array(b_id)



# user_input =st.number_input("Enter user Id here for books recommendations",1, len(b_id),1)
# st.write("***Input***" , user_input)


# st.write(len(user))
# st.write(len(b_id))
# 
# model_file = "model.h5"
model = load_model( 'model.h5', compile = False )
# model = load_model(model)


# if st.button("Predict"):
# 	user = np.array([user_input for i in range(len(b_id))])
# 	pred = model.predict([book_arr, user])
# 	pred = pred.reshape(-1)
# 	pred_ids = (-pred).argsort()[0:5]

# 	st.write(books_df.iloc[pred_ids].title)

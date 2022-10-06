
import streamlit as st
from textblob import TextBlob

def main():
    # title
    st.title("This is my sentiment analysis app")
    st.subheader("Hello World")

    # sentiment
    message = st.text_area("Enter Text Here")
    if st.button("Analyze"):
        blob = TextBlob(message)
        result_sentiment = blob.sentiment
        st.success(result_sentiment)
    
    st.sidebar.subheader("About the App")
    st.sidebar.text("NLP for everyone.")

if __name__ == '__main__':
    main()
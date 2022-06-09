import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    ps = PorterStemmer()
    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.set_page_config(page_title="SMS Spam Classifier")

hide_streamlit_style = """<style>
                            #MainMenu {visibility: hidden;}
                            footer {visibility: hidden;}
                            </style>"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title('SMS Spam Classifier')

st.markdown('Spam messages are messages sent to a large group of recipients without their prior consent, '
            'typically advertising for goods and services or business opportunities. '
            'In the recent period, the percentage of scam messages amongst spam have increased sharply. '
            'Scam messages typically trick people into giving away money or personal '
            'details by offering an attractive or false deal.', unsafe_allow_html=False)

st.markdown('**A spam message classification is a step towards building a tool for scam message '
            'identification and early scam detection.**', unsafe_allow_html=False)

input_sms = st.text_area('Enter Message')

if st.button('Predict'):
    transform_sms = transform_text(input_sms)

    vector_input = tfidf.transform([transform_sms])

    result = model.predict(vector_input)[0]

    if result == 1:
        st.header('spam')
    else:
        st.header('Not Spam')

html_link = """
    <a href="https://github.com/rjtprasad/SMS-Spam-Classifier" style="color:green;" target="_blank">Github</a><br>
    <a href="https://www.linkedin.com/in/prasadrajat/" style="color:green;" target="_blank">LinkedIn</a>
    """

st.markdown(html_link, unsafe_allow_html=True)
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


st.title('SMS Spam Classifier')
st.markdown('Spam messages are messages sent to a large group of recipients without their prior consent, '
            'typically advertising for goods and services or business opportunities. '
            'In the recent period, the percentage of scam messages amongst spam have increased sharply. '
            'Scam messages typically trick people into giving away money or personal '
            'details by offering an attractive or false deal.', unsafe_allow_html=False)

st.markdown('**A spam message classification is a step towards building a tool for scam message '
            'identification and early scam detection.**', unsafe_allow_html=False)

input_sms = st.text_area('Enter SMS')

if st.button('Predict'):
    transform_sms = transform_text(input_sms)

    vector_input = tfidf.transform([transform_sms])

    result = model.predict(vector_input)[0]

    if result == 1:
        st.header('spam')
    else:
        st.header('Not Spam')


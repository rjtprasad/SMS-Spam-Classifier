# SMS-Spam-Classifier
Spam messages are messages sent to a large group of recipients without their prior consent, typically advertising for goods and services or business opportunities. In the recent period, the percentage of scam messages amongst spam have increased sharply. Scam messages typically trick people into giving away money or personal details by offering an attractive or false deal.

A spam message classification is a step towards building a tool for scam message identification and early scam detection. In this project, I build a end to end SMS Classifier that classifying a message into spam or ham and deploy on heroku.

Dataset is taken from [kaggle](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset) and it contains set of SMS messages in English of 5,572 messages, tagged acording being ham (legitimate) or spam.

I used various machine learning algorithms to classify the text message and compared accuracy set across these models. Naive Bayes classifier gives the best result among all with an accuracy of over 97%. This article provides an overview of using different techniques to classify a text message as “spam” or “not”.Further, we can use deep learning models, LSTM and Bi-LSTM to get a better result.

![image](https://user-images.githubusercontent.com/54785312/172826241-ff4b3e18-bb09-40a3-974e-88ce18df6545.png)

For Demo: https://sms--spam--classifier.herokuapp.com

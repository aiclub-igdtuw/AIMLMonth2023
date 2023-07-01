Roll Number       :   23006 

Student Name      :   Aanya Singh Dhaka 

Project Title     :  Twitter Sentiment Analysis

Google Colab Link :  https://colab.research.google.com/drive/1wzDaD23s6K5I5R2K6nMqSpc3lX9CL6Mz?usp=sharing

Summary: This minor project focused on sentiment analysis using the Sentiment140 dataset, which contains tweets labeled with sentiment values. The objective was to develop a model that could predict the sentiment of a given tweet or sentence.

The project involved several essential steps. Firstly, the dataset was preprocessed to clean the text and remove any irrelevant information or noise. Next, feature engineering was applied to represent the text using the Bag-of-Words (BoW) approach, which transformed the text into a numerical representation.

The dataset was then split into training and test sets, with an 80:20 ratio. The chosen model for sentiment analysis was Naive Bayes, a popular algorithm in natural language processing tasks. The model was trained on the training set and evaluated using various metrics, including accuracy, precision, recall, and F1-score.

To enhance the model's performance, hyperparameter tuning was conducted using GridSearchCV. This technique explored different combinations of hyperparameters to find the best configuration for the Naive Bayes model.

Once the model was trained and fine-tuned, it was ready for predictions. By providing a new tweet or sentence as input, the model would assign it a sentiment value. The numerical values used in the Sentiment140 dataset represented sentiments as follows: 0 for negative, 4 for positive, and 2 for neutral.

By running the model on any tweet or sentence of choice, one could obtain the sentiment prediction as a numerical value, making it possible to classify the sentiment as negative, positive, or neutral.

**In summary, this minor project successfully implemented sentiment analysis using the Sentiment140 dataset. The trained model allowed users to input their own tweets or sentences and receive sentiment predictions in the form of numerical values, enabling classification into negative, positive, or neutral
sentiments.**

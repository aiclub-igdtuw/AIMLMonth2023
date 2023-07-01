Roll Number       :   < Roll no. 23415 >

Student Name      :   < Somya Arora >

Project Title     :   < 24. Video Games Rating By 'ESRB' >

Google Colab Link :   < https://colab.research.google.com/drive/1wzhi8cQsN3gaMcPL-qqbBdsLxHUEeQN1 >

Summary(Optional) :   < In this project, we focused on analyzing the ESRB (Entertainment Software Rating Board) ratings of video games. Here's a summary of the operations we performed:

Dataset Import: We imported the dataset containing video game ratings from the provided GitHub repository using the pandas library.

Distribution of ESRB Ratings: We calculated the distribution of ESRB ratings by counting the number of games in each rating category using the value_counts() method. This provided an overview of how many games fell into each rating category (E, ET, T, M).

Bar Plot Visualization: We created a bar plot using matplotlib to visualize the distribution of ESRB ratings. The bar plot represented the rating categories on the x-axis and the number of games on the y-axis.

Content Features Analysis: We selected specific columns from the dataset related to ESRB ratings and content features such as violence, sexual content, language, and drug reference.

Binary Indicator Variables: We transformed the selected columns into binary indicator variables, representing the presence or absence of each content feature for each game. We used the apply() method with a lambda function to convert values greater than 0 to True and values equal to 0 to False.

Frequency Table Calculation: We created a frequency table to calculate the frequency of content feature combinations for each ESRB rating category. The frequency table consisted of rows representing different rating categories and columns representing content features. We iterated over the binary data and updated the frequency table accordingly. >

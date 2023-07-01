Roll Number       :   23153

Student Name      :   Ishita gupta

Project Title     :   Classification of Robots from their Conversation ✒

Google Colab Link :   https://colab.research.google.com/drive/1BJJERaJpR81aBxnofbBEZ90OFsHZHbXp?usp=sharing

Summary(Optional) :   5 Robots, named quite unexpectedly *0,1,2,3,4 *are having a uniform conversation, where each of them spits out a series of 10 numbers at a time in a round-robin fashion. The task is to train a model which can predict the robot when given the 10 numbers spoken by it, with a good accuracy. A log of a long conversation between these 5 robots has been given, this is your datasets.

Tasks 1 -
How many unique robots are present in the dataset? Calculate the count of distinct robot labels (0, 1, 2, 3, 4) and display it.
There are 5 unique robots present namely 0,1,2,3,4
The value count for 0,1,2,3,4 are 1000 for each respectively.

What is the distribution of the robot labels in the dataset? Generate a bar plot to visualize the frequency of each robot label.
![image](https://github.com/Ishitagupta252004/AIMLMonth2023/assets/122256718/0c448f92-aa35-4d45-8a55-4c650101071c)

Are there any missing values in the dataset? Check for any null or missing values in the sequence of 10 numbers and display the count of missing values, if any.
There are no null and missing value in the sequence of 10 numbers and thus there sum is zero.

How balanced is the dataset in terms of robot labels? Calculate the number of samples for each robot label and visualize it using a pie chart or bar plot.
since the value count for each robot is same hence the dataset is balance,this is also shown with the help of bargraph,the height of each robot is same.

Is there any correlation or pattern between the numbers in the sequence spoken by each robot? Compute the correlation matrix for the sequence of 10 numbers and display it as a heatmap to identify any potential relationships.
Case 1 : Robot 0
from the correlation table we can observe that some values are negative and some are less than.1 .Hence we can say that there is no linear relationship between variables

case 2 : Robot 1
from the correlation table we can observe that all values are grater than equal to .9 . Hence we can conclude that there is a positive correlation between variables

Case 3 : Robot 2
from the correlation table we can observe that some values are between 0 and 0.3 some are between 0.3 and 0.7 and very few values are greater than 0.7 .hence we can conclude that there is weak positive linear relationship between variables

case 4 : Robot 3
from the correlation table we can observe that all values are equal to 1 . Hence we can conclude that there is a positive correlation between variables

case 5 : Robot 4
from the correlation table we can observe that all values are equal to 1 . Hence we can conclude that there is a positive correlation between variables

Task 2-
Determine whether the problem requires classification or regression analysis.
Implement the appropriate classification or regression techniques on the dataset

Summary
The problem required classification as we had to determine the robot on the basis of the 10 numbers spoken by it.

Result

The acccuracy of KNeighborsClassifier is 91%

The accuracy of LogisticRegression is 30%

The accuracy of GaussianNB is 43%

Therefore the models works well with KNeighborsCLassifier

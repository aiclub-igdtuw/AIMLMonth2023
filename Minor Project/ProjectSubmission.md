Roll Number       :   23216

Student Name      :  Mahita Boyina

Project Title     :   Cirrhosis Prediction

Google Colab Link : https://colab.research.google.com/drive/1-VyyEnkZ7rejsyeQJenIHcSnX00zffv5?usp=sharing 

Summary(Optional) : Liver cirrhosis is a widespread problem due to high intake of alcohol , it is the 3 Stage of fibrosis 
scarring of the liver . The dataset is the information collected from the Mayo Clinic
trial in primary biliary cirrhosis (PBC) of the liver conducted between 1974 and 1984
This dataset contains a total of 424 PBC patient's records.
##ATTRIBUTE INFORMATION##
1) ID: unique identifier
2) N_Days: number of days between registration and the earlier of death, transplantation, or study analysis time in July 1986
3) Status: status of the patient C (censored), CL (censored due to liver tx), or D (death)
4) Drug: type of drug D-penicillamine or placebo
5) Age: age in [days]
6) Sex: M (male) or F (female)
7) Ascites: presence of ascites N (No) or Y (Yes)
8) Hepatomegaly: presence of hepatomegaly N (No) or Y (Yes)
9) Spiders: presence of spiders N (No) or Y (Yes)
10) Edema: presence of edema N (no edema and no diuretic therapy for edema), S (edema present without diuretics, or edema resolved by diuretics),
     or Y (edema despite diuretic therapy)
11) Bilirubin: serum bilirubin in [mg/dl]
12) Cholesterol: serum cholesterol in [mg/dl]
13) Albumin: albumin in [gm/dl]
14) Copper: urine copper in [ug/day]
15) Alk_Phos: alkaline phosphatase in [U/liter]
16) SGOT: SGOT in [U/ml]
17) Triglycerides: triglicerides in [mg/dl]
18) Platelets: platelets per cubic [ml/1000]
19) Prothrombin: prothrombin time in seconds [s]
20) Stage: histologic stage of fibrosis sca (1, 2, 3, or 4)
MY tasks were to perform EDA and Regression/Classification
I first tried comprehending the dataset by understanding the meaning of the clinical features and how they are related to cirrhosis. Handled missing values using median for 
numerical data and most frequent feature for categorical data , found outliers in the dataset , understood the relationship between different attributes and how they affect the 
dependent variable(Stage) through different plotting techniques of matplotlib and seaborn library of python.
I did feature of encoding of categorical attributes(a necessary step for data preprocessing) , cleaned the data removed unnecessary rows and columns and then finally based on the
task I was given I decided to go with the algorithm of Logistic Regression for classification which predict cirrhosis.

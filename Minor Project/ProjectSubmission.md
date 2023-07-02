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
7) Ascites: fluid buildup causing abdominal swelling
 presence of ascites N (No) or Y (Yes)
9) Hepatomegaly:It is an enlarged liver, which means it's swollen beyond its usual size
   presence of hepatomegaly N (No) or Y (Yes)
11) Spiders: presence of spiders N (No) or Y (Yes)
12) Edema: presence of edema(Edema occurs when tiny blood vessels in the body, also known as c 
    capillaries, leak fluid)
    N (no edema and no diuretic therapy for edema), S (edema present 
    without diuretics, or edema resolved by diuretics),
    or Y (edema despite diuretic therapy)
13) Bilirubin:an orange-yellow pigment formed in the liver by the breakdown of haemoglobin and 
    excreted in bile.
    serum bilirubin in [mg/dl]
15) Cholesterol: serum cholesterol in [mg/dl]
16) Albumin:It is a protein made by your liver.
    albumin in [gm/dl]
18) Copper: urine copper in [ug/day]
19) Alk_Phos: alkaline phosphatase in [U/liter]
20) SGOT:A glutamic-oxaloacetic transaminase (SGOT) or aspartate aminotransferase (AST) test 
    measures the levels of the enzyme AST in the blood to assess liver health.
  SGOT in [U/ml]
22) Triglycerides:an ester formed from glycerol and three fatty acid groups. Triglycerides are 
    the main constituents of natural fats and oils.
     triglicerides in [mg/dl]
24) Platelets: platelets per cubic [ml/1000]
25) Prothrombin:measures how long it takes for a clot to form in a blood sample. 
    prothrombin time in seconds [s]
27) Stage: histologic stage of fibrosis sca (1, 2, 3, or 4)
MY tasks were to perform EDA and Regression/Classification
I first tried comprehending the dataset by understanding the meaning of the clinical features and how they are related to cirrhosis. Handled missing values using median for 
numerical data and most frequent feature for categorical data , found outliers in the dataset , understood the relationship between different attributes and how they affect the 
dependent variable(Stage) through different plotting techniques of matplotlib and seaborn library of python.
I did feature of encoding of categorical attributes(a necessary step for data preprocessing) , cleaned the data removed unnecessary rows and columns and then finally based on the
task I was given I decided to go with the algorithm of Logistic Regression for classification which predict cirrhosis.

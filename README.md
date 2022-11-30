# GRA4157
Course material for  GRA 4157 - (Big) Data Curation, Pipelines, and Management.

# Exams
Mid term-exam (30%) Thursday October 13th 14:00 - 16:00. Technical knowledge, concepts from programming with data

The final exam assignment (70%), is based on the two group presentations (1 - 3 per group) during the semester. You should write a data science report about a topic of choise. A more precise text on the expectations has been [published](https://github.com/BI-DS/GRA4157/blob/main/exam/GRA4157-final-report.pdf). The deadline is Friday December 9. 12:00 (noon). 

# Guest lecture resources
Hei Vegard,

forsinket mail her, men veldig hyggelig å holde forelesning for studentene sammen med Christian fredag 7. oktober! Flinke og engasjerte studenter med reflekterte tanker rundt et stort og viktig tema i data science-verden.


Vi avtalte å tilgjengeliggjøre noen referanser for studentene, legger disse under her:


[Powerpoint](https://github.com/BI-DS/GRA4157/blob/main/Gjesteforelesning_BI_DataPipelines_for_ML.pdf)
 

BearingPoint sin medium-side:

https://bearingpoint-analytics-ai.medium.com/
 

Våre epost-adresser:

yngve.sture@bearingpoint.com

christian.svalesen@bearingpoint.com


Noen nøkkelteknologier vi anbefalte:

    Gradient boosted trees
        XGBoost (https://xgboost.readthedocs.io/en/stable/) ,
        LightGBM (https://lightgbm.readthedocs.io/en/v3.3.2/)
    Google BigQuery (datavarehusteknologi med all funksjonalitet man trenger for å lagre og transformere store datamengder. Kan lagre opptil 10GB gratis.)
    Cloud providers: AWS, Azure, Google Cloud platform
    MLOps (vi anbefaler å bruke et av disse eller lignende verktøy for å holde styr på trening og sammenligning av ulike modeller):
        MLflow
        Neptune

Podcasttips:

    The Analytics Engineering Podcast
    Practical AI

Bøker:

    The Phoenix Project - Essensielt om hvorfor DevOps er viktig, strategibok
    Competing In The Age of AI - Grunnleggende AI-strategi fra Harvard-professorer
    Prediction Machines - fra Professorer ved Creative Destruction Lab, Rotman School of Managements StartupHub
    AI First Company - Hvordan bygge gode AI selskaper fra Ash Fontana, Venture Capitalist
    Weapons of Math Destruction – Bok som peker på noen av de etiske fallgruvene man risikerer ved bruk av AI

# Machine learning resources
For an introduction to machine learning I recommend the scikit-learn [tutorial](https://scikit-learn.org/stable/tutorial/basic/tutorial.html). I have uploaded notebooks in the folder 07-scikit-learn, which are in part based on the scikit-learn tutorial. I will spend 30 minutes of the next class to lecture machine learning, and you get the rest of the time to work on projects. The ML project is posted in the scikit-learn folder and also linked in the lecture plan below. 

# Lectures
Lectures will be held each Friday 12-13:45 between September 2nd and November 18th.  
I have office hours at BI every Friday 09:00 - 16:00 at office B3 - 054 in the Data Science Department. Outside these hours you may contact me at vegard@simula.no or vegard.vinje@bi.no. 


# Topics
Part 1:   
Basic Python lists, dictionaries and operations.   
Reading from and writing to files, flexible solutions.  
Numerical python with numpy, arrays, array slicing for vectorized computations.   


Part 2:   
Working with the pandas library 
Reading data from websites  
Data visualisation  

Part 3:  
Cleaning data, combining data sets  
Machine learning workflows with scikit learn  
Assess machine learning models based on various assumptions on data (outliers etc)  


# Written material 
We will use three books for references: https://rl.talis.com/3/binorway/lists/76C6E5C4-F0D7-76B8-78B3-266D02955988.html  
Link to notebooks: https://mybinder.org/v2/gh/BI-DS/GRA4157/vegarvi-patch-1


# Preliminary lecture plan
For a given lecture, the reading gives an approximate overview of what is expected to be known after the lecture. I expect you to solve the exercises after the lecture. Each week, we start the lecture with a student presentation of a exercise of choice. Send an email to vegard.vinje@bi.no to volunteer for an exercise. For exercises regarding pandas we refer to the w3resource (W3) https://www.w3resource.com/python-exercises/pandas/index-dataframe.php
| Date  | Topic | Reading | Exercises | Student presentation |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| Sep. 2  | Course Introduction. Python recap, lists and dictionaries. Testing.  | Sundnes: Chap 1,2,3 (and 7) | Sundnes: 2.7, 2.8, 2.9, 2.15, 2.18, 3.3, 3.6, 3.17 | |
| Sep. 9  | Reading and writing to file. User input. Exceptions. More on command line arguments  | Sundnes: Chap 5 | Sundnes: 4.4, 4.9, 4.10, 4.12, 4.13, 4.17, 4.23 | Augusta (notebook exercise) |
| Sep. 16  | Numerical Python and plotting  | Sundnes: Chap 6 | Sundnes: 5.1, 5.2, 5.3, 5.4, 5.10, 5.12, 5.14, 5.28, 5.46, 5.54    | Anders | 
| Sep. 23  | Pandas | McKinney: Chap 5 | W3: DataFrames: 2.-22., 73  | Peter | 
| Sep. 30 | File formats and web scraping | KcKinney: Chap 6 | [Exercise](https://github.com/BI-DS/GRA4157/blob/main/mid-term-exercise/Exercise_project.pdf). Also mandatory assignment deadline | Ulrik |
| Oct. 7 | Guest lecture Bearingpoint | Marius Reed and Christian Svalesen | |
| Oct. 12 | Q & A Mid-term 10 - 12 | | | 
| Oct. 13 | Mid-term | | |
| Oct. 21 | Map visualization | Project 1 | [Project text](https://github.com/BI-DS/GRA4157/blob/main/lectures/06-visualization-project/GroupProject.pdf) | Oleksandra |
| Oct. 28 | Group presentations and intro to machine learning | | |
| Nov. 4 | Machine learning | Project 2 | [Project text](https://github.com/BI-DS/GRA4157/blob/main/lectures/07-scikit-learn/GroupProjectML.pdf) |
| Nov. 11| Group presentations | | | 
| Nov. 18 | Final lecture | Exam/assignment information | [Exam text](https://github.com/BI-DS/GRA4157/blob/main/exam/GRA4157-final-report.pdf) | 
| Dec. 1 | Q&A | 08:00 - 08:20: Anders. 08:20 - 08:40: Oleksandra, Tuan, Serik. 08:40 - 09:00: Augusta, Sondre, Peter. 09:00 - 09:20: Mihn |time: 08 - 10 | room: C2-005 |

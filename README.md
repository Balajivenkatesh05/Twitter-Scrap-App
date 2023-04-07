# Twitter-Scrap-App

How the App works??

The First step is to collect the inputs from user such as search_term(Hashtag/keyword), start date, end date, limit. 
![image](https://user-images.githubusercontent.com/121443485/222351165-a934f2ae-e1be-43b6-8a4a-b67345cfb5a6.png)
Then using snscrape module the tweets are scrapped as per the limit mentioned by the user. The user can download the dataset either in CSV format or as a JSON file 

The dataset is uploaded in the MongoDB
![image](https://user-images.githubusercontent.com/121443485/222349520-f29ead3a-be5b-487d-bdaa-61ccd886440c.png)

Libraries and Versions:
1. Streamlit (1.21.0)
2. Pandas (2.0.0)
3. Numpy (1.24.2)
4. Pymongo (4.3.3)
5. snscrape (0.6.2.20230320)

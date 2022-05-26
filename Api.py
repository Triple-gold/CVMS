import requests

url = "https://job-and-resume-matching-for-hr-management-systems.p.rapidapi.com/api/v1.0/tools/resume-analyzer"

payload = "{\r\n    \"text\": \"LINA HATM\\nDATA SCIENTIST\\nlina.hatm@mouseatwork.com\\nPhone: +1 5146385647\\nWORK EXPERIENCE\\nNLP Specialist | Mouse At Work\\nFebruary 2019 - October 2020\\n• Perform analysis, design, and development of new features related to sentiment analysis, topic modeling and named entity extraction modules\\n• Participate in the implementation of the machine learning pipelines\\n• Participate in technological choices for the evolution of architecture\\n• Identify and optimize bottlenecks in algorithms and workflows\\nData Scientist |  Facebook Inc.\\nJanuary 2014 to December 2014\\n• Lead and develop NLP solutions in the field of human resources.\\n• Identify and assess new NLP solutions\\n• develop analytical models\\nNLP Specialist | Desjardins\\nFebruary 2010 - May 2014\\n• Support and create a broad range of data driven solutions by applying a variety of techniques to build out complex models\\n• Develop and implement NLP algorithms related to sentiment analysis\\n• Review code\\n• Build Non-functional business reUuirements\\n• Explain and communicate analysis results\\n• Jevelop and train machine learning algorithms\\nEDUCATION\\nPhD in computer science | University of Nantes | Sept. 2010 - Jan. 2014\\nMaster 2 in NLP | University of Caen Basse-Normandie | Sept. 2008 - Sept. 2009\\nSKILLS\\nNatural Language Processing (NLP):\\nSentiment Analysis\\nNamed Entity Extraction\\nTopic Modeling\\nDeep learning (Neural networks, RNN, CNN, LSTM, etc.)\\nWord embedding models\\nMachine learning\\nSeq2seq\\nPredictive Analytics\\nData Visualization\\nRegression\\nText Mining\\nClustering\\nData mining\\nArtificial intelligence (AI)\\nText semantic similarity\\nText classification\\nTime-series forecasting\\nText transcription\\nMachine learning libraries:\\nTensorFlow\\nPytorch\\nKeras\\nSpacy\\nTextBlob\\nNLTK\\nBERT\\nPandas\\nStanfordNLP\\nMXNet\\nHuggingFace\\nScikit-learn\\nProgramming Languages:\\nMongodb\\nSQL\\nElasticsearch\\nData preparation\\nGraphQL\\nSOFT SKILLS:\\nAttention to detail\\nCuriosity\\nQuickly prototype ideas\\nStrategic mindset\\nTime management\"\r\n}"
headers = {
    'content-type': "application/json",
    'x-rapidapi-host': "job-and-resume-matching-for-hr-management-systems.p.rapidapi.com",
    'x-rapidapi-key': "f71211e6camsh3431fafae13b44ap1c5f9ajsn0ef2c6f7c921"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)


# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 08:01:54 2021

@author: sansk
"""

#Stemming
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

paragraph = """At present India is one of the best countries to live in. India is one of the best tourist attractions in the world. It has 29 states and every state has its varied culture. Hence, India has the richest varieties of cuisines in the world derived from all states. India is rich in climatic and topographic conditions.

The range is huge from hot and cold deserts to Snow- Capped Mountains, from beaches with floras and faunas to natural rivers supporting agriculture in many states. India being a developing economy has cheap labor and agriculture-based economy gives a low cost of food hence making the cost of living in India very low.

India is a hub for education and healthcare facilities. People around the world prefer the low cost and good quality higher education and medical health care in India in comparison to developed nations. India has a high growth rate and a very large market thus it attracts many foreign investors. There are more than 19000 languages and dialects spoken in the country, therefore, attracting many faculties of literature from around the world.

ISRO launched its 100th satellite. Electricity is now in every house in the country. India has the tallest statue in the world. Indian sportspersons are achieving greater heights. Asia’s longest tunnel and Asia’s longest rail bridge are India’s pride. Women empowerment and supporting girl education are some of the major projects of our government.

Future of India
In 2022 India will be launching its first manned space mission. India may be ruling with the world’s largest working population. Further, I would like to add that in times to come India would be heading more startups which may include agriculture, education, technology, financial and social- impact projects.

After the abolition of Article 35A and Article 370 Kashmiri Pandits and other Indian Citizens may get settled in Jammu and Kashmir. This would, therefore, attract more tourists from around the world. Politics may attract more educated classes in the future. More power to the Indian Army would be given and hence the Army would neutralize the terrorism.

Conclusion
I would like to conclude by saying that no matter how much I praise my country’s achievement, it would always be less. Our country is our motherland and we should always be grateful for whatever we have got from our country. We should participate and put positive efforts in the growth and development of our nation.

I would like to request you to make our nation proud, may it be by keeping our vicinity clean, educating and empowering the weaker section of the society, paying our taxes or conserving our natural resources by recycling and reusing. I would like to thank God for giving me this great nation India as my motherland.

Thanks. """

sentences = nltk.sent_tokenize(paragraph)
#object created for class PorterStemmer
Stemmer = PorterStemmer()
#Stemming Process
for i in range (len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [Stemmer.stem[word] for word in words if word not in set(stopwords.word('english'))]
    sentences[i] = ' '.join(words)
    
    
import json
import pandas as pd
import re
import nltk
import typing
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords
import math

def is_english(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

def remove_links(text):
    # Remove any hyperlinks that may be in the text starting with http
    return re.sub(r"http\S+", "", text)

def style_text(text):
    # Convert to lowercase
    return text.lower()

def remove_words(text_data, list_of_words_to_remove):
    # Remove all words as specified in a custom list of words
    return [item for item in text_data if item not in list_of_words_to_remove]

def collapse_list_to_string(string_list):
    # This is to join back together the text data into a single string
    return ' '.join(string_list)

def clean_text(text):
    # Convert to lowercase, and remove stop words
    cleaned_text = remove_links(text)
    cleaned_text = re.sub(r'[^\w]', ' ', cleaned_text)
    cleaned_text = re.sub(r'[0-9]', ' ', cleaned_text)
    cleaned_text = re.sub(r'[_]', ' ', cleaned_text)
    cleaned_text = style_text(cleaned_text)
    cleaned_text = remove_words(cleaned_text.split(), stopcorpus)
    cleaned_text = collapse_list_to_string(cleaned_text)
    
    # Lemmatize text and remove stopwords
    lemmatized_text = lemmatize_text(cleaned_text)
    lemmatized_text = collapse_list_to_string(lemmatized_text)
    lemmatized_text = remove_words(lemmatized_text.split(), stopcorpus)
    
    final_word_list = []
    
    for word in lemmatized_text:
        if len(word) > 2 and is_english(word):
            final_word_list.append(word)

    return final_word_list

stopcorpus: typing.List = stopwords.words('english')
w_tokenizer = nltk.tokenize.WhitespaceTokenizer()
lemmatizer = nltk.stem.WordNetLemmatizer()

def lemmatize_text(text):
    return [lemmatizer.lemmatize(w) for w in w_tokenizer.tokenize(text)]

#######

with open('fraudulent_emails_v2.json') as f:
    data = json.load(f)

text_data = []
unemployment_data = {}
attacker_titles = {}

for email in data:
    message_data = {}
    message = email['X-TIKA:content']
    se_tag = email['se_tag']
    try:
        titles = email['author_titles']
    except KeyError:
        titles = []

    # Clean and lemmatize message
    cleaned_text = clean_text(message)

    # Save processed message text to dict
    message_data['message'] = cleaned_text
    message_data['se_tag'] = se_tag

    try:
        captions = email['GPT2_gen_images']['Phish_Iris_image']['Image_caption']['captions']
        message_data['caption'] = []
        for i in captions:
            caption = i['sentence']
            # Clean and lemmatize caption
            cleaned_caption = clean_text(caption)

            # Save processed caption text to dict
            message_data['caption'] = cleaned_caption
    except:
        pass
    
    text_data.append(message_data)

    ## Extract Unemployment info

    try:
        unemployment = email['GlobalUnemployment']
    except KeyError:
        continue

    # If unemployment data exists, then add it to a dictionary
    if unemployment != []:
        for i in unemployment:    # Unemployment is a list of dicts
            for key, value in i.items():
                
                # Extract data from the dictionary
                country = value['country']
                year = value['year']
                unemp_val = value[str(year) + '_unemployment']

                # If the unemployment data is NaN, skip and move on
                if math.isnan(unemp_val):
                    continue

                # Add the country and year to the dictionary with a frequency count for use in a heat map
                if country in unemployment_data:
                    unemployment_data[country]['freq'] += 1
                    
                    # Check if the year is in the dictionary and update count
                    if year in unemployment_data[country]:
                        unemployment_data[country][year]['freq'] += 1
                    else:
                        unemployment_data[country][year] = {'unemployment': unemp_val, 'freq': 1}
                    
                    # Check if the se_tag is in the dictionary and update count
                    if se_tag in unemployment_data[country]['se']:
                        unemployment_data[country]['se'][se_tag] += 1
                    else:
                        unemployment_data[country]['se'][se_tag] = 1

                # If the country is not already in the dictionary, then add it
                else:
                    unemployment_data[country] = {}
                    unemployment_data[country]['freq'] = 1
                    unemployment_data[country][year] = {'unemployment': unemp_val, 'freq': 1}
                    unemployment_data[country]['se'] = {se_tag: 1}
    
    for title in titles:
        if title in attacker_titles:
            attacker_titles[title] += 1
        else:
            attacker_titles[title] = 1

# Save the attacker titles in a specific json format for uploading into d3
attackers_to_json = {}
i = 1
for key, value in attacker_titles.items():
    attackers_to_json['attacker_' + str(i)] = {'title': key, 'value': value}
    i += 1

# Save the word frequencies in a specific json format for uploading into d3
new_text = {'caption': {}, 'reply': {}, 'social_engineering': {}, 'recon': {}, 'phishing': {}, 'malware': {}}
for i in text_data:
    try:
        message = i['message']
    except KeyError:
        message = []
    
    try:
        caption = i['caption']
    except KeyError:
        caption = []
    
    se_tag = i['se_tag']
    
    for word in message:
        if word in new_text[se_tag]:
            new_text[se_tag][word] += 1
        else:
            new_text[se_tag][word] = 1
    
    for word in caption:
        if word in new_text['caption']:
            new_text['caption'][word] += 1
        else:
            new_text['caption'][word] = 1

text_out_json = {'unique_keywords': []}
for key, value in new_text.items():    # key is se_tag
    sort_dict= list(sorted(value.items(), key=lambda item: item[1], reverse=True))
    for i in sort_dict[:50]:
        text_out_json['unique_keywords'].append({'word': i[0], 'se_tag': key, 'freq': i[1]})


## Save data to json files

with open('filtered_keywords.json', 'w') as text_out:
    json.dump(text_out_json, text_out, indent=2)

with open('unemployment.json', 'w') as unemp_out:
    json.dump(unemployment_data, unemp_out, indent=2)

with open('titles.json', 'w') as titles_out:
    json.dump(attackers_to_json, titles_out, indent=2)

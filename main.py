#!/usr/bin/python3
"""
Import section:
All imports were thought following good practice methods
"""
import os
import src.xml.xml_manipulation as xml
import src.csv.csv as csv
import src.nlp.spacy as spacy
import spacy as sp
import pandas as pd
import string
import fr_core_news_md
import de_core_news_md
import matplotlib.pyplot as plt
import gensim
from stop_words import get_stop_words
from gensim.models import CoherenceModel
from gensim import corpora
import pyLDAvis
import pyLDAvis.sklearn
import pyLDAvis.gensim_models
from multiprocessing import Process
from nltk.corpus import stopwords

"""
CSV CREATION STEPS
"""
def get_csv_data(root_dir, tree):
    """
    This function will gather all the information about a single XML file that will be written
    Inside the CSV file, along with the language detection data.
    """
    #This will be the full row data list
    full_data=[] 
    #This is the xml part of the data, only tag extraction
    xml_data = [xml.extract_tag(tree, xml.tag_dict["source"]),
                xml.extract_tag(tree, str(xml.tag_dict["date"])),
                xml.extract_tag(tree, xml.tag_dict["publisher"]),
                xml.extract_tag(tree, xml.tag_dict["description"])
                ]
    #This is the language detection data
    spacy_data = spacy.get_lang(xml.extract_tag(tree, xml.tag_dict["description"]))
    xml_data.append(spacy_data["language"])
    xml_data.append(spacy_data["score"])
    full_data = xml_data
    return full_data

def write_to_csv(root_dir, file_list, csv_name):
    """
    Opens a csv file, writes the header (Source, Date, Publisher and Description).
    Then, writes in a sequence all extracted tag data from XML files.
    """
    with open(csv_name, 'w', encoding='UTF8') as f:
        # Opens the CSV and writes the Header titles
        csv.writer(f).writerow(csv.header)
        # For each file, tag data will be extracted, and written into the CSV file
        for file in file_list:
            tree = xml.open_xml(root_dir, file)
            file_data = get_csv_data(root_dir, tree)
            csv.writer(f).writerow(file_data)
    f.close()

def main_csv():
    """
    XML to CSV file transition, this gets the following header:
    Source, Date, Publisher, Description, Language, Score
    """
    #Variables declaration
    root_dir = './ADS/'
    files = os.listdir(root_dir)
    range1 = files[:30000]
    range2 = files[30000:60000]
    range3 = files[60000:90000]
    range4 = files[100000:140000]
    range_total = len(range1+range2+range3+range4)

    process_1 = Process(target=write_to_csv, args=(root_dir,  range1, './advertisements1.csv'))
    process_2 = Process(target=write_to_csv, args=(root_dir,  range2, './advertisements2.csv'))
    process_3 = Process(target=write_to_csv, args=(root_dir,  range3, './advertisements3.csv'))
    process_4 = Process(target=write_to_csv, args=(root_dir,  range3, './advertisements4.csv'))
    print('Writing to CSV and analysing language...')

    process_1.start()
    process_2.start()
    process_3.start()
    process_4.start()
    process_1.join()
    process_2.join()
    process_3.join()
    process_4.join()
    print('Operation complete!')

    def filter_csv(filename):
        #Read CSV file
        df = pd.read_csv(filename)
        #Filter CSV by target Lnguage
        df = df[(df['Language']=='fr') | (df['Language']=='de')]
        df[df['Language']=='fr'].to_csv('Ads1FR.csv')
        df[df['Language']=='de'].to_csv('Ads1DE.csv')
"""
LDA related functions
These functions follow a certain order of process to complete the desired LDA model
"""
def clean_text(text):
  delete_dict = {sp_char: '' for sp_char in string.punctuation}
  delete_dict[' '] =' '
  table = str.maketrans(delete_dict)
  text1 = text.translate(table)
  textArr= text1.split()
  text2 = ' '.join([w for w in textArr if ( not w.isdigit() and
                                           ( not w.isdigit() and len(w)>3))])
  return text2.lower()

def remove_stopwords(text):
    textArr = text.split(' ')
    rem_text = " ".join([i for i in textArr if i not in stop_words])
    return rem_text

def lemmatization(texts,allowed_postags=['NOUN', 'ADJ', 'VERB']):
	output = []
	for sent in texts:
		doc = nlp(sent)
		output.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
	return output



def lda_total(topics_range):
    print('Cleaning text and removing stopwords')
    #Clean text
    df['Description'] = df['Description'].apply(clean_text)
    #Remove stopwords
    df['Description'] = df['Description'].apply(remove_stopwords)
    #Lemmatization
    print('Done!')
    print('\nApplying Lemmatization...')

    text_list = df['Description'].tolist()
    print('Test list: ',text_list[2])
    #nlp = de_core_news_md.load(disable=['parser', 'ner'])
    tokenized_ads = lemmatization(text_list)
    print('List[2]: ',tokenized_ads[2])
    # convert to document term frequency:
    dictionary = corpora.Dictionary(tokenized_ads)
    doc_term_matrix = [dictionary.doc2bow(rev) for rev in tokenized_ads]
    # Creating the object for LDA model using gensim library
    LDA = gensim.models.ldamodel.LdaModel
    # Build LDA model
    print('Building LDA model...')
    lda_model = LDA(corpus=doc_term_matrix, id2word=dictionary,
                num_topics=topics_range, random_state=100,
                chunksize=1000, passes=100,iterations=250)
    # print lda topics with respect to each word of document
    lda_model.print_topics()
    print('Top topics:',lda_model.top_topics(doc_term_matrix))
    doc_lda = lda_model[doc_term_matrix]
    # calculate perplexity and coherence
    print('\nPerplexity: ', lda_model.log_perplexity(doc_term_matrix,
                                               total_docs=10000)) 
    # calculate coherence
    coherence_model_lda = CoherenceModel(model=lda_model,
                                     texts=tokenized_ads, dictionary=dictionary ,
                                     coherence='u_mass', processes=4)
    print('Calculating coherence...')
    coherence_lda = coherence_model_lda.get_coherence()
    print('Coherence: ', coherence_lda)

if __name__=="__main__":
    #Open CSV file
    
    """ Language-dependent variables declarations """
    # FR
    df = pd.read_csv("Ads1FR.csv")
    nlp = fr_core_news_md.load(disable=['parser', 'ner'])
    stop_words = set(get_stop_words('french')) | set(stopwords.words('french'))
    # DE
    #df = pd.read_csv("Ads1DE.csv")
    #nlp = de_core_news_md.load(disable=['parser', 'ner'])
    #stop_words = set(get_stop_words('german')) | set(stopwords.words('german'))
    """ End of declaration """

    for i in range(10,55,5):
        print(f'LDA Model with {i} topics:\n') 
        lda_total(i)
    # Now, we use pyLDA vis to visualize it
    pyLDAvis.sklearn.prepare(lda_tf, dtm_tf, tf_vectorizer)
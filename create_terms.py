import json
import nltk
import random

article_json_file = './article.json'
terms_file = './terms_of_finance.txt'


def create_terms_from_content(content):
    terms = []
    content_len = len(content)
    while content:
        idx = random.randint(4, 21) 
        terms.append(content[:idx])
        content = content[idx:]

    return terms


fo_terms = open(terms_file, 'w')
with open(article_json_file, 'r') as fo:
    for line in fo:
        line_json = json.loads(line.strip())
        content = ' '.join(line_json['content']).replace('\n', '')
        terms = create_terms_from_content(content)
        for term in terms:
            fo_terms.write(term + '\n')

fo_terms.close()
print('all done!')

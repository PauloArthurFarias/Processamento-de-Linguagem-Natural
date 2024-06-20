#importando arquivo (não entendi tanto, talvez pesquisar melhor caso necessário)

"""import nltk
nltk.download('machado')
nltk.download('punkt')
from nltk.corpus import machado

machado.fileids()[:3]

print(machado.raw('contos/macn001.txt'))"""

"""import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
print(stopwords.words('portuguese'))"""

#tokenização

"""import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

texto = 'Goku is a hero in the Dragon Ball ! Goku saved the earth many times.'
print(nltk.sent_tokenize(texto))
print(word_tokenize(texto))"""

#radicalização

"""from nltk.stem.snowball import SnowballStemmer
print(SnowballStemmer.languages)
SnowballStemmer = SnowballStemmer("portuguese")
print(SnowballStemmer.stem('computação'))
print(SnowballStemmer.stem('computador'))"""

#lematização
#melhor é lexema de bom; bom é lema de melhor

import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
WordNetLemmatizer = WordNetLemmatizer()
print("-"*5)
print(WordNetLemmatizer.lemmatize("rocks"))
print(WordNetLemmatizer.lemmatize("better", pos="a"))
print(WordNetLemmatizer.lemmatize("walked", pos='v'))
print("-"*5)

#pos-tagging (identificar classe gramatical)

"""import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

text2 = 'Rafael is working at Google in South America'
print(nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(text2))))"""

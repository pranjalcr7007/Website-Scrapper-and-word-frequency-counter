from django.http import HttpResponse
from django.shortcuts import render
import operator
import re
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
from .models import data
	


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)





def frequency(request): # request variable has information about the users
	# return render(request, 'home.html', {'hithere': 'This is the key'})
	
	

	return render(request, 'frequency.html')


def result(request):
	url = request.POST.get('url')

	global html 
	html= urllib.request.urlopen(url).read()
	data(html=html, url=url).save()

	wordlist = text_from_html(html).split()

	word_dictionary = {}
	
	
	stopwords = ["A","the","of","and","a","to","in","is","you","that","it","he","was","for","on","are","as","with","his","they","I","at","be","this","have","from","or","one","had","by","word","but","not","what","all","were","we","when","your","can","said","there","use","an","each","which","she","do","how","their","if","will","up","other","about","out","many","then","them","these","so","some","her","would","make","like","him","into","time","has","look","two","more","write","go","see","number","no","way","could","people","my","than","first","water","been","call","who","oil","its","now","find","long","down","day","did","get","come","made","may","part"]
	
	new_wordlist = list(filter(lambda w: w not in stopwords, wordlist))
	 
				
	for word in new_wordlist:
		if word in word_dictionary:
			#increase the frequency
				word_dictionary[word] += 1
		else:
			# add the word to the dictionary
			word_dictionary[word] = 1
	# word_dictionary.items convert the dict into list
	sorted_words = sorted(word_dictionary.items(),key=operator.itemgetter(1), reverse = True)
	print(sorted_words)
	
	  
	return render(request, 'result.html', {'fulltext':text_from_html(html),'result':len(wordlist),'word_dictionary':word_dictionary,'sorted':sorted_words})
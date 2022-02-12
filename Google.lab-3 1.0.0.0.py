def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    # I know that regEX is poss :)
    text = (file_contents.replace('!', '').replace('(', '').replace(')', '').replace('-', '').replace('.', '')
            .replace('[', '').replace(']', '').replace('{', '').replace('}', '').replace(';', '').replace(':', '')
            .replace('"', '').replace("'", '').replace('\\', '').replace(',', '').replace('<', '').replace('>', '')
            .replace('/', '').replace('?', '').replace('@', '').replace('#', '').replace('$', '').replace('%', '')
            .replace('&', '').replace('*', '').replace('_', '').replace('`', '').replace('~', '').replace('^', '')
            )
    final_text = {}
    for word in text.split():
        if word in uninteresting_words and word.isalpha():
            continue
        final_text[word.lower()] = final_text.get(word.lower(), 0) + 1
    
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(final_text)
    return cloud.to_array()
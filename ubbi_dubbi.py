'''In Ubbi Dubbi, every vowel (a, e, i, o, or u) is prefaced with ub. Thus milk becomes mubilk (m-ub-ilk) 
and program becomes prubogrubam  (prub-ogrub-am)'''

def ubbi_dubbi():
    word = input('Enter the word to translate: ')
    
    translated_word = []
    
    for letter in word:
        if letter in 'aeiou':
            translated_word.append(f'ub{letter}')
        else:
            translated_word.append(letter)
            
    if word.istitle():
        return ''.join(translated_word).title()
    else:
        return ''.join(translated_word)
    

def remove_authors():
    '''Given a string containing an article and a  separate  list  of  strings  containing  authors’  names,
    replace  all  names  in  the article with _ characters
    
    '''
    article = '''
    This is the stroy about Tom and Jerry. They lived in a beautiful village called Kangemi. Mathias was their cousing and Dorcas was their mother.
    The father was Kamau of Thuge.
    '''
    
    authors = ['Dorcas', 'Kamau', 'Tom']

    return ' '.join(['_' if author in authors else author for author in article.split()])

def url_encode_string():
    ''' In  URLs,  we  often  replace  special  and  non printable characters with a % followed by the character’s ASCII value in hexadecimal.
    Forexample,  if  a  URL  is  to  include  a  space  character  (ASCII  32,  aka  0x20),  we replace it with %20.
    Given a string, URL-encode any character that isn’t a letteror  number. 
    For  the  purposes  of  this  exercise,  we’ll  assume  that  all  charactersare indeed in ASCII '''
    
    string_to_encode = 'This is the string that we need to encode.'
    
    encoded_string = ''
    
    for character in string_to_encode:
        if character.isalnum():
            encoded_string += character
        else:
            encoded_string += '%' + format(ord(character), '02X')
    return encoded_string
    
if __name__ == '__main__':
    # print(ubbi_dubbi())
    # print(remove_authors())
    print(url_encode_string())
            
    
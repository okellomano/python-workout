'''Takes a sentence from the user and translates every word into a pig latin equivalent, then prints the result in a single line. '''

def pig_ltin_sentence():
    user_sentence = input('Enter a sentence: ').casefold()
        
    translated_words = []
        
    if not user_sentence:
        return
        
    for word in user_sentence.split():
        if word[0] in 'aeiou':
            translated_words.append(f'{word}way')
        else:
            translated_words.append(f'{word[1:]}{word[0]}ay')
                
    return ' '.join(translated_words)



def create_nonsensical_sentence(file_path):
    '''Take  a  text  file,  creating  (and  printing)  a  nonsensical  sentence  from  the nth word on each of the first 10 lines,
    where n is the line number. '''
    try:
        with open(file_path, 'r') as file:
            nonsensical_sentence = ''
            # Read the first 10 lines from the file
            for i, line in enumerate(file):
                if i >= 10:
                    break
                words = line.split()
                if len(words) > i:
                    nonsensical_sentence += words[i] + ' '
            return nonsensical_sentence.strip()
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        

def transpose_strings(list_of_strings):
    '''Transposes  a  list  of  strings,  in  which  each  string  contains multiple words separated by whitespace.
    Specifically, it should perform in such away that if you were to pass the list ['abc def ghi','jkl mno pqr','stu vwx yz']to the function, 
    it would return ['abc jkl stu','def mno vwx','ghi pqr yz']
    
    '''
        
    word_list = [string.split() for string in list_of_strings]
    
    # Transpose the list of strings
    transposed_words = list(zip(*word_list))
    
    transposed_strings = [' '.join(word) for word in transposed_words]
    
    return transposed_strings


def extract_ip_from_logs(log_file_path):
    '''
    Read through an Apache logfile. If there is a 404 error—you can just search for'404', if you want—display the IP address, 
    which should be the first element.
    '''
    
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                # Search for lines containing "404"
                if '404' in line:
                    # Split the line by whitespace and extract the IP address (first element)
                    ip_address = line.split()[0]
                    print("IP Address:", ip_address)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    # print(pig_ltin_sentence())
    transpose_strings(['abc def ghi','jkl mno pqr','stu vwx yz'])
        
        
        
        
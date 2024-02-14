
import socket
import string

#start a connection
def new_connection():
    host = 'localhost'
    port = 10000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    print("Connected to server")
    return s

#send data to the server
def send_data(s,data):
    s.send(data.encode())
    data = s.recv(1024).decode()
    return data

#close the connection
def close_connection(s):
    s.close()

#read the file
def read_file():
    file = open("backdoor.txt","r")
    data = file.read()
    file.close()
    return data

#split the file into a list of paragraphs
def split_paragraphs(data):
    paragraphs = data.split("\n\n")
    return paragraphs

def read_paragraph_into_lines(paragraphs,paragraph_number):
    lines = paragraphs[paragraph_number-1].split("\n")
    return lines

def read_line_into_words(lines,line_number):
    words = lines[line_number-1].split(" ")
    return words

def get_word_from_words(words,word_number):
    word = words[word_number-1]
    return word

def get_word_code_from_word(word,paragraph_number,line_number,word_number):
    word_code = str(paragraph_number) + "," + str(line_number) + "," + str(word_number)
    return word_code



def main():
    #get a connection
    s = new_connection()
    #send "stuff n things" to the server
    data = send_data(s,"stuff n things")
    #read the response from the server
    print(data)
    #split data into a list by newline character
    codewords = data.split("\n")
    newcodewords = []
    for words in codewords:
        newcodewords.append(words.split(","))
    newcodewords.pop()
    for word in newcodewords:
        for piece in word:
            piece = int(piece)
    print(newcodewords)
    #read the file
    File = read_file()
    submission = ""
    for each in newcodewords:
        #get the paragraph number
        paragraph_number = int(each[0])
        #get the line number
        line_number = int(each[1])
        #get the word number
        word_number = int(each[2])
        #split the file into paragraphs
        paragraphs = split_paragraphs(File)
        #read the paragraph into lines
        lines = read_paragraph_into_lines(paragraphs,paragraph_number)
        #read the line into words
        words = read_line_into_words(lines,line_number)
        #get the word from the words
        word = get_word_from_words(words,word_number)
        #get the word code from the word
        word_code = get_word_code_from_word(word,paragraph_number,line_number,word_number)
        #if word has punctuation remove it
        word = word.strip(string.punctuation)
        print(word)
        submission = submission + "\n" + word
        print(submission)
 
    print(submission)
    #send submission to the server
    data = send_data(s,submission)
    #receive the data from the server
    print(data)
        
main()
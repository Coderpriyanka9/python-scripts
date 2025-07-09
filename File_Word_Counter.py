def count_word(filename):
    try:
        with open(filename , "r") as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
             print("Error:File not found")
             return 0
file_name = "sample.txt"
with open(file_name , "w") as f:
    f.write("Hello, Priyanka!. Please tell me about yourself")
wordCount = count_word(file_name)
print(wordCount)

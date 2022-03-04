from collections import Counter
def word_count(fname):
        with open(fname, encoding="utf8") as f:
                return str(dict(Counter(f.read().split()).most_common())).replace(',','\n')

with open("D:/Codes/output.txt","w", encoding="utf8") as f: #replace with your output file name with location
    f.write(word_count("D:/Codes/majmoo-fatawa-bin-baz-volume-1-20-text-file.txt")) #replace with your input file name and location 
    f.close()
    print("File Created successfully")

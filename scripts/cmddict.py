import requests as rq
from bs4 import BeautifulSoup
 
def query(word):
    r = rq.get('http://dict.youdao.com/w/eng/' + word)

    soup = BeautifulSoup(r.text, "html.parser")
    # pron_div = soup.find('span', {'class':'phonetic'})
    # output = [elem.string for elem in pron_div]
    # for line in output:
    #     print(line)

    trans_div = soup.find('div', {'class':'trans-container'})
    output = [elem.string for elem in trans_div.findAll('li') if elem.string]
    output = [st.replace(" ", "\t") for st in output]
    for line in output:
        print(line)

if __name__ == '__main__':
    print("")
    while True:
        try:
            word = input('Q: ')
            query(word)
            print("")
        except KeyboardInterrupt:
            break
        except:
            print("Word not found: {}\n".format(word))

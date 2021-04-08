import requests
import bs4
import tkinter 

URL = 'https://www.worldometers.info/coronavirus/'

def get_covid_data():
    data = requests.get(URL)
    bs = bs4.BeautifulSoup(data.text,'html.parser')
    page_info = bs.find('div',class_='content-inner').findAll('div',id="maincounter-wrap")
    all_data = ""

    for block in page_info:
        text = block.find('h1',class_= None).get_text()

        count = block.find('span',class_= None).get_text()

        all_data = all_data + text + " " + count+ "\n"
    return(all_data)     


def get_country_data():
    name = textfield.get()
    print(name)
    data = requests.get('https://www.worldometers.info/coronavirus/country/' + name)
    print(name)
    bs = bs4.BeautifulSoup(data.text,'html.parser')
    print(name)    
    page_info = bs.find('div',class_='content-inner').findAll('div',id="maincounter-wrap")
    all_data = ""

    for block in page_info:
        text = block.find('h1',class_= None).get_text()
        print(name)
        count = block.find('span',class_= None).get_text()

        all_data = all_data + text + " " + count+ "\n"
    print(name)
    print(all_data)
    mainlabel['text'] = all_data


def reload():
    new_data= get_covid_data()
    mainlabel['text'] = new_data


root = tkinter.Tk()
root.geometry("1200x1000")
root.title("Covid Data")
f = ("poppins",35,"bold")

banner=tkinter.PhotoImage(file = "Coronavirus.png")
bannerlabel = tkinter.Label(root,image = banner)
bannerlabel.pack()

textfield = tkinter.Entry(root,width=50,font =f)
textfield.pack()

mainlabel = tkinter.Label(root, text = get_covid_data(),font = f)
mainlabel.pack()

get_country_btn = tkinter.Button(root, text= "Get Data", font= f,relief="solid", command= get_country_data)
get_country_btn.pack()

reload_btn = tkinter.Button(root, text= "Reload", font= f,relief="solid", command= reload)
reload_btn.pack()


root.mainloop()
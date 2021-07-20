from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')


    #Grab the first H5 header tag

    first_h5 = soup.find('h5')
    print(first_h5)

    #Grab all the H5 header tags

    all_h5 = soup.find_all('h5')
    print(all_h5)

    #Grab the course names HTML tags

    course_names = soup.find_all('h5')
    for titles in course_names:
        print(titles.text)

    
    #

    course_cards = soup.find_all('div', class_='card')
    print(course_cards)
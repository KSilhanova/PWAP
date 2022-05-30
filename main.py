from website import create_app

app = create_app() 

if __name__ == '__main__': #pouze když rozběhneme tuto složku, ne když ji importujeme tak rozběhneme to podtím, prostě když spustíme to directly tak pak další řádek
    app.run(debug=True) #run web server, automatically rerun the server

# website nahoře, protože můžeme importovat vše ze složky website
#tohle celé je na run flask applikation, teď už běží ruuning server

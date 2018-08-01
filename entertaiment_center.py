#!/usr/local/bin/python
# coding: latin-1
import media
import fresh_tomatoes

# Define os filmes favoritos
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "https://cdn.europosters.eu/image/1300/posters/toy-story-woody-buzz-i24759.jpg",  # noqa
    "https://www.youtube.com/watch?v=4KPTXpQehio")

avatar = media.Movie(
    "Avatar",
    "A marine on a alien planet",
    "https://upload.wikimedia.org/wikipedia/pt/thumb/b/b0/Avatar-Teaser-Poster.jpg/250px-Avatar-Teaser-Poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=d1_JBMrrYw8")

inception = media.Movie(
    "Inception",
    "Don Cobb e um ladrao que invade os sonhos das \
    pessoas e rouba segredos do subconsciente.",
    "https://upload.wikimedia.org/wikipedia/pt/thumb/7/74/A_origem_poster_portugues.jpg/250px-A_origem_poster_portugues.jpg",  # noqa
    "https://www.youtube.com/watch?v=d3A3-zSOBT4")

school_of_rock = media.Movie(
    "School of Rock",
    "Using rock music to learn",
    "https://upload.wikimedia.org/wikipedia/pt/thumb/1/1b/Schoolrockposter.jpg/210px-Schoolrockposter.jpg",  # noqa
    "https://www.youtube.com/watch?v=3PsUJFEBC74")

midnight_in_paris = media.Movie(
    "Midnight in Paris",
    "Going back in time to meet authors",
    "https://neymotta.files.wordpress.com/2012/01/img283.jpg",
    "https://www.youtube.com/watch?v=BYRWfS2s2v4")

hunger_games = media.Movie(
    "Hunger Games",
    "A really real reality show",
    "http://t2.gstatic.com/images?q=tbn:ANd9GcQLwURCI0Kd6XbibMlXByNwq3LTF0ta5o0KMLJFgjt2vM-I9HrR",  # noqa
    "https://www.youtube.com/watch?v=4S9a5V9ODuY")

toy_story3 = media.Movie(
    "Toy Story 3",
    "Andy se prepara para ir para a faculdade e, inesperadamente,\
     seus leais brinquedos acabando sendo enviados para uma creche.",
    "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-12561-wt2it4_fbf729c8.jpeg?region=0%2C0%2C300%2C450",  # noqa
    "https://www.youtube.com/watch?v=CFQsQzu2KP8")

thor_ragnarok = media.Movie(
    "Thor: Ragnarok",
    "Thor está preso do outro lado do universo. Ele precisa correr\
     contra o tempo para voltar a Asgard e parar Ragnarok, \
     a destruição de seu mundo, que está nas mãos da poderosa \
     e implacável vilã Hela.",
    "http://t0.gstatic.com/images?q=tbn:ANd9GcRr9Ql3T-MXK5X_x2lHdNB4lmB0XC_zFHTCtcIT6YwGbXgrNdbT",  # noqa
    "https://www.youtube.com/watch?v=ue80QwXMRHg")

velozes_e_furiosos2 = media.Movie(
    "+ Velozes + Furiosos",
    "O ex-policial Brian O'Conner se muda de Los Angeles\
     para Miami para recomeçar sua vida. Ele acaba se \
     envolvendo em rachas na sua nova cidade com seu amigo Tej e Suki. ",
    "http://megafilmes.esy.es/gold-app/gold-uploads/media/-velozes-furiosos.jpg",  # noqa
    "https://www.youtube.com/watch?v=Uot4LdQKaQU")

como_treinar_dragao = media.Movie(
    "Como Treinar o Seu Dragao",
    "Soluço é um adolescente viking da ilha de Berk, \
    onde lutar contra dragões é um meio de vida. ",
    "http://telecine.img.estaticos.tv.br/cache/cartazes/como_treinar_dragao_dois_cartaz_220x283.jpg",  # noqa
    "https://www.youtube.com/watch?v=PehM9QaN-aY")

interestelar = media.Movie(
    "Interestelar",
    "As reservas naturais da Terra estão chegando ao fim \
    e um grupo de astronautas recebe a missão de verificar \
    possíveis planetas para receberem a população mundial, \
    possibilitando a continuação da espécie.",
    "http://t2.gstatic.com/images?q=tbn:ANd9GcQMHMl9U1z1txXWCBgKbSlwH0tV3wVIsxyd6CQLhR0CkgC8Nagf",  # noqa
    "https://www.youtube.com/watch?v=zSWdZVtXT7E")

# Armazena os filmes favoritos para uma lista.
moviesFirstLine = [toy_story3, inception, thor_ragnarok]
moviesSecLine = [velozes_e_furiosos2, como_treinar_dragao, interestelar]
movies = moviesFirstLine + moviesSecLine
# Chama a pagina para criação dos filmes \
# com a lista de filmes por parametro.
fresh_tomatoes.open_movies_page(movies)

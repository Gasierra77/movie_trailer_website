import fresh_tomatoes
import Media

toy_story = Media.Movie("Toy Story",
                        "A Story of a boy and his toys that come to life",
                        "http://img.lum.dolimg.com/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

school_of_rock = Media.Movie("Shool of Rock",
                     "Jack Black stars as a hell-raising guitarist with delusions of grandeur. Kicked out of his band and desperate for work, he impersonates a substitute teacher and turns a class of fifth grade high-achievers into high-voltage rock and rollers. Joan Cusack portrays the principal of the private school where Black is prepping the kids for a Battle of the Bands.",
                     "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                     "https://www.youtube.com/watch?v=3PsUJFEBC74&ab_channel=ParamountMovies")

midnight_in_paris = Media.Movie("Midnight in Paris",
                     "This is a romantic comedy set in Paris about a family that goes there because of business, and two young people who are engaged to be married in the fall have experiences there that change their lives. It's about a young man's great love for a city, Paris, and the illusion people have that a life different from theirs would be much better. It stars Owen Wilson, Rachel McAdams, Marion Cotillard, Kathy Bates, Carla Bruni, among others.",
                     "https://thoughtfultomes.files.wordpress.com/2015/06/midnight.jpg",
                     "https://www.youtube.com/watch?v=FAfR8omt-CY&ab_channel=SonyPicturesClassics")

blind_side = Media.Movie("The Blind Side",
                     "The story of Michael Oher, a homeless and traumatized boy who became an All American football player and first round NFL draft pick with the help of a caring woman and her family.",
                     "https://upload.wikimedia.org/wikipedia/en/6/60/Blind_side_poster.jpg",
                     "https://www.youtube.com/watch?v=gvqj_Tk_kuM&ab_channel=MovieclipsTrailerVault")

despicable_me_2 = Media.Movie("Despicable Me II",
                     "While Gru, the ex-supervillain is adjusting to family life and an attempted honest living in the jam business, a secret Arctic laboratory is stolen. The Anti-Villain League decides it needs an insider's help and recruits Gru in the investigation. Together with the eccentric AVL agent, Lucy Wilde, Gru concludes that his prime suspect is the presumed dead supervillain, El Macho, whose his teenage son is also making the moves on his eldest daughter, Margo. Seemingly blinded by his overprotectiveness of his children and his growing mutual attraction to Lucy, Gru seems on the wrong track even as his minions are being quietly kidnapped en masse for some malevolent purpose.",
                     "https://upload.wikimedia.org/wikipedia/en/2/29/Despicable_Me_2_poster.jpg",
                     "https://www.youtube.com/watch?v=uU3hpF7XLPg&ab_channel=MovieclipsTrailers")

forrest_gump = Media.Movie("Forrest Gump",
                     "Forrest Gump is a 1994 American epic romantic-comedy-drama film based on the 1986 novel of the same name by Winston Groom. The film was directed by Robert Zemeckis and stars Tom Hanks, Robin Wright, Gary Sinise, Mykelti Williamson, and Sally Field. The story depicts several decades in the life of Forrest Gump, a slow-witted but kind-hearted, good-natured and athletically prodigious man from Alabama who witnesses, and in some cases influences, some of the defining events of the latter half of the 20th century in the United States; more specifically, the period between Forrest's birth in 1944 and 1982.",
                     "http://www.wichitaorpheum.com/wp-content/uploads/2013/12/Forrest-Gump-Poster.jpg",
                     "https://www.youtube.com/watch?v=uPIEn0M8su0&ab_channel=HolasPhilosophy")

movies = [toy_story, school_of_rock, midnight_in_paris, blind_side, despicable_me_2, forrest_gump]
fresh_tomatoes.open_movies_page(movies)
#print (Media.Movie.VALID_RATINGS)

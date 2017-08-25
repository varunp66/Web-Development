import fresh_tomatoes
import media



# the below lines calls the function def _inti_ from media.py and
# shows the content on the browser
beauty_beast = media.Movie("Beauty and the Beast",
                        "A story of of a village girl who becomes a princess",
                        "https://upload.wikimedia.org/wikipedia/en/d/d6/Beauty_and_the_Beast_2017_poster.jpg",
                        "https://www.youtube.com/watch?v=OvW_L8sTu5E")


la_land = media.Movie("La La Land",
                             "A musical romantic drama",
                             "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",
                             "https://www.youtube.com/watch?v=DBUXcNTjviI")

little_mermaid = media.Movie("The Little Mermaid",
                     "Story of Mermaid",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BODMyNjI5ZjMtNTJmYi00MmEwLWIwYmUtZTgyMzg2OWExNzEzXkEyXkFqcGdeQXVyNjQ3NTcyNzQ@._V1_.jpg",
                     "https://www.youtube.com/watch?v=wWhmheEtIdI")

green_lantern = media.Movie("Green Lantern",
                     "Green Lantern",
                     "https://upload.wikimedia.org/wikipedia/en/6/6b/Green_Lantern_poster.jpg",
                     "https://www.youtube.com/watch?v=vkPx0oyfzeY")

finding_dory = media.Movie("Finding Dory",
                     "Dory, a Regal blue tang, gets separated from her parents as a child.\
                           As she grows up, Dory attempts to search for them",
                     "https://upload.wikimedia.org/wikipedia/en/3/3e/Finding_Dory.jpg",
                     "https://www.youtube.com/watch?v=UXpe8-zCwhI")


dofus = media.Movie("Dofus",
                     "Xelorium: The land of Xelors - The time Manipulators ",
                     "https://static-cdn.jtvnw.net/ttv-boxart/Dofus-138x190.jpg",
                     "https://www.youtube.com/watch?v=Tzc35QVpzfA")


fantastic_four = media.Movie("Fantastic 4: Rise of the Silver Surfer",
                     "Fantstic 4 and silver surfer",
                     "https://upload.wikimedia.org/wikipedia/en/e/e6/Fantastic_Four_2_Poster.jpg",
                     "https://www.youtube.com/watch?v=wuaE80L9y6w") 


harry_potter = media.Movie("Harry Potter: Deathly Hallows 2",
                                "Last sequel of Harry Potter",
                                "https://upload.wikimedia.org/wikipedia/en/d/df/Harry_Potter_and_the_Deathly_Hallows_%E2%80%93_Part_2.jpg",
                                "https://www.youtube.com/watch?v=mObK5XD8udk")


harry_pottr = media.Movie("Harry Potter: Prisoner of Azkaban",
                           "Harry Potter meets Sirius Black",
                           "https://fanart.tv/fanart/movies/673/movieposter/harry-potter-and-the-prisoner-of-azkaban-54f744bb0b117.jpg",
                           "https://www.youtube.com/watch?v=R69laoH02xg")



movies = [beauty_beast, la_land, little_mermaid, green_lantern,
          finding_dory, dofus, fantastic_four, harry_potter, harry_pottr]

#below line takes the movies list from the above line and then opens it on the web browser
fresh_tomatoes.open_movies_page(movies)





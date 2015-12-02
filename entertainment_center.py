import media
import fresh_tomatoes

# Defining static instances of Movies based on movies's information
# Title, Story_line, (Image_url, width, height), youtube_url, production_company, release_date, Location

image_mt1 = media.Image(
    "http://static.srcdn.com/slir/w700-h350-q90-c700:350/wp-content/uploads/Batman-V-Superman-Official-Trailer-Logo.jpg", # NOQA
    "610", "350")
movie_trail1 = media.Movie("Batman-VS-Superman: Dawn of Justice",
                           "Fearing the actions of a god-like Super Hero left"
                           " unchecked, Gotham City's own formidable, forceful"
                           " vigilante takes on Metropolis' most revered,"
                           " modern-day savior, while the world wrestles with"
                           " what sort of hero it really needs. And with"
                           " Batman and Superman at war with one another, a"
                           " new threat quickly arises, putting mankind in"
                           " greater danger than it's ever known before.",
                           image_mt1,
                           "https://www.youtube.com/watch?v=IwfUnkBfdZ4",
                           "Warner Bross",
                           "March 2016",
                           "EE.UU")

image_mt2 = media.Image(
    "http://4.bp.blogspot.com/-9rdcckoeZPU/U8Ctud6cPlI/AAAAAAAAASI/7evngUKhle4/s1600/star_wars_episode_vii_poster_by_nei1b-d6z819w.jpg",  # NOQA
    "500", "664")
movie_trail2 = media.Movie("Star War Episode  VII: The Force Awakens ",
                           "A continuation of the saga created by George Lucas"
                           " and set thirty years after Star Wars: Episode VI"
                           " - Return of the Jedi (1983)",
                           image_mt2,
                           "https://www.youtube.com/watch?v=sGbxmsDFVnE",
                           "LucasFilm",
                           "December 2015",
                           "EE.UU")

image_mt3 = media.Image(
    "http://t2.gstatic.com/images?q=tbn:ANd9GcQJHE0wTHT_pNRdZlnJj5IkzF49uMF3be1gfIIKw8A8z_3oHVRO",  # NOQA
    "560", "840")
movie_trail3 = media.Movie("Captain America: Civil War",
                           "After another incident involving the Avengers"
                           " results in collateral damage, political pressure"
                           " mounts to install a system of accountability,"
                           " headed by a governing body to oversee and direct"
                           " the team. The new status quo fractures the"
                           " Avengers, resulting in two camps, one led by"
                           " Steve Rogers and his desire for the Avengers to"
                           " remain free to defend humanity without"
                           " government interference, and the other following"
                           " Tony Stark's surprising decision to support"
                           " government oversight and accountability",
                           image_mt3,
                           "https://www.youtube.com/watch?v=xnv__ogkt0M",
                           "Marvel Studios",
                           "May 2016",
                           "EE.UU")

# Create a list of movies with variables movie_trailX
movies = []
movies.append(movie_trail1)
movies.append(movie_trail2)
movies.append(movie_trail3)

# call the function to create the html file to open in the browser
fresh_tomatoes.open_movies_page(movies)

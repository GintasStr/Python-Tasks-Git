# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# wasExpensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False. 

class Movie:
    def __init__(self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget


    def wasExpensive(self):
        if self.budget >= 100000000:
            print(f"Filmas: {self.title}. Direktorius: {self.director} Biudžetas {self.budget}")
            return True
        else:
            print(f"Filmas: {self.title}. Direktorius: {self.director}. Biudžetas {self.budget}")
            return False
        

movie2 = Movie('About python', 'Gintas S.', 99999999)
print(movie2.wasExpensive())

movie3 = Movie('Zen of Python', 'Gintas S.', 100000050)
print(movie3.wasExpensive())
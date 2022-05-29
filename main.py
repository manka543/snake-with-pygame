import game

# TODO: Dodać bordery do ciała węża; Zamiast borderu trzeba malować małe prostokąty bo w pygame.draw.rect() nie ma bodreru dla konkretnej krawędzi
# TODO: Lepszy endscreen
# TODO: Czas na klatke; Nie wiem czy to będzie dobre rozwiązanie bo może to zabużyć responsywność w poruszaniu się węża
# TODO: Naprawić start węża; Pierwszy i drugi element ciała węża pojawia się w tym samym miejscu i dubluje się; nie mam pojęcia dlaczego to nie działa ale nie działa :(

gra = game.Game()

gra.gameloop()
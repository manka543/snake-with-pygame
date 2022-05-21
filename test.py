import snake
import apple

# Nie potrafie pisać testów jednostkowych
# Robie to bez żadnego tutoriala
# Tak dla beki
# Wiem że nie mają sensu

class SnakeUnitTests:
    # True means positive end; False means negative test
    Test1: bool

    def __init__(self):
        self.Test1 = self.test1()
        
        self.showresults()

    

    def test1():
        Snake = snake.Snake("nic") # Jak wywołasz funkcje rysującą go na ekranie to wywali skrypt tak o
        for i in range(10000):
            Apple = (18,12)
            if Apple in Snake.body:
                return False
        return True
    
    def showresults(self):
        print("Tests results:")
        print("Test1: ",self.Test1)

snakeUnitTests = SnakeUnitTests()
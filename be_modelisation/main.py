from view import show_results
from model import Parameters, trajectoire, Point

def run():
    # Paramètres du robot (à modifier)
    parameters = Parameters(
        [1, 1, 1, 1, 1],    # [L1, L2, L3, L4, L5]
        [1, 1]              # [h1, h2]
    )
    
    # Paramètres de la trajectoire (à modifier)
    a = Point(4, 1, 3) # Point(x, y, z)
    b = Point(3, 1, 5) # Point(x, y, z)
    theta = 0
    v = 1

    # Calcul de la trajectoire et affichage des résultats
    livrable = trajectoire(a, b, theta, v, parameters)
    show_results(livrable, parameters, a, b)


if __name__ == "__main__":
    run()
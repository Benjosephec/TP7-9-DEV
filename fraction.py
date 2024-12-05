class Fraction:
    """Class representing a fraction and operations on it.

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """Construit une fraction basée sur un numérateur et un dénominateur.

        PRE: den != 0
        RAISES: ValueError si den == 0.
        POST: La fraction est réduite à sa forme la plus simple.
        """
        pass

    @property
    def numerator(self) -> int:
        pass

    @property
    def denominator(self) -> int:
        pass

    # ------------------ Textual representations ------------------

    def __str__(self) -> str:
        """Retourne une représentation textuelle de la forme réduite de la fraction.

        POST: Retourne la fraction sous la forme "numerateur/denominateur" ou sous forme d'entier si le dénominateur est égal à 1.
        """
        pass

    def as_mixed_number(self) -> str:
        """Retourne une représentation textuelle de la fraction sous forme de nombre mixte.

        Un nombre mixte est la somme d'un entier et d'une fraction propre.

        POST: Retourne une chaîne sous la forme "partie_entière numerateur/denominateur" ou "partie_entière" si aucun reste.
        """
        pass

    # ------------------ Operators overloading ------------------

    def __add__(self, other) -> "Fraction":
        """Surcharge de l'opérateur + pour les fractions.

        PRE: other doit être une fraction
        RAISES: TypeError si other n'est pas une Fraction.
        POST: Retourne un nouvel objet Fraction représentant la somme.
        """
        pass

    def __sub__(self, other) -> "Fraction":
        """Surcharge de l'opérateur - pour les fractions.

        PRE: other doit être une fraction
        RAISES: TypeError si other n'est pas une Fraction.
        POST: Retourne un nouvel objet Fraction représentant la différence.
        """
        pass

    def __mul__(self, other) -> "Fraction":
        """Surcharge de l'opérateur * pour les fractions.

        PRE: other doit être une fraction
        RAISES: TypeError si other n'est pas une Fraction.
        POST: Retourne un nouvel objet Fraction représentant le produit.
        """
        pass

    def __truediv__(self, other) -> "Fraction":
        """Surcharge de l'opérateur / pour les fractions.

        PRE: other.numerator != 0, other doit être une fraction
        RAISES: ZeroDivisionError si other.numerator == 0, TypeError si other n'est pas une Fraction.
        POST: Retourne un nouvel objet Fraction représentant le quotient.
        """
        pass

    def __pow__(self, power: int) -> "Fraction":
        """Surcharge de l'opérateur ** pour les fractions.

        PRE: power est un entier
        RAISES: TypeError si power n'est pas un entier.
        POST: Retourne un nouvel objet Fraction représentant la puissance.
        """
        pass

    def __eq__(self, other) -> bool:
        """Surcharge de l'opérateur == pour les fractions.

        POST: Retourne True si les fractions sont équivalentes, sinon False.
        """
        pass

    def __float__(self) -> float:
        """Retourne la valeur décimale de la fraction.

        POST: Retourne une valeur float de la fraction.
        """
        pass

    # ------------------ Properties checking  ------------------

    def is_zero(self) -> bool:
        """Vérifie si la valeur de la fraction est égale à 0.

        POST: Retourne True si la fraction est égale à 0, sinon False.
        """
        pass

    def is_integer(self) -> bool:
        """Vérifie si la fraction est un entier.

        POST: Retourne True si la fraction est un entier, sinon False.
        """
        pass

    def is_proper(self) -> bool:
        """Vérifie si la valeur absolue de la fraction est < 1.

        POST: Retourne True si la fraction est propre, sinon False.
        """
        pass

    def is_unit(self) -> bool:
        """Vérifie si le numérateur de la fraction est égal à 1 dans sa forme réduite.

        POST: Retourne True si le numérateur est égal à 1, sinon False.
        """
        pass

    def is_adjacent_to(self, other) -> bool:
        """Vérifie si deux fractions diffèrent d'une fraction unitaire.

        RAISES: TypeError si other n'est pas une Fraction.
        POST: Retourne True si la différence absolue est une fraction unitaire.
        """
        pass

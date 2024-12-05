from math import gcd

class Fraction:
    """Classe représentant une fraction et les opérations qui peuvent être effectuées sur celle-ci.

    Auteur : V. Van den Schrieck
    Date : Octobre 2021
    Cette classe permet de manipuler des fractions via plusieurs opérations.
    """

    def __init__(self, num: int = 0, den: int = 1):
        """Construit une fraction à partir d'un numérateur et d'un dénominateur.

        PRÉCONDITIONS :
        - `den` ne doit pas être égal à zéro (division par zéro non définie).
        - `num` et `den` doivent être des entiers.
        POSTCONDITIONS :
        - La fraction est stockée sous forme simplifiée.
        - Le dénominateur est toujours positif (le signe est ajusté sur le numérateur si nécessaire).
        """
        if den == 0:
            raise ValueError("Le dénominateur ne peut pas être zéro.")
        common = gcd(num, den)
        self.num = num // common
        self.den = den // common
        if self.den < 0:
            self.num = -self.num
            self.den = -self.den

    @property
    def numerator(self) -> int:
        """Retourne le numérateur de la fraction."""
        return self.num

    @property
    def denominator(self) -> int:
        """Retourne le dénominateur de la fraction."""
        return self.den

    def __str__(self) -> str:
        """Retourne une représentation textuelle de la fraction sous forme réduite.

        PRÉCONDITIONS : None
        POSTCONDITIONS :
        - Return une chaîne de caractères au format 'numérateur/dénominateur'
          ou simplement 'numérateur' si le dénominateur est 1.
        """
        if self.den == 1:
            return f"{self.num}"
        return f"{self.num}/{self.den}"

    def as_mixed_number(self) -> str:
        """Retourne une représentation textuelle de la fraction sous forme de nombre mixte."""
        if abs(self.num) < self.den:
            return str(self)

        # Calcul de la partie entière (ajustée pour les négatifs)
        if self.num < 0:
            whole = -(abs(self.num) // self.den)  # Partie entière correcte
            remainder = abs(self.num) % self.den
        else:
            whole = self.num // self.den
            remainder = self.num % self.den

        # Si le reste est nul, retourne uniquement la partie entière
        if remainder == 0:
            return f"{whole}"

        # Retourne le nombre mixte au format attendu
        return f"{whole} {remainder}/{self.den}"

    def __add__(self, other: 'Fraction') -> 'Fraction':
        """Surcharge de l'opérateur + pour les fractions.

        PRÉCONDITIONS :
        - `other` doit être une instance de `Fraction`.
        POSTCONDITIONS :
        - Return une nouvelle instance de `Fraction` représentant la somme de `self` et `other`, sous forme simplifiée.
        """
        if not isinstance(other, Fraction):
            raise TypeError("L'autre opérande doit être une instance de Fraction.")
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        return Fraction(num, den)

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        """Surcharge de l'opérateur - pour les fractions.

        PRÉCONDITIONS :
        - `other` doit être une instance de `Fraction`.
        POSTCONDITIONS :
        - Return une nouvelle instance de `Fraction` représentant la différence de `self` et `other`, sous forme simplifiée.
        """
        if not isinstance(other, Fraction):
            raise TypeError("L'autre opérande doit être une instance de Fraction.")
        num = self.num * other.den - other.num * self.den
        den = self.den * other.den
        return Fraction(num, den)

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        """Surcharge de l'opérateur * pour les fractions.

        PRÉCONDITIONS :
        - `other` doit être une instance de `Fraction`.
        POSTCONDITIONS :
        - Return une nouvelle instance de `Fraction` représentant le produit de `self` et `other`, sous forme simplifiée.
        """
        if not isinstance(other, Fraction):
            raise TypeError("L'autre opérande doit être une instance de Fraction.")
        return Fraction(self.num * other.num, self.den * other.den)

    def __truediv__(self, other: 'Fraction') -> 'Fraction':
        """Surcharge de l'opérateur / pour les fractions.

        PRÉCONDITIONS :
        - `other` doit être une instance de `Fraction`.
        - `other` ne doit pas être égal à zéro.
        POSTCONDITIONS :
        - Return une nouvelle instance de `Fraction` représentant le quotient de `self` et `other`, sous forme simplifiée.
        """
        if not isinstance(other, Fraction):
            raise TypeError("L'autre opérande doit être une instance de Fraction.")
        if other.num == 0:
            raise ZeroDivisionError("Division par une fraction nulle.")
        return Fraction(self.num * other.den, self.den * other.num)

    def __pow__(self, power: int) -> 'Fraction':
        """Surcharge de l'opérateur ** pour les fractions.

        PRÉCONDITIONS :
        - `power` doit être un entier.
        POSTCONDITIONS :
        - Return une nouvelle instance de `Fraction` représentant `self` élevé à la puissance `power`, sous forme simplifiée.
        """
        if not isinstance(power, int):
            raise TypeError("La puissance doit être un entier.")
        return Fraction(self.num ** power, self.den ** power)

    def __eq__(self, other: 'Fraction') -> bool:
        """Surcharge de l'opérateur == pour les fractions.

        PRÉCONDITIONS :
        - `other` doit être une instance de `Fraction`.
        POSTCONDITIONS :
        - Return True si `self` et `other` sont égaux, False sinon.
        """
        if not isinstance(other, Fraction):
            return False
        return self.num * other.den == self.den * other.num

    def __float__(self) -> float:
        """Retourne la valeur décimale de la fraction.

        PRÉCONDITIONS : None
        POSTCONDITIONS :
        - Return un flottant correspondant à la valeur de la fraction.
        """
        return self.num / self.den

    def is_zero(self) -> bool:
        """Vérifie si la valeur de la fraction est 0.

        PRÉCONDITIONS : None
        POSTCONDITIONS :
        - Return True si la fraction est égale à 0, False sinon.
        """
        return self.num == 0

    def is_integer(self) -> bool:
        """Vérifie si une fraction est entière (exemple : 8/4, 3, 2/2).

        PRÉCONDITIONS : None
        POSTCONDITIONS :
        - Return True si la fraction est entière, False sinon.
        """
        return self.num % self.den == 0

    def is_proper(self) -> bool:
        """Vérifie si la valeur absolue de la fraction est < 1.

        PRÉCONDITIONS : None
        POSTCONDITIONS :
        - Return True si la valeur absolue de la fraction est inférieure à 1, False sinon.
        """
        return abs(self.num) < self.den

    def is_unit(self) -> bool:
        """Vérifie si le numérateur de la fraction réduite est 1.

        PRÉCONDITIONS : None
        POSTCONDITIONS :
        - Return True si la fraction est une fraction unité, False sinon.
        """
        return self.num == 1 and self.den > 0

    def is_adjacent_to(self, other: 'Fraction') -> bool:
        """Vérifie si deux fractions diffèrent par une fraction unité.

        PRÉCONDITIONS :
        - `other` doit être une instance de `Fraction`.
        POSTCONDITIONS :
        - Return True si la valeur absolue de la différence entre `self` et `other` est une fraction unité.
        """
        if not isinstance(other, Fraction):
            raise TypeError("L'autre opérande doit être une instance de Fraction.")
        return (self - other).is_unit()

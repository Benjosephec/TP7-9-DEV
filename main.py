from Classdesaad import Fraction

def main():
    try:
        # Création de fractions
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 4)
        f3 = Fraction(5, 0)
    except ValueError as e:
        print(f"Erreur lors de la création de la fraction : {e}")

    try:
        result_add = f1 + f2
        print(f"{f1} + {f2} = {result_add}")

        result_sub = f1 - f2
        print(f"{f1} - {f2} = {result_sub}")

        result_mul = f1 * f2
        print(f"{f1} * {f2} = {result_mul}")

        result_div = f1 / f2
        print(f"{f1} / {f2} = {result_div}")

        f_zero = Fraction(0, 1)
        result_div_zero = f1 / f_zero
    except ZeroDivisionError as e:
        print(f"Erreur lors de la division : {e}")

    try:
        result_pow = f1 ** 2
        print(f"{f1} ** 2 = {result_pow}")

        print(f"{f1} == {f2}: {f1 == f2}")

        print(f"Valeur décimale de {f1}: {float(f1)}")

        print(f"{f1} est nul : {f1.is_zero()}")
        print(f"{f1} est un entier : {f1.is_integer()}")
        print(f"{f1} est propre : {f1.is_proper()}")
        print(f"{f1} est une unité : {f1.is_unit()}")

        # Adjacence
        print(f"{f1} est adjacent à {f2}: {f1.is_adjacent_to(f2)}")
    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    main()

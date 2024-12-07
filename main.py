from fraction import Fraction

def main():
    print("=== Demonstration of the Fraction class ===")
    try:
        # Création de fractions
        print("\n--- Creation of fractions ---")
        f1 = Fraction(3, 5)
        f2 = Fraction(7, 10)
        f3 = Fraction(4, 7)
        f4 = Fraction(-6, -12)  # Devrait être réduit à 1/2
        print(f"Fraction 1: {f1}")  # 3/5
        print(f"Fraction 2: {f2}")  # 7/10
        print(f"Fraction 3: {f3}")  # 4/7
        print(f"Fraction 4 (reduced): {f4}")  # 1/2

        # Opérations mathématiques
        print("\n--- Mathematical operations ---")
        print(f"Addition: {f1} + {f2} = {f1 + f2}")  # 41/50
        print(f"Subtraction: {f1} - {f2} = {f1 - f2}")  # -1/10
        print(f"Multiplication: {f1} * {f3} = {f1 * f3}")  # 12/35
        print(f"Division: {f2} / {f3} = {f2 / f3}")  # 49/40

        # Comparaisons
        print("\n--- Comparisons ---")
        print(f"{f4} == {Fraction(1, 2)} = {f4 == Fraction(1, 2)}")  # True

        # Propriétés de fractions
        print("\n--- Fraction properties ---")
        print(f"{f1} is zero: {f1.is_zero()}")  # False
        print(f"{f4} is proper: {f4.is_proper()}")  # True
        print(f"{f3} is an integer: {f3.is_integer()}")  # False
        print(f"{f4} is a unit fraction: {f4.is_unit()}")  # True
        print(f"{f1} is adjacent to {f2}: {f1.is_adjacent_to(f2)}")  # False

        # Représentation sous forme de nombre mixte
        print("\n--- Mixed number representation ---")
        f5 = Fraction(11, 6)
        print(f"{f5} as mixed number: {f5.as_mixed_number()}")  # 1 5/6

        # Gestion des erreurs
        print("\n--- Handling errors ---")
        try:
            Fraction(1, 0)  # Devrait lever une ValueError
        except ValueError as e:
            print(f"Error creating fraction: {e}")

        try:
            f1 / Fraction(0, 1)  # Division par zéro
        except ZeroDivisionError as e:
            print(f"Error during division: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()

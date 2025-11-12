class NegativeNumberDetectedError(ValueError):
    """Wird geworfen, wenn eine negative Zahl eingegeben wurde."""
    pass

class InvalidInputDataError(ValueError):
    """Wird geworfen, wenn der Eingabestring leer ist oder keine gültigen Daten enthält."""
    pass

def parse_numbers():
    try:
        eingabe = input("gib mir 4 nummer bitt (getrennt durch komma): ")

        if not eingabe or not eingabe.strip():
            raise InvalidInputDataError("Keine Eingabe vorhanden.")

        parts = [p.strip() for p in eingabe.split(",") if p.strip() != ""]
        if len(parts) != 4:
            raise InvalidInputDataError("Bitte genau 4 Zahlen eingeben (komma-getrennt).")

        zahlen = tuple(int(x) for x in parts)  # ValueError bei nicht-numerischen Werten

        if any(n < 0 for n in zahlen):
            raise NegativeNumberDetectedError("Negative Zahl erkannt. Bitte nur positive Zahlen.")

        print("du hast das geschafft!!")
        return zahlen

    except ValueError:
        print("Das war keine gültige Zahl! Bitte gib nur Ziffern ein.")
    except NegativeNumberDetectedError as e:
        print(e)
    except InvalidInputDataError as e:
        print(e)

    return None

result = parse_numbers()
print(f"Eingegeben: {result}")
print(f"Typ: {type(result)}")


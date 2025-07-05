import random

# Databáze otázek rozdělená podle témat
QUESTIONS = {
    "vztek": [
        "Co bys chtěl/a vykřičet do světa a proč?",
        "Na koho nebo na co tě nejvíc štveš a co bys mu/ji řekl/a, kdybys mohl?",
        "Jaká energie se skrývá za tvým vztekem – zklamání, bezmoc, nebo něco jiného?",
        "Co potřebuješ udělat, aby se tvůj vztek mohl bezpečně uvolnit?",
        "Co by ti pomohlo necítit se pod tlakem?"
    ],
    "smutek": [
        "Co ti v poslední době chybělo nejvíc?",
        "Kdy naposledy jsi měl/a pocit, že ti nikdo nerozumí?",
        "Jaký okamžik ti poslední dobou vehnal slzy do očí – i vnitřní?",
        "Co tě v srdci tíží, ale nechceš to nahlas přiznat?",
        "Jak bys popsal/a svůj smutek jako obraz nebo zvuk?"
    ],
    "radost": [
        "Co tě dnes potěšilo, i kdyby jen na pár vteřin?",
        "Kdy naposledy ses smál/a bez zábran?",
        "Co ti dává pocit naplnění?",
        "Jak si můžeš dopřát víc okamžiků, které tě dobíjejí?",
        "Na co se momentálně těšíš – i kdyby to byla maličkost?"
    ],
    "reflexe": [
        "Co sis dnes o sobě uvědomil/a?",
        "Jaká myšlenka ti dnes nedá spát?",
        "Které rozhodnutí tě poslední dobou nejvíc ovlivnilo?",
        "Co ti dnes sebralo energii – a co ji vrátilo?",
        "Kdy jsi naposledy byl/a laskavý/á sám/a k sobě?"
    ]
}

def generate_journaling_question(theme=None):
    if theme in QUESTIONS:
        return random.choice(QUESTIONS[theme])
    # Pokud není zadáno téma nebo je neplatné, losuj ze všech
    all_questions = [q for sublist in QUESTIONS.values() for q in sublist]
    return random.choice(all_questions)

# Ukázka použití
if __name__ == "__main__":
    print("Obecná otázka:", generate_journaling_question())
    print("Otázka pro téma 'smutek':", generate_journaling_question("smutek"))
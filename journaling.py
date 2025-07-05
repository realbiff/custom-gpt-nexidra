import random

def generate_journaling_question():
    questions = [
        "Co ti dnes vzalo nejvíc energie?",
        "Kdy ses naposledy cítil/a skutečně v klidu?",
        "Jakou myšlenku dnes nejde dostat z hlavy?",
        "Co bys nejraději právě teď vykřičel/a do světa?",
        "Kdo nebo co ti dnes udělalo radost – i když jen malou?",
        "Co se ti honí hlavou, ale ještě jsi to nikomu neřekl/a?",
        "Jaké by bylo jedno malé rozhodnutí, které by ti teď mohlo ulevit?",
        "Co ti tvůj dnešní vnitřní hlas říká?",
        "Jaké emoce si dnes všiml/a, ale ignoroval/a je?",
        "Co si přeješ, aby ti někdo pochopil – beze slov?"
    ]
    return random.choice(questions)

# Ukázkové použití
if __name__ == "__main__":
    print(generate_journaling_question())
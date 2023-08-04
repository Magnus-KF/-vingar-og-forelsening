
from InquirerPy import inquirer

choices = ["kort", "medium", "lang"]

valg = inquirer.select(message="Kor lang tur vil du gå?", choices=choices).execute()
bekreft = inquirer.confirm(message="Er du sikker?").execute()

if valg == choices[0]:
    print("Spesielle ting for kort tur skjer")
elif valg == choices[1]:
    print("Spesielle ting for medium tur skjer")
elif valg == choices[2]:
    print("Spesielle ting for lang tur skjer")

    
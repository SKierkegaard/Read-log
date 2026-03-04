import csv
from datetime import datetime
from pathlib import Path

LOG_DIR = Path("logs")
LOG_FILE = LOG_DIR / "log.csv"

def init_log():
    LOG_DIR.mkdir(exist_ok = True)

    if not LOG_FILE.exists():
        with open(LOG_FILE, "w", newline = "", encoding = "utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["day", "date", "title", "author", "minutes"])

def get_day():
    with open(LOG_FILE, "r", encoding = "utf-8") as f:
        reader  = csv.reader(f)
        date = 0
        day = 0
        for i in reader:
            day = i[0]
            date = i[1]

        if date == "day":
            return 0, 0
        
        return int(day), date

def update_log(): 
    get_current_day = get_day()
    current_date = datetime.now().strftime("%d-%m-%Y")
    
    if get_current_day[1] != current_date:
        day = get_current_day[0] + 1
    else:
        day = get_current_day[0]

    date = datetime.now().strftime("%d-%m-%Y")
    title = input("Título da leitura: ")
    author = input("Nome do autor: ")

    while True:
        try:
            minutes = int(input("Minutos lidos: "))
            break
        except ValueError:
            print("Digite um inteiro pra os minutos.")

    with open(LOG_FILE, "a", newline = "", encoding = "utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([day, date, title, author, minutes])

    print("Leitura registrada com sucesso!")

def main():
    init_log()

    add_read = input("Adcionar leitura [y/n]: ").casefold()
    if add_read == "y":
        update_log()
    else:
        print("Saindo...")

main()

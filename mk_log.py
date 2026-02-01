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
        lines = f.readlines()
        if len(lines) <= 1:
            return 0

        last_line = lines[-1]
        return int(last_line.split(",")[0])

def update_log(): 
    first_read = input("Esta é sua primeira leitura do dia? [y/n]: ").strip().lower()
    current_day = get_day()

    if first_read == 'y':
        day = current_day + 1
    else:
        day = current_day

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

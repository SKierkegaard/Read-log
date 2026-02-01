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
    with open(LOG_FILE, "r") as f:
        reader = csv.reader(f)
        next(reader)
        a = 0
        for i in reader:
            a = i[0]
        
        return a

def update_log():
    first_read = input("Esta é sua primeira leitura do dia? [y/n]: ").casefold()
    day = int(get_day())

    if first_read == "y":
        day += 1
        date = datetime.now().strftime("%d-%m-%Y")
        title = input("Título da leitura: ")
        author = input("Nome do autor: ")
        minutes = int(input("Minutos lidos: "))

        with open(LOG_FILE, "a", newline = "", encoding = "utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([day, date, title, author, minutes])
    else:
        date = datetime.now().strftime("%d-%m-%Y")
        title = input("Título da leitura: ")
        author = input("Nome do autor: ")
        minutes = input("Minutos lidos: ")

        with open(LOG_FILE, "a", newline = "", encoding = "utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([day, date, title, author, minutes])

def main():
    init_log()

    add_read = input("Adcionar leitura [y/n]: ").casefold()
    if add_read == "y":
        update_log()
    else:
        print("Saindo...")

main()

import csv
from connect import connect

# insert from csv
def insert_from_csv():
    conn = connect()
    cur = conn.cursor()
    
    with open("contacts.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (row[0], row[1]))

    conn.commit()
    cur.close()
    conn.close()

# insert from console
def insert_manual():
    name = input("Name: ")
    phone = input("Phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))

    conn.commit()
    cur.close()
    conn.close()

# query
def search():
    keyword = input("Search: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s OR phone LIKE %s", (f"%{keyword}%", f"%{keyword}%"))

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()

# update
def update():
    name = input("Enter name to update: ")
    new_phone = input("New phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (new_phone, name))

    conn.commit()
    cur.close()
    conn.close()

# delete
def delete():
    name = input("Enter name to delete: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))

    conn.commit()
    cur.close()
    conn.close()

# menu
while True:
    print("\n1.Insert CSV\n2.Insert Manual\n3.Search\n4.Update\n5.Delete\n6.Exit")

    choice = input("Choose: ")

    if choice == "1":
        insert_from_csv()
    elif choice == "2":
        insert_manual()
    elif choice == "3":
        search()
    elif choice == "4":
        update()
    elif choice == "5":
        delete()
    elif choice == "6":
        break
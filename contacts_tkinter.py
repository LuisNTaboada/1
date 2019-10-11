import pickle

from time import sleep
from tkinter import *
from tkinter import ttk, StringVar

ACTION_ADD_CONTACT = 1
ACTION_REMOVE_CONTACT = 2
ACTION_FIND_CONTACT = 3
ACTION_EXPORT_CONTACT = 4
ACTION_EXIT = 5

SAVE_FILE_NAME = "contacts.save"

MENU__OPTIONS = [ACTION_ADD_CONTACT, ACTION_REMOVE_CONTACT, ACTION_FIND_CONTACT, ACTION_EXPORT_CONTACT ,ACTION_EXIT]

def ask_until_expected(options):

    selected_action = " "

    while not selected_action.isdigit() or (selected_action.isdigit() and int(selected_action) not in options):
        selected_action = input("Que quieres hacer? ")

    return int(selected_action)


def show_menu():
    print("Acciones disponibles: ")
    print("1- Añadir contacto ")
    print("2- Borrar contacto ")
    print("3- Buscar contacto ")
    print("4- Exportar contacto ")
    print("5- Salir")
    return ask_until_expected(MENU__OPTIONS)

def add_contact(contacts, name, phone, email):
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)

    return contact

def ask_new_contact(contacts):
    print("\n\nAñadir contacto\n")
    contact = add_contact(contacts, input("Nombre: "), input("Telefono: "), input("Email: "))

    print("Se ha añadido {} correctamente\n".format(contact["name"]))
    sleep(1)



def remove_contact(contacts):
    search_term = input("Que contacto quieres borrar ?")
    for contact in contacts:
        if contact["name"] == search_term:
            contacts.remove(contact)

def find_contact(contacts):
    print("\n\nBuscar contacto\n")
    search_term = input("Dime el nombre del contacto o parte de el: ")
    found_contacts = []

    print("He encontrado los siguientes contactos:\n")
    contact_counter = 1
    contact_indexes = []

    for contact in contacts:
        if contact["name"].find(search_term) >= 0:
            found_contacts.append(contact)


            print("{} - {}".format(contact_counter, contact["name"]))
            contact_indexes .append(contact_counter)
            contact_counter += 1

    contact_index = 0

    if len(contact_indexes) > 1:
        contact_index = ask_until_expected(contact_indexes)

    elif len(contact_indexes) == 0:
        print("No se ha encontrado nada")

        return

    print("\nInformacion sobre {}\n\n".format(found_contacts[contact_index]["name"]))
    print("Nombre:{name}, Telefono {phone}, Email {email}\n\n ".format(**found_contacts[contact_index]))
    return found_contacts

def export_contact():
    pass


def load_contacts():
    try:
        contacts = pickle.load(open(SAVE_FILE_NAME, "rb"))
    except FileNotFoundError:
        return[]

def save_contacts(contacts):
    with open(SAVE_FILE_NAME, "wb") as save_file:
        pickle.dump(contacts, save_file)
    print("Data saved correctly")

def main():
    contacts = []

    name = StringVar()
    email = StringVar()
    phone = StringVar()

    contacts = load_contacts()

    root = Tk()
    frame_add_contact = ttk.Frame(root, padding ="10,10,10,10")
    frame_add_contact.grid()

    contact_list = ttk.Frame(root, padding="12,12,12,12")
    contact_list.grid()

    ttk.Label(frame_add_contact, text="Nombre").grid(column=1, row=1)
    ttk.Label(frame_add_contact, text="Email").grid(column=2, row=1)
    ttk.Label(frame_add_contact, text="Telefono").grid(column=3, row=1)

    ttk.Entry(frame_add_contact, width=7, textvariable=name).grid(column=1, row=2)
    ttk.Entry(frame_add_contact, width=7, textvariable=email).grid(column=2, row=2)
    ttk.Entry(frame_add_contact, width=7, textvariable=phone).grid(column=3, row=2)

    ttk.Button(frame_add_contact,
               text="Añadir",
               command=lambda: add_contact(contacts, name.get(), phone.get(), email.get())).grid(column=3, row=3)

    root.mainloop()

if __name__ == "__main__" :
    main()
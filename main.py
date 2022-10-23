import string
import secrets
import csv

while True:

    # Getting letters, numbers, and special characters
    characters = string.ascii_letters + string.punctuation + string.digits

    # Randomizing
    password = "".join(secrets.choice(characters) for x in range(16))

    title = input("\nTitle of Password:\n>>")

    print("Title:\n" + title + "\n\nPassword:\n" + password)

    with open("test.csv", "a", encoding="utf-8") as file:

        writer = csv.writer(file)

        # Writes the title
        writer.writerow([str(title)])

        # Writes the generated password
        writer.writerow([str(password)])

        # Creates a new row
        writer.writerow("\n")

        # Repeat? y/n
        choice = input("\nEnter another? [y/n]")

        if choice == "y":
            continue
        else:
            break
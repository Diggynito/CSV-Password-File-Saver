Lines 1-3: Three modules, string, secrets, and csv are required, and I’ve linked to each of their documentation if further reading is needed. Python recommends using secrets in lieu of the random module noting: “In particular, secrets should be used in preference to the default pseudo-random number generator in the random module, which is designed for modelling and simulation, not security or cryptography.”

Line 5: The entire Python code is wrapped in a while True loop, which will run as long as the conditional expression evaluates to True. This is to allow the user to enter more generated passwords, which will be found on line 31-36.

Lines 8 and 11: These are variables to be used later. The characters variable makes use of the string module to use ascii_lowercase and ascii_uppercase constants, punctuations (e.g. !”#$%&'()*+,-./:;<=>?@[\]^_`{|}~), and digits (e.g. 0123456789). Combining these three constants will help create a strong password. To make this much more secure, the secrets module is used to randomize the password in 16 characters.

Line 13: The title variable is used to help the user to correlate what the password is referencing.

Line 15: In order for the user to identify their password, Python prompts “Title of Password:”. Once a title is entered, a password will be generated.

Line 17: This portion has a few interesting things to get the data moved to a CSV spreadsheet. Firstly, it’s going to open() a file, followed by a file name/location. Next, "a" is used, which opens a file for appending. If the file doesn’t exist, it creates a new file for writing. I see a lot of people using "w", which opens a file for writing only and overwrites the file if the file exists. In this case, I don’t want to blow away my data every time I update, so I use 'a'. Lastly, encoding="utf-8'" makes sure the data is encoded properly.

Lines 19-28: To write to a CSV file in Python, we use the csv.writer() function. This function writes the user’s data into a delimited string. This string can then be used to write into CSV files using the writerow(). writer.writerow([str(title)]) and writer.writerow([str(password)]) store the variables into the CSV spreadsheet. Using str() allows the data to be in one cell. If that was removed, each character would be on its own cell.

Lines 31-36: The user is asked whether they want to add more entries or quit. A simple if else will determine either repeating the loop or quitting.

## Read Me: Passphrase Validator

This program checks the validity of passphrases in a text file and counts the number of correct ones.

**Requirements:**

* Python 3

**How to Use:**

1.  **Create a text file:** Save your passphrases, one per line, in a text file. 
2.  **Run the program:** Execute the `validation.py` script in your terminal. 
    * The script will attempt to open the file named "test.txt" by default.
    * If "test.txt" is not found, it will try to open "test.txt.txt".
    * If neither file is found, the program will prompt you to check the file name and try again.
3.  **Output:** The program will print the following information:
    * A list containing each line from the file along with:
        * A validation status (True/False)
        * Counters for spaces, capital letters, and punctuation marks (used for debugging purposes)
    * The total number of valid passphrases found in the file.

**Passphrase Criteria:**

A valid passphrase must meet the following criteria:

* Consist of more than one word (separated by spaces)
* End with a punctuation mark (!, ?, .)
* Not contain the same word repeated
* Only contain lowercase letters (a-z)
* Only contain characters from the English alphabet (no special characters or numbers)

**Notes:**

* This program focuses on validating the format of the passphrases, not their meaning.
* The code uses helper functions to check for specific criteria like punctuation, whitespace, capitalization, and repeated words. 
* Global variables are used to track counts during validation (space_counter, capital_counter, punctuation_counter). These are reset for each line processed.

**Further Development:**

* You can modify the program to write the validation results to a separate file.
* Error handling can be improved to provide more specific feedback for invalid passphrases.

We recommend using a more secure password management solution for storing actual passwords. 

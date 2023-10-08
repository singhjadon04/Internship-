#!/usr/bin/env python
# coding: utf-8

# In[46]:


# Sample text-1
text = 'Python Exercises, PHP exercises.'

# Replace space, comma, and dot with a colon
result = text.replace(' ', ':').replace(',', ':').replace('.', ':')
print(result)


# In[48]:


# Sample text-
import re

def find_words_starting_with_a_or_e(input_string):
    # Split the input string into words using regular expression
    words = re.findall(r'\b\w+\b', input_string)
    
   
    result = []
    for word in words:
        if word[0].lower() in ['a', 'e']:
            result.append(word)
    
    return result

# Input string
input_string = "Apple is an amazing fruit. Elephants are enormous."

words_starting_with_a_or_e = find_words_starting_with_a_or_e(input_string)
print("Words starting with 'a' or 'e':", words_starting_with_a_or_e)



# In[49]:


# Sample text-3
import re

def find_words_at_least_4_characters(input_string):
    pattern = re.compile(r'\b\w{4,}\b')
    
    
    words = pattern.findall(input_string)
    
    return words


input_string = "This is a sample string with some words of different lengths."

result = find_words_at_least_4_characters(input_string)

print("Words at least 4 characters long:", result)


# In[50]:


# Sample text-4
import re

def find_words_of_lengths(input_string):
   
    pattern = re.compile(r'\b\w{3,5}\b')
    
    words = pattern.findall(input_string)
    
    return words

input_string = "This is a sample string with some words of various lengths."

result = find_words_of_lengths(input_string)

print("Words of lengths 3, 4, and 5 characters:", result)


# In[51]:


# Sample text-5
import re

def remove_parentheses(strings):
    # Define a regular expression pattern to match parentheses and their contents
    pattern = re.compile(r'\([^)]*\)')
    
    result = []
  
    for string in strings:
       
        cleaned_string = pattern.sub('', string)
        result.append(cleaned_string)
    
    return result

sample_text = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]

result = remove_parentheses(sample_text)

for cleaned_string in result:
    print(cleaned_string)


# In[52]:


# Sample text-6
import re


def remove_parentheses(text):
    pattern = re.compile(r'\([^)]*\)')
    cleaned_text = pattern.sub('', text)
    
    return cleaned_text

# Read text from the file
file_path = "sample_text.txt"

try:
    with open(file_path, "r") as file:
        original_text = file.read()
    modified_text = remove_parentheses(original_text)

    with open(file_path, "w") as file:
        file.write(modified_text)

    print("Parentheses removed and updated in the file.")

except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print("An error occurred:", str(e))


# In[11]:


# Sample text-7
import re

sample_text = "ImportanceOfRegularExpressionsInPython"
uppercase_letters = re.findall(r'[A-Z]', sample_text)

print(uppercase_letters)


# In[53]:


# Sample text-8


import re
def insert_spaces_before_numbers(text):
  
    pattern = re.compile(r'(?<=[a-zA-Z])(?=\d)')
    modified_text = pattern.sub(' ', text)
    
    return modified_text


sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"

result_text = insert_spaces_before_numbers(sample_text)
print(result_text)


# In[54]:


# Sample text-9
import re

def insert_spaces(text): 
    pattern = re.compile(r'(?<=[a-z])(?=[A-Z0-9])|(?<=[A-Z])(?=[A-Z][a-z0-9])|(?<=\d)(?=\D)|(?<=\D)(?=\d)')
    
    modified_text = pattern.sub(' ', text)
    
    return modified_text

sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"

result_text = insert_spaces(sample_text)

print(result_text)


# In[55]:


# Sample text-10
import re

def extract_emails_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            text = file.read()
            
            email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')
            
            emails = email_pattern.findall(text)
            
            return emails

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print("An error occurred:", str(e))


file_path = "sample_text.txt"


extracted_emails = extract_emails_from_file(file_path)
print("Extracted email addresses:")
for email in extracted_emails:
    print(email)


# In[56]:


# Sample text-11
import re

def is_valid_string(input_string):
  
    pattern = re.compile(r'^[a-zA-Z0-9_]+$')
    if pattern.match(input_string):
        return True
    else:
        return False

test_strings = ["Hello123", "Good_Morning", "123_456", "Not Valid!", "spaces not valid"]

for test_string in test_strings:
    if is_valid_string(test_string):
        print(f"'{test_string}' is a valid string.")
    else:
        print(f"'{test_string}' is not a valid string.")


# In[57]:


# Sample text-12
def starts_with_number(input_string, number):
    # Convert the number to a string for comparison
    number_str = str(number)
    
    if input_string.startswith(number_str):
        return True
    else:
        return False
test_strings = ["12345Hello", "4567World", "Hello123", "123abc", "abc123"]

specific_number = 123

for test_string in test_strings:
    if starts_with_number(test_string, specific_number):
        print(f"'{test_string}' starts with {specific_number}.")
    else:
        print(f"'{test_string}' does not start with {specific_number}.")


# In[58]:


# Sample text-13
def remove_leading_zeros(ip_address):
    # Split the IP address into octets
    octets = ip_address.split('.')
    cleaned_octets = []
    for octet in octets:
      
        cleaned_octets.append(str(int(octet)))
    cleaned_ip = '.'.join(cleaned_octets)
    
    return cleaned_ip

ip_addresses = ["192.001.002.003", "10.0.01.05", "001.002.003.004"]

for ip_address in ip_addresses:
    cleaned_ip = remove_leading_zeros(ip_address)
    print(f"Original IP: {ip_address}, Cleaned IP: {cleaned_ip}")


# In[59]:


# Sample text-14
import re

def find_dates_in_text(text):
   
    date_pattern = re.compile(r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:st|nd|rd|th)?\s+\d{4}')
    
    dates = date_pattern.findall(text)
    
    return dates

sample_text = "On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country."

found_dates = find_dates_in_text(sample_text)
print("Found date strings:")
for date in found_dates:
    print(date)


# In[60]:


# Sample text-15
def search_literals(text, literals):
    results = {}
    for literal in literals:
        index = text.find(literal)
        if index != -1:
            results[literal] = index
    return results

sample_text = 'The quick brown fox jumps over the lazy dog.'
search_strings = ['quick', 'fox', 'lazy', 'elephant']
found_strings = search_literals(sample_text, search_strings)
for literal, index in found_strings.items():
    print(f"'{literal}' found at index {index}")


# In[25]:


# Sample text-16

def search_literal(text, pattern):
    index = text.find(pattern)
    return index

# Sample textsample_text = 'The quick brown fox jumps over the lazy dog.'

# Literal string to search for
search_string = 'fox'
index = search_literal(sample_text, search_string)

if index != -1:
    print(f"'{search_string}' found at index {index} in the text.")
else:
    print(f"'{search_string}' not found in the text.")


# In[61]:


# Sample text-17


def find_substrings(text, substring):
    start = 0
    results = []
    
    while start < len(text):
        index = text.find(substring, start)
        if index == -1:
            break
        results.append((index, index + len(substring)))
        start = index + 1
    
    return results
sample_text = 'Python exercises, PHP exercises, C# exercises'
substring = 'exercises'
occurrences = find_substrings(sample_text, substring)

if occurrences:
    print(f"'{substring}' found at the following positions:")
    for start, end in occurrences:
        print(f"Start: {start}, End: {end}")
else:
    print(f"'{substring}' not found in the text.")


# In[62]:


# Sample text-18
def find_substring_occurrences(text, substring):
    start = 0
    occurrences = []
    
    while start < len(text):
        index = text.find(substring, start)
        if index == -1:
            break
        occurrences.append((index, index + len(substring)))
        start = index + 1
    
    return occurrences

def main():

    sample_text = 'Python exercises, PHP exercises, C# exercises'

    
    substring = 'exercises'
    occurrences = find_substring_occurrences(sample_text, substring)

    if occurrences:
        print(f"'{substring}' found at the following positions:")
        for i, (start, end) in enumerate(occurrences, 1):
            print(f"Occurrence {i}: Start: {start}, End: {end}")
    else:
        print(f"'{substring}' not found in the text.")

if __name__ == "__main__":
    main()


# In[63]:


# Sample text-19

from datetime import datetime

def convert_date(date_str):
   
    original_date = datetime.strptime(date_str, '%Y-%m-%d')
    new_date_format = original_date.strftime('%d-%m-%Y')
    
    return new_date_format
date_input = "2023-10-08"
new_date_format = convert_date(date_input)
print(f"Original Date: {date_input}")
print(f"New Date Format: {new_date_format}")


# In[64]:


# Sample text-20
import re

def find_decimal_numbers(text):
    pattern = re.compile(r'\b\d+\.\d{1,2}\b')
    decimal_numbers = pattern.findall(text)
    
    return decimal_numbers
sample_text = "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
found_decimal_numbers = find_decimal_numbers(sample_text)
print("Found decimal numbers:")
for number in found_decimal_numbers:
    print(number)


# In[65]:


# Sample text-21
def separate_and_print_numbers(text):
    numbers = []  # List to store numbers found
    positions = []  # List to store positions of numbers

    for i, char in enumerate(text):
        if char.isdigit():
            number_start = i
            while i < len(text) and (text[i].isdigit() or text[i] == '.'):
                i += 1
            number_end = i
            numbers.append(text[number_start:number_end])
            positions.append(number_start)

    for number, position in zip(numbers, positions):
        print(f"Number: {number}, Position: {position}")

# Sample text
sample_text = "The price of the product is $19.99, and the discount is 15%."
separate_and_print_numbers(sample_text)



# In[66]:


# Sample text-22

import re

def extract_largest_numeric_value(text):
    # Define a regular expression pattern to match numeric values
    numeric_pattern = re.compile(r'-?\d+(\.\d+)?')
    
    numeric_values = numeric_pattern.findall(text)
    
    if numeric_values:
        numeric_values = [float(value) for value in numeric_values]
        largest_value = max(numeric_values)
        return largest_value
    else:
        return None

# Sample text
sample_text = "The prices are $19.99, $25.50, and $15.75."
largest_numeric_value = extract_largest_numeric_value(sample_text)

if largest_numeric_value is not None:
    print(f"The largest numeric value is: {largest_numeric_value}")
else:
    print("No numeric values found in the text.")


# In[68]:


# Sample text-23

import re

def extract_largest_numeric_value(text):
    # Define a regular expression pattern to match numeric values
    numeric_pattern = re.compile(r'\b\d+\b')
    numeric_values = numeric_pattern.findall(text)
    
    if numeric_values:
         numeric_values = [int(value) for value in numeric_values]
        largest_value = max(numeric_values)
        return largest_value
    else:
        return None

# Sample text
sample_text = 'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'

largest_numeric_value = extract_largest_numeric_value(sample_text)

if largest_numeric_value is not None:
    print(f"The largest numeric value is: {largest_numeric_value}")
else:
    print("No numeric values found in the text.")


# In[69]:


# Sample text-23
import re

def insert_spaces_between_capital_words(text):
   
    modified_text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    modified_text = modified_text.capitalize()
    
    return modified_text

sample_text = "RegularExpressionIsAnImportantTopicInPython"
result = insert_spaces_between_capital_words(sample_text)
print("Modified Text:")
print(result)


# In[70]:


# Sample text-24

import re

text = "This is an Example with Some UPPERCase words and Another Example."

pattern = r'[A-Z][a-z]+'
matches = re.findall(pattern, text)

# Print the matches
print(matches)


# In[71]:


# Sample text-25


import re

def remove_continuous_duplicates(text):
    # Use regular expression to find continuous duplicate words
    pattern = r'\b(\w+)(\s+\1)+\b'
    modified_text = re.sub(pattern, r'\1', text, flags=re.IGNORECASE)
    
    return modified_text

sample_text = "Hello hello world world"
result = remove_continuous_duplicates(sample_text)
print("Modified Text:")
print(result)


# In[72]:


# Sample text-26


import re

def is_valid_string(input_string):
    pattern = r'^.*[a-zA-Z0-9]$'
    
    if re.search(pattern, input_string):
        return True
    else:
        return False
input_string = input("Enter a string: ")

if is_valid_string(input_string):
    print("The string ends with an alphanumeric character.")
else:
    print("The string does not end with an alphanumeric character.")


# In[ ]:


# Sample text-27

import re

def extract_hashtags(text):
    # Define a regular expression pattern to match hashtags
    pattern = r'#\w+'
    
    # Use the findall method to find all matching hashtags in the text
    hashtags = re.findall(pattern, text)
    
    return hashtags
sample_text = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""

found_hashtags = extract_hashtags(sample_text)
print("Extracted Hashtags:")
for hashtag in found_hashtags:
    print(hashtag)



# In[42]:


# Sample text-28

import re

def remove_u_plus_symbols(text):
    # Define a regular expression pattern to match <U+..> like symbols
    pattern = r'<U\+[0-9A-Fa-f]+>'
    
    # Use the sub method to replace the matched symbols with an empty string
    modified_text = re.sub(pattern, '', text)
    
    return modified_text

# Sample text
sample_text = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"

# Remove <U+..> like symbols from the text
result = remove_u_plus_symbols(sample_text)

# Print the modified text
print("Modified Text:")
print(result)


# In[2]:


# Sample text-29

import re

def extract_dates_from_text(text):
    # Define a regular expression pattern to match dates in the format DD-MM-YYYY
    pattern = r'\d{2}-\d{2}-\d{4}'
    dates = re.findall(pattern, text)
    
    return dates
with open('sample_text.txt', 'r') as file:
    text = file.read()
found_dates = extract_dates_from_text(text)
print("Extracted Dates:")
for date in found_dates:
    print(date)


# In[1]:


# Sample text-30


import re

def remove_words_with_length_between_2_and_4(text):
    # Define a regular expression pattern to match words with length between 2 and 4
    pattern = re.compile(r'\b\w{2,4}\b')
    
    # Use the sub method to replace the matched words with an empty string
    modified_text = pattern.sub('', text)
    
    return modified_text

# Sample text
sample_text = "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

# Remove words with length between 2 and 4 from the text
result = remove_words_with_length_between_2_and_4(sample_text)

# Print the modified text
print("Modified Text:")
print(result)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





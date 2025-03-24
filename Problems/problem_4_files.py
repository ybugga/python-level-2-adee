"""
A program that takes a letter and outputs a text file of
all of the countries that start with that letter
"""

# Todo: Read data/countries.txt and save all countries
countriesDict = {}
with open("Problems/data/countries.txt", "r") as file:
    countriesList = file.read().strip().split("\n")
    print(countriesList)
    for country in countriesList:
        firstletter = country[0]
        if firstletter in countriesDict.keys():
            countriesDict[firstletter].append(country)
        else:
            countriesDict[firstletter] = [country]
# Get user to provide a letter
try:
    letter = str(input('Number of countries that start with letter: ').upper())
except Exception as e:
    print(f"Invalid letter: {repr(e)}")
    exit()
# Todo: Print the number of countries that start with the letter
countries = countriesDict.get(letter,[])
print(len(countries))
# Todo: Create text file that lists the countries starting with the letter
with open("Problems/data/countriesOut.txt", "w") as file:
    file.writelines("\n".join(countries))
def get_dict(team_list):
    dictionary = {}
    year = 1903
    
    for item in team_list:
        teams = item.strip()
        if teams not in dictionary:
             dictionary[teams] = []
        
        dictionary[teams].append(year)
        year += 1
            
    return dictionary
        

def display(dictionary):
    for key, value in dictionary.items():
        print(f'{key}:')
        print(value)

def specific_team(dictionary):
    key = input('Enter a teams name: ')
    if key in dictionary:
        print(dictionary[key])
        
       
def main():
    file = open('WorldSeriesWinners.txt', 'r')
    lines = file.readlines()
    
    team_list = [name for name in lines]
    dictionary = get_dict(team_list)
    
    check = False
    
    while check == False:
        print('1. View a teams info')
        print('2. View all teams info')
        print('3. Delete a teams info')
        print('4. Change a teams info')
        print('5. Quit')

        stop = int(input('Please choose an option: '))

        if stop == 1:
            specific_team(dictionary)
        elif stop == 2:
            display(dictionary)
        elif stop == 3:
            remove = input('Enter a team to delete: ')
            print(f'The {remove} was deleted')
        elif stop == 4:
            team = input('enter a teams name: ')
            new_years = int(input('Enter this teams new winning years: '))
            print(f'{team} changed')
        else:
            check = True
            print('Goodbye!')
                             

if __name__=='__main__':
    main()


'''1. View a teams info
2. View all teams info
3. Delete a teams info
4. Change a teams info
5. Quit
Please choose an option: 1
Enter a teams name: New York Yankees
[1923, 1927, 1928, 1932, 1936, 1937, 1938, 1939, 1941, 1943, 1947, 1949, 1950, 1951, 1952, 1953, 1956, 1958, 1961, 1962, 1977, 1978, 1996, 1998, 1999, 2000]
1. View a teams info
2. View all teams info
3. Delete a teams info
4. Change a teams info
5. Quit
Please choose an option: 3
Enter a team to delete: Atlanta Braves
The Atlanta Braves was deleted
1. View a teams info
2. View all teams info
3. Delete a teams info
4. Change a teams info
5. Quit
Please choose an option: 4
enter a teams name: Toranto Blue Jays
Enter this teams new winning years: 2003
Toranto Blue Jays changed
1. View a teams info
2. View all teams info
3. Delete a teams info
4. Change a teams info
5. Quit
Please choose an option: 2
Boston Americans:
[1903]
none:
[1904, 1994]
New York Giants:
[1905, 1921, 1922, 1933, 1954]
Chicago White Sox:
[1906, 1917, 2005]
Chicago Cubs:
[1907, 1908]
Pittsburgh Pirates:
[1909, 1925, 1960, 1971, 1979]
Philadelphia Athletics:
[1910, 1911, 1913, 1929, 1930]
Boston Red Sox:
[1912, 1915, 1916, 1918, 2004, 2007]
Boston Braves:
[1914]
Cincinnati Reds:
[1919, 1940, 1975, 1976, 1990]
Cleveland Indians:
[1920, 1948]
New York Yankees:
[1923, 1927, 1928, 1932, 1936, 1937, 1938, 1939, 1941, 1943, 1947, 1949, 1950, 1951, 1952, 1953, 1956, 1958, 1961, 1962, 1977, 1978, 1996, 1998, 1999, 2000]
Washington Senators:
[1924]
St. Louis Cardinals:
[1926, 1931, 1934, 1942, 1944, 1946, 1964, 1967, 1982, 2006]
Detroit Tigers:
[1935, 1945, 1968, 1984]
Brooklyn Dodgers:
[1955]
Milwaukee Braves:
[1957]
Los Angeles Dodgers:
[1959, 1963, 1965, 1981, 1988]
Baltimore Orioles:
[1966, 1970, 1983]
New York Mets:
[1969, 1986]
Oakland Athletics:
[1972, 1973, 1974, 1989]
Philadelphia Phillies:
[1980, 2008]
Kansas City Royals:
[1985]
Minnesota Twins:
[1987, 1991]
Toronto Blue Jays:
[1992, 1993]
Atlanta Braves:
[1995]
Florida Marlins:
[1997, 2003]
Arizona Diamondbacks:
[2001]
Anaheim Angels:
[2002]
1. View a teams info
2. View all teams info
3. Delete a teams info
4. Change a teams info
5. Quit
Please choose an option: 5
Goodbye!'''

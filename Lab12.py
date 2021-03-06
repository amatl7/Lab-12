# By submitting this assignment, I agree to the following:
#  Aggies do not lie, cheat, or steal, or tolerate those who do
#  I have not given or received any unauthorized aid on this assignment
#
# Name:         Anthony Matl Landon Matak
# Section:      273
# Assignment:   THE ASSIGNMENT NUMBER Lab 2B Program 1
# Date:         1 September 2020
dashes = '-' * 30
import csv
import pathlib
from numpy import random
#Testing github
#Hello
pokedex = open('PokeList_v2.csv','r')
def main_menu(filename):
    '''This function displayes a main menu and runs the selected menu option'''
    print('{} MAIN MENU {}\n\n1. View Pokemon\n2. Battle Pokemon\n3. View Items\n4. Catch New Pokemon\n'.format(dashes, dashes))
    selection = int(input())
    if selection == 1:
        view_pokemon(filename)
    elif selection == 2:
        battle_pokemon(filename)
    elif selection == 3:
        view_items(filename)
    elif selection == 4:
        catch_pokemon(filename)
def view_pokemon(filename):
    '''Displays a list of pokemon'''
    pokemons = open(filename, 'r')
    for i in pokemons:
        print(pokemons)
def battle_pokemon(filename):
    '''Allows another player to be selected then initiates battle'''
def view_items(filename):
    '''Displays the items in inventory'''
def catch_pokemon(filename):
    '''Runs a minigame where user may catch the random pokemon'''
def player_select():
    '''This function displays a list of players and allows the user to select the player then runs main menu'''
    print('{} PLAYER SELECT {}\n\n1. New Player\n2. Returning Player'.format(dashes, dashes))
    selection = int(input())
    if selection == 1:
        create_new_player()
    elif selection == 2:
        select_player()
def select_player():
    '''This function displays a list from the player file and allows user to select a player, returns that player then goes to main menu'''
    print('Select your player')
    counter = 1
    with open('playerdatabase.txt', 'r') as playerdatabase:
        for line in playerdatabase:
            print('{}. {}'.format(counter, line), end='')
            counter += 1
        counter = 1
        selected_player = int(input())
    with open('playerdatabase.txt', 'r') as playerdatabase:
        for line in playerdatabase:
            if selected_player == counter:
                filename = line[0:6]
            counter += 1
    print(filename)
    main_menu(filename)
def create_new_player():
    '''This function creates a new player and adds it to file then creates a new player file then goes to main menu'''
    username = input('Enter your player username: ')
    filename = username + '.csv'
    starter = random.randint(1,151)
    pokeman = csv.reader(pokedex, delimiter=',')
    playerbase = pathlib.Path('playerdatabase.txt')
    if playerbase.exists():
        with open('playerdatabase.txt', 'a') as  playerdatabase:
            playerdatabase.write(username + '\n')
    else:
        with open('playerdatabase.txt', 'w') as playerdatabase:
            playerdatabase.write(username + '\n')
    for i in pokeman:
        if i[0] == str(starter):
            print('\n\nCongratulation {}!!!\nYou have received your first pokemon!!!\nAnd that pokemon is.....\nA {}!!!!!!'.format(username, i[1]))
            with open(filename, 'w') as playerfile:
                playerfile.write(username + '\n')
                playerfile.write(i[0] + ',' + i[1] + ',' + '1' + ',' + i[2] + ',' + i[3])
    main_menu(filename)


player_select()
pokedex.close()
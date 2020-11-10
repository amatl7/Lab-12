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
from numpy import random

pokedex = open('PokeList_v2.csv','r')
def main_menu():
    '''This function displayes a main menu and runs the selected menu option'''
    print('{} MAIN MENU {}\n\n1. View Pokemon\n2. Battle Pokemon\n3. View Items\n4. Catch New Pokemon\n'.format(dashes, dashes))
    selection = int(input())
    if selection == 1:
        view_pokemon()
    elif selection == 2:
        battle_pokemon()
    elif selection == 3:
        view_items()
    elif selection == 4:
        catch_pokemon()
def view_pokemon():
    '''Displays a list of pokemon'''
def battle_pokemon():
    '''Allows another player to be selected then initiates battle'''
def view_items():
    '''Displays the items in inventory'''
def catch_pokemon():
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
    main_menu()
def create_new_player():
    '''This function creates a new player and adds it to file then creates a new player file then goes to main menu'''
    username = input('Enter your player username: ')
    filename = username + '.csv'
    starter = random.randint(1,151)
    pokeman = csv.reader(pokedex, delimiter=',')
    for i in pokeman:
        if i[0] == str(starter):
            print('Congratulation {}!!!\nYou have received your first pokemon!!!\nAnd that pokemon is.....\nA {}!!!!!!'.format(username, i[1]))
            with open(filename, 'w') as playerfile:
                playerfile.write(username + '\n')
                playerfile.write(i[0] + ',' + i[1] + ',' + i[2] + ',' + i[3])
            with open('playerdatabase', 'w') as playerdatabase:
                playerdatabase.write(username + '\n')
                playerdatabase.write(username + '\n')
    main_menu()


player_select()
pokedex.close()
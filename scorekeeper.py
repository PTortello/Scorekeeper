"""
Baseball Scorekeeper
Copyright (C) 2020 - Pedro Tortello
ptortello@hotmail.com
"""


# TODO: Create main functions. <PTO 2020-08-12 p:3>
#def team_loader
#def player_loader
#def main_menu
#def team_menu
#def score_keep


class Player:
    def __init__(self, jersey, name, position):
        self.jersey = jersey
        self.name = name
        self.position = position
        #stats = [0,0,0,0,0]

player1 = Player('10', 'Pedro Tortello', 'CF')
print(player1.jersey + ' ' + player1.name + '\t' + player1.position)


position = {'DH':0, 'P':1, 'C':2, '1B':3, '2B':4,
            '3B':5, 'SS':6, 'LF':7, 'CF':8, 'RF':9}

#filename = path.join(filedir, 'teams/' + team + '.txt')
#with open(filename, 'w') as f:
    #f.write(team.title() + '\n')

teams = ('angels', 'astros', 'athletics', 'bluejays', 'braves', 'brewers',
            'cardinals', 'cubs', 'dbacks', 'dodgers', 'giants', 'indians',
            'mariners', 'marlins', 'mets', 'nationals', 'orioles', 'padres',
            'phillies', 'pirates', 'rangers', 'rays', 'reds', 'redsox',
            'rockies', 'royals', 'tigers', 'twins', 'whitesox', 'yankees')

counter = 0
for team in teams:
    tab = '\t' if len(team) > 7 else '\t\t'
    print(team + tab, end='')
    counter += 1
    if counter == 6:
        print()
        counter = 0

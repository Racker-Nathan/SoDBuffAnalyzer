classlist = ['warrior', 'paladin', 'rogue', 'hunter', 'priest', 'shaman', 'druid', 'mage', 'warlock']

#Create some kind of interface that a user can input their information that's user friendly.  Maybe a csv file as a starting point?  Could have the UI then push a .csv file for the script to pull from
#Access data to find out what buffs and debuffs each class brings
#Bring in data from the user on what classes and specs are being brought, trying to include runes - Maybe just keep it simple and keep it as to "What's possible?"
#Create a table that displays what class/specs your raid comp is, what buffs/debuffs are covered and which aren't.  Also spit out a table showing what each class is capable of bringing


def import_data(compfile):
    
    return

def __main__():
    compfile = input("Where is the .csv file to pull data from?  Leave blank to use ./ClassComp.csv ")
    if compfile == '':
        import_data(compfile = './ClassComp.csv')
    else:
        import_data(compfile)
    return

__main__()    
import gspread

gc = gspread.service_account(filename='GameData/sokoban-338317-ea8c79b29c7f.json')\

sh = gc.open('Sokoban')
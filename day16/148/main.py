from prettytable import PrettyTable

table = PrettyTable()



table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])

print(table.align)

table.align["base_align_value"]="l"
table.align["Pokemon Name"]="l"
table.align["Type"]="l"

print(table)

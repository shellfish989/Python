def how_eligible(essay):
    number = 0
    if '?' in essay:
        number = number + 1
    if '"' in essay:
        number = number + 1
    if ',' in essay:
        number = number + 1
    if '!' in essay:
        number = number + 1
    print number
        
    
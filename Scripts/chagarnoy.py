import re

def chagarnoy(text: str):
    w = text.split(' ')

    invalid_characters = re.compile(r'[\/:*?"<>|\n.]')
    
    for i in range(len(w)):
        if invalid_characters.search(w[i]):
            with open(f'output/{i}.txt', 'w', encoding='utf-8') as file:
                file.write(w[i])
        else:
            with open(f'output/{i}_{w[i]}.txt', 'w', encoding='utf-8'):
                pass
    
    return True
    
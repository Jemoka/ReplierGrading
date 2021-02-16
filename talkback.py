import os
import csv
import getch
import cursor
import random
from prettytable import PrettyTable

REVIEWER = "Houjun Liu"
RESULT = "./final_result.csv"

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[38;5;214m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   ORANGE= '\033[38;5;202m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

data = []
with open("./replier_talking_data.csv", "r") as df:
    reader = csv.reader(df)
    for row in reader:
        data.append([row[-1], row[0], row[1]])
       

with open("./human_talkback_data.csv", "r") as df:
    reader = csv.reader(df)
    for indx, row in enumerate(reader):
        data[indx].append(row[1])

def rubric(data, index, evaluate=2, isPsych=False):
    x = PrettyTable()
    x.field_names = [f'{color.BLUE}{REVIEWER}/{color.BLUE}{index}{color.END}{color.BLUE} {color.BOLD}1{color.END}', f'{color.PURPLE}{data[0]}{color.END}', f'{color.UNDERLINE}{color.CYAN}Clarity categorization{color.END}']
    x.add_row(['Q/A', f'{data[1]}', f'{data[evaluate]}'])
    print(x)
    print()
    print("Please indicate the clarity of the response.")
    print()
    print(f'{color.RED}{color.BOLD}1{color.END}{color.RED}: Incoherent {color.END}')
    print(f'{color.ORANGE}{color.BOLD}2{color.END}{color.ORANGE}: Coherent and illogical {color.END}')
    print(f'{color.YELLOW}{color.BOLD}3{color.END}{color.YELLOW}: Logical {color.END}')
    print(f'{color.GREEN}{color.BOLD}4{color.END}{color.GREEN}: Logical and clearly voiced {color.END}')
    botClarity = getch.getch()
    os.system('clear')


    x = PrettyTable()
    x.field_names = [f'{color.BLUE}{REVIEWER}/{color.BLUE}{index}{color.END}{color.BLUE} {color.BOLD}1{color.END}', f'{color.PURPLE}{data[0]}{color.END}', f'{color.UNDERLINE}{color.CYAN}Specificty categorization{color.END}']
    x.add_row(['Q/A', f'{data[1]}', f'{data[evaluate]}'])
    print(x)
    print()
    print("Please indicate the specificity of the response.")
    print()
    print(f'{color.RED}{color.BOLD}1{color.END}{color.RED}: Irrelevant {color.END}')
    print(f'{color.ORANGE}{color.BOLD}2{color.END}{color.ORANGE}: Addressses question {color.END}')
    print(f'{color.YELLOW}{color.BOLD}3{color.END}{color.YELLOW}: Engages question {color.END}')
    print(f'{color.GREEN}{color.BOLD}4{color.END}{color.GREEN}: Opionates upon question {color.END}')
    botSpecificity = getch.getch()
    os.system('clear')


    if isPsych:
        x = PrettyTable()
        x.field_names = [f'{color.BLUE}{REVIEWER}/{color.BLUE}{index}{color.END}{color.BLUE} {color.BOLD}1{color.END}', f'{color.PURPLE}{data[0]}{color.END}', f'{color.UNDERLINE}{color.CYAN}Psycological helpfulness categorization{color.END}']
        x.add_row(['Q/A', f'{data[1]}', f'{data[evaluate]}'])
        print(x)
        print()
        print("Please indicate the psycological helpfulness of the response.")
        print()
        print(f'{color.RED}{color.BOLD}1{color.END}{color.RED}: Negatively influences the issue {color.END}')
        print(f'{color.ORANGE}{color.BOLD}2{color.END}{color.ORANGE}: Non-psych/does not address the issue {color.END}')
        print(f'{color.YELLOW}{color.BOLD}3{color.END}{color.YELLOW}: Addresses the psycological issue {color.END}')
        print(f'{color.GREEN}{color.BOLD}4{color.END}{color.GREEN}: Positively influences the issue {color.END}')
        botPsych = getch.getch()
        os.system('clear')

    else:
        botPsych = 2


    return {'clarity': int(botClarity), 'specificity': int(botSpecificity), 'psycology': int(botPsych)}

def turing(data, index, evaluate=2):
    x = PrettyTable()
    x.field_names = [f'{color.BLUE}{REVIEWER}/{color.BLUE}{index}{color.END}{color.BLUE} {color.BOLD}2{color.END}', f'{color.PURPLE}{data[0]}{color.END}', f'{color.UNDERLINE}{color.CYAN}Turing test{color.END}']
    x.add_row(['Q/A', f'{data[1]}', f'{data[evaluate]}'])
    print(x)
    print()
    print("Was this response generated?")
    print()
    print(f'{color.RED}{color.BOLD}1{color.END}{color.RED}: Bot {color.END}')
    print(f'{color.YELLOW}{color.BOLD}2{color.END}{color.YELLOW}: Unsure {color.END}')
    print(f'{color.GREEN}{color.BOLD}3{color.END}{color.GREEN}: Human {color.END}')
    result = getch.getch()
    os.system('clear')
    return int(result)


def review(db, index):
    data = db[index]
    os.system('clear')


    x = PrettyTable()
    x.field_names = [f'{color.BLUE}{REVIEWER}/{color.BLUE}{index}{color.END}{color.BLUE} {color.BOLD}0{color.END}', f'{color.PURPLE}{data[0]}{color.END}', f'{color.UNDERLINE}{color.CYAN}Question type categorization{color.END}']
    x.add_row(['', f'Question: ', f'{data[1]}'])
    print(x)
    print()
    print("Please indicate if this question pretains to psycology")
    print()
    print(f'{color.RED}{color.BOLD}1{color.END}{color.RED}: Non Psycology{color.END} | {color.GREEN}{color.BOLD}2{color.END}{color.GREEN}: Psycology{color.END}')
    isPsycology = getch.getch()
    os.system('clear')
    
    if random.uniform(0,1) < 0.5:
        botRubric = rubric(data, index, 2, isPsycology=='2')
        humanRubric = rubric(data, index, 3, isPsycology=='2')
    else:
        humanRubric = rubric(data, index, 3, isPsycology=='2')
        botRubric = rubric(data, index, 2, isPsycology=='2')

    if random.uniform(0,1) < 0.5:
        botTuring = turing(data, index, 2)
        humanTuring = turing(data, index, 3)
    else:
        humanTuring = turing(data, index, 3)
        botTuring = turing(data, index, 2)

    os.system('clear')
    return {"isPsych": isPsycology=='2', "botRubric": botRubric, "humanRubric": humanRubric, "botTuring": botTuring, "humanTuring": humanTuring, 'model': data[0]}

# print(color.CYAN + data[0][0] + color.END, "is cool.")
# print(getch.getch())

total = len(data)
def do(index, writer):
    cursor.hide()
    result = review(data, index)
    print(f"Done with {index}/{total}. That's {((index/total)*100):.2f}%")
    print(f"{color.BOLD}Do over? ({color.RED}Y(0){color.END}/{color.BOLD}{color.GREEN}N(1){color.END}{color.BOLD}){color.END} or quit (Q)")
    do = getch.getch()
    if do == 'Q':
        cursor.show()
        return [index, True]
    while do == 'Y' or do == '0':
        result = review(data, index)
        print(f"Done with {index}/{total}. That's {((index/total)*100):.2f}%")
        print(f"{color.BOLD}Do over? ({color.RED}Y(0){color.END}/{color.BOLD}{color.GREEN}N(1){color.END}{color.BOLD}){color.END} or quit (Q)")
        do = getch.getch()
    writer.writerow([index, REVIEWER, result["model"], result["isPsych"], result["botRubric"]["clarity"], result["botRubric"]["specificity"], result["botRubric"]["psycology"], result["humanRubric"]["clarity"], result["humanRubric"]["specificity"], result["humanRubric"]["psycology"], result["botTuring"], result["humanTuring"]])
    cursor.show()
    return [index, False]


def execute():
    startIndex = int(input(f'''Are you ready to grade some sentences, {REVIEWER}?
No? Too bad. Except for this question, all other questions are single char responses
that DOES NOT REQUIRE PRESSING ENTER. This will be the last time pressing return is needed.

Note: These dataset are not 50/50 bot/human. 
One of the question is a traditional Turing test, where you are tasked with judging if 
the response is bot/human.  If one of your response is "human", the other is not necesarily bot.

{color.RED}{color.BOLD}DO NOT Ctrl-C THE SCRIPT. You will have an opportunity to quit after each question.{color.END}
The file does not save without intentionally ending.

Where do you want to start from? 0 for the start of data. ''').strip())-1

    index = startIndex
    isEnded = False
    while isEnded == False:
        index+=1
        df = open(RESULT, "a")
        writer = csv.writer(df)
        index, isEnded = do(index, writer)
        df.close()

    if isEnded:
        print(f'Ended. Next time start from {index}')
    else:
        print("Ok. That's it. Thank you.")


execute()

# df = open("./test", "a")
# do(12, csv.writer(df))
# df.close()

## Question score just for me
# Non psycology | psycology

## Response scores a la 2002.01862

# Clarity         - Unclear or incoherent response   | Coherent illogical response          | Logical response    | Logical and clearly directed response
# Specificty      - Irrelevant to the question itself| Addressses the question              | Engages the question| Engages and opionates upon the quesitons
# P. Helpfulness  - Negatively Influences the Issue  | Non-psych/Does not address the Issue | Addresses the Issue | Positively Influences the Issue

## Spot the Bot Touring a la 2010.02140
# Response A      - Bot | Unsure | Human
# Response B      - Bot | Unsure | Human



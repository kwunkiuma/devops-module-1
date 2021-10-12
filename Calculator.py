import string

def getInputs():
    inputs = [''] * 3

    inputs[0] = input("Enter overator: ")
    inputs[1] = int(input("Enter operand 1: "))
    inputs[2] = int(input("Enter operand 2: "))
    return inputs

def calc(inputs):
    answer = 0
    match inputs[0]:
        case "+":
            answer = int(inputs[1]) + int(inputs[2])
        case "-":
            answer = int(inputs[1]) - int(inputs[2])
        case "/":
            answer = int(inputs[1]) // int(inputs[2])
        case "x":
            answer = int(inputs[1]) * int(inputs[2])
    return answer

def step2():
    total = 0
    with open("step_2.txt", mode='r') as f:
        for text_string in f:
            if text_string == '':
                break
            inputs = text_string.split()
            print(inputs)
            total += calc(inputs[1:])

    print(total)

def step3():
    with open("step_3.txt", mode='r') as f:
        seen = []
        lines = f.readlines()
        index = 0
        while True:
            line = lines[index]
            seen.append(index)
            words = line.split()
            newIndex = 0
            if words[1] == "calc":
                newIndex = calc(words[2:]) - 1
            else:
                newIndex = int(words[1]) - 1
            if newIndex in seen:
                print(index + 1)
                print(line)
                break
            index = newIndex

def remove(lines, line):
    del lines[line]

def replace(lines, replaced, replacer):
    if replaced >= len(lines):
        return
    if replacer >= len(lines):
        return
    lines[replaced] = lines[replacer]

def step4():
    with open("step_4.txt", mode='r') as f:
        lines = f.readlines()
        seen = [False] * len(lines)
        lines.insert(0, "")
        seen.insert(0, "")
        index = 1
        while True:
            line = lines[index]
            seen[index] = True
            words = line.split()
            print(words)
            match words[0]:
                case "remove":
                    del lines[index]
                    del seen[index]
                case "replace":
                    replace(lines, int(words[1]), int(words[2]))
                    replace(seen, int(words[1]), int(words[2]))
                    index += 1
                case "goto":
                    newIndex = 0
                    if words[1] == "calc":
                        newIndex = calc(words[2:])
                    else:
                        newIndex = int(words[1])
                    if seen[newIndex] or newIndex >= len(lines):
                        print(index)
                        print(line)
                        break
                    index = newIndex

step4()
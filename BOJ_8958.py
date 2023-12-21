cnt = int(input())

for i in range(cnt):
    ox_list = input()
    combostate = 0
    score = 0
    for i in range(len(ox_list)):
        if ox_list[i] == 'O':
            if combostate == 0:
                score += 1
                combostate += 1
            else :
                score += combostate + 1
                combostate += 1
        elif ox_list[i] == 'X':
            combostate = 0
    print(score)
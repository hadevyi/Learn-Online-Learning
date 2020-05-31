while True:
    line = input('> ')
    if line[0] == '#' :
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')

# > hello there 입력
# hello there로 출력
# # don't print this '#'을 입력하게 되면 continue를 만나게 되고 continue는 loop의 시작점으로 다시 돌아가서 loop를 실행하게 됩니다.
# > print this! 입력
# print this!로 출력
# > done 입력
# Done!으로 출력 done을 입력하게 되면 break를 만나게 되고 break는 loop끝나는 점 바로 다음에 오는 코드를 실행하게 됩니다.

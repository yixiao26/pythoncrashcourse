while True:
    reason = input("Why do your like programming? (or 'q' to quit): ")
    if reason.lower() == 'q':
        break
    with open('programming_poll.txt', 'a') as file_object:
        file_object.write(reason + '\n')
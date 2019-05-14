from timeutils import Stopwatch





while True:
    sw = Stopwatch(start=True)
    key = readchar.readkey()
    if key == 'w' or key == 'W':
        print('Command forward ')
        print(str(sw.stop()))
        # forward()
    elif key == 'a' or key == 'A':
        print('Command left ')
        print(str(sw.stop()))
        # left()
    elif key == 's' or key == 'S':
        print('Command backward ')
        print(str(sw.stop()))
        # backward()
    elif key == 'd' or key == 'DS':
        print('Command right ')
        print(str(sw.stop()))
        # right()
    elif key == 'u':
        print('Finish')
        break
        # right()
with open('registrations.txt', 'r',encoding='utf8') as f:
    line = True
    while line:
        line = f.readline()
        n = line
        s = n.split()
        v = 0
        z = 0
        if len(s)==3:
            if s[0].isalpha():
                z += 1
            else:
                with open('registrations_bad.log.txt',
                          'a') as f1:
                    file_content = n
                    f1.write(file_content)

            if '.' in s[1]:
                z += 0.5
            else:
                with open('registrations_bad.log.txt',
                          'a') as f1:
                    file_content = n
                    f1.write(file_content)
            if '@' in s[1]:
                z += 0.5
            else:
                with open('registrations_bad.log.txt',
                          'a') as f1:
                    file_content = n
                    f1.write(file_content)
            if s[2].isdigit():
                v = int(s[2])
                if 10 <= v <= 99:
                    z += 1
                if v >= 100:
                    with open('registrations_bad.log.txt',
                              'a') as f1:
                        file_content = n
                        f1.write(file_content)
            if z == 3:
                with open('registrations_good.log.txt.log.txt',
                          'a') as f2:
                    file_content = n
                    f2.write(file_content)
        else:
            with open('registrations_bad.log.txt','a') as f1:
                file_content = n
                f1.write(file_content)

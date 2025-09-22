import sys
input = sys.stdin.readline

while True:
    try:
        dance = list(map(str, input().split()))
        if not dance:  
            break

        p1 = p2 = p3 = p4 = p5 = False

        copy = dance.copy()

        dip = [i for i, value in enumerate(dance) if value == 'dip']
        for i in dip:
            valid = False
            if i-1 >= 0 and dance[i-1] == 'jiggle':
                valid = True

            if i-2 >= 0 and dance[i-2] == 'jiggle':
                valid = True

            if i+1 < len(dance) and dance[i+1] == 'twirl':
                valid = True

            if not valid:
                copy[i] = copy[i].upper()
                p1 = True

        if ''.join(dance[-3:]) != "clapstompclap":
            p2 = True

        if ('twirl' in dance) and ('hop' not in dance):
            p3 = True

        if dance[0] == 'jiggle':
            p4 = True

        if dance.count('dip') == 0: 
            p5 = True

        errors = []
        if p1: errors.append(1)
        if p2: errors.append(2)
        if p3: errors.append(3)
        if p4: errors.append(4)
        if p5: errors.append(5)

        if not errors:
            msg = "form ok: "
        elif len(errors) == 1:
            msg = f"form error {errors[0]}: "
        else:
            msg = "form errors "
            msg += ", ".join(map(str, errors[:-1]))
            msg += f" and {errors[-1]}: "

        print(msg + " ".join(copy))

    except:
        break

#!/usb/bin/python3

class Calendar(object):
    """ Hónapok és napok kiírása """
    def __init__(self):
        t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
        t2 = ["Január", "Február", "Március", "Április", "Május", "Június", "Július", "Augusztus", "Szeptember", "Október", "November", "December"];
        t3 = [];
        a = 0;
        while a < 12:
            t3.append("{0}:".format(t2[a]));
            t3.append(t1[a]);
            a = a + 1;

        i = 0;
        szoveg = "";
        while i < 12:
            szoveg = szoveg + " {0}".format(t2[i]);
            i = i + 1;

        print(szoveg);

Calendar();

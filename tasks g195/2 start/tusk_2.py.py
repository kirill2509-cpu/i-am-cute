
def get_resistor_value(t):
        cifri = {
            'bk': 0, 'br': 1, 'rd': 2, 'or': 3, 'yl': 4,
            'gr': 5, 'bl': 6, 'vi': 7, 'gy': 8, 'wh': 9
        }
        mnozh = {
            'bk': 1, 'br': 10, 'rd': 100, 'or': 1000, 'yl': 10000,
            'gr': 100000, 'bl': 1000000, 'vi': 10000000, 'gy': 100000000,
            'wh': 1000000000
        }
        otklon = {
            'bk': None, 'br': 1, 'rd': 2, 'or': None,
            'yl': 5, 'gr': 0.5, 'bl': 0.25, 'vi': 0.1,
            'gy': 0.05, 'wh': None, 'au': 5, 'ag': 10
        }
        if len(t) < 4:
                print(f'Predostavleno menee 4 tsvetov: {t}');
                return None, None;
        if any(t1 not in cifri and t1 not in mnozh and t1 not in otklon for t1 in t):
            print(f'nedopustimyy tsvet polosy v markirovke: {t}');
            return None, None;
        first = cifri[t[0]]
        second = cifri[t[1]]
        mnozh = mnozh[t[2]]
        otklon = otklon[t[3]]
        resistance_value = (first * 10 + second) * mnozh
        return resistance_value, otklon
print(get_resistor_value(['br', 'bk', 'yl', 'ag']))
print(get_resistor_value(['yl', 'vi', 'rd', 'au']))
print(get_resistor_value(['vi', 'yl', 'rd', 'gr']))
print(get_resistor_value(['ws', 'yl', 'rd', 'rd']))
print(get_resistor_value(['vi', 'yl', 'rd']))

iban = {
    "AL": 28, "AD": 24, "AT": 20, "BE": 16, "BA": 20, "BR": 29, "BG": 22, "HR": 21,
    "CY": 28, "CZ": 24, "DK": 18, "EE": 20, "FO": 18, "FI": 18, "FR": 27, "GE": 22,
    "DE": 22, "GI": 23, "GR": 27, "GL": 18, "HU": 28, "IS": 26, "IE": 22, "IL": 23,
    "IT": 27, "JO": 30, "KW": 30, "LV": 21, "LB": 28, "LI": 21, "LT": 20, "LU": 20,
    "MK": 19, "MT": 31, "MU": 30, "MD": 24, "MC": 27, "ME": 22, "NL": 18, "NO": 15,
    "PK": 24, "PS": 29, "PL": 28, "PT": 25, "QA": 29, "AZ": 28, "RO": 24, "SM": 27,
    "SA": 24, "RS": 22, "SK": 24, "SI": 19, "ES": 24, "SE": 24, "CH": 21, "TN": 24,
    "TR": 26, "GB": 22
}
tt = input()
if "0" in tt or "1" in tt or "2" in tt or "3" in tt or "4" in tt or "5" in tt or "6" in tt or "7" in tt or "8" in tt or "9" in tt:
    pp = [pm for pm, mk in iban.items() if mk == int(tt)]
    print(" ".join(pp))
else:
    print(iban.get(tt))
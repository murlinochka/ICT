postalcode =   {"A":"Newfoundland","B":"Nova Scotia","C":"Prince Edward Island",
                "E":"New Brunswick","G":"Quebec","H":"Quebec","J":"Quebec",
                "K":"Ontario","L":"Ontario","M":"Ontario","N":"Ontario","P":"Ontario",
                "R":"Manitoba","S":"Saskatchewan","T":"Alberta","V":"British Columbia",
                "X":"Nunavut,Northwest Territories","Y":"Yukon"}

code = input()

if code[0] not in postalcode:
    print('Invalid postal code')
else:
    province = postalcode[code[0]]
if code[1]==0:
    address = "rural"
else:
    address = "urban"
print('The postal code is for {:s} address in'.format(address),end=" ")
print(" or ".join(province.split(",")))
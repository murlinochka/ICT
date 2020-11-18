def check(s1, s2): 
    if sorted(s1)== sorted(s1):
        print("The strings are anagrams.")  
    else: 
        print("The strings aren't anagrams.")          
          
s1 ="William Shakespear"
s2 ="I am a weakish speller" 
s11 = s1.replace(' ', '')
s22 = s2.replace(' ', '')
str1 = s11.upper()
str2 = s22.upper()
check(str1, str2) 
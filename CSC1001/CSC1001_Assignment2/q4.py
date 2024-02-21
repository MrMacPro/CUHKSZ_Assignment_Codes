def isAnagram(s1,s2):   #Function to check if s1 and s2 are anagrams
    s1=s1.lower()   #Set all character in s1 into lower case
    s2=s2.lower()   #Set all character in s2 into lower case
    s1 = sorted(s1) #Sort s1
    s2 = sorted(s2) #Sort s2
    return s1 == s2 #Return if 2 sorted str are same
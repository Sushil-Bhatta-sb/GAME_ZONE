s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

# Step 1: Check length
if len(s1) != len(s2):
    print("Not Anagrams")
else:
    count = {}

    # Step 2: Count characters in first string
    for ch in s1:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    # Step 3: Decrease count using second string
    for ch in s2:
        if ch in count:
            count[ch] -= 1
        else:
            print("Not Anagrams")
            break
    
        # Step 4: Check all counts are zero
        for value in count.values():
          if value != 0:
             print("Not Anagrams")
             break
          else:
             print("Anagrams")
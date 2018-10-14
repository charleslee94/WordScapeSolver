# WordScapeSolver


### Introduction

This is a simple little python script I cooked up to "solve" wordscape puzzles from the popular app store app "WordScapes".
Essentially the script does a few things.

1. Get all permutations from the given string. The string can have repeating characters, so the algorithm checks that the returned permutations do not have more of any character than the initial string. There are also optional arguments that can narrow down the permutations a bit further. They are in order: number of letters in the permutation, character that the permutation starts with, and any characteres that have already been found (can be written as a string, not individual characters)

2. Group permutations by number of letters for ease of reading

3. Check the permutations against PyEnchant's spell checker. There are a few false positives returned for things like abreviations, or whatnot, but this is negligible.

4. Pretty print out the results



This was a fun little project!

### To use
```
pip install -r requirements.txt
   # Navigate to file directory
   python solveWordPuzzle.py characterString <OptionalWordLength> <OptionalCharStartsWith> <OptionalCharIncludedString>

```

Have fun!

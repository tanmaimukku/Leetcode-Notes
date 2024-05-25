# Backtracking 

## String Partitioning

- Partition a string into all possible substrings
- Uses recursive calls to partition and check whatever valid condition needs to be checked (eg. is a palindrome, is present in a dictionary etc.)
- Example Problems 

  <table><tbody><tr><th colspan="1" rowspan="1"><p>Problem</p></th><th colspan="1" rowspan="1"><p>Link</p></th></tr><tr><td colspan="1" rowspan="1"><p>Palindrome Partitioning</p></td><td colspan="1" rowspan="1"><p><a target="_blank" rel="noopener noreferrer nofollow" href="https://leetcode.com/problems/palindrome-partitioning/description/" title="https://leetcode.com/problems/palindrome-partitioning/description/ (Ctrl or Cmd-click to open)">https://leetcode.com/problems/palindrome-partitioning/description/</a></p></td></tr><tr><td colspan="1" rowspan="1"><p>Word Break II</p></td><td colspan="1" rowspan="1"><p><a target="_blank" rel="noopener noreferrer nofollow" href="https://leetcode.com/problems/word-break-ii/description/" title="https://leetcode.com/problems/word-break-ii/description/ (Ctrl or Cmd-click to open)">https://leetcode.com/problems/word-break-ii/description/</a></p></td></tr></tbody></table>

```python
result = []
n = len(s)

def backtrack(curr_partition, start):
    if start == n:
        result.append(curr_partition)
        return
    
    for end in range(start + 1, n + 1):
        substring = s[start:end]
        if is_valid_substring(substring): #is_valid_substring changes with the type of problem at hand
            curr_partition.append(substring)
            backtrack(curr_partition, end) #Can also use backtrack(curr_partition + [substring], end)
            curr_partition.pop()

backtrack([], 0)
return result
```

`result`: A list to store all the valid partitions.

`backtrack` **Function**: A helper function that performs the actual backtracking.

- `curr_partition`: The current partition being constructed.
- `start`: The starting index for partitioning the string.

**Base Case**: If `start` reaches the end of the string (`n`), we add the current partition to the result.

**Recursive Case**: We iterate through possible end indices (`end`), generate substrings from `start` to `end`, and check if they are valid using the `is_valid_substring` function. If valid, we recursively call `backtrack` with the new substring added to the current partition. After the recursive call, we backtrack by removing the last added substring.
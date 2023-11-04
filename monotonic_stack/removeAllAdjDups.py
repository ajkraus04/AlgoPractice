"""Given a string S, remove all adjacent duplicate 
characters recursively to generate the resultant string.

Examples

Input: s = "abccba"
Output: ""
Explanation: First, we remove "cc" to get "abba". Then, we remove "bb" to get "aa". 
Finally, we remove "aa" to get an empty string.

Input: s = "foobar"
Output: "fbar"
Explanation: We remove "oo" to get "fbar".

Input: s = "abcd"
Output: "abcd"
Explanation: No adjacent duplicates so no changes."""

    def removeDuplicates(self, s: str) -> str:
        # TODO: Write your code here
        stack = []
        for char in s:
            if stack and char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)

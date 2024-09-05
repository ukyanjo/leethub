class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            print(set('cbacdcbc'), set('cdcbc'))
            if set(s) == set(suffix):
                # print(suffix)
                # print(self.removeDuplicateLetters(suffix.replace(char,'')))
                return char + self.removeDuplicateLetters(suffix.replace(char,''))
            
        return ''

#         counter, seen, stack = collections.Counter(s), set(), []
            
#         for char in s:
#             counter[char] -= 1
#             if char in seen:
#                 continue
                
#             while stack and char < stack[-1] and counter[stack[-1]] > 0:
#                 seen.remove(stack.pop())
                
#             stack.append(char)
#             seen.add(char)
            
#         return ''.join(stack)
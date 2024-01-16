'''
Dada una cadena 's' que contiene solo caracteres '(', ')', '{', '}', '[' y ']' y , determine 
si la cadena de entrada es valida.

Una cadena de entrada es validad si:

1. Los corchetes abiertos deben estar cerrados por el mismo tipo de corchetes.
2. Los corchetes abiertos deben cerrarse en el orden correcto.
3. Cada corchete cerrado tiene un corchete abierto correspondiente del mismo tipo.

Ejemplo 1:
    Imput: s = "()"
    Output: true

Ejemplo 2:
    Imput: s = "()[]{}"
    output: true

Ejemplo 3:
    Imput: s = "(]"
    Output: false

Restricciones:
- 1 <= s.length <= 10^4
- 's' consta solo de parentesis. '()[]{}'
'''

## Para LeetCode (inicio) ##
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        brackets = {'(':')', '[':']', '{':'}'} 

        for char in s:
            if char in brackets:
                stack.append(char)
            else:
                if not stack or brackets[stack.pop()] != char:
                    return False

        return not stack
## Para LeetCode (fin) ##

sol = Solution()

print(sol.isValid("()"))
print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))

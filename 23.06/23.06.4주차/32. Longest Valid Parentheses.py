class Solution:
    def longestValidParentheses(self, s: str) -> int:
            stack = [-1]  # 스택을 초기화하고 -1을 넣어 시작합니다.
            max_length = 0  # 최대 길이를 저장하는 변수입니다.
            
            for i in range(len(s)):
                if s[i] == '(':
                    stack.append(i)  # 열리는 괄호인 경우 인덱스를 스택에 추가합니다.
                else:
                    stack.pop()  # 닫히는 괄호인 경우 스택에서 맨 위의 인덱스를 제거합니다.
                    if len(stack) == 0:
                        stack.append(i)  # 스택이 비어있는 경우 닫히는 괄호의 인덱스를 스택에 추가합니다.
                    else:
                        max_length = max(max_length, i - stack[-1])  # 유효한 괄호의 길이를 계산하여 최대 길이를 갱신합니다.
            
            return max_length
# BOJ 10809 알파벳 찾기
import sys
input = sys.stdin.readline

s = input()

for i in range(97, 123):
    print(s.find(chr(i)), end = ' ')

#* 강의 풀이
'''
import sys
input = sys.stdin.readline
arr = [-1] * 26 # a부터 z까지의 알파벳은 총 26개 
data = input().strip() # 문자열 입력

for i in range(len(data)): # 문자를 하나씩 확인
    # 알파벳 a는 인덱스 0, z는 인덱스 25에 해당 
    index = ord(data[i]) - ord('a')
    if arr[index] == -1: # 처음 등장한 알파벳이라면
        arr[index] = i # 등장한 위치 기록

for x in arr: # 각 알파벳이 처음 등장하는 위치 출력
    print(x, end=' ')
    '''
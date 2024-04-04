seq1 = "AAAA"
seq2 = "ABABAAA"
dp = dict()

def helper(i, j):
    if i == len(seq1) and j == len(seq2):
        return '', '', 0
    if i == len(seq1):
        return ' ' * (len(seq2) - j), seq2[j:], -2 * (len(seq2) - j)
    if j == len(seq2):
        return seq1[i:], ' ' * (len(seq1) - i), -2 * (len(seq1) - i)
    if (i, j) in dp:
        return dp[(i, j)]

    ansChar1 = ''
    ansChar2 = ''
    ansScore = -100000000

    if seq1[i] == seq2[j]:
        subString1, subString2, subScore = helper(i + 1, j + 1)
        currScore = subScore + 1
        if currScore > ansScore:
            ansScore = currScore
            ansChar1 = seq1[i] + subString1
            ansChar2 = seq2[j] + subString2

    subString1, subString2, subScore = helper(i + 1, j)
    currScore = subScore - 2
    if currScore > ansScore:
        ansScore = currScore
        ansChar1 = seq1[i] + subString1
        ansChar2 = ' ' + subString2

    subString1, subString2, subScore = helper(i, j + 1)
    currScore = subScore - 2
    if currScore > ansScore:
        ansScore = currScore
        ansChar1 = ' ' + subString1
        ansChar2 = seq2[j] + subString2

    subString1, subString2, subScore = helper(i + 1, j + 1)
    currScore = subScore - 1
    if currScore > ansScore:
        ansScore = currScore
        ansChar1 = seq1[i] + subString1
        ansChar2 = seq2[j] + subString2

    dp[(i, j)] = ansChar1, ansChar2, ansScore
    return ansChar1, ansChar2, ansScore

result1, result2, score = helper(0, 0)
print("Optimal string 1:", result1)
print("Optimal string 2:", result2)
print("Score:", score)

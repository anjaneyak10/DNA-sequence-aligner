# Sequence Alignment Tool

This tool aligns two sequences to maximize their similarity score.

## Introduction

This code implements a sequence alignment algorithm to align two DNA sequences in order to maximize their similarity score. The algorithm inserts spaces at arbitrary locations in the sequences to create aligned sequences of the same length. 

## Similarity Measurement

The similarity between the aligned sequences is measured using the following scoring criteria for each position:
- **+1** if characters at the corresponding positions are identical (and neither is a space).
- **-1** if characters at the corresponding positions are different (and neither is a space).
- **-2** if either of the characters at the corresponding positions is a space.

## Usage

To use this tool, simply provide two sequences as input. The tool will output the optimal alignment of the sequences along with the maximum similarity score.

```python
# Example usage
seq1 = "AGTACG"
seq2 = "ATAGC"
result1, result2, score = helper(seq1, seq2)
print("Optimal string 1:", result1)
print("Optimal string 2:", result2)
print("Score:", score)

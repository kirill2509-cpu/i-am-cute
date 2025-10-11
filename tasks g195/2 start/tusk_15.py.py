seq = 'AGCGGCCERCCCGGGGGGGGGGGGTTTTTTTTTTTT'
print(f"G+C: {(seq.count('G') + seq.count('C')) / len(seq) * 100:.2f}%")
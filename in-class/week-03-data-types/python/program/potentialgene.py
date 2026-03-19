import sys

def is_potential_gene(dna):
  # number of bases is multiple of 3
  if (len(dna) % 3) != 0: return False

  # starts with start codon
  if not dna.startswith("ATG"): return False

  # no intervening stop codons
  for i in range(len(dna) - 3):
    if i % 3 == 0:
      if dna[i:i+3] == "TAA": return False
      if dna[i:i+3] == "TAG": return False
      if dna[i:i+3] == "TGA": return False

  # ends with a stop codon
  if dna.endswith("TAA"): return True
  if dna.endswith("TAG"): return True
  if dna.endswith("TGA"): return True

  return False


if __name__ == "__main__":
  dna = sys.argv[1]
  print(is_potential_gene(dna))
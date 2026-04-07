import sys
import program.merge as merge

from program.counter import Counter
# from counter import Counter         # If we run it from terminal


def _main():
  filename = sys.argv[1]
  with open(filename, "r") as fp:
    data = fp.readlines() 
  
  words = " ".join(data).split()
  # words.sort()      // using Python system sort
  merge.sort(words)
  # print(words)
  zipf = []
  for i in range(len(words)):
    if (i == 0) or (words[i] != words[i-1]):
      entry = Counter(words[i], len(words))
      # print(entry)
      zipf += [entry]

    zipf[len(zipf) - 1].increment()
  
  zipf.sort()
  zipf.reverse()

  max_chars = len(f"{zipf[0]._max_count}")
  max_rows = 100
  for idx, entry in enumerate(zipf):
    print(f"{entry._count:{max_chars}}: {entry._name}")

    if idx > max_rows:
      break


if __name__ == "__main__": _main()
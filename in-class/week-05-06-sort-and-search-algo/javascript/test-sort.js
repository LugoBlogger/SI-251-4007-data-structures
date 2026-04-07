const start = performance.now();

let a = null;
for (let i = 0; i < 10_000; i++) {
  // Create an array of random number between 0 and 99 (inclusively)
  a = Array.from({length: 1_000}, () => Math.floor(Math.random() * 100));
  a.sort()
}

const end = performance.now();
console.log(`Execution time: ${(end - start)/1000.} s`)
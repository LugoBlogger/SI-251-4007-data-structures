// Install the @stdlib/random-iter-uniform with the following command
// npm install @stdlib/random-iter-uniform

import iterator from "@stdlib/random-iter-uniform";

// const seed = 26_04_16;    // Group E
// const num_of_students = 36;

const seed = 26_04_17;    // Group D
const num_of_students = 43;

let iter = iterator(0., 1., {"seed": seed}); 

let rand_num = [];
for (let i = 0; i < num_of_students; i++) {
  rand_num.push(iter.next().value)
}

// console.log(rand_num);
for (let i = 0; i < num_of_students; i++) {
  console.log(rand_num[i]);
}

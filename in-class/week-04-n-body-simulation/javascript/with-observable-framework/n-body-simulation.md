---
title: n-body-simulation
---

There are three files to simulate three-body problem

```js
import { Vector } from './components/vector.js';
import { Body } from '/components/body.js';
import { Universe } from './components/universe.js';
import { animate, svg, createTimeline} from 'animejs';
```

<div id="animation-container" style="position: relative; 
     width: 400px; height: 400px;">
<svg id="svg-container" width="400" height="400" viewBox="0 0 400 400" 
     style="position: absolute; top: 0; left: 0; z-index: 1;">
</svg>
</div>


<style>
.circle {
  background-color: white; 
  height: 10px;
  width: 10px;
  border-radius: 50%;
  position: absolute;
  top: -5px;
  left: -5px;
  z-index: 2;
  box-sizing: border-box;     /* keeps the circle size consistent if we add borders */
}
</style>

```js
// let dataString = await FileAttachment("./data/2body.txt").text();
let dataString = await FileAttachment("./data/3body.txt").text();
// let dataString = await FileAttachment("./data/4body.txt").text();

// let dataString = await FileAttachment("./data/2bodyTiny.txt").text();
// let dataString = await FileAttachment("./data/3body-ia-ic-1-2.txt").text();

// display(dataString);

let universe = new Universe(dataString);
// display(universe.toString());

const dt = 20_000;

let tMax = 200_000_000;    // for 2body.txt
if (universe._n === 3) { tMax = 60_000_000; }     // for 3body.txt

const screenRadius = 200;

let pathsData = Array.from( { length: universe._n }, 
  () => ({ mass: 0, x: [], y: [] }));

for (let i = 0; i < universe._n; i++)  {
  pathsData[i].mass = universe._bodies[i]._mass;
}

// display(pathsData);

for (let tStart = 0; tStart < tMax; tStart += dt) {

  universe.increaseTime(dt);
  for (let i = 0; i < universe._n; i++ ) {
    let xPos = universe._bodies[i]._r.at(0);
    let yPos = universe._bodies[i]._r.at(1);

    // -- rescale to the screenRadius
    xPos = xPos/universe._radius * screenRadius + screenRadius;
    yPos = yPos/universe._radius * screenRadius + screenRadius;

    pathsData[i].x.push(xPos);
    pathsData[i].y.push(yPos);
  }

}

// display(pathsData);

```


```js
// const pathsData = [
//   { x: [20, 100, 250, 350], y: [50, 150, 80, 300] },
//   { x: [370, 230, 90, 10], y: [310, 50, 200, 70] }
// ]

const svgContainer = document.getElementById('svg-container');
const animContainer = document.getElementById('animation-container');

const colors = ['red', 'blue', 'green', 'orange', 'purple'];
const duration = Math.round(tMax / dt) * 5;

const tl = createTimeline({
  defaults: { duration: duration, ease: 'linear' }
})

pathsData.forEach((data, index) => {
  const color = colors[index % colors.length];

  const pointsString = data.x.map((xVal, i) => `${xVal},${data.y[i]}`).join(' ');
  // display(pointsString);

  const polyline = document.createElementNS('http://www.w3.org/2000/svg', 'polyline');
  polyline.setAttribute('points', pointsString);
  polyline.setAttribute('stroke', color);
  polyline.setAttribute('stroke-width', '1');
  polyline.setAttribute('stroke-opacity', '0.75');
  polyline.setAttribute('fill', 'none');
  svgContainer.appendChild(polyline);

  const circle = document.createElement("div");
  circle.className = 'circle';
  // circle.style.backgroundColor = color;
  circle.style.border = `2px solid ${color}`;
  animContainer.appendChild(circle);

  const motionPath = svg.createMotionPath(polyline);

  tl.add(svg.createDrawable(polyline), { draw: '0 1' }, 0)
    .add(circle, { x: (progress) => motionPath.translateX(progress), 
                   y: (progress) => motionPath.translateY(progress) }, 0);

})
```
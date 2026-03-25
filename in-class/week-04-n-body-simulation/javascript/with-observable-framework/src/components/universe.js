/* 
  Logs
  - [2026/03/22]   
     Reading file is complicated (maybe there is a way, but for this moment
     I use dataString as the argument in the constructor)
 */
import { Vector } from '/components/vector.js'
import { Body } from '/components/body.js'

export class Universe {
  constructor(dataString) {

    this._dataArr = dataString.split("\n");
    
    this._n = parseInt(this._dataArr[0]);
    this._radius = parseFloat(this._dataArr[1]);
        
    this._bodies = new Array(this._n);
    for (let i = 0; i < this._n; i++) {
      const row = (this._dataArr[i+2]).trim().split(/\s+/);
      const rx = parseFloat(row[0]);
      const ry = parseFloat(row[1]);
      const vx = parseFloat(row[2]);
      const vy = parseFloat(row[3]);
      const mass = parseFloat(row[4]);

      const r = new Vector([rx, ry]);
      const v = new Vector([vx, vy]);

      this._bodies[i] = new Body(r, v, mass);
    }

  }

  increaseTime(dt) {
    const n = this._n;
    let f = Array.from({ length: n }, () => new Vector([0.0, 0.0]))
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (i !== j) {
          let body_i = this._bodies[i];
          let body_j = this._bodies[j];
          f[i] = f[i].add(body_i.forceFrom(body_j));
        }
      }
    }

    for (let i = 0; i < n; i++) {
      this._bodies[i].move(f[i], dt)
    }
  }

  toString() {
    let dataString = `n = ${this._n}\n`
      + `radius = ${this._radius}\n`
    for (let i = 0; i < this._n; i++) {
      dataString += "  " + this._bodies[i].toString() + "\n";
    }
    return dataString;
  }


}
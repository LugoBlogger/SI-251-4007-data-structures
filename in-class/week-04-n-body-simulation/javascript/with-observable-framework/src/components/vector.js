export class Vector {
  constructor(a) {
    this._coords = [...a];      // avoid copy by reference
    this._n = a.length;
  }

  add(other) {
    const result = this._coords.map((val, i) => val + other._coords[i]);
    return new Vector(result);
  }

  sub(other) {
    const result = this._coords.map((val, i) => val - other._coords[i]);
    return new Vector(result)
  }

  dot(other) {
    return this._coords.reduce((sum, val, i) => sum + val*other._coords[i], 0);
  }

  scale(alpha) {
    const result = this._coords.map(val => val * alpha);
    return new Vector(result);
  }

  direction() { return this.scale(1.0 / this.abs()); }

  abs() { return Math.sqrt(this.dot(this)) }

  at(i) { return this._coords[i]; }

  get length() { return this._n; }

  toString() { return `[${this._coords.join(', ')}]`; }

}
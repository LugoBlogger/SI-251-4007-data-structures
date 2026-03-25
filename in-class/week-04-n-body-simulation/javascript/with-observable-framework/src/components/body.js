
export class Body {
  constructor(r, v, mass) {
    this._r = r;
    this._v = v;
    this._mass = mass;
  }

  move(f, dt) {
    let a = f.scale(1.0 / this._mass);
    this._v = this._v.add(a.scale(dt));
    this._r = this._r.add(this._v.scale(dt));
  }

  forceFrom(other) {
    const G = 6.67e-11;
    let delta = other._r.sub(this._r);
    let dist = delta.abs();
    let m1 = this._mass;
    let m2 = other._mass;
    let magnitude = G * m1 * m2 / (dist * dist);
    return delta.direction().scale(magnitude)
  }

  toString() { 
    return `r = ${this._r.toString()}; `
     + `v = ${this._v.toString()}; `
     + `m = ${this._mass}`; }
}
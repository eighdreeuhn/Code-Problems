circleIntersection=(a,b,r)=> {
    let d = Math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
    let t = Math.acos(d/2/r)*2
    let s = (r**2/2)*t
    let q = (r**2/2)*Math.sin(t)
    return (s-q)*2
}

const c1 = [0, 0]
const c2 = [7, 0]
const r = 5

circleIntersection(c1, c2, r)

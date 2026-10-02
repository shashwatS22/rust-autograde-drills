enum Shape { Circle(f64), Rect(f64, f64) }
fn area(s: &Shape) -> f64 {
    match s {
        Shape::Circle(r) => std::f64::consts::PI * r * r,
        Shape::Rect(w, h) => w * h,
    }
}
fn main() {
    println!("{:.2}", area(&Shape::Circle(5.0)));
    println!("{:.2}", area(&Shape::Rect(3.0, 4.0)));
}

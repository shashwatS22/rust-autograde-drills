fn main() {
    cc::Build::new().file("native/add.c").compile("native_add");
}

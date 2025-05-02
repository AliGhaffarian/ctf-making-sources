use std::time::{SystemTime, UNIX_EPOCH};
use std::fs::File;
use std::io::Write;
use std::io;

fn encrypt(data : &str, key : u8)->Vec::<u8>{
    return data.bytes().map(|bytes| bytes ^ key).collect();
}
fn main() {
    let mut now = SystemTime::now()
            .duration_since(UNIX_EPOCH).unwrap()
            .as_secs();

    let mut file = File::create("flag.enc").expect("unexpected error");
    //touch flag.enc
    //generate timestamp
    now = (now / 1000) * 1000;
    now = now & 0b11111111;

    let mut secret : String = Default::default();
    io::stdin().read_line(&mut secret).unwrap();

    let mut enc = encrypt(secret.trim(), now as u8);
    enc.reverse();

    file.write_all(&enc);
    file.flush().unwrap();

    println!("now nobody can uncover your secrets!");
}

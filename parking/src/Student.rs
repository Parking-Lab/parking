use std::collections::HashMap;
use std::fs;
use std::error::Error;
use serde_json::{Value, Map};

pub struct Student{
    name: str,
    score: f32,
    row: Vec<u8>,
}

impl Student{
    const DISTANCES: Map<String, Value> = Student::read_config("~/parking/distance.json").unwrap();
    
    fn read_config(path: &str) -> Result<Map<String, Value>, Box<Error>> {
        let config = fs::read_to_string(path)?;
        let parsed: f32 = serde_json::from_str(&config)? as f32;
        let obj: Map<String, f32> = parsed.as_object().unwrap().clone();
        Ok(obj)
    }

    pub fn new(student_name: &str, row: &Vec<i32>) -> Student{
        Student {
            name: *student_name,
            row: row,
        }
    }

    pub fn generate_score(&self, day: u8) -> f32{
        let crit: u8 = self.row[2..7][day];
        let sports: u8 = self.row[7..12][day];
        let dist: f32 = Student::DISTANCES[String::from(self.row[1])]?;
        let carpoolSeniors: f32 = self.row[12][day];
        let carpoolYoungns: f32 = self.row[13][day];
        
    }

    pub fn can_parallel_park(&self) -> bool{
        self.row[16] == 1
    }
    pub fn has_small_car(&self) -> bool{
        self.row[0] == 1
    }
    pub fn get_name(&self) -> str{
        self.name
    }

}
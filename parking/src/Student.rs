use std::collections::HashMap;
use std::fs;
use std::error::Error;
use serde_json::{Value, Map};
use rand::distributions::{Normal, Distribution};

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
            row: row.clone(),
        }
    }

    pub fn generate_score(&self, day: usize) -> f32{
        let crit: u8 = self.row[2..7][day];
        let sports: u8 = self.row[7..12][day];
        let fp_free = self.row[14];
        let lp_free = self.row[15];
        let dist: f32 = Student::DISTANCES[self.row[1]];
        let carpool_seniors: u8 = self.row[12];
        let carpool_youngns: u8 = self.row[13];
        let strikes = self.row[17]
        let weights: Vec<f32> = vec![16.0, 8.0, 10.0, 40.0, -20];
        let mut score: f32 = weights.iter().zip(vec![fp_free, lp_free, crit, sports, strikes].iter()).map(|(x, y)| x * (*y as f32)).sum();
        score *= 1.0 + carpool_seniors as f32 + (carpool_youngns as f32 * 0.25);
        score += Normal::new(0.0, 5.0);

        score
    }

    pub fn can_parallel_park(&self) -> bool{
        self.row[16] == 1
    }
    pub fn has_small_car(&self) -> bool{
        self.row[0] == 1
    }
    pub fn get_name(&self) -> String{
        String::from(&self.name)
    }

}
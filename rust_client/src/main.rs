use reqwest::Client;
use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize, Debug)]
struct TextData {
    text: String,
}

#[tokio::main]
async fn main() {
    let client = Client::new();

    // Le texte à anonymiser
    let text_to_anonymize = TextData {
        text: String::from("Jean rencontra Marie a Paris en 2010 ils visiterent ensemble le Louvre pendant trois jours puis ils partirent a Rome en 2012 pour explorer les ruines antiques"),
    };

    // Appel à l'API FastAPI
    let res = client
        .post("http://127.0.0.1:8000/anonymize") // Assurez-vous que l'API FastAPI fonctionne sur ce port
        .json(&text_to_anonymize)
        .send()
        .await;

    match res {
        Ok(response) => {
            let anonymized_text: serde_json::Value = response.json().await.unwrap();
            println!("Texte anonymisé : {}", anonymized_text["anonymized_text"]);
        }
        Err(e) => {
            eprintln!("Erreur lors de l'appel de l'API : {}", e);
        }
    }
}

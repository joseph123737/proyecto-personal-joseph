import { config } from "../config";
import { v4 as uuidv4 } from "uuid";
export async function saveNewQuizz(quizz,quizz_name) { 
    let quizz_to_save = {id_quizz:uuidv4(),quizz_name:quizz_name,quizzes:quizz}
    const settings = {
        method: "POST",
        body: JSON.stringify(quizz_to_save),
        headers: {
          "Content-Type": "application/json",
        },
    };
    let response =  await fetch(`${config.API_PATH}/quizz/add-quizz`,settings)     
    return response   
}
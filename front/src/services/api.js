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

export async function getQuizzById(id){
  let response =  await fetch(`${config.API_PATH}/quizz/${id}`)
  return response
}

export async function getAllQuizzes(){
  let response = await fetch(`${config.API_PATH}/quizz`)
  return response
}

export async function updateUsersStats(newData){
  const userJson = localStorage.getItem("auth");
  const user = JSON.parse(userJson);
  const settings = {
        method: "PUT",
        body: JSON.stringify(newData),
        headers: {
          "Content-Type": "application/json"
        },
  };
  let response =  await fetch(`${config.API_PATH}/users/users-stats/change-stats/${user.user_id}`,settings)
  return response
}

export async function getUserStatsById(id){
    let response = await fetch(`${config.API_PATH}/users/users-stats/${id}`)
    return response
}
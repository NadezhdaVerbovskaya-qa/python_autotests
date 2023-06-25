import requests
import pytest

token='d937b358db69926505189ed595d98185'
host='https://pokemonbattle-stage.me:9101/'

def test_status_code():

    ans_info_train_code=requests.get(f'{host}/trainers', params={"trainer_id":1050}, 
                                 headers={"Content-Type":"application/json", "trainer_token":token})

    assert ans_info_train_code.status_code == 200


def test_answer_body():

    ans_info_train_body=requests.get(f'{host}/trainers', params={"trainer_id":1050}, 
                                 headers={"Content-Type":"application/json", "trainer_token":token})

    assert ans_info_train_body.json()['trainer_name'] == 'Nadu4a'
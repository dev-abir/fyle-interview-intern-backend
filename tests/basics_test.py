from datetime import datetime


def test_get_index(client):
    min_response_time_possible = datetime.utcnow()
    response = client.get("/")
    max_response_time_possible = datetime.utcnow()

    # TODO: add warning for very high response time?
    # TODO: also check time in reponse

    assert response.status_code == 200

    data = response.json
    assert data["status"] == "ready"
    assert "time" in data
    print(data['time'])
    # time = datetime.strptime(data['time'], )
    # assert time > min_response_time_possible and time < max_response_time_possible


def test_no_such_api(client, h_teacher_1):
    response = client.post(
        "/randomroute", headers=h_teacher_1, json={"id": 2, "grade": "A"}
    )

    assert response.status_code == 404

    data = response.json
    assert data["error"] == "NotFound"
    assert (
        data["message"]
        == "404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."
    )

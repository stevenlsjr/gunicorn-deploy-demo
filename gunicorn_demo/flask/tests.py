from unittest import mock

import pytest

service = None


@pytest.fixture(autouse=True, scope='function')
def before_all():
    from ..poll_service import PollService
    global service
    service = mock.MagicMock(spec=PollService)


def mock_get_poll_service():
    return service

@mock.patch('gunicorn_demo.flask.api_v1.get_poll_service',
                    new=mock_get_poll_service)
def test_poll_list(client):
    from gunicorn_demo import poll_service
    polls = [{
        'id': 0,
        'name': 'my poll',
        'agree_count': 1,
        'disagree_count': -1
    }]
    service.list.return_value = polls
    res = client.get('/api/v1/polls/?limit=1')
    assert res.status_code == 200
    assert res.json['results'] == polls
    assert res.json['limit'] == 1

@mock.patch('gunicorn_demo.flask.api_v1.get_poll_service',
                    new=mock_get_poll_service)
def test_poll_get(client):
    from gunicorn_demo import poll_service
    poll = {
        'id': 0,
        'name': 'my poll',
        'agree_count': 1,
        'disagree_count': -1
    }
    service.get.return_value = poll
    res = client.get('/api/v1/polls/0/')
    assert res.status_code == 200
    assert res.json == poll

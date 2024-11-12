import pytest
from book import Survey

@pytest.fixture
def age_survey():
    age_survey = Survey(question='123')
    return age_survey

def test_1(age_survey):
    age_survey.store_response('1')
    assert '1' in age_survey.responses

def test_123(age_survey):
    # question = '123'
    responses = ['1','2','3']
    for response in responses:
        age_survey.store_response(response)
    for response in responses:
        assert response in age_survey.responses

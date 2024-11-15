# import pytest
# from book import Survey

# @pytest.fixture
# def age_survey():
#     age_survey = Survey(question='123')
#     return age_survey

# def test_1(age_survey):
#     age_survey.store_response('1')
#     assert '1' in age_survey.responses

# def test_123(age_survey):
#     # question = '123'
#     responses = ['1','2','3']
#     for response in responses:
#         age_survey.store_response(response)
#     for response in responses:
#         assert response in age_survey.responses

import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text="Label 1", bg="yellow")
label1.pack(pady=10)  # 上下各有 10 像素的间距

label2 = tk.Label(root, text="Label 2", bg="cyan")
label2.pack(pady=20)  # 上下各有 20 像素的间距

root.mainloop()

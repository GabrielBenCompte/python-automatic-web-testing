from webtester import WebTester


"""To test all json files in a directory"""
directory_to_test = ''
web_tester = WebTester()
if directory_to_test:
    web_tester.test_files(directory_to_test)


"""To test specific data"""
data_to_test = {
        "name": "Test 'What does the “yield” keyword do?' still in python top questions in stackoverflow",
        "resolution": {
            "width": 1280,
            "height": 720
        },
        "actions": [
            {"type": "GO", "url": "https://stackoverflow.com/"},
            {"type": "FILL", "xpath": "//*[@id='search']/div/input", "text": "python", "send": True},
            {"type": "CLICK", "xpath": "//*[@id='mainbar']/div[4]/div[2]/div/a[5]"},
            {"type": "CLICK", "xpath": "//*[@id='question-summary-231767']/div[2]/h3/a"},
            {"type": "CHECK", "xpath": "//*[@id='question-header']/h1/a", "values": ["What does the “yield” keyword do?"]}
        ]

        }
web_tester.test_data(data=data_to_test)

"""To test specific actions"""

actions_to_test = [
    {"type": "GO", "url": "https://stackoverflow.com/"},
    {"type": "FILL", "xpath": "//*[@id='search']/div/input", "text": "python", "send": True},
    {"type": "CLICK", "xpath": "//*[@id='mainbar']/div[4]/div[2]/div/a[5]"},
    {"type": "CLICK", "xpath": "//*[@id='question-summary-231767']/div[2]/h3/a"},
    {"type": "CHECK", "xpath": "//*[@id='question-header']/h1/a", "values": ["What does the “yield” keyword do?"]}
]
web_tester.test_actions(actions_to_test)


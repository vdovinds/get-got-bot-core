import unittest

import handler


class TestHandlerMethods(unittest.TestCase):

    def test_should_return_poem_when_action_is_poem(self):
        evenWithPoemAction = {
            'queryStringParameters': {
                'action': 'poem',
                'user_id': '12345',
                'user_type': 'test',
                'user_info': {
                    'login': 'test_login',
                    'name': 'test_name'
                }
            }
        }
        result = handler.handler(evenWithPoemAction, '')

        self.assertEqual(result['statusCode'], 200)
        self.assertTrue('body' in result)
        self.assertTrue('poem' in result['body'])
        self.assertTrue('poem_template' in result['body'])
        self.assertTrue('first' in result['body'])
        self.assertTrue('second' in result['body'])
        self.assertTrue('third' in result['body'])
        self.assertTrue('ru' in result['body'])

    def test_should_issue_task(self):
        evenWithTaskAction = {
            'queryStringParameters': {
                'action': 'task',
                'user_id': '12345',
                'user_type': 'test',
                'user_info': {
                    'login': 'test_login',
                    'name': 'test_name'
                }
            }
        }
        result = handler.handler(evenWithTaskAction, '')
        self.assertEqual(result['statusCode'], 200)
        self.assertTrue('ru' in result['body'])
        self.assertTrue('first' in result['body'])
        self.assertTrue('second' in result['body'])
        self.assertTrue('third' in result['body'])
        self.assertTrue('expected_verb_form' in result['body'])

    def test_should_check_task(self):
        evenWithTaskAction = {
            'queryStringParameters': {
                'action': 'check',
                'user_id': '12345',
                'user_type': 'test',
                'answer': 'test',
                'user_info': {
                    'login': 'test_login',
                    'name': 'test_name'
                }
            }
        }
        result = handler.handler(evenWithTaskAction, '')
        self.assertEqual(result['statusCode'], 200)
        self.assertTrue('result' in result['body'])

    def test_should_get_answer_for_task(self):
        evenWithTaskAction = {
            'queryStringParameters': {
                'action': 'answer',
                'user_id': '12345',
                'user_type': 'test',
                'user_info': {
                    'login': 'test_login',
                    'name': 'test_name'
                }
            }
        }
        result = handler.handler(evenWithTaskAction, '')
        self.assertEqual(result['statusCode'], 200)
        self.assertTrue('poem' in result['body'])


if __name__ == '__main__':
    unittest.main()

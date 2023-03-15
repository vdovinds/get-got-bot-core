import unittest

import handler


class TestHandlerMethods(unittest.TestCase):

    def test_should_return_poem_when_action_is_poem(self):
        evenWithPoemAction = {
            'queryStringParameters': {
                'action': 'poem',
                'user_id': '12345',
                'user_type': 'test'
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


if __name__ == '__main__':
    unittest.main()

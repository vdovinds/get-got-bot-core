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

        self.assertEqual(result['body'], 'get poem')
        self.assertEqual(result['statusCode'], 200)


if __name__ == '__main__':
    unittest.main()

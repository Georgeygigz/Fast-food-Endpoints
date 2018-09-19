# app/test/v1/test_views.py

'''
Testing our api endpoints
'''

import unittest
import json
from app import app
from app.api.v1.models import Orders

food_orders=Orders().get_food_orders()


class TestApiEndpoint(unittest.TestCase):
    def setUp(self):
        '''
        Code executed before every test
        '''
        self.app = app.test_client()
        self.app.testing = True
        self.food_items ={"id":1,
                          "food_name":'Piza',
                          "description":"fast",
                          "quantity":2,
                          "status":"pedding"}
    
    '''
    Test for placement of new order
    '''
    def test_user_can_place_an_order(self):
        '''
        Test API can place a new order (POST request)
        '''
        result = self.app.post('/app/v1/orders',data=json.dumps(self.food_items))

        self.assertEqual(result.status_code, 201)


    '''Test for getting the list of order'''
    def test_get_list_of_orders(self):
        '''Test API Endpoint can get list of order(GET Request)'''
        response=self.app.get('/app/v1/orders',
                                    headers={'content_type': 'application/json'})
        
        
        self.assertEqual(response.status_code, 200)
    
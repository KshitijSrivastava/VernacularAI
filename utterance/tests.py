from django.test import TestCase

# Create your tests here.

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# data = {
#             "invalid_trigger": "invalid_ids_stated",
#             "key": "ids_stated",
#             "name": "govt_id",
#             "reuse": True,
#             "support_multiple": True,
#             "pick_first": False,
#             "supported_values": [
#                 "pan",
#                 "aadhaar",
#                 "college",
#                 "corporate",
#                 "dl",
#                 "voter",
#                 "passport",
#                 "local"
#                 ],
#             "type": [
#                 "id"
#                 ],
#             "validation_parser": "finite_values_entity",
#             }

class ValidateSlotValuesTests(APITestCase):

    def case1(self):
        """
       
        """
        url = reverse('validate-slot')

        data = {
            "invalid_trigger": "invalid_ids_stated",
            "key": "ids_stated",
            "name": "govt_id",
            "reuse": True,
            "support_multiple": True,
            "pick_first": False,
            "supported_values": [
                "pan",
                "aadhaar",
                "college",
                "corporate",
                "dl",
                "voter",
                "passport",
                "local"
                ],
            "type": [
                "id"
                ],
            "validation_parser": "finite_values_entity",
            }

        data["values"] = [
                    {
                        "entity_type": "id",
                        "value": "college"
                    }
                ]
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, 
        { "filled": True, "partially_filled": False, "trigger": "", "parameters": {
            "ids_stated": [ "COLLEGE" ] } })

    # def case2(self):
    #     """
       
    #     """
    #     url = reverse('validate-slot')
    #     data["values"] = [
    #                 {
    #                     "entity_type": "id",
    #                     "value": "other"
    #                 }
    #             ]
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data, 
    #     { "filled": False, "partially_filled": True, "trigger": "invalid_ids_stated", 
    #     "parameters": {} })


    

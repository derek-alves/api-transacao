from rest_framework import status
from rest_framework.test import APITestCase

from mixer.backend.django import mixer

from app.models import Transacao

class ViewsTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super(ViewsTestCase, cls).setUpClass()
        mixer.blend(Transacao)
    
    def test_post(self):
        data = {"estabelecimento": "45.283.163/0001-67", "cliente": "094.214.930-01", "valor": 590.01, "descricao": "Almoço em restaurante chique pago via Shipay!"}
        response = self.client.post("/api/v1/transacao/", data=data)
        data["valor"] = "a"
        bad_response = self.client.post("/api/v1/transacao/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(bad_response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get(self):
        response = self.client.get("/api/v1/transacao/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

from django.test import TestCase

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(Title='Item 1', Price=9.99, Inventory=10)
        Menu.objects.create(Title='Item 2', Price=12.49, Inventory=15)
        Menu.objects.create(Title='Item 3', Price=5.99, Inventory=5)

    def test_getall(self):
        client = APIClient()
        response = client.get('/api/menu/')
        menu_queryset = Menu.objects.all()
        expected_data = MenuSerializer(menu_queryset, many=True).data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected_data)
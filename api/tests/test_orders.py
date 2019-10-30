from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.orders.models import OrderModel, OrderItemModel


class OrderTests(APITestCase):
    fixtures = ['products']

    def test_create_order(self):
        url = reverse('ordermodel-list')
        data = 	{
            'customer_full_name': 'brian',
            'customer_address': 'larco 264',
            'customer_city': 'lima',
            'customer_post_code': '12345',
            'items': [
                {
                    'pizza_variant_id': 1, # Hawaiian personal
                    'quantity': 1
                },
                {
                    'pizza_variant_id': 7, # American personal
                    'quantity': 1
                }
            ]
        }
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(OrderModel.objects.count(), 1)
        self.assertEqual(OrderItemModel.objects.count(), 2)

    def test_update_order_with_good_next_delivery_status(self):
        url_orders = reverse('ordermodel-list')
        data = 	{
            'customer_full_name': 'brian',
            'customer_address': 'larco 264',
            'customer_city': 'lima',
            'customer_post_code': '12345',
            'items': [
                {
                    'pizza_variant_id': 1,
                    'quantity': 1
                }
            ]
        }
        resp_create = self.client.post(url_orders, data, format='json')

        url_order_detail = reverse('ordermodel-detail', args=[resp_create.data['id']])
        data = 	{'delivery_status': 'preparing'}
        resp = self.client.patch(url_order_detail, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(OrderModel.objects.get().delivery_status, 'preparing')

    def test_update_order_with_bad_next_delivery_status(self):
        url_orders = reverse('ordermodel-list')
        data = 	{
            'customer_full_name': 'brian',
            'customer_address': 'larco 264',
            'customer_city': 'lima',
            'customer_post_code': '12345',
            'items': [
                {
                    'pizza_variant_id': 1,
                    'quantity': 1
                }
            ]
        }
        resp_create = self.client.post(url_orders, data, format='json')
        url_order_detail = reverse('ordermodel-detail', args=[resp_create.data['id']])

        data = 	{'delivery_status': 'preparing'}
        self.client.patch(url_order_detail, data, format='json')

        data = 	{'delivery_status': 'created'}
        resp = self.client.patch(url_order_detail, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(OrderModel.objects.get().delivery_status, 'preparing')

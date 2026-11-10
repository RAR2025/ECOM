from django.contrib.auth.models import User
from django.http import Http404
from django.test import RequestFactory, TestCase
from django.urls import reverse

from .context_processors import cart_count
from .models import Cart, Product
from .views import remove_from_cart


class CartViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='cart-user',
            password='test-password',
        )
        self.other_user = User.objects.create_user(
            username='other-user',
            password='test-password',
        )
        self.request_factory = RequestFactory()
        self.product = Product.objects.create(
            title='Test Product',
            selling_price=100,
            discounted_price=80,
            description='Test product',
            category='ML',
        )
        self.client.login(username='cart-user', password='test-password')

    def test_add_to_cart_increments_existing_item_for_current_user(self):
        add_url = reverse('add-to-cart')

        self.client.get(add_url, {'prod_id': self.product.pk})
        self.client.get(add_url, {'prod_id': self.product.pk})

        cart_item = Cart.objects.get(user=self.user, product=self.product)
        self.assertEqual(cart_item.quantity, 2)
        self.assertEqual(Cart.objects.filter(user=self.other_user).count(), 0)

    def test_cart_update_and_remove_are_limited_to_current_user(self):
        cart_item = Cart.objects.create(
            user=self.user,
            product=self.product,
            quantity=1,
        )
        other_item = Cart.objects.create(
            user=self.other_user,
            product=self.product,
            quantity=3,
        )

        response = self.client.post(
            reverse('update-cart', args=[cart_item.pk]),
            {'quantity': 4},
        )
        self.assertRedirects(
            response,
            reverse('showcart'),
            fetch_redirect_response=False,
        )
        cart_item.refresh_from_db()
        self.assertEqual(cart_item.quantity, 4)

        request = self.request_factory.post(
            reverse('remove-from-cart', args=[other_item.pk]),
        )
        request.user = self.user
        with self.assertRaises(Http404):
            remove_from_cart(request, other_item.pk)
        self.assertTrue(Cart.objects.filter(pk=other_item.pk).exists())

        response = self.client.post(
            reverse('remove-from-cart', args=[cart_item.pk]),
        )
        self.assertRedirects(
            response,
            reverse('showcart'),
            fetch_redirect_response=False,
        )
        self.assertFalse(Cart.objects.filter(pk=cart_item.pk).exists())

    def test_ajax_quantity_change_returns_updated_totals(self):
        cart_item = Cart.objects.create(
            user=self.user,
            product=self.product,
            quantity=1,
        )

        response = self.client.post(
            reverse('update-cart', args=[cart_item.pk]),
            {'quantity': 3},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest',
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'removed': False,
            'cart_count': 1,
            'item_total': 240,
            'cart_total': 240,
        })

    def test_cart_count_is_available_and_zero_for_empty_cart(self):
        request = self.request_factory.get(reverse('showcart'))
        request.user = self.user
        self.assertEqual(cart_count(request), {'cart_count': 0})

        Cart.objects.create(user=self.user, product=self.product)
        self.assertEqual(cart_count(request), {'cart_count': 1})

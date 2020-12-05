from django.conf import settings
from parksystemapp.models import Reservation, ParkProperty

class Cart(object):
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        def add (self, product):
            product_id = str(Reservation.id)
            if product_id not in self.cart:
                self.cart[product.id] = {'price': str(ParkProperty.property_price)}
            self.save()

        def save(self):
            self.session.modified = True

        def remove(self, product):
            product_id = str(Reservation.id)
            if product_id in self.cart:
                del self.cart[product_id]
                self.save()

        def __iter__(self):
             """
            Iterate over the items in the cart and get the reservations
            from the database.
            """
            product_ids = self.cart.keys()
            products = Reservation.objects.filter(id__in=product_ids)
            cart = self.cart.copy()
            for product in products:
                cart[str(product.id)]['product'] = product
            for item in cart.values():
                item['price'] = item['price']
                yield item

        def __len__(self):
            #Count all items in cart
            return sum(item['quantity'] for item in self.cart.values())
        
        def get_total_price(self):
            return sum(item['price'] for item in self.cart.value())
        
        def clear(self):
            del self.session[settings.CART_SESSION_ID]
            self.save()
from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):
    def test_item_name_is_required(self):
        #  name field is required
        # instantiating a form where user not filled in details
        form = ItemForm({'name': ''})
        # form should not be valid
        self.assertFalse(form.is_valid())  
        # When the form is invalid, should send back dict of fields w/ errors
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_name_is_not_required(self):
        # only name is listed here, done is missing
        form = ItemForm({'name': 'Test Todo Item'})  
        # form should be valid
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm()  # instantiate an empty form
        # ensure that only fields displayed in form - name, done
        self.assertEqual(form.Meta.fields, ['name', 'done'])

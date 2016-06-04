from django.shortcuts import resolve_url as r
from django.test import TestCase
from ..models import Plan


class LandingTest(TestCase):
    def setUp(self):
        self.r = self.client.get(r('landing:index'))

    def test_landing_status_code(self):
        '''GET /landing should return 200'''
        self.assertEqual(200, self.r.status_code)

    def test_template(self):
        '''GET /landing should render landing/index.html'''
        self.assertTemplateUsed(self.r, 'landing/index.html')

    def test_context(self):
        '''Landing page should contain plans'''
        with self.subTest():
            self.assertIn('plans', self.r.context)
            self.assertIs(Plan, self.r.context['plans'].model)

    def test_privacy(self):
        '''Landing page should contain link to privacy'''
        self.assertContains(self.r, 'Política de privacidade')

    def test_terms(self):
        '''Landing page should contain Terms of Use link'''
        self.assertContains(self.r, 'Termos de uso')

    def test_contact_form(self):
        '''Landing page should contain contact form'''
        self.assertContains(self.r, '>Enviar mensagem<')
from django.db import models


class Plan(models.Model):
    name = models.CharField('nome', max_length=255)
    headline = models.CharField('descrição', max_length=255)
    monthly_price = models.FloatField('preço mensal')
    users = models.IntegerField('número de usuários', default=0)
    automatic_register = models.BooleanField('marcação automática', default=False)
    dynamic_reminders = models.BooleanField('lembretes automáticos', default=False)
    support_all_time = models.BooleanField('suporte 24/7', default=False)
    unlimited_users = models.BooleanField('usuários ilimitados', default=False)
    is_popular = models.BooleanField('popular', default=False)
    is_free = models.BooleanField('gratuito', default=False)

    created_at = models.DateTimeField('criado em', auto_now_add=True)
    modified_at = models.DateTimeField('modificado em', auto_now=True)

    class Meta:
        verbose_name = 'plano'
        verbose_name_plural = 'planos'

    @property
    def display_price(self):
        if not self.is_free and self.monthly_price > 0:
            return self.monthly_price
        elif self.is_free:
            return 'Grátis'
        else:
            return '?'

    @property
    def show_currency(self):
        return not self.is_free

    def display_period(self):
        if self.is_free:
            return 'para sempre'
        return 'por mês'

    def __str__(self):
        return self.name

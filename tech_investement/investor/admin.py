from django.contrib import admin
from .models import UserProfile, UserAccount, Transaction_ids, Deposit, Withdrawal, WithdrawalRequest
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(UserAccount)
admin.site.register(Transaction_ids)
admin.site.register(Deposit)
admin.site.register(Withdrawal)
admin.site.register(WithdrawalRequest)

from django.contrib import admin
from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from trade_engine.views import base, indicators, user_registration, account_settings, ticker_view, depth_view, CreateBalanceFormView, CreateActiveOrderFormView, CreateTradeFormView, CreateCancelOrderView, CreateTradeHistoryView, CreateUserAccountView, UpdateUserAccountView, DeleteUserAccountView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', base, name='base'),
    url(r'^indicators/', login_required(indicators), name='indicators'),
    url(r'^login/', login, name='login'),
    url(r'^logout/', logout, {'next_page': 'base'}, name='logout'),
    url(r'^registration/', user_registration, name='user_registration'),
    url(r'^account_settings/', login_required(account_settings), name='account_settings'),
    url(r'^get_balance/', login_required(CreateBalanceFormView.as_view()), name='get_balance_form'),
    url(r'^get_active_orders/', login_required(CreateActiveOrderFormView.as_view()), name='get_active_orders_form'),
    url(r'^get_ticker/', login_required(ticker_view), name='get_ticker'),
    url(r'^get_depth/', login_required(depth_view), name='get_depth'),
    url(r'^trade/', login_required(CreateTradeFormView.as_view()), name='create_trade_form'),
    url(r'^cancel_trade/', login_required(CreateCancelOrderView.as_view()), name='create_cancel_order_view'),
    url(r'^get_trade_history/', login_required(CreateTradeHistoryView.as_view()), name='trade_history_view'),
    url(r'^create_user_profile/', login_required(CreateUserAccountView.as_view()), name='create_user_account'),
    url(r'^update_user_profile/(?P<pk>\d+)/', login_required(UpdateUserAccountView.as_view()), name='update_user_account'),
    url(r'^delete_user_profile/(?P<pk>\d+)/', login_required(DeleteUserAccountView.as_view()), name='delete_user_account'),
]
